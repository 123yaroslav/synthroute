"""synthroute · Kaggle GPU smoke test: proves the compute is reachable and measures a quick fp16 matmul throughput."""
import subprocess, time, json

print(subprocess.run(["nvidia-smi", "--query-gpu=name,memory.total,driver_version", "--format=csv"], capture_output=True, text=True).stdout)
import torch

info = {"torch": torch.__version__, "cuda_available": torch.cuda.is_available(), "devices": []}
for i in range(torch.cuda.device_count()):
    p = torch.cuda.get_device_properties(i)
    info["devices"].append({"name": p.name, "vram_gb": round(p.total_memory / 1024**3, 1)})
if info["cuda_available"]:
    a = torch.randn(4096, 4096, device="cuda", dtype=torch.float16)
    b = torch.randn(4096, 4096, device="cuda", dtype=torch.float16)
    torch.cuda.synchronize(); t = time.perf_counter()
    for _ in range(50):
        a @ b
    torch.cuda.synchronize(); dt = time.perf_counter() - t
    info["fp16_matmul_tflops"] = round(50 * 2 * 4096**3 / dt / 1e12, 1)
print(json.dumps(info))
