#!/usr/bin/env python3
"""Generate the report's inline SVG diagrams (themed via CSS vars, no external deps)."""
from __future__ import annotations
import html, textwrap
from pathlib import Path

OUT = Path(__file__).parent / "diagrams.html"
CHAR = 6.15  # avg char width at 10.5px


def wrap(text: str, width_px: float, size: float = 10.5) -> list[str]:
    return textwrap.wrap(text, max(6, int(width_px / (size * 0.585)))) or [""]


def box(x, y, w, h, title, sub=None, cls="b", rx=7):
    dark = cls in ("io", "hdr")
    lines = wrap(title, w - 12, 11)
    th = len(lines) * 13
    sh = 12 if sub else 0
    top = y + (h - th - sh) / 2 + 10
    out = [f'<rect class="{cls}" x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}"/>']
    for i, ln in enumerate(lines):
        out.append(f'<text class="t{" inv" if dark else ""}" x="{x + w / 2}" y="{top + i * 13}">{html.escape(ln)}</text>')
    if sub:
        out.append(f'<text class="s{" inv2" if dark else ""}" x="{x + w / 2}" y="{top + th + 2}">{html.escape(sub)}</text>')
    return "".join(out)


def arrow(x1, y1, x2, y2, cls="a", dash=False, label=None, lx=None, ly=None):
    d = ' stroke-dasharray="4 3"' if dash else ""
    s = f'<path class="{cls}" d="M{x1},{y1} L{x2},{y2}" marker-end="url(#ah)"{d}/>'
    if label:
        s += f'<text class="s" x="{lx or (x1 + x2) / 2}" y="{ly or (y1 + y2) / 2 - 4}">{html.escape(label)}</text>'
    return s


def curve(x1, y1, x2, y2, bend, cls="a", dash=False, label=None):
    mx = (x1 + x2) / 2
    head = "ahx" if "loop" in cls else "ah"
    s = f'<path class="{cls}" d="M{x1},{y1} C{mx},{y1 + bend} {mx},{y2 + bend} {x2},{y2}" fill="none" marker-end="url(#{head})"'
    s += ' stroke-dasharray="5 4"/>' if dash else "/>"
    if label:
        s += f'<text class="s" x="{mx}" y="{y1 + bend * 0.78}">{html.escape(label)}</text>'
    return s


def svg(w, h, body, title, desc=""):
    return (f'<svg class="dia" viewBox="0 0 {w} {h}" role="img" aria-label="{html.escape(title)}">'
            f"<title>{html.escape(title)}</title><desc>{html.escape(desc)}</desc>"
            '<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">'
            '<path d="M0,1 L9,5 L0,9 z" class="ahf"/></marker><marker id="ahx" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="ahx"/></marker></defs>' + body + "</svg>")


# ── 1. Block 3: end-to-end process with lanes and the verify→repair loop ───────
def d_pipeline() -> str:
    W, H = 1180, 430
    lane_y = {"in": 40, "llm": 120, "code": 250, "out": 360}
    p = []
    p.append(f'<rect class="lane llm" x="88" y="{lane_y["llm"] - 26}" width="{W - 100}" height="118" rx="9"/>')
    p.append(f'<rect class="lane code" x="88" y="{lane_y["code"] - 26}" width="{W - 100}" height="118" rx="9"/>')
    p.append(f'<text class="lbl llmt" x="14" y="{lane_y["llm"] + 36}">LLM</text>')
    p.append(f'<text class="lbl codet" x="14" y="{lane_y["code"] + 30}">детермини-</text>')
    p.append(f'<text class="lbl codet" x="14" y="{lane_y["code"] + 44}">рованный код</text>')

    # input / output
    p.append(box(14, lane_y["in"], 150, 46, "МНН + ограничения", "масштаб, запреты, стадии", "io"))
    p.append(box(W - 164, lane_y["out"], 150, 46, "HTML (offline) + PDF", "дисклеймер, источники", "io"))

    code = [  # (x, w, title, sub)
        (100, 104, "Входной гейт", "fail-closed"),
        (216, 104, "Разрешение МНН", "PubChem · ChEMBL"),
        (332, 116, "Сбор свидетельств", "адаптеры · RAG"),
        (460, 112, "Ретросинтез", "AiZynthFinder"),
        (584, 116, "Нормализация", "RouteSpec · RDKit"),
        (712, 116, "route-lint", "коды диагностик"),
        (840, 112, "Ранжирование", "метрики · кластеры"),
        (964, 104, "Визуализация", "Vue Flow"),
        (1080, 86, "Экспорт", "offline"),
    ]
    for x, w, t, s in code:
        p.append(box(x, lane_y["code"], w, 68, t, s, "code"))
    llm = [(332, 116, "Извлечение", "статьи · патенты"), (460, 112, "Кандидаты", "из литературы"),
           (712, 116, "Ремонт", "по диагностикам"), (964, 104, "Чат-правки", "новая версия")]
    for x, w, t, s in llm:
        p.append(box(x, lane_y["llm"], w, 68, t, s, "llm"))

    p.append(arrow(89, lane_y["in"] + 23, 99, lane_y["code"] + 10))
    for i in range(len(code) - 1):
        x, w, *_ = code[i]
        p.append(arrow(x + w + 1, lane_y["code"] + 34, code[i + 1][0] - 2, lane_y["code"] + 34))
    for x, w, *_ in llm:                       # код → LLM и обратно
        p.append(arrow(x + w / 2 - 14, lane_y["code"] - 1, x + w / 2 - 14, lane_y["llm"] + 69, "a thin"))
        p.append(arrow(x + w / 2 + 14, lane_y["llm"] + 69, x + w / 2 + 14, lane_y["code"] - 1, "a thin"))
    p.append(arrow(1123, lane_y["code"] + 69, 1123, lane_y["out"] - 2))
    # repair loop: lint → repair → normalize
    p.append(curve(770, lane_y["code"] - 1, 642, lane_y["code"] - 1, -46, "a loop", True, "не прошло → ремонт → перепроверка"))
    p.append(f'<text class="s em" x="{W / 2}" y="{H - 10}">Ни один шаг LLM не завершается без последующей детерминированной проверки</text>')
    return svg(W, H, "".join(p), "Схема процесса synthroute",
               "Ввод МНН проходит гейт, разрешение структуры, сбор свидетельств, ретросинтез и извлечение из литературы, "
               "нормализацию в RouteSpec, проверку route-lint с циклом ремонта, ранжирование, визуализацию и экспорт.")


# ── 2. Block 3: component architecture ────────────────────────────────────────
def d_components() -> str:
    W, H = 1180, 470
    p = []
    rows = [
        (18, "Frontend · Vue 3 + TS", "fe", [("Холст маршрута (Vue Flow)", 206), ("Технологический режим", 186),
                                             ("Сравнение маршрутов", 176), ("Чат + версии", 130), ("Режим эксперта", 140)]),
        (104, "API · FastAPI", "api", [("REST + SSE прогресса", 180), ("services: generate · edit · export", 250)]),
        (190, "Домен (чистый код)", "code", [("safety: гейт", 116), ("chem: RDKit", 120), ("validation: route-lint", 176),
                                             ("routes: модель · метрики · diff", 228), ("export: HTML · PDF", 160)]),
        (276, "LLM-слой", "llm", [("agents: планировщик · извлечение · ремонт", 300),
                                  ("llm/gateway: роли · профили · кассеты · трассы", 326)]),
        (362, "Данные и внешние", "data", [("sources: PubChem · ChEMBL · Crossref · патенты · ORD", 364),
                                           ("ретросинтез-сервис (отдельное окружение)", 290),
                                           ("SQLite: версии · трассы", 182), ("RAG-индекс", 110)]),
    ]
    for y, label, cls, items in rows:
        p.append(box(14, y, 168, 72, label, None, "hdr"))
        x = 196
        for t, w in items:
            p.append(box(x, y, w, 72, t, None, cls))
            x += w + 10
    for y in (18, 104, 190, 276):
        p.append(arrow(98, y + 73, 98, y + 85, "a thin"))
    p.append(box(14, 448 - 2, 168, 0, "", None, "hdr"))  # spacer no-op
    p.append(f'<text class="s em" x="{W / 2}" y="{H - 12}">Импорты только сверху вниз: домен не знает про HTTP и LLM (правило PY-004)</text>')
    return svg(W, H, "".join(p), "Компонентная архитектура synthroute",
               "Пять слоёв: фронтенд на Vue, API на FastAPI, чистый домен, слой LLM с gateway и слой данных.")


# ── 3. Block 2: architectural archetypes of market solutions ──────────────────
ARCH = [
    ("A. Экспертные правила", "SYNTHIA · RetroBioCat",
     ["структура цели", "база экспертных правил", "поиск по графу с отсечением", "стоп на каталоге сырья", "ранжирование"],
     [1, 1, 1, 1, 1], "Интерпретируемо, есть лабораторная валидация. Правила пишутся вручную, покрытие ограничено."),
    ("B. Шаблонный ML + поиск", "AiZynthFinder · ASKCOS · Spaya · Reaxys",
     ["структура цели", "нейросеть ранжирует шаблоны", "фильтр реализуемости", "MCTS / Retro*", "сток покупаемых", "скоринг маршрута"],
     [1, 2, 2, 1, 1, 1], "Самый массовый класс. Условия, масштаб и источники не выводятся."),
    ("C. Трансформер (seq2seq)", "IBM RXN · Chemformer · RetroChimera",
     ["SMILES цели", "трансформер предсказывает предшественников", "поиск по гиперграфу", "round-trip прямой моделью", "ранжирование"],
     [1, 2, 1, 2, 1], "Сильное прямое предсказание даёт обратную проверку. «Чёрный ящик», ссылок нет."),
    ("D. Литературный поиск + предсказание", "CAS SciFinder · Reaxys Combined",
     ["цель", "поиск стадий в курированной базе", "предсказанные стадии правилами", "дерево с лимитами цены", "план со ссылками"],
     [1, 1, 2, 1, 1], "Единственные, кто показывает первоисточник стадии. Закрыто подпиской, выгрузки нет."),
    ("E. LLM-агент с инструментами", "ChemCrow · Coscientist · DeepRetro · steer",
     ["запрос", "LLM-планировщик (ReAct)", "вызов инструмента", "наблюдение в цикл", "ответ"],
     [1, 3, 2, 2, 3], "Диалог и объяснения. Нет статуса проверки у факта, LLM-судья ненадёжен."),
    ("F. Регуляторная проверка", "Lhasa Mirabilis · Derek/Sarah",
     ["готовая схема от человека", "предсказание фактора очистки", "сравнение с требуемым", "опция контроля ICH M7"],
     [1, 1, 1, 1], "Единственные, кто принимает маршрут и выдаёт формализованный вердикт. Маршруты не генерируют."),
]


def d_archetypes() -> str:
    W = 1180
    rowh, gap = 96, 16
    H = 30 + len(ARCH) * (rowh + gap)
    p, y = [], 24
    for name, who, steps, kinds, note in ARCH:
        p.append(f'<text class="hh" x="0" y="{y + 12}">{html.escape(name)}</text>')
        p.append(f'<text class="s end" x="{W}" y="{y + 12}">{html.escape(who)}</text>')
        n = len(steps)
        avail = W - (n - 1) * 26
        bw = avail / n
        x = 0
        for i, (t, k) in enumerate(zip(steps, kinds)):
            cls = {1: "code", 2: "mlb", 3: "llm"}[k]
            p.append(box(x, y + 20, bw, 44, t, None, cls))
            if i < n - 1:
                p.append(arrow(x + bw + 2, y + 42, x + bw + 23, y + 42))
            x += bw + 26
        p.append(f'<text class="s st" x="0" y="{y + 82}">{html.escape(note)}</text>')
        y += rowh + gap
    return svg(W, H, "".join(p), "Шесть архитектурных архетипов решений рынка",
               "Каждое из разобранных решений сводится к одному из шести конвейеров.")


css = """
.dia{width:100%;height:auto;display:block;margin:10px 0 4px;overflow:visible}
.dia text{font:10.5px var(--sans);fill:var(--ink);text-anchor:middle;dominant-baseline:middle}
.dia .t{font-weight:600}
.dia .s{font-size:9.5px;fill:var(--ink-3)}
.dia .s.em{font-size:10px;font-style:italic}
.dia .st{text-anchor:start} .dia .end{text-anchor:end}
.dia .inv{fill:var(--hero-ink,#f4f2ec)} .dia .inv2{fill:#b9b5aa;font-size:9.5px}
.dia .ahx{fill:var(--accent)}
.dia .hh{font-size:12px;font-weight:700;fill:var(--ink);text-anchor:start;dominant-baseline:middle}
.dia .lbl{font-size:10px;font-weight:700;text-anchor:start}
.dia .llmt{fill:var(--llm)} .dia .codet{fill:var(--code)}
.dia rect{stroke-width:1}
.dia .code{fill:var(--code-soft);stroke:none}
.dia .llm{fill:var(--llm-soft);stroke:none}
.dia .mlb{fill:var(--surface-2);stroke:var(--line)}
.dia .io{fill:var(--hero);stroke:none}
.dia .hdr{fill:var(--hero);stroke:none}
.dia .fe,.dia .api,.dia .data{fill:var(--surface-2);stroke:var(--line)}
.dia .lane{fill:none;stroke:var(--line);stroke-dasharray:3 4}
.dia .lane.llm{fill:none}
.dia .a{stroke:var(--ink-3);stroke-width:1.4;fill:none}
.dia .a.thin{stroke-width:1;opacity:.55}
.dia .a.loop{stroke:var(--accent);stroke-width:1.6}
.dia .ahf{fill:var(--ink-3)}
"""

parts = {"pipeline": d_pipeline(), "components": d_components(), "archetypes": d_archetypes()}
OUT.write_text("<style>" + css + "</style>\n" + "\n<!--SPLIT-->\n".join(f"<!--{k}-->\n{v}" for k, v in parts.items()), encoding="utf-8")
print("written", OUT, {k: len(v) for k, v in parts.items()})
