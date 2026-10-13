# Модели, лимиты и рабочее окружение: Gemini API, Gemma, слой абстракции, вычисления и химические инструменты

- **Дата:** 2026-10-13. Все источники открыты в этот день.
- **Вопрос:** какие модели и инструменты доступны проекту прямо сейчас, на каких условиях (лимиты, цены, данные, регион) и как собрать окружение, чтобы модель менялась конфигом (инвариант 4), а тесты шли на кассетах (LLM-006).
- **Статус:** исследовательская заметка (DOC-004). Факты даны со ссылками `[n]`. Наши интерпретации и гипотезы явно помечены и вынесены в раздел «Выводы для проекта».
- **Метод:**
  - Официальные страницы скачаны (curl/WebFetch) и прочитаны в тексте.
  - Версии пакетов взяты из PyPI JSON API (`https://pypi.org/pypi/<pkg>/json`).
  - Страницы документации Kaggle рендерятся JavaScript'ом, их текст получен через бэкенд документации Kaggle и сверен с поисковым сниппетом kaggle.com.
  - Часть сбора (разделы 3–5) выполнена параллельными агентами-исследователями. Ключевые значения (версии PyPI, пины зависимостей, лицензия Gemma 4, инцидент LiteLLM) перепроверены отдельно.
  - Если значение не удалось подтвердить на официальной странице, стоит пометка «не подтверждено».
- **Связанные правила:** LLM-001…008, CORE-004, CORE-005, DOC-004, EVAL-*.

## Источники

| # | Источник (URL) | Тип | Дата доступа |
|---|---|---|---|
| 1 | https://ai.google.dev/gemini-api/docs/models | документация (обзор моделей, обновлена 2026-10-09) | 2026-10-13 |
| 2 | https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash | документация (карточка модели) | 2026-10-13 |
| 3 | https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash | документация (карточка модели) | 2026-10-13 |
| 4 | https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite | документация (карточка модели) | 2026-10-13 |
| 5 | https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite | документация (карточка модели) | 2026-10-13 |
| 6 | https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview | документация (карточка модели) | 2026-10-13 |
| 7 | https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview | документация (карточка модели) | 2026-10-13 |
| 8 | https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro · …/gemini-2.5-flash · …/gemini-2.5-flash-lite | документация (карточки моделей) | 2026-10-13 |
| 9 | https://ai.google.dev/gemini-api/docs/models/gemini-embedding-2 · …/gemini-embedding-001 | документация (карточки моделей) | 2026-10-13 |
| 10 | https://ai.google.dev/gemini-api/docs/rate-limits | документация (лимиты, обновлена 2026-10-09) | 2026-10-13 |
| 11 | https://ai.google.dev/gemini-api/docs/pricing | документация (цены) | 2026-10-13 |
| 12 | https://ai.google.dev/gemini-api/terms | условия использования (Gemini API Additional Terms, действуют с 2026-03-23) | 2026-10-13 |
| 13 | https://ai.google.dev/gemini-api/docs/available-regions | документация (регионы, обновлена 2026-04-28) | 2026-10-13 |
| 14 | https://ai.google.dev/gemma/docs/core/gemma_on_gemini_api | документация (Gemma в Gemini API) | 2026-10-13 |
| 15 | https://ai.google.dev/gemma/docs/core | документация (обзор Gemma 4, таблица памяти) | 2026-10-13 |
| 16 | https://ai.google.dev/gemini-api/docs/structured-output · https://ai.google.dev/gemini-api/docs/generate-content/structured-output | документация (structured output) | 2026-10-13 |
| 17 | https://ai.google.dev/gemini-api/docs/google-search | документация (grounding) | 2026-10-13 |
| 18 | https://ai.google.dev/gemini-api/docs/url-context | документация (URL context) | 2026-10-13 |
| 19 | https://ai.google.dev/gemini-api/docs/batch-api | документация (Batch API) | 2026-10-13 |
| 20 | https://ai.google.dev/gemini-api/docs/embeddings | документация (эмбеддинги) | 2026-10-13 |
| 21 | https://ai.google.dev/gemini-api/docs/interactions-overview | документация (Interactions API) | 2026-10-13 |
| 22 | https://ai.google.dev/gemini-api/docs/changelog | release notes | 2026-10-13 |
| 23 | https://ai.google.dev/gemini-api/docs/deprecations | документация (график вывода моделей) | 2026-10-13 |
| 24 | https://ai.google.dev/gemini-api/docs/latest-model | документация (руководство по 3.8 Flash и миграции) | 2026-10-13 |
| 25 | https://ai.google.dev/gemini-api/docs/billing | документация (биллинг, обновлена 2026-09-28) | 2026-10-13 |
| 26 | https://ai.google.dev/gemini-api/docs/tokens | документация (подсчёт токенов) | 2026-10-13 |
| 27 | https://ai.google.dev/api/generate-content | API reference (GenerateContentResponse, UsageMetadata) | 2026-10-13 |
| 28 | https://ai.google.dev/gemini-api/docs/api-key | документация (ключи, обновлена 2026-10-06) | 2026-10-13 |
| 29 | https://pypi.org/project/google-genai/ (JSON API) | реестр пакетов | 2026-10-13 |
| 30 | https://github.com/googleapis/python-genai (`google/genai/types.py`, `_api_client.py`, `_replay_api_client.py`, `tests/conftest.py`) | исходный код | 2026-10-13 |
| 31 | https://pypi.org/project/litellm/ (JSON API) | реестр пакетов | 2026-10-13 |
| 32 | https://docs.litellm.ai/docs/providers/gemini · …/completion/json_mode · …/routing · …/completion/reliable_completions · …/completion/mock_requests · …/caching/all_caches · …/completion/token_usage | документация | 2026-10-13 |
| 33 | https://docs.litellm.ai/blog/security-update-march-2026 | официальный блог (инцидент безопасности) | 2026-10-13 |
| 34 | https://github.com/BerriAI/litellm/security/advisories | security advisories | 2026-10-13 |
| 35 | https://pypi.org/project/pydantic-ai/ · https://pypi.org/project/pydantic-ai-slim/ (JSON API) | реестр пакетов | 2026-10-13 |
| 36 | https://pydantic.dev/docs/ai/models/google/ · …/models/overview/ · …/overview/migration/ | документация | 2026-10-13 |
| 37 | https://pydantic.dev/docs/ai/core-concepts/output/ · …/core-concepts/agent/ | документация | 2026-10-13 |
| 38 | https://pydantic.dev/docs/ai/guides/testing/ · …/guides/embeddings/ · …/integrations/logfire/ | документация | 2026-10-13 |
| 39 | https://github.com/pydantic/pydantic-ai (`pyproject.toml`, `tests/conftest.py`, `tests/cassette_hooks.py`) | исходный код | 2026-10-13 |
| 40 | https://pypi.org/project/instructor/ · https://python.useinstructor.com/integrations/genai/ | реестр пакетов, документация | 2026-10-13 |
| 41 | https://ai.google.dev/gemini-api/docs/openai | документация (OpenAI-совместимость Gemini) | 2026-10-13 |
| 42 | https://github.com/mozilla-ai/any-llm · https://docs.mozilla.ai/any-llm/providers/ · PyPI JSON: `any-llm-sdk`, `openai`, `langchain-google-genai`, `dspy` | исходный код, документация, реестр | 2026-10-13 |
| 43 | https://pypi.org/pypi/vcrpy/json · https://github.com/kevin1024/vcrpy/releases · https://vcrpy.readthedocs.io/en/latest/advanced.html | реестр, release notes, документация | 2026-10-13 |
| 44 | https://pypi.org/project/pytest-recording/ · https://pypi.org/pypi/pytest-vcr/json · https://pypi.org/pypi/cassetter/json | реестр пакетов | 2026-10-13 |
| 45 | https://www.kaggle.com/docs/efficient-gpu-usage | документация Kaggle | 2026-10-13 |
| 46 | https://www.kaggle.com/docs/notebooks | документация Kaggle | 2026-10-13 |
| 47 | https://www.kaggle.com/docs/tpu | документация Kaggle | 2026-10-13 |
| 48 | https://www.nvidia.com/en-us/data-center/tesla-t4/ | спецификация производителя | 2026-10-13 |
| 49 | https://images.nvidia.com/content/tesla/pdf/nvidia-tesla-p100-PCIe-datasheet.pdf | спецификация производителя | 2026-10-13 |
| 50 | https://research.google.com/colaboratory/faq.html | FAQ Colab | 2026-10-13 |
| 51 | https://colab.research.google.com/signup | страница тарифов Colab | 2026-10-13 |
| 52 | https://ai.google.dev/gemma/docs/core/model_card_4 | model card Gemma 4 | 2026-10-13 |
| 53 | https://opensource.googleblog.com/2026/03/gemma-4-expanding-the-gemmaverse-with-apache-20.html | официальный блог (лицензия Gemma 4) | 2026-10-13 |
| 54 | https://huggingface.co/collections/google/gemma-4 | репозиторий весов | 2026-10-13 |
| 55 | https://huggingface.co/collections/Qwen/qwen35 · https://huggingface.co/Qwen/Qwen3.8-27B | репозиторий весов | 2026-10-13 |
| 56 | https://docs.vllm.ai/en/latest/getting_started/installation/gpu.html · …/features/quantization/ · …/models/supported_models.html · …/configuration/engine_args.html | документация vLLM | 2026-10-13 |
| 57 | https://docs.ollama.com/gpu · https://ollama.com/library/gemma4 | документация Ollama | 2026-10-13 |
| 58 | https://huggingface.co/docs/bitsandbytes/main/en/installation · https://huggingface.co/docs/transformers/model_doc/gemma4 | документация | 2026-10-13 |
| 59 | https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md | документация llama.cpp | 2026-10-13 |
| 60 | https://pypi.org/pypi/rdkit/json · https://pypi.org/pypi/rdkit/2023.9.6/json · https://api.github.com/repos/rdkit/rdkit/releases | реестр пакетов, релизы | 2026-10-13 |
| 61 | https://api.anaconda.org/package/conda-forge/rdkit | реестр conda-forge | 2026-10-13 |
| 62 | https://pypi.org/pypi/aizynthfinder/json · https://raw.githubusercontent.com/MolecularAI/aizynthfinder/master/pyproject.toml · …/README.md | реестр, исходный код | 2026-10-13 |
| 63 | https://github.com/MolecularAI/aizynthfinder/pull/205 · …/issues/189 · …/pull/197 · …/issues/40 | issue tracker | 2026-10-13 |
| 64 | `aizynthfinder/tools/download_public_data.py` (GitHub) · https://zenodo.org/api/records/7797465 · https://zenodo.org/api/records/7341155 · https://api.figshare.com/v2/articles/12334577/files | исходный код, репозитории данных | 2026-10-13 |
| 65 | https://molecularai.github.io/aizynthfinder/configuration.html | документация | 2026-10-13 |
| 66 | https://gitlab.com/mlpds_mit/askcosv2/askcos2_core (README, LICENSE, `Dockerfile_app`, `configs/`) | исходный код | 2026-10-13 |
| 67 | https://askcos-docs.mit.edu/guide/1-Introduction/1.1-Introduction.html · …/guide/4-Deployment/4.1-Customizing-local-deployment.html · …/release-notes/7.2-ASKCOS-v2/13-2026.07-Release-Notes.html · …/release-notes/8-Changelogs.html | документация ASKCOS | 2026-10-13 |
| 68 | https://askcos-docs.mit.edu/guide/10-Privacy-&-Terms-of-Service/10.1-ASKCOS-Terms-of-Service.html | условия использования | 2026-10-13 |
| 69 | https://pypi.org/pypi/syntheseus/json · https://github.com/microsoft/syntheseus (`.github/workflows/ci.yml`, `docs/single_step.md`, `environment_full.yml`, `syntheseus/search/algorithms`) · https://microsoft.github.io/syntheseus/stable/installation/ | реестр, исходный код, документация | 2026-10-13 |
| 70 | PyPI JSON: `syntheseus-megan`, `syntheseus-local-retro`, `tensorflow`, `pandas`, `reaction-utils` | реестр пакетов | 2026-10-13 |
| 71 | https://pypi.org/pypi/rxnmapper/json · https://github.com/rxn4chemistry/rxnmapper (`setup.cfg`, `.github/workflows/tests.yaml`, `rxnmapper/core.py`) | реестр, исходный код | 2026-10-13 |
| 72 | https://github.com/rxn4chemistry/rxnmapper/issues/54 · …/issues/70 · …/pull/81 | issue tracker | 2026-10-13 |
| 73 | https://setuptools.pypa.io/en/latest/history.html | release notes | 2026-10-13 |
| 74 | PyPI JSON: `ord-schema`, `rxn-chem-utils`, `rdchiral`, `numpy`, `fastapi`, `onnxruntime` | реестр пакетов | 2026-10-13 |
| 75 | https://devguide.python.org/versions/ | жизненный цикл версий Python | 2026-10-13 |

---

## 1. Google AI Studio / Gemini API на 2026-10-13

### 1.1. Что изменилось (важно, если опираться на «старые» знания)

- **Линейка моделей обновляется почти ежемесячно.**
  - Актуальные текстовые модели — семейство Gemini 3.x: `gemini-3.8-flash` (GA 2026-09-02), `gemini-3.6-flash` и `gemini-3.5-flash-lite` (GA 2026-07-21), `gemini-3.1-flash-lite` (GA 2026-05-07) [1][22][23].
  - Модели Gemini 2.0 и `gemini-3-pro-preview` уже отключены [1][23].
- **Модели 2.5 не объявлены устаревшими, но новым проектам недоступны.** С 2026-09-18 Google ограничил доступ к ним пользователями, которые уже работали с этими моделями раньше. Для новых проектов рекомендованы 3.5 Flash-Lite или 3.8 Flash [1][22].
- **Устаревшие id могут молча перенаправляться на новые модели.** Запросы к `gemini-3.7-flash` уходят на `gemini-3.8-flash`, к `gemini-3.5-flash` — на `gemini-3.6-flash` [22][23]. Ответ `generateContent` содержит поле `modelVersion` («The model version used to generate the response») [27].
- **Детерминизм через сэмплирование больше недоступен.** С 2026-07-21 параметры `temperature`, `top_p` и `top_k` для Gemini 3+ объявлены deprecated, `candidate_count` не поддерживается [22][24].
- **Основной API у Google теперь Interactions API.** Это `client.interactions.create`, GA с июня 2026 года, рекомендован для новых проектов. `generateContent` назван legacy, но «remains fully supported» [21].
  - Только в `generateContent` пока доступны Batch API, автоматический function calling (Python), explicit caching и пользовательские safety settings [21][19].
- **Interactions API по умолчанию хранит запросы** (`store=true`): 1 день на free tier и 55 дней на paid. Хранение отключается параметром `store=false` [21].
- **Новые ключи и ключи без ограничений.** С 2026-05-28 новые ключи AI Studio создаются как authorization keys, привязанные к сервисному аккаунту. Запросы с неограниченных standard keys API отклоняет [28].

### 1.2. Модели и возможности

**Текстовые модели Gemini.** Возможности взяты из карточек моделей [2]–[8], колонка «Free tier» — со страницы цен [11]: «да» означает «Free of charge» в колонке Free Tier.

| Модель | Model ID | Статус | Вход / выход, токенов | JSON schema (structured output) | Function calling | Search grounding | URL context | Batch API | Free tier |
|---|---|---|---|---|---|---|---|---|---|
| Gemini 3.8 Flash | `gemini-3.8-flash` | Stable, GA 2026-09-02 | 1 048 576 / 65 536 | да | да | да | да | да | да |
| Gemini 3.6 Flash | `gemini-3.6-flash` | Stable, GA 2026-07-21 | 1 048 576 / 65 536 | да | да | да | да | да | да |
| Gemini 3.5 Flash-Lite | `gemini-3.5-flash-lite` | Stable, GA 2026-07-21 | 1 048 576 / 65 536 | да | да | да | да | да | да |
| Gemini 3.1 Flash-Lite | `gemini-3.1-flash-lite` | Stable, GA 2026-05-07; shutdown не раньше 2027-05-07, замена — 3.5 Flash-Lite [23] | 1 048 576 / 65 536 | да | да | да | да | да | да |
| Gemini 3.1 Pro | `gemini-3.1-pro-preview` (также `gemini-3.1-pro-preview-customtools`) | Preview | 1 048 576 / 65 536 | да | да | да | да | да | **нет** («Not available») |
| Gemini 3 Flash | `gemini-3-flash-preview` | Preview, legacy | 1 048 576 / 65 536 | да | да | да | да | да | да |
| Gemini 2.5 Pro / Flash / Flash-Lite | `gemini-2.5-pro` · `gemini-2.5-flash` · `gemini-2.5-flash-lite` | Stable, доступ ограничен (1.1) | 1 048 576 / 65 536 | да | да | да | да | да | да, но только при наличии доступа |

Thinking поддерживают все перечисленные модели. У `gemini-3.8-flash` уровни `low`, `medium` (по умолчанию) и `high`; уровень `minimal` возвращает ошибку [2][24]. Google предупреждает, что 3.8 Flash на сложных задачах «can use more tokens… by design» и для повседневных задач предлагает снизить уровень рассуждений или взять 3.6 Flash [24].

**Gemma через Gemini API** [14][15][11][22]. Модели добавлены в API 2026-04-02.

| Модель | Model ID | Контекст | JSON schema | Function calling | Search grounding | Тарифы |
|---|---|---|---|---|---|---|
| Gemma 4 31B (dense) | `gemma-4-31b-it` | 256K по документации Gemma 4 для средних моделей [15]; лимит именно в API **не подтверждён** | **не подтверждено**: Gemma нет в таблице поддержки structured output [16], на странице [14] не упоминается | да (пример в [14]) | **противоречие**: в [14] есть пример с `google_search`, на странице цен [11] — «Not available» | Free: «Free of charge»; Paid: «Not available» [11] |
| Gemma 4 26B A4B (MoE, ~4B активных) | `gemma-4-26b-a4b-it` | то же | **не подтверждено** | да | то же противоречие | то же |

Поскольку Gemma в API есть только во free tier [11], к ней всегда применяются условия бесплатного уровня: «Used to improve our products: Yes» (см. 1.5).

**Эмбеддинги** [9][20][22][11].

| Модель | Model ID | Вход | Лимит входа | Размерность | Цена |
|---|---|---|---|---|---|
| Gemini Embedding 2 | `gemini-embedding-2` (GA 2026-04-22 [22]; обзорная страница [1] всё ещё показывает `gemini-embedding-2-preview`, но карточка [9] и [20] используют `gemini-embedding-2`) | текст, изображения, видео, аудио, PDF | 8 192 токена | 128–3072 (MRL), рекомендованы 768 / 1536 / 3072 | Free: бесплатно; Paid: $0.20 за 1M текстовых токенов, batch $0.10 |
| Gemini Embedding | `gemini-embedding-001` | только текст | 2 048 токенов | 128–3072, рекомендованы 768 / 1536 / 3072 | на странице [11] **не найдена** (не подтверждено) |

Отличия двух моделей [20]:
- **Пространства несовместимы.** Векторы `gemini-embedding-001` и `gemini-embedding-2` нельзя сравнивать между собой. При смене модели нужно переэмбеддить весь корпус.
- **Тип задачи.** У `gemini-embedding-2` нет параметра `task_type`, задачу описывают инструкцией в тексте. У `001` он есть (например, `SEMANTIC_SIMILARITY`).
- **Несколько входов в одном запросе.** `gemini-embedding-2` возвращает один агрегированный вектор. `001` возвращает отдельный вектор для каждой строки списка. Для массовой обработки Google советует Batch API (−50 %).

**Инструменты.**
- **Grounding with Google Search** [17][11]:
  - Поддерживают 3.8 Flash, 3.6 Flash, 3.5 Flash-Lite, 3.1 Pro Preview, 3 Flash Preview и 2.5 [17].
  - **Во free tier для Gemini 3+ — «Not available»**, со сноской «Can be tested in Google AI Studio».
  - На paid tier 5 000 бесплатных запросов в месяц на все модели Gemini 3+, далее $14 за 1 000 [11].
- **URL context** [18][11]:
  - Поддерживают 3.8 Flash, 3.6 Flash, 3.5 Flash-Lite, 3.1 Pro Preview, 3.1 Flash-Lite, 3 Flash Preview и 2.5.
  - Ограничения: до 20 URL на запрос, до 34 MB с одного URL, только публичные адреса. Paywalled-контент и Google Docs не поддерживаются.
  - Тарификация: во free tier бесплатно, на paid — как входные токены.
- **Batch API** [19][10][11]:
  - −50 % к цене, целевое время выполнения 24 часа.
  - Входной JSONL-файл до 2 GB, inline-запросы до 20 MB.
  - Работает **только через `generateContent`**.
  - Во free tier для большинства моделей «Not available».

### 1.3. Лимиты free tier (RPM / TPM / RPD)

**Официальная страница лимитов [10] на 2026-10-13 не публикует числа по моделям.** Цитата: «Rate limits depend on a variety of factors (such as your usage tier) and can be viewed in Google AI Studio… Specified rate limits are not guaranteed and actual capacity may vary». Страница AI Studio с лимитами (`aistudio.google.com/rate-limit`) открывается только после входа в аккаунт, поэтому в рамках исследования её прочитать не удалось.

Что подтверждено на [10]:
- лимиты считаются по RPM, TPM (входные токены) и RPD. Превышение любого из них даёт 429;
- лимиты действуют **на проект, а не на ключ**;
- RPD сбрасывается в полночь по тихоокеанскому времени;
- у preview- и experimental-моделей лимиты жёстче;
- spend-based лимит для free tier — «N/A».

Для перехода на Tier 1 нужен billing-аккаунт с предоплатой от $5 [25].

| Модель | RPM | TPM | RPD |
|---|---|---|---|
| `gemini-3.8-flash` | не подтверждено | не подтверждено | не подтверждено |
| `gemini-3.6-flash` | не подтверждено | не подтверждено | не подтверждено |
| `gemini-3.5-flash-lite` | не подтверждено | не подтверждено | не подтверждено |
| `gemini-3.1-flash-lite` | не подтверждено | не подтверждено | не подтверждено |
| `gemma-4-31b-it` · `gemma-4-26b-a4b-it` | не подтверждено (тезис программы «Gemma почти без лимитов» официально не подтверждён) | не подтверждено | не подтверждено |
| `gemini-embedding-2` · `gemini-embedding-001` | не подтверждено | не подтверждено | не подтверждено |

Сторонние блоги приводят по free tier противоречивые цифры, поэтому в проекте они не используются.

### 1.4. Цены paid tier, USD за 1M токенов [11]

Режим Standard; в скобках указан Batch.

| Model ID | Вход | Выход (включая thinking) | Context caching | Примечание |
|---|---|---|---|---|
| `gemini-3.8-flash` | $0.75 до 2026-12-31, с 2027-01-01 $1.50 (batch $0.375 → $0.75) | $3.75 → $7.50 (batch $1.875 → $3.75) | $0.075 → $0.15 | вводная цена [11][24] |
| `gemini-3.6-flash` | $0.75 → $1.50 (batch $0.375 → $0.75) | $3.75 → $7.50 (batch $1.875 → $3.75) | $0.075 → $0.15 | вводная цена |
| `gemini-3.5-flash-lite` | $0.30 (batch $0.15) | $2.50 (batch $1.25) | $0.03 | |
| `gemini-3.1-flash-lite` | $0.25 за текст, изображения и видео (batch $0.125) | $1.50 (batch $0.75) | $0.025 | самая дешёвая из актуальных |
| `gemini-3.1-pro-preview` | $2.00 (≤200k) / $4.00 (>200k); batch $1.00 / $2.00 | $12.00 / $18.00; batch $6.00 / $9.00 | $0.20 / $0.40 | во free tier недоступна |
| `gemini-3-flash-preview` | $0.50 (batch $0.25) | $3.00 (batch $1.50) | $0.05 | legacy |
| `gemini-2.5-pro` | $1.25 / $2.50 | $10.00 / $15.00 | $0.125 / $0.25 | доступ ограничен |
| `gemini-2.5-flash` | $0.30 | $2.50 | $0.03 | доступ ограничен |
| `gemini-2.5-flash-lite` | $0.10 | $0.40 | $0.01 | доступ ограничен |
| `gemma-4-31b-it` · `gemma-4-26b-a4b-it` | Paid: «Not available» | — | — | только free tier |
| `gemini-embedding-2` | $0.20 за текст (batch $0.10) | — | — | |

Кроме Standard, есть уровни Flex (по цене batch) и Priority (около 1.8× от Standard) [11].

### 1.5. Как Google использует данные free tier [12][11]

Gemini API Additional Terms, действуют с 2026-03-23 [12].

**Unpaid Services** — это AI Studio и бесплатная квота Gemini API.
- Google получает право использовать данные для улучшения своих продуктов: «Google uses the content you submit to the Services and any generated responses to provide, improve, and develop Google products and services and machine learning technologies».
- Ответы могут читать люди: «human reviewers may read, annotate, and process your API input and output… Do not submit sensitive, confidential, or personal information to the Unpaid Services».
- На странице цен у каждой модели есть строка «Used to improve our products: **Yes** (Free) / **No** (Paid)» [11].

**Paid Services** — API через проект с активным billing.
- Google «doesn't use your prompts… or responses to improve our products».
- Промпты логируются на ограниченный срок, только для выявления нарушений [12].

Прочие условия [12]:
- Для пользователей из EEA, Швейцарии и UK условия paid tier действуют и на бесплатное использование. К России это не относится.
- Пользователь должен быть старше 18 лет.
- Запрещено разрабатывать модели, конкурирующие с сервисом.

### 1.6. Региональная доступность и Россия [13][12]

- **Россия отсутствует** в официальном списке стран и территорий, где доступны Gemini API и Google AI Studio. Страница обновлена 2026-04-28 [13].
  - Беларуси в списке тоже нет.
  - Казахстан, Армения, Грузия, Кыргызстан и Узбекистан в списке есть [13].
- Условия требуют: «You may only access the Services (or make API Clients available to users) within an available region» [12].
- **Факт для проекта:** использование Gemini API и AI Studio с территории РФ официальной документацией не поддерживается. Обходные пути в этой заметке не рассматриваются. Последствия для архитектуры описаны в «Выводах для проекта».

## 2. Роли → модели (гипотеза, подтверждается малыми тестами)

> **Весь раздел — гипотеза.** Для каждой роли нужен мини-eval на 20–30 задачах. Метрики: доля валидных по схеме ответов, точность по эталону, стоимость, латентность и доля упёршихся в лимит запросов. Результат фиксируется в ADR. Model ID живут только в конфиге (LLM-002).

| Роль | Free-профиль (основная) | Альтернатива / paid-профиль | Local-профиль | Обоснование гипотезы |
|---|---|---|---|---|
| **planner**: многошаговое планирование маршрута, самая трудная задача | `gemini-3.8-flash`, `thinking_level=high` | `gemini-3.1-pro-preview` (только paid, $2 / $12) как верхняя граница в leaderboard | Gemma 4 31B, 4-bit | Это сильнейшая модель с бесплатным доступом: Google описывает её как «long-horizon… autonomous agents» [2][24]. Pro во free tier недоступна [11]. Вызовов немного, поэтому RPD менее критичен, чем качество. Риск — расход токенов на thinking [24]. |
| **extractor**: реакции, условия, ссылки из статей и патентов, большой объём | `gemini-3.5-flash-lite` + native structured output | `gemini-3.6-flash` для трудных документов (таблицы, Markush в патентах); на paid tier — Batch API (−50 %) | Gemma 4 26B A4B | Нужна нативная JSON Schema [16] и контекст 1M, чтобы брать патент целиком. Flash-Lite позиционируется как модель для «high-volume… data processing» [11]. Лицензированные полные тексты сюда не идут (см. «Выводы»). |
| **classifier / filter**: релевантность, тип реакции, дедупликация | `gemma-4-26b-a4b-it` | `gemini-3.5-flash-lite`; `gemini-3.1-flash-lite` — самая дешёвая платная ($0.25 / $1.50), но shutdown не раньше 2027-05-07 [23] | Gemma 4 26B A4B или Gemma 4 12B | Ответ — enum или bool, его легко провалидировать и без нативной схемы. Gemma в API бесплатна [11], а MoE с ~4B активных параметров должна быть быстрой. Структурированный вывод и реальные лимиты нужно подтвердить тестом. |
| **chat**: правки маршрута в диалоге | `gemini-3.6-flash` (thinking `low`/`medium`) | `gemini-3.8-flash`, `thinking_level=low` | Gemma 4 31B | Решает латентность. Google сам предлагает 3.6 Flash как экономную альтернативу 3.8 Flash для повседневных задач [24] и отмечает её «improved token efficiency» [22]. |
| **embeddings**: RAG по литературе | `gemini-embedding-2`, размерность зафиксирована (768 или 1536) | `gemini-embedding-001` (текст, `task_type`, список строк за один запрос) | открытая модель эмбеддингов, выбор **не исследован** | Вход до 8 192 токенов и мультимодальность (схемы реакций на рисунках PDF) [9][20]. Модель и размерность записываются в метаданные индекса, а смена модели означает полный переиндекс [20]. |

## 3. Слой абстракции моделей в Python

### 3.1. Кандидаты

Версии сверены с PyPI JSON API на 2026-10-13.

**`google-genai` — официальный SDK** [29][30]
- **Версия:** 2.30.0 (2026-10-13), `requires_python >=3.10`, классификаторы 3.10–3.14.
- **Зависимости:** httpx, pydantic ≥ 2.12.5, tenacity; aiohttp опционален.
- **Structured output:** `response_json_schema` или `response_schema`, второй принимает Pydantic-класс. Результат доступен в `response.parsed`.
- **Прочие возможности:** function calling (автоматический по умолчанию), эмбеддинги (`client.models.embed_content`), Batch (`client.batches`).
- **Usage:** `prompt_token_count`, `candidates_token_count`, `thoughts_token_count`, `cached_content_token_count`, `tool_use_prompt_token_count`, `total_token_count` [30].
- **Другие провайдеры:** не поддерживаются, только Gemini Developer API и Agent Platform (бывший Vertex).
- **Record/replay:** модуль `_replay_api_client.py` с режимами record / replay / auto / api, он вычищает `x-goog-api-key`. Но модуль **внутренний**: подчёркивание в имени, в README его нет.
- **Транспорт:** асинхронный клиент молча переключается на aiohttp, если aiohttp установлен [30].

**LiteLLM** [31][32][33][34]
- **Версия:** 1.105.0 (2026-10-11), `>=3.10,<3.15`, тяжёлые зависимости (boto3, tokenizers, huggingface-hub, openai…).
- **Смена провайдера конфигом:** строки `gemini/<model>`, Router с `model_list` в YAML, `fallbacks`, `num_retries`.
- **Structured output:** `response_format=PydanticClass`; для Gemini используется нативный `responseJsonSchema`.
- **Стоимость:** `completion_cost()`.
- **Для тестов:** `mock_response` (токены в usage пустые) и дисковый кэш. Работает ли vcrpy с aiohttp-транспортом LiteLLM — **не подтверждено**.
- **Безопасность:**
  - 2026-03-24 на PyPI были загружены троянизированные релизы 1.82.7 и 1.82.8 со стилером учётных данных. Он собирал переменные окружения, SSH-ключи и облачные креды и отправлял их на `models.litellm.cloud`. Чистый релиз — 1.83.0 [33].
  - В 2026 году опубликованы advisories уровня Critical/High, в основном по proxy-серверу [34].

**PydanticAI** [35]–[39]
- **Версия:** `pydantic-ai` / `pydantic-ai-slim` 2.55.0 (2026-10-09), `>=3.11`, классификаторы 3.11–3.14, статус Production/Stable [35].
- **Смена провайдера:**
  - Строки `'<provider>:<model>'`. Для Gemini API используется `google:<model>`; в v2 префикс `google-gla:` переименован в `google:`, а `GeminiModel` — в `GoogleModel` [36].
  - Для локальных и сторонних моделей есть префиксы `ollama:`, `vllm:`, `openrouter:`, `litellm:`.
  - Есть `FallbackModel` [36].
- **Structured output:**
  - Режимы `ToolOutput` (по умолчанию), `NativeOutput` и `PromptedOutput` [37].
  - `@agent.output_validator` + `ModelRetry` запрашивают ответ повторно с текстом ошибки; бюджет повторов задаётся через `retries={'output': N}` [37].
- **Тесты:**
  - Есть `TestModel`, `FunctionModel`, `Agent.override` и `ALLOW_MODEL_REQUESTS=False` [38].
  - Официальное руководство по тестированию VCR не упоминает [38]. Сам проект PydanticAI тестируется на кассетах: плагин `cassetter`, маркер `@pytest.mark.vcr`, чистка заголовков [39].
- **Трассировка и учёт:**
  - OpenTelemetry по GenAI semconv.
  - `RunUsage` хранит токены и оценку стоимости; ограничение бюджета — `UsageLimits(cost_limit=…)` [37][38].
- **Эмбеддинги:** `Embedder('google:gemini-embedding-001')` и `TestEmbeddingModel` [38].
- **Не подтверждено:** какой API Google (`generateContent` или Interactions) использует `GoogleModel`.

**Instructor** [40]
- **Версия:** 1.17.0 (2026-09-09), `>=3.9,<4.0`; жёстко зависит от `openai`.
- **Возможности:** `instructor.from_provider("google/…")`, повтор с ошибкой валидации через `max_retries`.
- **Оценка:** это слой структурированного вывода, а не gateway.

**Прочие варианты**
- **OpenAI SDK через OpenAI-совместимый endpoint Gemini.**
  - Адрес: `https://generativelanguage.googleapis.com/v1beta/openai/`. Статус **beta** [41].
  - Поддерживаются chat, tools, `parse(response_format=Pydantic)`, эмбеддинги, batch и `reasoning_effort`. Gemma в описании не упоминается.
  - `openai` 3.29.0 работает на httpx2 [42].
- **`any-llm-sdk` (Mozilla.ai) 1.33.4**, `>=3.11`. Провайдеры gemini и ollama имеют статус «Verified»; поддержка Pydantic `response_format` **не подтверждена** [42].
- **`langchain-google-genai` 4.4.1** слишком тяжёл для одного gateway [42].
- **DSPy 3.4.1** зависит от LiteLLM; это фреймворк оптимизации промптов [42].

**Record/replay** [43][44]
- **`vcrpy` 8.3.0** (2026-07-04), `>=3.10`, классификаторы только до 3.13. Работа на Python 3.12 подтверждена, на 3.14 — **не подтверждена**. С 8.2.0 поддерживает httpx2, в 8.2.1 исправлена небезопасная загрузка YAML-кассет [43].
- **`pytest-recording` 0.14.0** (2026-10-01), `>=3.10`. По умолчанию `--record-mode=none`, есть `--block-network` [44].
- **`pytest-vcr`** 1.0.2 вышел в 2019 году и заброшен. **`cassetter`** 0.14.0 появился только в 2026-02 [44].
- **Чистка секретов Gemini в кассетах:** `filter_headers=['x-goog-api-key', 'authorization']` и для подстраховки `filter_query_parameters=['key']` [43][30].

### 3.2. Сравнение

| | Смена провайдера конфигом | Structured output + повтор с ошибкой | Record/replay | Python | Риски |
|---|---|---|---|---|---|
| google-genai | нет (только Google) | нативная схема, `.parsed`; повтор пишем сами | внутренний `_replay_api_client`; использовать vcrpy | 3.10–3.14 | API быстро меняется (Interactions) |
| LiteLLM | да (строки, Router YAML, fallbacks) | `response_format=Pydantic`; повтора с ошибкой нет | mock/cache; совместимость vcrpy с aiohttp не подтверждена | 3.10–3.14 | supply-chain-инцидент 2026-03, CVE прокси, тяжёлые зависимости |
| PydanticAI | да (`google:`, `ollama:`, `vllm:`, `FallbackModel`) | Tool / Native / Prompted + validator + `ModelRetry` | TestModel / FunctionModel + vcrpy ≥ 8.2 / pytest-recording | 3.11–3.14 | частые релизы, переименования в v2 |
| Instructor | да (`from_provider`) | сильный повтор с ошибкой | нет | 3.9+ | узкая область |
| OpenAI SDK + compat | да (`base_url`) | `parse()` | vcrpy (httpx2) | 3.10–3.14 | compat-слой Gemini в beta |

### 3.3. Рекомендация

**Свой тонкий `app/llm/gateway.py` (LLM-001), внутри которого работает PydanticAI** с зафиксированной версией (`pydantic-ai-slim[google,openai]==2.55.*`). Как это покрывает правила:
1. **LLM-002 (роль → модель).** Строка модели берётся из конфига: `google:gemini-3.5-flash-lite`, `google:gemma-4-26b-a4b-it`, `ollama:…`. Профиль переключается переменной `LLM_PROFILE`.
2. **LLM-004 (схема и повторы).**
   - Результат описан Pydantic-типом. `output_validator` + `ModelRetry` повторяют запрос с текстом ошибки, после N попыток следует явный отказ.
   - Режим вывода задаётся на роль. Для Gemini это `NativeOutput`. Для Gemma — `PromptedOutput` или `ToolOutput`, пока нативный режим не подтверждён тестом.
3. **LLM-005 (трасса).** Токены и стоимость дают `RunUsage` и OTel. Версию промпта, хэш входа, латентность и `modelVersion` gateway добавляет сам.
4. **LLM-006 (кассеты).**
   - Юнит-тесты работают на `TestModel` / `FunctionModel` с `ALLOW_MODEL_REQUESTS=False`.
   - Интеграционные тесты идут на кассетах `pytest-recording` + `vcrpy>=8.2`, в CI с `record_mode=none` и `--block-network`.
   - Кассеты сопоставляются по методу и пути запроса. Перезапись кассет делается отдельным PR.
5. **LLM-008 (лимиты).** `FallbackModel` + `UsageLimits` + собственный rate limiter, лимиты которого берутся из конфига.
6. **Batch API и загрузка файлов** идут через «сырой» клиент `google-genai`, который отдаёт `GoogleProvider`, но тоже только внутри `app/llm/`.

LiteLLM в процесс бэкенда **не подключаем** [33][34]. Если понадобится роутинг LiteLLM, его proxy поднимается отдельным контейнером за OpenAI-совместимым endpoint.

Запасной вариант — свой gateway поверх `google-genai` + `openai` SDK с ручным повтором. Он проще по зависимостям, но retry, fallback, трассировку и учёт стоимости придётся писать самим.

## 4. Вычислительные ресурсы и локальные модели

### 4.1. Kaggle Notebooks [45][46][47][48][49]

- **Квота GPU:** «30 hours or sometimes higher depending on demand and resources» в неделю, сбрасывается еженедельно [45]. **TPU** считается отдельно: 20 ч в неделю, до 9 ч за сессию [47].
- **Ускорители** (Kaggle оговаривает: «at time of writing») [46]:

  | Вариант | Процессор | RAM |
  |---|---|---|
  | 1× Tesla P100 | 4 ядра | 29 GB |
  | 2× Tesla T4 | 4 ядра | 29 GB |
  | TPU v3-8 | 96 ядер | 330 GB |
  | только CPU | 4 ядра | 30 GB |

  В часы пик за GPU бывает очередь.
- **VRAM:** Kaggle её не указывает.
  - У T4 16 GB GDDR6, и в спецификации NVIDIA нет BF16 [48].
  - P100 выпускается с 16 или 12 GB, какой вариант у Kaggle — **не подтверждено** [49].
- **Сессия:** до 12 ч на CPU/GPU и до 9 ч на TPU [46].
- **Диск:** 20 GB в `/kaggle/working` сохраняются после сессии, дополнительный scratch — нет [46].
- **Интернет:** включается переключателем в Settings [46].
- **Idle timeout:** документация противоречит сама себе — 20 мин [46] и 60 мин [45].
- **Фоновые прогоны:** «Save & Run All» длится до 12 ч, можно запускать несколько параллельно. Kaggle API запускает версии без интерактивной сессии [45][46].
- **Верификация телефона** в официальной документации **не подтверждена**.
- **Бонус для Colab Pro/Pro+:** +15 / +30 GPU-часов в неделю на Kaggle, акция помечена как экспериментальная [46].

### 4.2. Google Colab (free) [50][51]

- **GPU:** FAQ конкретных типов не называет — они «vary over time», а бесплатный доступ к GPU «heavily restricted». Что на free дают T4, **не подтверждено**.
- **Сессия:** «at most 12 hours, depending on availability and your usage patterns». Лимиты не публикуются и «sometimes fluctuate» [50].
- **Что запрещено на бесплатных рантаймах:** SSH и remote desktop, работа в основном через веб-UI вместо ноутбука, распределённые воркеры [50].
- **Цены:** Pro $9.99 в месяц, Pro+ $49.99 в месяц, Pay As You Go 100 CU за $9.99. Страница была показана для региона «KZ», в других странах цены могут отличаться [51].
- **Доступность Colab и Kaggle из России** по официальным страницам **не подтверждена**.

### 4.3. Открытые модели: Gemma 4 [15][52][53][54][55]

- **Лицензия.** Gemma 4 вышла под **Apache 2.0** («License: Apache 2.0» в model card [52]). Это первая Gemma под OSI-лицензией [53]. Gemma 3 и более ранние остаются под Gemma Terms of Use.
- **Размеры** [52]:
  - E2B — 2.3B эффективных параметров, контекст 128K;
  - E4B — 4.5B эффективных, 128K;
  - 12B «Unified» — 256K;
  - 26B A4B MoE — 25.2B всего, 3.8B активных, 256K;
  - 31B dense — 30.7B, 256K.
- **Веса:** выложены в Hugging Face (`google/gemma-4-*`, включая `-it` и QAT Q4_0) и на Kaggle [54][15].
- **Память под веса** (официально, с накладными ~20 %, без KV-кэша) [15] и оценка, что куда поместится:

| Модель | BF16 | 8-bit (SFP8) | 4-bit (Q4_0) | 1× T4 16 GB (оценка) | 2× T4 (оценка, с шардированием) |
|---|---|---|---|---|---|
| E2B | 11.4 GB | 5.7 GB | 2.9 GB | все варианты | все |
| E4B | 17.9 GB | 8.9 GB | 4.5 GB | 8-bit, 4-bit | также FP16 |
| 12B | 26.7 GB | 13.4 GB | 6.7 GB | 4-bit; 8-bit впритык при коротком контексте | 8-bit |
| 26B A4B | 57.7 GB | 28.8 GB | 14.4 GB | нет (только с CPU offload, медленно) | 4-bit |
| 31B | 69.9 GB | 34.9 GB | 17.5 GB | нет | 4-bit |

Последние две колонки — **наша оценка**. Считали так: веса + KV-кэш FP16 на 32K токенов (≈0.5–3.5 GB, оценка по `config.json`) + ~1 GB на рантайм, и всё это должно уложиться в ~15 GB на карту. Два T4 не образуют единый пул на 32 GB: модель приходится шардировать (tensor или pipeline parallel, либо `device_map="auto"`). MoE-модели 26B A4B нужно держать в памяти все 25.2B параметров [15].

- **Другие открытые модели** [55]:
  - семейство Qwen3.5: dense 0.8B–27B и MoE от 35B-A3B;
  - Qwen3.8-27B: Apache-2.0, контекст 262K.

  Химически специализированных версий Gemma или Qwen не найдено.

### 4.4. Движки инференса на T4/P100 [56][57][58][59]

- **vLLM** требует compute capability ≥ 7.5: **T4 подходит, P100 (CC 6.0) — нет** [56].
  - На Turing работают AWQ, GPTQ, INT8 W8A8, bitsandbytes и GGUF; FP8 не работает. Gemma 4 есть в списке поддерживаемых моделей [56].
  - У T4 нет BF16, поэтому нужен `--dtype half` или квантизация. Стабильна ли Gemma 4 в FP16 — **не подтверждено**.
- **Ollama** требует CC ≥ 5.0; P100 и T4 есть в списке поддерживаемых. Размеры тегов `gemma4`: от 4.6–7.5 GB (e2b) до 19–20 GB (31b) [57]. Версия драйвера на Kaggle **не подтверждена**.
- **transformers + bitsandbytes:** NF4/FP4 работают при CC ≥ 6.0 (P100 и T4), LLM.int8 — только при ≥ 7.5, то есть на T4 [58].
- **llama.cpp** собирается с `-DGGML_CUDA=ON` [59].

### 4.5. Когда локальный инференс оправдан для проекта

**Оправдан:**
- **Замороженные eval-прогоны для статьи (EVAL-*).** Фиксируются веса, квантизация, версия движка, используется greedy-декодирование. В API так не получится: id перенаправляются, `temperature` объявлен deprecated (1.1).
- **Лицензированные полные тексты и данные эксперта**, которые нельзя отправлять во free tier (1.5).
- **Профиль непрерывности** на случай, если доступа к Gemini API нет (1.6).
- **Массовая классификация**, когда упираемся в RPD free tier.
- **Эксперименты с дообучением.** QLoRA на E4B или 12B на 2× T4 по оценке реалистична, но **не проверено**.

**Не оправдан:**
- **Интерактивный чат и planner в UI:** T4 медленный, BF16 нет, а самое большое, что помещается, — 31B в 4-bit.
- **Повседневная разработка:** ~30 GPU-часов в неделю, сессии до 12 ч, idle timeout, очереди и загрузка 15–20 GB весов при каждом запуске.

## 5. Химические инструменты: версии, Python, установка

### 5.1. RDKit [60][61]

- **Версия:** 2026.9.1 (на PyPI с 2026-10-09; релиз на GitHub `Release_2026_09_1` — 2026-10-03), лицензия BSD-3-Clause. `requires_python` не задан, зависимость одна — numpy.
- **Колёса:**
  - Python: cp310, cp311, cp312, cp313, cp314, cp315.
  - Платформы: `macosx_11_0_arm64`, `manylinux_2_28_x86_64`, `manylinux_2_28_aarch64`, `win_amd64`.
  - **Колёс для macOS x86_64 в 2026.x нет** (последние были в 2025.9.1) [60].
- **conda-forge:** сборки 2026.09.1 есть для py311–py314 [61].

### 5.2. AiZynthFinder [62]–[65]

- **Версия:** 4.4.1 (2025-12-09), лицензия MIT.
  - `requires_python` — **`>=3.10,<3.13`**, классификаторы 3.10–3.12; README пишет «python 3.10 - 3.12» [62].
- **Жёсткие пины:** **`rdkit<2024.0.0,>=2023.9.1`**, **`numpy<2.0.0`**, `onnxruntime>=1.23,<2`; extra `[tf]` требует `tensorflow>=2.20` [62].
- **Python 3.13:** поддержка 3.13 и numpy 2 есть только в **открытом, не выпущенном** PR #205 (создан 2026-09-16). По словам мейнтейнера, «We haven't fully tested it with python 3.13 yet» [63].
- **Публичные данные:** их скачивает команда `download_public_data <папка>`, она же создаёт `config.yml` [62][64]. Всего около **0.79 GB**:
  - Zenodo 7797465 (CC-BY-4.0): `uspto_model.onnx` (91.5 MB), `uspto_ringbreaker_model.onnx` (15.0 MB), `uspto_filter_model.onnx` (16.8 MB);
  - Zenodo 7341155: шаблоны реакций (`uspto_unique_templates.csv.gz`, 3.3 MB);
  - figshare: ZINC stock `zinc_stock_17_04_20.hdf5` (663.2 MB) [64].
- **`config.yml`:** секции `expansion`, `filter`, `stock`, `search` (`algorithm: mcts`, `iteration_limit` 100, `time_limit` 120 s, `max_transforms` 6) и `post_processing`. Поддерживается подстановка `${VAR}` [65].
- **Работа только на CPU** возможна: по умолчанию ставится CPU-сборка `onnxruntime`. Автоматическая поддержка GPU пока только в открытом PR #197, а сам мейнтейнер оценивал выигрыш от GPU как «only a very small advantage» [63].
- **Наша проверка для Mac разработчика** (arm64, 16 GB RAM): у `rdkit 2023.9.6` есть колесо `cp312-macosx_11_0_arm64`, у `onnxruntime` 1.31.0 — `cp312-macosx_14_0_arm64` [60][74]. Отдельное окружение на Python 3.12 локально выглядит реализуемым. Установку мы **не запускали**.

### 5.3. ASKCOS v2 [66][67][68]

- **Где код:** **GitLab** `gitlab.com/mlpds_mit/askcosv2/askcos2_core`, лицензия **MIT**. В GitHub-организации ASKCOS лежит только v1 [66].
- **Версия:** последний релиз 2026.07 [67].
- **Развёртывание:**
  - `git clone … && make deploy`; рекомендован Docker Compose на одной машине, Kubernetes поддерживается ограниченно [67].
  - API-шлюз на FastAPI, документация на порту `:9100/docs` [66][67].
  - Есть облегчённые конфигурации, например `module_config_backend_retro_minimal.py` (только модель template-relevance) [67].
- **Железо:**
  - CPU x86, не меньше 4 ядер; **Apple Silicon не поддерживается**.
  - **RAM ≥ 32 GB** («highly recommended» для полной сборки).
  - GPU нужен только для переобучения: ≥ 8 GB VRAM, CUDA ≥ 11.3. В конфигурации по умолчанию `"enable_gpu": False`.
  - Объём диска для v2 **не подтверждён** [66][67].
- **ПО:** рекомендованы Ubuntu ≥ 20.04 и Docker ≥ 20. Внутри образа шлюза Python 3.13.15 и rdkit 2026.3.6 [66].
- **Публичный сервер** `askcos.mit.edu` отвечает. Его Terms of Service ничего не говорят об автоматическом доступе или использовании API, поэтому разрешение на такое использование **не подтверждено** [68].

### 5.4. Syntheseus [69][70]

- **Версия:** 0.9.0 (PyPI, 2026-09-23), лицензия MIT, `requires_python >=3.8`. Ядро тестируется в CI на **3.8–3.13** [69].
- **Одношаговые модели (11):**
  - RetroChimera (рекомендована по умолчанию) и её подмодели RetroChimeraEdit и RetroChimeraDeNovo — обучены на Pistachio;
  - Chemformer, GLN, Graph2Edits, LocalRetro, MEGAN, MHNreact, RetroKNN, RootAligned — обучены на USPTO-50K.

  Чекпойнты скачиваются автоматически с figshare [69].
- **Поиск:** Retro*, MCTS, PDVN (CLI), а в библиотеке ещё breadth-first и случайный поиск [69].
- **Extras:** по одному на модель (`chemformer`, `graph2edits`, `local-retro`, `megan`, `mhn-react`, `retro-knn`, `retrochimera`, `root-aligned`), плюс `all-single-step` и `all`. GLN через pip не ставится, для него нужен отдельный Docker-образ [69].
- **Ограничения по Python для моделей:**
  - Официальное полное окружение `environment_full.yml` фиксирует **python==3.9.7** (поддержка 3.9 закончилась 2025-10-31), pytorch 2.2.2 и rdkit 2023.09.6 [69][75].
  - `syntheseus-megan` фиксирует `tensorflow==2.20.0` (колёса до cp313).
  - `syntheseus-local-retro` требует `pandas<2.2` (колёса до cp312) [70].

### 5.5. RXNMapper [71][72][73]

- **Версия:** 0.4.3 (2026-02-13), лицензия MIT, `requires_python >=3.6`. Классификаторы и CI доходят только до **3.11** [71].
- **Зависимости:** `torch>=1.5.0`, **`transformers<5.0.0,>=4.0.0`**, `rxn-chem-utils`. Поддержка transformers 5 пока в **открытом** PR #81, который ссылается на CVE в ветке 4.x [72].
- **Python 3.12:** проблему с установкой исправили в 0.3.1, и есть пользовательский отчёт, что всё работает (#54). Официально **не подтверждено** [72].
- **Риск (наш вывод, отдельного issue нет):** `core.py` по-прежнему делает `import pkg_resources`, а setuptools 82.0.0 (2026-02-08) удалил `pkg_resources` [71][73]. Без пина `setuptools<82` импорт, вероятно, упадёт.

### 5.6. Прочее [74][75]

- **`ord-schema` 0.9.2** (2026-10-13): `>=3.11`, классификаторы 3.11–3.14, требует **`rdkit>=2025.03.4`**. Это **прямо противоречит** пину AiZynthFinder `rdkit<2024`.
- **`rxn-chem-utils` 1.6.0** (2024-07-18, классификаторы до 3.11) и **`rdchiral` 1.1.0** (2021) — чистый Python.
- **`numpy` 2.5.x** требует `>=3.12`. **FastAPI** 0.143.0 — `>=3.10`.
- **Жизненный цикл Python** (только security-фиксы):
  - 3.11 — до 2027-10;
  - 3.12 — до 2028-10;
  - 3.13 — до 2029-10.

  Python 3.14 получает багфиксы до 2030-10 [75].

### 5.7. Матрица совместимости и версия Python

| Инструмент (последняя версия) | 3.11 | 3.12 | 3.13 | 3.14 |
|---|---|---|---|---|
| RDKit 2026.9.1 | ✅ колёса | ✅ | ✅ | ✅ |
| AiZynthFinder 4.4.1 | ✅ | ✅ | ❌ `<3.13` (PR #205 не выпущен) | ❌ |
| ASKCOS v2 2026.07 | Docker; на хосте Python ≥ 3.6, в контейнере 3.13; **только x86** | то же | то же | то же |
| Syntheseus 0.9.0 (ядро) | ✅ CI | ✅ CI | ✅ CI | не подтверждено (нет в CI) |
| Syntheseus, одношаговые модели | не подтверждено | не подтверждено | не подтверждено | вероятно ❌ (у TF 2.20 нет cp314) |
| RXNMapper 0.4.3 | ✅ | не подтверждено (есть пользовательский отчёт); нужен `setuptools<82` | не подтверждено | не подтверждено |
| ord-schema 0.9.2 | ✅ | ✅ | ✅ | ✅ |
| google-genai 2.30.0 / PydanticAI 2.55.0 | ✅ | ✅ | ✅ | ✅ |
| vcrpy 8.3.0 | ✅ | ✅ | ✅ | не подтверждено (нет классификатора) |

**Несовместимости:**
1. AiZynthFinder (`rdkit<2024`, `numpy<2`) нельзя поставить в одно окружение с ord-schema (`rdkit>=2025.03.4`) и современным стеком на numpy 2 — **независимо от версии Python**.
2. Python 3.14 исключает AiZynthFinder и MEGAN на TensorFlow, а для vcrpy поддержка 3.14 не подтверждена.
3. ASKCOS не запускается на Apple Silicon и требует ≥ 32 GB RAM. На Mac разработчика (arm64, 16 GB — наша проверка) его не поднять.
4. RXNMapper ограничен `transformers<5` и `setuptools<82`.

**Рекомендация: Python 3.12 для основного бэкенда.** Это самая новая версия, на которой все нужные основному окружению пакеты подтверждены классификаторами или CI. Исключение — RXNMapper: для 3.12 есть только пользовательский отчёт. Кроме того, на 3.12 доступен numpy 2.5, а security-поддержка идёт до 2028-10.

Версия фиксируется в `.python-version` и через uv, потому что системный `python3` на машине разработчика — 3.14.8 (наша проверка).

Тяжёлые движки выносятся в отдельные сервисы:
- **AiZynthFinder** — отдельное окружение или контейнер на 3.12 с `rdkit 2023.9.x` и `numpy<2` за небольшим REST-адаптером (`sources/aizynthfinder`).
- **ASKCOS v2** — отдельный Docker Compose на x86 Linux с ≥ 32 GB RAM.
- **Одношаговые модели Syntheseus** — отдельный контейнер по `environment_full.yml`.
- **RXNMapper** — в основном окружении с пинами, а если стек потребует transformers 5, тоже выносится отдельно.

## 6. Как проверяем, что доступ работает

### 6.1. Чек-лист

1. **Ключ.** Хранится только в `.env` как `GEMINI_API_KEY`; если задан `GOOGLE_API_KEY`, приоритет у него [28]. `.env` в `.gitignore`, gitleaks зелёный (CORE-004). Ключ должен быть authorization key или иметь ограничения: неограниченные standard keys API отклоняет [28].
2. **Доступность моделей.** `models.list` показывает, какие id из конфига реально доступны проекту. Особенно важно из-за ограниченного доступа к 2.5 и перенаправления id [1][23].
3. **Вызов на каждую роль.** Один минимальный вызов на роль с крошечной Pydantic-схемой (например, `{"ok": bool}`). Ответ валидируется, в лог пишется строка формата 6.2.
4. **Эмбеддинги.** Один вызов; размерность вектора совпадает с конфигом.
5. **Обработка 429.** Бэкофф, затем fallback по цепочке роли, затем явная запись о деградации в трассе (LLM-008).
6. **Кассеты.** Прогон с `LLM_MODE=record`, затем `LLM_MODE=replay` **без сети и с пустым ключом**: тест должен пройти (LLM-006). В кассете нет заголовка `x-goog-api-key` и query-параметра `key`.
7. **Лимиты.** Лимиты своего проекта из AI Studio перенесены в конфиг с датой, когда их сняли (1.3).

### 6.2. Что должно быть в логе успешного вызова

Поля берутся из ответа API:
- `generateContent`: `usageMetadata.promptTokenCount`, `candidatesTokenCount`, `thoughtsTokenCount`, `cachedContentTokenCount`, `toolUsePromptTokenCount`, `totalTokenCount`, а также `modelVersion` и `responseId` [27].
- Interactions API: `usage.total_input_tokens`, `total_output_tokens`, `total_thought_tokens`, `total_cached_tokens`, `total_tool_use_tokens`, `total_tokens` [26]. В примере на странице URL context [18] имена полей другие (`input_tokens`, `output_tokens`, `thoughts_tokens`), поэтому их нужно сверить на первом реальном вызове.

```json
{
  "ts": "2026-10-13T12:00:00Z",
  "provider": "gemini",
  "api": "generateContent",
  "profile": "free",
  "role": "extractor",
  "model_requested": "gemini-3.5-flash-lite",
  "model_version": "<modelVersion из ответа>",
  "response_id": "<responseId из ответа>",
  "prompt_id": "extract_reaction@v1",
  "input_sha256": "9f2c…",
  "latency_ms": 1840,
  "tokens": {"input": 2310, "output": 412, "thinking": 0, "cached": 0, "total": 2722},
  "schema_valid": true,
  "retries": 0,
  "http_status": 200,
  "cost_usd_est": 0.0,
  "mode": "live",
  "key_source": "env:GEMINI_API_KEY"
}
```

**Чего в логе быть не должно:** ключа или его фрагментов, URL с `?key=`, заголовков запроса и полного текста промпта. Вместо текста пишется хэш, а сам промпт и так лежит версионированным в `prompts/`.

---

## Выводы для проекта

> Всё ниже — наши интерпретации и решения-кандидаты, а не цитаты.

1. **Gemini не может быть единственным провайдером.** Россия не входит в список доступных регионов [13], а условия требуют использовать сервис только оттуда [12]. Поэтому инвариант 4 («модель меняется конфигом») — требование непрерывности работы, а не удобство.
   - В конфиге три профиля: `free`, `paid`, `local`. Профиль `local` (Gemma 4 через vLLM или Ollama) обязан проходить те же smoke-тесты.
   - Как программа обеспечивает легальный доступ участников, нужно выяснить у организаторов (см. «Открытые вопросы»).
2. **Free tier подходит только для открытых данных.** Free tier означает «content used to improve our products» и возможное чтение людьми [12]. Поэтому через него идут только патенты, OA-статьи с подходящей лицензией, записи ORD и аннотации. Лицензированные полные тексты и данные эксперта идут через paid или local. В Interactions API — `store=false`.
3. **Воспроизводимость — только кассеты и замороженные модели.** `temperature` объявлен deprecated, а id перенаправляются на новые модели [22][23]. Поэтому:
   - в трассе обязательно пишется `modelVersion` (дополнение к LLM-005);
   - числа для статьи получаются из кассет или из локальных замороженных моделей (EVAL-*);
   - нужно следить за `changelog` и `deprecations`.
4. **Лимиты неизвестны заранее, их нужно снять в своём проекте.** Free-tier лимиты по моделям официально не опубликованы [10]. Владелец ключа снимает их в AI Studio, они попадают в конфиг, а rate limiter строится на них. Лимит считается на проект, поэтому несколько ключей его не увеличивают [10].
5. **Без paid tier нет Batch и Search grounding.** Batch для большинства моделей и Search grounding для Gemini 3+ во free tier недоступны [11]. Массовое извлечение во free-профиле идёт последовательно через limiter, а поиск литературы — через собственные адаптеры `sources/`, что лучше и для происхождения фактов (инвариант 2).
6. **Роли (гипотеза):**
   - planner `gemini-3.8-flash`;
   - extractor `gemini-3.5-flash-lite`;
   - classifier `gemma-4-26b-a4b-it`;
   - chat `gemini-3.6-flash`;
   - embeddings `gemini-embedding-2` с фиксированной размерностью.

   Подтверждается мини-eval и ADR.
7. **Gateway:** свой фасад `app/llm/gateway.py` + PydanticAI 2.55.x + `pytest-recording`/`vcrpy>=8.2`. LiteLLM в процесс не подключаем. Оформить ADR после спайка.
8. **Окружение:**
   - Python **3.12** для бэкенда (через uv, `.python-version`);
   - AiZynthFinder — отдельное окружение 3.12 с `rdkit 2023.9.x` и `numpy<2`;
   - ASKCOS v2 — отдельный x86-сервер с ≥ 32 GB RAM;
   - модели Syntheseus — отдельный контейнер;
   - RXNMapper — с пинами `transformers<5` и `setuptools<82`.

   Оформить ADR о версии Python и разбиении на сервисы.
9. **Kaggle 2× T4** нужен для финальных локальных прогонов: Gemma 4 26B A4B или 31B в 4-bit через vLLM (AWQ/GPTQ) или llama.cpp. Это «локальные близнецы» API-моделей `gemma-4-*-it`, на которых можно сравнить API и локальный инференс на одинаковых задачах.

## Открытые вопросы

**Для самостоятельной проверки (малые тесты):**
- Реальные лимиты free tier (RPM/TPM/RPD) по каждой модели для нашего проекта: страница AI Studio Rate limits требует входа.
- Поддерживает ли Gemma 4 в Gemini API нативный structured output (`response_format` с JSON Schema)? Работает ли Search grounding для Gemma (документация [14] и страница цен [11] противоречат друг другу)?
- Какой API Google (`generateContent` или Interactions) использует `GoogleModel` в PydanticAI, и как это влияет на Batch и `store`?
- Цена и лимиты `gemini-embedding-001` (на странице цен её нет).
- Как vcrpy работает на Python 3.12 с httpx2 и с aiohttp-транспортом google-genai.
- Kaggle: какой P100 (12 или 16 GB), какая версия драйвера, нужна ли верификация телефона. Colab free: всё ещё ли T4.
- Стабильна ли Gemma 4 в FP16 на T4 под vLLM.
- Запускается ли RXNMapper 0.4.3 на Python 3.12 с `setuptools<82`. Работают ли одношаговые модели Syntheseus (LocalRetro, RetroChimera) вне Python 3.9.7.
- Сколько места на диске нужно ASKCOS v2 (не подтверждено), какая минимальная retro-конфигурация подойдёт.
- Условия использования чекпойнтов RetroChimera, обученных на Pistachio (коммерческий датасет), и данных AiZynthFinder (CC-BY-4.0) в нашем открытом проекте.
- Разрешено ли автоматизированное использование публичного `askcos.mit.edu`.

**Для организаторов программы и эксперта** (перенести в `docs/expert/questions.md`, DOC-005):
- Как программа обеспечивает участникам из РФ легальный доступ к Gemini API или AI Studio: регион, ключи, инфраструктура? Есть ли бюджет на paid tier?
- Есть ли у ИТМО x86-сервер с ≥ 32 GB RAM (для ASKCOS) или GPU-сервер вместо Kaggle/Colab?
- Какие лицензии на полные тексты есть у ИТМО (TDM-условия издательств), и можно ли передавать эти тексты внешним LLM API на paid tier?
