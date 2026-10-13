# Анализ и сравнение существующих решений на мировых рынках

- **Дата:** 2026-10-13
- **Вопрос:** какими способами задача «получить несколько вариантов маршрута синтеза для одобренного препарата» решается сегодня (люди, автоматизация, ИИ-конкуренты, бенчмарки), какова эффективность каждого способа, как устроен его конвейер и чего в этих решениях нет. Нужно для позиционирования платформы и для раздела «related work» статьи.
- **Охват:** 16 основных решений + краткие справки (~15 дополнительных), 4 группы бенчмарков.
- **Границы:** только уровень ПО, рынка и методик оценки. Химические процедуры, условия реакций и конкретные маршруты веществ в заметке отсутствуют сознательно (SAFE-004, DOC-004).

## Как читать заметку

- **Метки доказательств:** `VENDOR` — заявление вендора; `DEV` — публикация, написанная авторами самого инструмента (peer-review есть, независимости нет); `IND` — независимая третья сторона.
- Числа без метки `IND` нельзя использовать в статье как сравнение: единого воспроизводимого бенчмарка коммерческих систем не существует (см. «Что работает / что нет»).
- «не подтверждено» означает, что факт не удалось увидеть в первоисточнике; выдумывать нельзя (CORE-005).
- Часть источников читалась через зеркала (Europe PMC, arXiv HTML, Crossref API), потому что издательские сайты (nature.com, pubs.rsc.org, pubs.acs.org, sciencedirect) отдавали 403 или редирект на логин. Это помечено в таблице.
- Все страницы из таблицы были открыты в ходе этого обзора (сбор шёл шестью параллельными исследовательскими прогонами с требованием дословных цитат). Выборочно перепроверены вручную и поэтому наиболее надёжны источники [2], [25], [27], [31], [38], [54], [57], [69], [77], [90], [94]. Факты, встречавшиеся только в поисковой выдаче, в заметку не включены.

## Источники

| # | Источник (DOI / URL) | Тип | Дата доступа |
|---|---|---|---|
| 1 | https://www.synthiaonline.com/resources/articles/research-grants-2026-advancing-molecule-synthesis-and-discovery | сайт вендора (SYNTHIA) | 2026-10-13 |
| 2 | https://www.chemeurope.com/en/products/1130694/synthia-lab.html | каталог продукта, цена SYNTHIA Lab | 2026-10-13 |
| 3 | https://content.knowledgehub.wiley.com/wp-content/uploads/2026/01/Transforming-Chemical-Synthesis-Pathways_Merck.pdf | whitepaper Merck KGaA (01.2026) | 2026-10-13 |
| 4 | https://www.pharmaceuticalprocessingworld.com/merck-kgaa-qa-solving-pharmas-make-step-with-synthias-ai-synthesis-planning/ | интервью с вендором (28.03.2025) | 2026-10-13 |
| 5 | https://doi.org/10.1016/j.chempr.2018.02.002 | статья, Klucznik et al., Chem 2018 (Chematica) | 2026-10-13 |
| 6 | https://doi.org/10.1038/s41586-020-2855-y | статья, Mikulak-Klucznik et al., Nature 2020 (метаданные через Europe PMC, PMID 33049755) | 2026-10-13 |
| 7 | https://kyodonewsprwire.jp/release/202312053863 | пресс-релиз AIDDISON (05.12.2023) | 2026-10-13 |
| 8 | https://www.cas.org/ja/press-releases/cas-drives-increase-in-r-d-productivity-with-launch-of-breakthrough-retrosynthesis-planner-in-scifinder-n | пресс-релиз CAS (01.07.2019) | 2026-10-13 |
| 9 | https://www.cas.org/solutions/cas-scifinder-discovery-platform/retrosynthesis | страница продукта CAS | 2026-10-13 |
| 10 | https://www.cas.org/press-releases/stereoselective-labeling-cas-scifinder-retrosynthesis | пресс-релиз CAS (29.10.2024) | 2026-10-13 |
| 11 | https://www.cas.org/press-releases/cas-scifinder-integrates-transformative-new-science-smart-ai-capabilities-to-enhance-r-d-efficiency-and-boost-innovation | пресс-релиз CAS (04.08.2025) | 2026-10-13 |
| 12 | https://www.cas.org/solutions/cas-scifinder-discovery-platform/cas-scifinder/releases | release notes CAS SciFinder (по 08.2026) | 2026-10-13 |
| 13 | https://www.elsevier.com/products/reaxys/predictive-retrosynthesis | страница продукта Reaxys PR | 2026-10-13 |
| 14 | https://www.prnewswire.com/news-releases/elsevier-and-pendingai-collaborate-on-ai-driven-chemistry-retrosynthesis-tool-301127890.html | пресс-релиз Elsevier + Pending.AI (15.09.2020) | 2026-10-13 |
| 15 | https://www.elsevier.com/about/press-releases/elsevier-and-iktos-partner-to-deliver-an-ai-driven-synthetic-chemistry | пресс-релиз Elsevier + Iktos (05.03.2024) | 2026-10-13 |
| 16 | https://www.elsevier.support/reaxys/answer/reaxys-predictive-retrosynthesis-powered-by-iktos-release-notes-for-april-2025 | release notes Reaxys PR / Iktos (04.2025) | 2026-10-13 |
| 17 | https://www.elsevier.support/reaxys/answer/release-notes-for-june-2025 | release notes Reaxys (06.2025) | 2026-10-13 |
| 18 | https://www.elsevier.support/reaxys/answer/release-notes-march-2026 | release notes Reaxys (03.2026) | 2026-10-13 |
| 19 | https://www.drugdiscoveryonline.com/doc/using-synthesis-and-route-design-technology-to-approach-api-complexity-0001 | кейс Lonza + Elsevier (соавторы — вендор) | 2026-10-13 |
| 20 | https://lib.ch.ntu.edu.tw/wp-content/uploads/Reaxys_2023_%E9%80%86%E5%90%88%E6%88%90AI%E8%A9%A6%E7%94%A8%E6%B4%BB%E5%8B%95_%E5%8F%B0%E7%81%A3%E5%A4%A7%E5%AD%B8.pdf | презентация Elsevier (2023.09) с пилотами ETH/Radboud | 2026-10-13 |
| 21 | https://doi.org/10.1038/nature25978 | статья, Segler, Preuss, Waller, Nature 2018 (3N-MCTS; метаданные через Europe PMC) | 2026-10-13 |
| 22 | https://iktos.ai/solution/spaya | страница продукта Spaya | 2026-10-13 |
| 23 | https://doi.org/10.1186/s13321-023-00742-8 | статья, Parrot et al., J Cheminform 2023 (RScore; полный текст PMC10507964) | 2026-10-13 |
| 24 | https://iktos.ai/ | сайт вендора Iktos (новости 2026) | 2026-10-13 |
| 25 | https://github.com/rxn4chemistry/rxn4chemistry | репозиторий + объявление об отключении IBM RXN (28.10.2026) | 2026-10-13 |
| 26 | https://github.com/rxn4chemistry/rxn-sandbox | репозиторий self-hosted IBM RXN | 2026-10-13 |
| 27 | https://accelerate.science/rxn-pricing | прайс IBM RXN | 2026-10-13 |
| 28 | https://accelerate.science/projects/rxn | страница продукта IBM RXN | 2026-10-13 |
| 29 | https://doi.org/10.1021/acscentsci.9b00576 | статья, Schwaller et al., ACS Cent Sci 2019 (Molecular Transformer; полный текст PMC6764164) | 2026-10-13 |
| 30 | https://doi.org/10.1039/c9sc05704h | статья, Schwaller et al., Chem Sci 2020 (round-trip, coverage; полный текст PMC8152799) | 2026-10-13 |
| 31 | https://arxiv.org/abs/2510.10645 | препринт RetroTrim (Molecule.one), v3 от 08.12.2025 | 2026-10-13 |
| 32 | https://www.chemical.ai/ai-retrosynthesis-faq | FAQ вендора Chemical.AI | 2026-10-13 |
| 33 | https://www.chemical.ai/chemairs | страница продукта ChemAIRS | 2026-10-13 |
| 34 | https://pr.mono.ipros.com/en/patcore/news/detail/198377/ | релиз дистрибьютора Patcore (01.2026) | 2026-10-13 |
| 35 | https://www.chemical.ai/news/aragen-collaboration | кейс вендора (Aragen, on-prem) | 2026-10-13 |
| 36 | https://postera.ai | сайт PostEra (2026: продукт Proton) | 2026-10-13 |
| 37 | https://doi.org/10.1126/science.abo7201 | статья, Boby et al., Science 2023 (COVID Moonshot; полный текст PMC7615835) | 2026-10-13 |
| 38 | https://www.biorxiv.org/content/10.1101/2025.03.07.642029v1.full | препринт Mokaya, Deane, Bradley (10.03.2025), независимое сравнение Postera и AiZynthFinder | 2026-10-13 |
| 39 | https://www.cambridgenetwork.co.uk/news/optibrium-and-postera-collaborate-integrate-ai-drug-discovery-solutions | новость об интеграции StarDrop + Manifold (15.03.2023) | 2026-10-13 |
| 40 | https://molecule.one | сайт Molecule.one (2026: Maria) | 2026-10-13 |
| 41 | https://www.standardindustries.com/standard-industries-announces-molecule-one-as-winner-of-1-million-ai-challenge/ | пресс-релиз конкурса (12.06.2025) | 2026-10-13 |
| 42 | https://www.prnewswire.com/news-releases/grace-and-moleculeone-to-transform-peptide-building-block-synthesis-with-ai-and-automation-302635354.html | пресс-релиз (08.12.2025) | 2026-10-13 |
| 43 | https://arxiv.org/abs/2412.05269 | препринт RetroChimera (Microsoft + Novartis), v2 от 12.08.2025 | 2026-10-13 |
| 44 | https://ai.azure.com/catalog/models/RetroChimera | карточка модели в Azure AI Foundry (Preview, MIT) | 2026-10-13 |
| 45 | https://www.chemify.io/technology | сайт Chemify (ASSEMBLER, χDL) | 2026-10-13 |
| 46 | https://chemai.io/publications | сайт ChemAI (ex-Deepmatter/InfoChem), Smartchemistry | 2026-10-13 |
| 47 | https://www.simbiosys.com | сайт SimBioSys: химического ПО больше нет, /archem/ → 404 | 2026-10-13 |
| 48 | https://github.com/MolecularAI/aizynthfinder | репозиторий AiZynthFinder (MIT, v4.4.1 от 09.12.2025, 904 звезды) | 2026-10-13 |
| 49 | https://doi.org/10.1186/s13321-020-00472-1 | статья, Genheden et al., J Cheminform 2020 (полный текст PMC7672904) | 2026-10-13 |
| 50 | https://doi.org/10.1186/s13321-024-00860-x | статья, Saigiridharan et al., J Cheminform 2024 (AiZynthFinder 4.0; полный текст PMC11112899) | 2026-10-13 |
| 51 | https://doi.org/10.1039/d3md00651d | статья, Shields et al., RSC Med Chem 2024 (3 года использования в AstraZeneca; доступна только аннотация) | 2026-10-13 |
| 52 | https://doi.org/10.1039/d5sc00927h | статья, Westerlund et al., Chem Sci 2025 (ограничения по связям; аннотация через Europe PMC) | 2026-10-13 |
| 53 | https://arxiv.org/html/2501.01835v1 | препринт ASKCOS v2 (01.2025) | 2026-10-13 |
| 54 | https://askcos-docs.mit.edu/release-notes/7.2-ASKCOS-v2/12-2026.04-Release-Notes.html | release notes ASKCOS v2 (04.2026, MCP chatbot) | 2026-10-13 |
| 55 | https://doi.org/10.1021/acs.accounts.5c00155 | статья, ASKCOS, Acc Chem Res 2025 (метаданные Crossref) | 2026-10-13 |
| 56 | https://github.com/microsoft/syntheseus | репозиторий Syntheseus (MIT, v0.8.0 от 03.08.2026, 212 звёзд) | 2026-10-13 |
| 57 | https://arxiv.org/html/2310.19796v3 | препринт Maziarz et al., Syntheseus (журнальная версия Faraday Discuss. 2025, 256, 568–586, DOI 10.1039/D4FD00093E) | 2026-10-13 |
| 58 | https://retrobiocat.com | веб-приложение RetroBioCat (v2025.10.16) | 2026-10-13 |
| 59 | https://doi.org/10.1038/s41929-020-00556-z | статья, Finnigan et al., Nat Catal 2021 (полный текст PMC7116764) | 2026-10-13 |
| 60 | https://github.com/willfinnigan/RetroBioCat-2 | репозиторий rbc2 (CC BY-NC 4.0, 5 звёзд) | 2026-10-13 |
| 61 | https://doi.org/10.1021/acscatal.3c01418 | статья, RetroBioCat Database, ACS Catal 2023 | 2026-10-13 |
| 62 | https://arxiv.org/abs/2006.15820 | препринт Chen et al., Retro*, ICML 2020 | 2026-10-13 |
| 63 | https://doi.org/10.1021/jacsau.1c00246 | статья, Chen & Jung, LocalRetro, JACS Au 2021 (полный текст PMC8549044) | 2026-10-13 |
| 64 | https://doi.org/10.1126/sciadv.abe4166 | статья, Schwaller et al., RXNMapper, Sci Adv 2021 (полный текст PMC8026122) | 2026-10-13 |
| 65 | https://doi.org/10.1021/acs.jcim.4c02004 | статья, SynPlanner, JCIM 2025 (аннотация через Europe PMC) | 2026-10-13 |
| 66 | https://arxiv.org/abs/2405.13983 | препринт DirectMultiStep (журнальная версия JCIM 2025, DOI 10.1021/acs.jcim.4c01982) | 2026-10-13 |
| 67 | https://github.com/open-reaction-database/ord-data | данные ORD (CC BY-SA 4.0, v0.2.0 от 31.08.2026, 350 звёзд) | 2026-10-13 |
| 68 | https://doi.org/10.1021/jacs.1c09820 | статья, Kearnes et al., ORD, JACS 2021 | 2026-10-13 |
| 69 | https://github.com/MolecularAI/PaRoutes | бенчмарк PaRoutes 2.0 с таблицей результатов | 2026-10-13 |
| 70 | https://doi.org/10.1039/d2dd00015f | статья, Genheden & Bjerrum, PaRoutes, Digital Discovery 2022 | 2026-10-13 |
| 71 | https://doi.org/10.1039/D3DD00252G | статья, Torren-Peraire et al., «Models Matter», Digital Discovery 2024 (препринт arXiv:2308.05522) | 2026-10-13 |
| 72 | https://doi.org/10.1038/s42256-024-00832-8 | статья, Bran et al., ChemCrow, Nat Mach Intell 2024 (полный текст PMC11116106) | 2026-10-13 |
| 73 | https://github.com/ur-whitelab/chemcrow-public | репозиторий ChemCrow (MIT, подмножество инструментов) | 2026-10-13 |
| 74 | https://www.futurehouse.org/research-announcements/launching-futurehouse-platform-ai-agents | анонс платформы FutureHouse (01.05.2025), агент Phoenix | 2026-10-13 |
| 75 | https://doi.org/10.1038/s41586-023-06792-0 | статья, Boiko et al., Coscientist, Nature 2023 (полный текст PMC10733136) | 2026-10-13 |
| 76 | https://github.com/gomesgroup/coscientist | репозиторий Coscientist (Apache 2.0 + Commons Clause, частичный) | 2026-10-13 |
| 77 | https://actu.epfl.ch/news/ai-helps-chemists-design-molecules-step-by-step | новость EPFL (28.04.2026) о статье в Matter, DOI 10.1016/j.matt.2026.102812 | 2026-10-13 |
| 78 | https://arxiv.org/html/2503.08537v2 | препринт Bran et al. (strategy-aware planning, v2 от 23.07.2025) | 2026-10-13 |
| 79 | https://github.com/schwallergroup/steer | репозиторий steer (MIT) | 2026-10-13 |
| 80 | https://arxiv.org/html/2505.07027v1 | препринт LLM-Syn-Planner (ICML 2025) | 2026-10-13 |
| 81 | https://aclanthology.org/2026.findings-acl.1734/ | статья AOT* (Findings of ACL 2026; препринт arXiv:2509.20988) | 2026-10-13 |
| 82 | https://arxiv.org/html/2507.07060v2 | препринт DeepRetro (19.08.2025, не прошёл рецензирование) | 2026-10-13 |
| 83 | https://arxiv.org/html/2410.04223v1 | препринт Llamole (ICLR 2025) | 2026-10-13 |
| 84 | https://cs.sjtu.edu.cn/en/news/1155.html | новость SJTU о Chemma в Nat Mach Intell (01.07.2025; препринт arXiv:2504.18340) | 2026-10-13 |
| 85 | https://doi.org/10.1039/d4sc04757e | статья, SynAsk, Chem Sci 2024 (полный текст PMC11587532) | 2026-10-13 |
| 86 | https://arxiv.org/html/2506.17238v2 | препринт ether0 (FutureHouse), открытые веса Apache-2.0 | 2026-10-13 |
| 87 | https://neurips.cc/virtual/2025/poster/120076 | постер Retro-R1, NeurIPS 2025 | 2026-10-13 |
| 88 | https://arxiv.org/html/2305.18365v3 | препринт Guo et al., NeurIPS 2023 D&B, бенчмарк LLM по 8 задачам химии | 2026-10-13 |
| 89 | https://ar5iv.labs.arxiv.org/html/2311.07361 | отчёт Microsoft Research AI4Science о GPT-4 в науке (2023) | 2026-10-13 |
| 90 | https://arxiv.org/html/2512.15567v1 | препринт «Evaluating LLMs in Scientific Discovery» (v1 17.12.2025), таблица solve rate | 2026-10-13 |
| 91 | https://doi.org/10.1038/s41557-025-01815-x | статья, Mirza et al., ChemBench, Nat Chem 2025 (препринт arXiv:2404.01475) | 2026-10-13 |
| 92 | https://doi.org/10.1038/s41598-023-41032-5 | статья, Walters & Wilder, Sci Rep 2023 (выдуманные ссылки; полный текст PMC10484980) | 2026-10-13 |
| 93 | https://arxiv.org/html/2402.09391v4 | препринт LlaSMol (валидность SMILES у LLM) | 2026-10-13 |
| 94 | https://doi.org/10.1039/d6dd00266h | статья, Voinarovska et al., Digital Discovery 2026, 5, 3648–3660 (люди против LLM как судей маршрутов) | 2026-10-13 |
| 95 | https://arxiv.org/html/2602.13136v2 | препринт «Order Matters in Retrosynthesis» (сводная таблица USPTO-50K/FULL) | 2026-10-13 |
| 96 | https://doi.org/10.1038/s41467-025-62308-6 | статья, RSGPT, Nat Commun 2025 (метаданные через RePEc) | 2026-10-13 |
| 97 | https://doi.org/10.1038/s41467-024-50617-1 | статья, EditRetro, Nat Commun 2024 (метаданные через RePEc) | 2026-10-13 |
| 98 | https://arxiv.org/abs/2507.17448 | препринт RetroDFM-R | 2026-10-13 |
| 99 | https://arxiv.org/abs/2310.09270 | препринт Retro-fallback (ICLR 2024) | 2026-10-13 |
| 100 | https://arxiv.org/abs/1910.08036 | препринт Schwaller et al. (метрики round-trip, coverage, diversity) | 2026-10-13 |
| 101 | https://arxiv.org/abs/2411.08306 | препринт SDDBench (round-trip оценка маршрутов) | 2026-10-13 |
| 102 | https://arxiv.org/pdf/1706.01643 | препринт Liu et al. 2017 (происхождение USPTO-50K; журнал — ACS Cent Sci, DOI 10.1021/acscentsci.7b00303) | 2026-10-13 |
</content>
| 103 | https://dwsim.org/index.php/download | сайт DWSIM: лицензии и тарифы Patreon | 2026-10-13 |
| 104 | https://github.com/DanWBR/dwsim | репозиторий DWSIM (архивирован 11.08.2026, read-only) | 2026-10-13 |
| 105 | https://dwsim.org/index.php/whatsnew | DWSIM: Fluent API (04.2026), MCP-сервер (05.2026), BioReactor | 2026-10-13 |
| 106 | https://sourceforge.net/projects/dwsim/ | SourceForge: ~800 загрузок DWSIM в неделю | 2026-10-13 |
| 107 | https://www.aspentech.com/en/products/pages/aspen-batch-modeler | страница продукта Aspen (batch modelling) | 2026-10-13 |
| 108 | https://www.aspentech.com/en/resources/press-releases/aspentech-delivers-batch-process-development-innovations-for-pharmaceutical-and-speci2147487780 | пресс-релиз AspenTech (2009), отзывы GSK и AstraZeneca | 2026-10-13 |
| 109 | https://www.emerson.com/en-us/news/2025/emerson-completes-acquisition-of-remaining-outstanding-shares-of-aspentech | Emerson завершила выкуп AspenTech (12.03.2025) | 2026-10-13 |
| 110 | https://www.siemens.com/en-us/products/gproms/formulated-products/ | страница продукта gPROMS FormulatedProducts (Siemens) | 2026-10-13 |
| 111 | https://www.scale-up.com/ | сайт Scale-up Systems (Dynochem, Reaction Lab), кейсы клиентов | 2026-10-13 |
| 112 | https://www.sec.gov/Archives/edgar/data/1037646/000103764622000008/mtd-20211231.htm | 10-K Mettler-Toledo: покупка Scale-up Systems (10.2021) | 2026-10-13 |
| 113 | https://www.intelligen.com/?p=1455 | прайс SuperPro Designer | 2026-10-13 |
| 114 | https://www.intelligen.com/products/superpro-product-features/ | функции SuperPro Designer | 2026-10-13 |
| 115 | https://acsgcipr.org/tools/ | индекс инструментов ACS GCI Pharmaceutical Roundtable | 2026-10-13 |
| 116 | https://acsgcipr.org/wp-content/uploads/2024/10/convergent-pmi-presentation.pdf | презентация ACS GCIPR: PMI-калькуляторы (2011, 2014) | 2026-10-13 |
| 117 | https://ideas.repec.org/a/nat/natsus/v2y2019i11d10.1038_s41893-019-0400-5.html | статья, Borovika et al., Nature Sustainability 2019 (PMI Predictor), DOI 10.1038/s41893-019-0400-5 | 2026-10-13 |
| 118 | https://acsgcipr.org/wp-content/uploads/2024/12/acs-gci-solvent-selection-tool-principles-and-guidance-2.pdf | руководство ACS GCI Solvent Selection Tool (ссылается на OPRD 2016, 20, 760–773) | 2026-10-13 |
| 119 | https://reagents.acsgcipr.org/about/ | ACS GCI Reagent Guides | 2026-10-13 |
| 120 | https://acsgcipr.org/tools/igal-2-0-scorecard-calculator/ | iGAL 2.0 (06.08.2021), база 64 процессов / 703 стадий / 12 компаний | 2026-10-13 |
| 121 | https://learning.acsgcipr.org/guides-and-metrics/solvent-selection-guides/the-chem21-solvent-selection-guide/ | CHEM21 solvent guide (Prat et al., Green Chem 2016, 18, 288–296) | 2026-10-13 |
| 122 | https://learning.acsgcipr.org/process-design/route-selection/recap-of-the-select-criteria/ | критерии SELECT (Butters et al., Chem Rev 2006, 106, 3002–3027) | 2026-10-13 |
| 123 | https://www.lhasalimited.org/wp-content/uploads/2023/02/Mirabilis-Purge-Ratio-Infographic.pdf | инфографика Lhasa Mirabilis: purge ratio и опции ICH M7 | 2026-10-13 |
| 124 | https://prnewswire.co.uk/news-releases/lhasa-limited-announces-the-launch-of-mirabilis-289123071.html | запуск Mirabilis (20.01.2015), состав консорциума | 2026-10-13 |
| 125 | https://www.lhasalimited.org/?p=2969 | вебинар Lhasa с данными опроса IQ по опции 4 ICH M7 | 2026-10-13 |
| 126 | https://lhasalimited.org/products/sarah-nexus.htm | Sarah Nexus: «две методологии» ICH M7 | 2026-10-13 |
| 127 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC7510098/fullTextXML | статья, Foster et al., Genes and Environment 2020;42:27 (Derek/Sarah) | 2026-10-13 |
| 128 | https://store.astm.org/ds51hol-eb.html | ASTM CHETAH 11.0 (2020) | 2026-10-13 |
| 129 | https://www.chemical.ai/impurity-prediction | модуль прогноза примесей ChemAIRS (заявления вендора) | 2026-10-13 |
| 130 | https://askcos-docs.mit.edu/guide/11-References/11.1-ASKCOS-related-papers.html | документация ASKCOS: список модулей и публикаций | 2026-10-13 |
| 131 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC7012039/fullTextXML | статья, Thakkar et al., Chem Sci 2020, 11, 154–168 (описание ручного ретросинтеза) | 2026-10-13 |
| 132 | https://www.patheon.com/content/dam/patheon/global/library/resources/fact-sheets/fs-route-scouting-for-a-cost-effective-process-development.pdf | fact sheet Thermo Fisher Patheon: route scouting (04.2023) | 2026-10-13 |
| 133 | https://sta.wuxiapptec.com/services-solutions/drug-substance/api-process-research-development/ | WuXi STA: сроки и масштаб process R&D | 2026-10-13 |
| 134 | https://www.almacgroup.com/api-chemical-development | Almac: услуги по разработке процессов (без чисел) | 2026-10-13 |

> Источники, которые встречались только в выдаче поиска и не были открыты, в таблицу не включены; в тексте такие факты помечены «не подтверждено».

## 0. Ручной baseline: как технолог ищет маршрут сегодня

- **Категория:** человеческий процесс, поддержанный поисковыми базами.
- **Владелец:** фарм-компании и CDMO/CRO.
- **Доступ:** стоимость — это рабочее время химиков плюс подписки на CAS SciFinder и Reaxys (цены не публикуются, «не подтверждено»).
- **Ключевые элементы:**
  - Ретросинтетический анализ «в обратную сторону» на базе личного опыта: химик «works in the reverse direction, using a knowledge-base of synthetic transformations», накопленный «years of experience» [131].
  - Поиск прецедентов в базах реакций (CAS SciFinder, Reaxys) и патентах; формальных данных о том, как именно распределяется использование этих баз при ручном дизайне маршрута, в открытых источниках найти не удалось — «не подтверждено».
  - Отбор по критериям **SELECT** (Safety, Environmental, Legal, Economics, Control, Throughput), Butters et al., Chem Rev 2006, 106, 3002–3027 [122].
  - Маршрут не фиксируется один раз: «synthetic routes can change during the development pipeline of an API, and post launch» [122]. Сколько именно редизайнов приходится на программу — «не подтверждено».
  - Промышленный вариант: route scouting в CDMO. Публичная схема Thermo Fisher Patheon: Synthetic Design (литература, стоимость и доступность сырья, отходы) → Feasibility (граммовый масштаб) → демонстрационная партия 10–100 г с первичной оценкой примесей и безопасности → масштабирование под клинику; заявлено «Parallel screening of multiple synthesis routes» и «~30 projects to manufacturing … more than 100 chemical steps per year» [132]. WuXi STA публикует нормативы темпа: «1.5 weeks/step» для RSM и «2.5 weeks/step» для АФИ, 15–20 месяцев до валидации процесса поздней фазы, 3 600+ химиков и аналитиков ранней фазы [133]; про route scouting и ИИ на этой странице не говорится. У Almac на странице разработки процессов числа отсутствуют вовсе, только формулировка про «challenging synthetic routes and process scale-up» [134] — то есть публичной измеримой картины услуги route scouting рынок не даёт.
- **Эффективность:**
  - Прямых публичных измерений «сколько стоит и сколько длится ручной route scouting» найти не удалось (цифры CDMO описывают темп стадий, а не стоимость поиска маршрута) — «не подтверждено».
  - Косвенная оценка качества человеческого baseline есть в двойных слепых сравнениях: химики считали компьютерные маршруты «equivalent to reported literature routes» [21], а в Turing-подобном тесте маршруты системы были «largely indistinguishable from those designed by humans» [6]. То есть человек остаётся эталоном, но уже не недостижимым.
- **Конвейер (по [122], [131], [132]):** МНН / структура цели → ретросинтетические идеи эксперта → поиск прецедентов в SciFinder/Reaxys → отбор 2–4 кандидатов по SELECT → лабораторная проверка (feasibility) → демонстрационная партия и оценка примесей/безопасности → масштабирование.
- **Сильные стороны:** учёт неформализуемого (доступность сырья у конкретного поставщика, оборудование площадки, патентный ландшафт, регуляторная история); ответственность и подпись человека; работает и там, где нет данных.
- **Слабые стороны:** дорого и медленно; охват литературы ограничен временем химика; смещение к «знакомой химии»; результат слабо воспроизводим и почти не документируется в машинном виде; знание уходит вместе с сотрудником.

## 1. Коммерческие системы компьютерного планирования синтеза (CASP)

### 1.1 SYNTHIA Retrosynthesis Software (Merck KGaA, ex-Chematica)

- **Категория:** CASP на экспертно закодированных правилах, SaaS. **Владелец:** Merck KGaA (MilliporeSigma в США).
- **Доступ:** подписка. Академический тариф **SYNTHIA Lab**: «1,049 EUR» со «50% introduction discount», «Unlimited number of molecules to run for 10 full users» (период оплаты на странице не указан) [2]; корпоративный прайс не публикуется — «не подтверждено». Есть программа грантов: до 3 грантов с «a 1-year full SYNTHIA® Retrosynthesis Software license», дедлайн 31.08.2026 [1].
- **Ключевые возможности:** «over 110,000 reaction rules» и «12+ million starting materials», модель SaaS [3]; поиск более «зелёных» альтернатив опасным реагентам [3]; Synthetic Accessibility Score через API, режим прямого синтеза, обмен планами, резервные маршруты на более дешёвых реагентах [4]; интеграция в платформу AIDDISON через «Synthia™ retrosynthesis software application programing interface (API) integration» [7].
- **Эффективность:**
  - `DEV` Klucznik et al., Chem 2018: маршруты для «eight structurally diverse targets … routes were successfully executed in the laboratory»; планирование «within 15–20 min for all targets» на 64-ядерной машине; на тот момент «Chematica's 50,000 rules» и поиск до коммерческих веществ по каталогу «200,000+ commercial substrates» [5].
  - `DEV` Mikulak-Klucznik et al., Nature 2020: «Using a Turing-like test administered to synthesis experts» маршруты «are largely indistinguishable from those designed by humans»; «We also successfully validated three computer-designed syntheses of natural products in the laboratory» [6].
  - `VENDOR` «Many companies, including GSK, use SYNTHIA» — без чисел [4].
  - Независимых бенчмарков не найдено — «не подтверждено».
- **Конвейер:** структура цели → применение экспертных правил (каждое правило — дерево решений с учётом стерео- и региоселективности) → поиск по графу/гиперграфу с эвристическим отсечением → остановка на коммерчески доступных веществах (каталог + цены) → ранжирование маршрутов (динамическое линейное программирование, пользовательские критерии) → UI, SAS API, AIDDISON [5], [6], [4].
- **Сильные стороны:** единственная система с рецензируемой лабораторной валидацией автономно спланированных маршрутов; интерпретируемые правила; доступный академический тариф; интеграции с API и автоматическим синтезом.
- **Слабые стороны:** валидация написана авторами системы; покрытие зависит от ручного кодирования правил; счётчик литературных подтверждений на стадию не заявлен («не подтверждено»); корпоративная цена непрозрачна; нет независимых сравнений.

### 1.2 CAS SciFinder Retrosynthesis + CAS Newton (CAS / ACS)

- **Категория:** гибрид «литературные стадии + предсказанные правилами стадии» внутри подписной поисковой платформы.
- **Доступ:** институциональная подписка; цены не публикуются — «не подтверждено».
- **Ключевые возможности:** планы смешивают стадии из курированной коллекции реакций CAS и предсказанные стадии; на каждой стадии видны доказательства, альтернативы и ссылки, есть фильтры по выходу, стоимости сырья и сложности, исключение стадий/реагентов, ссылки на поставщиков [9]. История: запуск в 2019 году частично на технологии Wiley ChemPlanner, «nearly 120 million reactions» [8]; «121 million reactions in the CAS collection» (2020). С 29.10.2024 — метки и фильтры стереоселективных стадий, «CAS also increased coverage of unique stereoselective transformations by 30%» [10]. С 04.08.2025 — «Interactive Retrosynthesis», которая «slashes the time needed to generate a synthetic plan from minutes to just a few seconds» [11]. Release notes 2025–2026 показывают донастройку правил (гетероароматика 12.2025, циклические правила 02.2026, бензоидные метки 05.2026), переопределение лимита стоимости, импорт molfile, агентный режим «CAS Newton» (04.2026), автоматическую выдачу плана ретросинтеза в Newton и экспорт SVG (07.2026), данные поставщиков в планах Newton (08.2026) [12].
- **Эффективность:** только `VENDOR`-утверждения; опубликованных метрик точности или доли решённых целей нет — «не подтверждено». Фигурирующие в релизе 93% относятся к бета-тестерам поиска, а не к ретросинтезу [11].
- **Конвейер:** цель (CAS Draw / molfile) → поиск стадий в курированных реакциях CAS → генерация предсказанных стадий правилами, обученными на реакциях CAS → расширение дерева с ограничениями по стоимости и сложности до коммерческих веществ (выведено из наличия лимитов и ссылок на поставщиков) → интерактивный план с доказательствами, ссылками и стерео-метками → экспорт или выдача через агент CAS Newton [9], [12]. Алгоритм поиска не раскрыт — «не подтверждено».
- **Сильные стороны:** крупнейший курированный корпус реакций; у литературных стадий есть ссылки на первоисточник (ровно то, что нужно для provenance); быстрый цикл релизов 2025–2026; агентный интерфейс уже встроен.
- **Слабые стороны:** метод не раскрыт и не проверяем; нет публичных бенчмарков; закрытые данные и подписка исключают воспроизводимость; результат нельзя выгрузить в открытый формат маршрута.

### 1.3 Reaxys Predictive Retrosynthesis (Elsevier; движки Pending.AI и Iktos)

- **Категория:** ML-ретросинтез как платный модуль к подписке на базу реакций. Пользователь выбирает движок: «Select from models by Iktos and Pending AI» [13].
- **Доступ:** add-on к Reaxys; цены не публикуются. Данные Reaxys доступны «via MCP, API or flat file as a separate license» [13].
- **Ключевые возможности:** «420,000+ expert rules», процедуры из «over 70 million reactions», 150M коммерчески доступных исходных веществ; задание связей для разрыва и защиты, включение/исключение интермедиатов, лимиты по цене и длине маршрута, стратегии хемо-, регио- и стереоселективности, API [13]. С 03.2026 — режим «Combined route»: предсказанные стадии (зелёные) объединяются с опубликованными реакциями Reaxys (синие) [18]. Движок Pending.AI: «deep neural networks trained on Reaxys data» + «a Monte Carlo tree search approach», «>400,000 reaction rules», извлечённых из «>15 million single-step organic reactions» [14]. Движок Iktos: «template-based disconnection prediction model» + проприетарный фильтр реализуемости с хемо- и региоселективностью, дообучение на внутренних реакциях заказчика [15].
- **Эффективность:**
  - `VENDOR` Iktos-модель (04.2025): «produces predicted synthesis routes for small drug like molecules in more than 90% of the cases» [16].
  - `VENDOR` релиз 06.2025: «approximately 26% faster on average», «20% more routes on average», библиотека building blocks выросла на 36,6% до 150,6 млн [17].
  - `VENDOR+партнёр` кейс Lonza (соавтор — Elsevier): «In five of the six cases, shorter strategies were devised when SMEs used Reaxys predictive retrosynthesis» [19].
  - `VENDOR` пилоты в ETH Zurich и Radboud: «7 teams, 3 to 4 researchers each», «30 molecules selected»; выводы качественные, включая «Retrosynthesis route may not be fully feasible» и «chemist needs to review proposals especially with regards to functional group tolerance» [20].
  - Метод-основа (`DEV`): Segler et al., Nature 2018 — система «solves for almost twice as many molecules, thirty times faster than the traditional computer-aided search method», а в двойных слепых AB-тестах «chemists on average considered our computer-generated routes to be equivalent to reported literature routes» [21].
- **Конвейер (Pending.AI, подтверждён [14] и [20]):** цель → нейросеть ранжирует вероятные разрывы (шаблоны извлечены автоматически; берутся реакции, воспроизведённые более чем в трёх публикациях) → применение retro-правила → «in-scope filter» оценивает реализуемость → MCTS до коммерчески доступных веществ или до исчерпания бюджета времени → ранжирование и показ литературных прецедентов (опционально режим Combined). Для Iktos-движка подтверждены шаблонный разрыв → фильтр реализуемости → поиск → лимит цены; что поиск именно MCTS — выведено по аналогии со Spaya, не подтверждено.
- **Сильные стороны:** два движка на выбор; показываются литературные прецеденты, то есть не чистый «чёрный ящик»; крупнейшая библиотека исходных веществ; API и дообучение на данных заказчика.
- **Слабые стороны:** все метрики — из release notes вендора; сравнения двух движков между собой нет; ограничения реализуемости признают сами пилотные пользователи; платный add-on поверх платной базы.

### 1.4 Iktos Spaya

- **Категория:** data-driven шаблонный нейроретросинтез, SaaS + API. **Владелец:** Iktos (Париж).
- **Доступ:** веб-приложение и demo по запросу; есть развёртывание «on AWS with autoscaling or on your VPC»; цены и условия пробного доступа — «не подтверждено» [22].
- **Ключевые возможности** [22]: «Unique data-driven approach, combining reinforcement learning and monte-carlo tree search»; «A template-based neural network trained on 6M reactions»; «+2000 name reactions»; сеть предсказания региоселективности; «+35 partnerships with providers»; «A proprietary scoring function to rank the final selected routes» и метрика RScore; батчевый API для «hundreds of thousands of molecules»; интеграции Knime, Pipeline Pilot, Jupyter; дообучение на данных заказчика «in a couple of week».
- **Эффективность (`DEV`, Parrot et al., J Cheminform 2023) [23]:** RScore в диапазоне 0–1 как функция числа стадий, вероятности разрывов, конвергентности и области применимости шаблонов; каталог ~60 млн соединений от 17 поставщиков; ранняя остановка при score > 0,6 или по таймауту 1 минута, в среднем ~42 с на молекулу; на 30 молекулах, размеченных 7 химиками, ROC-AUC: RScore3min 1,0 против SA score 0,63, RA score 0,41, SC score 0,201; около 66% выборки ChEMBL получают RScore ≥ 0,5. Авторы сами указывают ограничения: выборка 30 молекул, а эталон коррелирует с проверяемой метрикой. Независимых оценок нет — «не подтверждено».
- **Статус 2026:** на сайте вендора заголовки «Iktos Engine: APIs for Agentic workflows…» (21.05.2026) и участие в программе JETRO (25.08.2026); есть направление Iktos Robotics с автономной лабораторией, вывод Spaya заявлен совместимым с их роботами [24].
- **Конвейер:** SMILES → шаблонная нейросеть предлагает разрывы + предсказание региоселективности → MCTS с обучением с подкреплением до коммерческих веществ → ранняя остановка/таймаут → скоринг маршрута и RScore → UI, батч-API или роботизированная платформа [22], [23].
- **Сильные стороны:** очень дешёвая батчевая оценка синтезируемости; развёртывание в VPC заказчика; дообучение; публикация с описанием метрики.
- **Слабые стороны:** крошечная валидационная выборка; около трети выборки ChEMBL без хорошего маршрута; непрозрачные цены; нет независимой проверки.

### 1.5 IBM RXN for Chemistry — хостинг отключается 28.10.2026

- **Категория:** облачный CASP на трансформерах (Molecular Transformer) + прямое предсказание + генерация процедур. **Владелец:** IBM Research Zürich (под брендом Accelerated Discovery).
- **Критический факт:** «RXN for Chemistry is reaching end of service on October 28, 2026.» и «The hosted platform and programmatic APIs will be taken offline on that date.»; «A self-hostable version is available on GitHub» [25] → репозиторий `rxn-sandbox`: локальный инстанс для прямого предсказания и ретросинтеза, модели обучены на данных Pistachio 2025Q2, разворачивается через Docker/Podman compose, нужно 8 ГБ ОЗУ (16 ГБ для древесных предсказаний) и 10 ГБ диска [26].
- **Доступ и цены (хостинг, пока работает):** индивидуальный тариф pay-as-you-go только в США: «USD 0.70/minute» (0–480 мин/мес), «USD 0.50/minute» (480–960), «USD 0.40/minute» (960+); командный тариф «USD 88000/yr (up to 10 users)» или «USD 8150/month (up to 10 users)»; бесплатного тарифа на странице цен нет [27].
- **Ключевые возможности** [28], [25]: планирование маршрутов; прямое предсказание («molecular transformer models that are flexible and non-rule-based»); «Generate experimental procedures» (текст → действия) и перевод рецептов в машинные инструкции для автономного оборудования; атомное картирование «~7ms/reaction», модели «trained on over 3 million chemical reactions»; API `rxn4chemistry` с батчевым предсказанием, биокаталитической моделью ретросинтеза, извлечением действий из абзаца, картированием атомов и предсказанием выхода.
- **Эффективность:**
  - `IND` Molecular Transformer (ACS Cent Sci 2019): «achieving a top-1 accuracy above 90% on a common benchmark data set» (USPTO_MIT separated = 90,4%); «an accuracy of 88.6% when no distinction is drawn between reactants and reagents»; на шумном USPTO_STEREO «78.1 (separated) and 76.2%»; в сравнении с людьми модель «achieve[s] a top-1 accuracy of 87.5%, significantly higher than the average of the best human (76.5%)» на наборе из 80 реакций [29].
  - `IND` Chem Sci 2020: введены метрики round-trip accuracy, coverage, class diversity; для одностадийного ретросинтеза на 10 тыс. тестовых записей по 10 предсказаний round-trip 81,2% при coverage 95,1%; работа прямо показывает, что top-N accuracy вводит в заблуждение применительно к ретросинтезу [30].
  - `DEV конкурента` RetroTrim (Molecule.one, 2025): на 32 неопубликованных drug-like целях IBM RXN дал маршрут класса «Safe bet» для 12 из 32 целей при 15 из 32 «No pathway» — лучше AiZynthFinder, хуже RetroTrim и RetroChimera [31].
- **Конвейер:** SMILES цели → одностадийное расширение трансформером → многостадийный поиск по гиперграфу → остановка на коммерческих веществах → ранжирование (в том числе round-trip прямой моделью) → опционально генерация процедуры/действий → UI, REST API или робот [29], [30], [28].
- **Сильные стороны:** самая цитируемая и рецензируемая основа; уникальные функции (извлечение действий из текста, картирование атомов, RXNMapper под MIT); с `rxn-sandbox` появляется офлайн-воспроизводимый вариант, идеально подходящий университетской платформе.
- **Слабые стороны:** облачный сервис умирает 28.10.2026, любая интеграция должна целиться в `rxn-sandbox`; командный тариф дорогой; индивидуальный доступен только в США; измеримо высокая доля «нет маршрута» на сложных drug-like целях [31].

### 1.6 ChemAIRS (Chemical.AI)

- **Категория:** коммерческий ретросинтез с процессным уклоном (примеси, условия, масштаб, стоимость).
- **Доступ:** подписка в браузере; полное локальное/on-prem развёртывание для чувствительных данных, интеграция с ELN, AES-256, «21 CFR Part 11 ready» [32]. Прайс-лист — «не подтверждено». Дистрибьютор в Японии (Patcore) предлагает двухнедельный бесплатный триал [34].
- **Ключевые возможности** [33], [32], [129]: ретросинтез (реализуемые и разнообразные маршруты); модуль Process Chemistry (масштабирование, сырьё, доступное в тоннаже; отбор условий, показанных на масштабе ≥100 г или взятых из OPRD; поиск до 4 часов); собственный SA Score; оптимизация условий на данных ELN; **прогноз примесей** одной стадии по реагентам, условиям и переносимым следовым примесям с оценкой уверенности 0–100; прямой синтез для генерации библиотек; байесовская оптимизация; актуальные рыночные цены материалов.
- **Эффективность — только `VENDOR`:**
  - «ranked first among 9 leading CASP tools for both feasibility and diversity» — оценка CRO на 60 целях, судьи-химики; конкуренты не названы, публикации нет [32].
  - Внутреннее исследование 16 проектов: топ-3 маршрута совпали с выбором эксперта в 80% случаев; заявлена экономия времени ~90%; SA Score «validated» на 13 000+ молекулах с медхимиками Merck [32].
  - Прогноз примесей «over 90% accuracy»; в двух кейсах модуль нашёл 5 из 6 и 6 из 6 известных примесей [129]; маршруты «reduce synthesis steps by 20% to 70%» [33]; у дистрибьютора — база ~80 млн реакций и «50% reduction in experiments» [34].
  - Развёртывание у Aragen на их серверах; «works with over 100 companies and research institutes» [35].
  - Независимых проверок нет вообще — «не подтверждено». Про ICH M7 на страницах модуля примесей не говорится.
- **Конвейер:** SMILES → гибридное одностадийное расширение (ML + правила) по базе ~80 млн реакций → многостадийный поиск → проверка наличия и цены сырья в реальном времени → ранжирование по реализуемости, стоимости и числу стадий (+ SA Score) → дополнительные модули (условия, примеси, процесс) → веб или on-prem. Алгоритм поиска и формула ранжирования не раскрыты.
- **Сильные стороны:** самый широкий процессный набор среди коммерческих CASP (примеси, условия, масштаб, стоимость); on-prem; обучение на ELN заказчика; живая коммерческая тракция в 2026.
- **Слабые стороны:** нулевая независимая валидация; «бенчмарк 9 инструментов» без названий и без публикации; нет публичных цен и документации API; нет рецензируемых статей о методе.

### 1.7 PostEra Manifold

- **Категория:** ретросинтез + поиск building blocks, сейчас — компонент медхим-платформы Proton. **Владелец:** PostEra Inc.
- **Статус 2026:** на главной странице продвигается только Proton; Manifold, ретросинтез и цены не упоминаются [36]. Поддомены приложения из нашей песочницы не разрешались (DNS заблокирован, это не доказательство отключения). V1-эндпоинт ретросинтеза ещё использовался в марте 2025 по независимому препринту [38]. Условия доступа в 2026 — «не подтверждено».
- **Ключевые возможности:** ML-ретросинтез до покупаемых building blocks; оценка синтетической доступности из маршрута; ссылки на поставщиков и CRO; REST API (v1, выбор каталога building blocks, параметр глубины поиска) [38]; интеграция в StarDrop (Optibrium) [39].
- **Эффективность:**
  - `IND` (рецензируемая публикация, COVID Moonshot, Science 2023): «We employ an approach based on the Molecular Transformer technology»; «This proprietary platform is provided free of charge by PostEra Inc»; «We automatically computed synthetic routes for all crowdsourced submissions»; «returns efficient routes that leverage over 10 million in-stock advanced intermediates»; «predicts synthetic accessibility by taking the product of the probabilities along the whole route»; «Our predicted synthetic complexity correlated with the actual time taken to synthesize target compounds» (n=898). Важная оговорка авторов: «We did not use an 'autonomous' approach — expert judgment is used» [37].
  - `IND` Mokaya, Deane, Bradley (bioRxiv, 10.03.2025): доля целей с найденным маршрутом — «AiZynthFinder and Postera exhibited higher success rates for kinase targets (67% and 94%, respectively)», и «both tools showed reduced performance for non-kinase targets (58% and 82% success rates)»; использован «their v1 retrosynthesis endpoint with a maximum search depth of four and the Molport building block library» [38].
- **Конвейер:** SMILES → одностадийная модель трансформерного типа → многостадийный поиск (типично глубина ≤4) → проверка каталога building blocks (>10 млн интермедиатов) → произведение вероятностей по маршруту как оценка доступности → ранжирование + ссылки на CRO → UI, REST API, плагин StarDrop [37], [38], [39].
- **Сильные стороны:** единственный из коммерческих с **независимыми** числами и флагманским рецензируемым внедрением; чистый API; прозрачно описанный скор доступности.
- **Слабые стороны:** продукт больше не продвигается самостоятельно; условия доступа в 2026 непрозрачны; закрытая модель; нет модулей условий, примесей и процесса.

### 1.8 Molecule.one (Maria) и RetroTrim

- **Категория:** был облачный ретросинтез, сейчас — ИИ + автоматизированная микролаборатория. **Владелец:** Molecule.one (Варшава/Калифорния).
- **Статус:** флагман — Maria (Maria AI + Maria Lab, микролитровая HTE-лаборатория + Maria Data); отдельного ретросинтез-продукта на сайте нет, ретросинтез остался как внутренняя способность [40]. Самостоятельный доступ/цены — «не подтверждено». Вехи: победа в конкурсе Standard Industries на 1 млн долларов по ретросинтезу (12.06.2025; более 30 команд, 3 этапа оценки, независимые судьи) [41]; многолетний контракт с Grace (08.12.2025) [42].
- **Эффективность (`DEV`, но с самым полезным для нас протоколом):** препринт RetroTrim (arXiv:2510.10645 v3, все авторы — Molecule.one) [31]:
  - Обучение на проприетарном Pistachio 2024Q3 (~4 млн реакций после фильтрации), генератор — BART на root-aligned SMILES, поиск — Retro* (реализация из Syntheseus, лимит расширений 500), сырьё — eMolecules.
  - Разметка качества: «over 4,500 reactions», размеченных химиками с PhD; обещан публичный релиз 500 реакций и 32 целей.
  - Протокол экспертной оценки маршрута по худшей стадии в 4 градации: Safe bet / Worthwhile / Rather not / Nonsense, плюс «No pathway». На 32 новых drug-like целях RetroTrim «significantly increas[es] Safe Bet paths, maintain[s] zero Nonsense results»; RetroChimera «outputs pathways for the vast majority of targets», но с «a substantial number of Nonsense pathways» и «still fails on >25% targets»; AiZynthFinder «fails to identify viable pathways for significant number of the target molecules»; IBM RXN надёжнее AiZynthFinder, но «fails to produce valid synthetic routes for a considerable fraction of target compounds». Точные значения по градациям есть только на рисунке 3; в тексте их нет, поэтому числа по градациям (кроме приведённых в разделе 1.5 из сводки) мы в статье использовать не будем без извлечения из графика.
- **Конвейер:** SMILES → генератор RootAligned BART → **MetaScorer** из трёх независимых скореров (обученный prior реакции + графовая оценка правдоподобия + поиск прецедентов в кластерах) отсекает неправдоподобные ветви → поиск Retro* по выжившим узлам → остановка на eMolecules → скоринг и ранжирование по экспертному протоколу → передача в Maria Lab на HTE-проверку [31], [40].
- **Сильные стороны:** самая проработанная из опубликованных архитектур борьбы с «галлюцинациями реакций»; единственное сравнение IBM RXN / AiZynthFinder / LocalRetro / RetroChimera, оценённое экспертами; замыкание цикла на реальную лабораторию.
- **Слабые стороны:** самостоятельного продукта ретросинтеза в 2026 нет; оценка проведена вендором; выборка 32 цели; ключевые данные (Pistachio) лицензионные, воспроизвести извне нельзя.

### 1.9 Коротко: остальные коммерческие и облачные решения

- **RetroChimera (Microsoft Research + Novartis).** Ансамбль графовой шаблонной модели и de-novo трансформера; «pushing the top-10 accuracy by 1.7% and 1.6%» на USPTO-50K/USPTO-FULL, тест-сплит по времени из 146 393 реакций Pistachio, zero-shot перенос на 10 444 внутренних реакции Novartis; заявлено, что промышленные химики предпочитают предсказания модели реакциям из обучающего набора [43]. Доступна в Azure AI Foundry, статус Preview, лицензия MIT, вход — SMILES продукта, выход — ранжированные реакции [44]. Только одностадийная модель: поиска, каталога и UI нет. Независимая проверка [31] показывает сохраняющиеся «Nonsense» маршруты.
- **ChemAI (ex-Deepmatter / InfoChem), продукт Smartchemistry.** `deepmatter.io` редиректит на `chemai.io`; заявленный конвейер — цель и ограничения → ИИ-поиск маршрута → оценка стоимости и «зелёности» in silico → проверка IP и лаборатория; доступ только «get in touch», цен нет. ICSYNTH присутствует лишь как легаси-публикация [46]. Важно для нас тем, что публичное позиционирование строится на стоимостной и экологической оценке маршрута.
- **Chemify (Глазго).** ПО ASSEMBLER «identifies the most efficient synthetic path» по собственной базе валидированных классов реакций, прямо противопоставляя себя ситуации, когда «Traditional retrosynthesis often fails due to unreliable literature references»; язык χDL как «universal chemical programming language» и роботизированное исполнение. Чисел, цен и модели доступа нет — «не подтверждено» [45]. Это соседний рынок: маршрут → исполняемый протокол.
- **SimBioSys ARChem / Route Designer — закрыто.** На сайте остались только онкологические продукты, `/archem/` отдаёт 404 [47]. Легаси.
- **Не проверено:** Lilly TuneLab, Optibrium как самостоятельный планировщик, ReactWise, Deep Origin, AIDDISON как отдельный планировщик, ChemPlanner, WebReactions — «не подтверждено» (бюджет поиска исчерпан).

## 2. Открытые решения

### 2.1 AiZynthFinder (AstraZeneca)

- **Категория:** многостадийный планировщик (библиотека + CLI + GUI в Jupyter). **Владелец:** AstraZeneca Molecular AI.
- **Доступ:** MIT, PyPI/GitHub без регистрации, публичная модель расширения и сток ZINC загружаются одной командой; v4.4.1 от 09.12.2025, 904 звезды на 13.10.2026 [48].
- **Ключевые возможности** [48], [50]: шаблонная нейросеть политики расширения + опциональная фильтрующая политика; алгоритмы MCTS (по умолчанию), Breadth-First, DFPN, Retro*; несколько видов стока с отсечением по цене, количеству и массе; фреймворк скоринга маршрутов; кластеризация и анализ маршрутов; плагины ModelZoo (Chemformer, MHNreact, LocalRetro) и REST-обёртка Chemformer; ONNX-инференс; батчевый CLI с чекпойнтами.
- **Эффективность:**
  - `DEV` J Cheminform 2020 [49]: «The software is fast and can typically find a solution in less than 10 s and perform a complete search in less than 1 min»; прямое сравнение с веб-сервером ASKCOS на 100 случайных соединениях ChEMBL: «There were 47 compounds for which both tools found a route, 15 compounds where ASKCOS found a solution and AiZynthFinder did not, and 8 compounds where AiZynthFinder found a solution and ASKCOS did not»; сток ZINC — 17 422 831 соединение; «>85% of the code is covered by automatic unit and integration tests».
  - `DEV` J Cheminform 2024 (версия 4.0) [50]: 377 900 целей в 4 наборах. «The number of targets for which we find at least one route where all the starting material is in stock is 80% and 86% for the AZ designs and Reinvent sets»; «For ChEMBL, we only find solutions to 71% of the targets»; «For the GDB set we only find solutions to about 10%»; «The median search time is about 40 s for the ChEMBL set and 90 s for the Reinvent sets». Шаблоны: «about 180,000 templates in the internal AstraZeneca expansion model, and about 45,500 templates in the public USPTO-based expansion model», при этом реально используется лишь часть шаблонов. Внедрение: «AiZynthFinder is used daily in-house», задание запускается автоматически для каждой спроектированной молекулы. Числа по количеству пользователей не публикуются — «не подтверждено» (статья о трёхлетнем опыте применения существует, но доступна только аннотация [51]).
  - `DEV` Chem Sci 2025 [52]: при заданных пользователем ограничениях на разрываемые связи они выполняются для 75,57% целей PaRoutes против 54,80% при стандартном поиске.
  - `IND` третья сторона: доля решённых целей 67% (киназные) и 58% (не киназные) против 94% и 82% у PostEra [38]; на 32 сложных drug-like целях — слабейший результат из пяти систем по экспертной шкале [31].
- **Конвейер:** конфигурация (политики, сток, скорер) → политика расширения ранжирует шаблоны → применение шаблона даёт узлы-предшественники, фильтрующая политика отсекает неправдоподобные реакции → алгоритм поиска (MCTS/BFS/DFPN/Retro*) выбирает узлы → поиск по стоку завершает ветви → скоринг и извлечение лучших маршрутов → опционально кластеризация и вывод в GUI/CLI [49], [50].
- **Сильные стороны:** зрелость, MIT, подключаемые одностадийные модели, скорость, воспроизводимость на публичной модели и стоке, крупная база пользователей, тесты и документация. Для нас это естественный `B1` (шаблонный ретросинтез без LLM) из протокола.
- **Слабые стороны (признают авторы, [50]):** «severe limitations in efficient usage of the one-step retrosynthesis models»; «AiZynthFinder is incapable of taking advantage of the broad chemical space that is encoded in the template-based model»; скоринг маршрутов недостаточно надёжен, чтобы рекомендовать, а не подсказывать; почти нулевая решаемость вне литературного химического пространства (GDB ~10%); лучшие модели и стоки проприетарны, поэтому публичная конфигурация слабее внутренней.

### 2.2 ASKCOS v2 (MIT, консорциум MLPDS)

- **Категория:** полнофункциональный веб-сьют CASP на микросервисах + API. **Владелец:** MIT (Coley/Jensen/Green), развитие в рамках MLPDS.
- **Доступ:** код под MIT — «available under permissive MIT licenses» [53]; self-hosted через Docker Compose; требования ≥4 ядра x86 (Apple Silicon не поддерживается), ≥32 ГБ ОЗУ. Внимание: у легаси-версии v1 данные и обученные модели были под CC BY-NC-SA, то есть только для некоммерческого использования — условия надо проверять по каждой модели. Актуальный релиз на 10.2026 — 2026.07 [54].
- **Ключевые возможности** [53], [130]: четыре одностадийные модели ретросинтеза (template relevance, RetroSim, Transformer, Graph2SMILES); многостадийный Tree Builder с MCTS и Retro*; интерактивный планировщик (Interactive Path Planner) с баном узлов и ручным расширением; ранжирование маршрутов; бинарный «fast filter» правдоподобия; рекомендация условий (V1 и экспериментальная V2); предсказание прямого исхода, **примесей** (минорные продукты, переокисление, димеризация, аддукты растворителя), регио- и C–H-селективности; растворимость, подбор растворителя, QM-дескрипторы; каталог покупаемых веществ; FastAPI-шлюз + Vue-фронтенд. В релизах 2026 появились MCP-сервер для API-шлюза (2026.01) и интеграция чат-бота во фронтенд (2026.04) [54].
- **Эффективность:**
  - `DEV` [53]: «ASKCOS has assisted hundreds of medicinal, synthetic, and process chemists in their day-to-day tasks»; развёрнут «at dozens of pharmaceutical and chemical companies»; названы Janssen, Pfizer, Syngenta.
  - `DEV` кейс на 75 одобренных FDA новых молекулах 2019–2023: «The final list contains 75 unique targets in total»; «This baseline run takes about an hour to finish for all 75 targets on a typical desktop … corresponding to roughly one minute of wall time per molecule»; после 4 прогонов с разными настройками для 5 целей маршрут из покупаемых веществ так и не был найден. Точных значений «решено/не решено» по каждому прогону в статье нет [53].
  - Приведённые там же одностадийные точности USPTO-50K (top-1/top-10: template relevance 45,2/83,5; RetroSim 37,3/74,1; Transformer с аугментацией 53,2/85,2; Graph2SMILES 52,9/79,5) — это **перецитированные литературные числа**, а не новая независимая оценка [53].
  - Журнальная версия: Acc Chem Res 2025, 58, 1764–1775 [55].
- **Конвейер:** цель и настройки стратегии → одностадийное расширение выбранными моделями с лимитами по числу шаблонов и вероятности → фильтр правдоподобия → поиск дерева (MCTS или Retro*) с ограничениями по узлам, ветвлению, глубине и цене против каталога → перечисление и ранжирование маршрутов → обогащение стадий (условия, прямой исход, примеси, селективность, растворимость) → интерактивная доработка и экспорт [53].
- **Сильные стороны:** самый широкий открытый набор функций (план → условия → примеси → свойства), интерактивное планирование там, где автоматический поиск не справляется, MIT-код, развёртывание за файрволом, API и MCP, длинная история промышленного использования. Ближайший «полный» ориентир по функциональности для нашей платформы.
- **Слабые стороны (признают авторы):** трансформерные модели «more black-box», предсказанные вероятности «may not be a robust measure of confidence for a particular result»; оценка выделения и очистки «remains elusive»; автоматический поиск отказывает на части целей; тяжёлая инфраструктура; лучшие шаблонные наборы (Reaxys/Pistachio/CAS) лицензионные, поэтому полностью открытое развёртывание слабее.

### 2.3 Syntheseus (Microsoft Research)

- **Категория:** библиотека для честного бенчмаркинга и единый каркас поиска (не продукт для химика). **Владелец:** Microsoft Research AI for Science. MIT, v0.8.0 от 03.08.2026, 212 звёзд [56].
- **Ключевые возможности** [56]: обёртки для 8 одностадийных моделей (Chemformer, GLN, Graph2Edits, LocalRetro, MEGAN, MHNreact, RetroKNN, RootAligned); алгоритмы поиска (MCTS, best-first/Retro*, BFS, PDVN, random); дедупликация и строгий exact-match по умолчанию; абстракции AND/OR-графа; CLI для одностадийной оценки.
- **Эффективность — это главный `IND`-источник в нише** (Maziarz et al., Faraday Discuss. 2025, 256, 568–586, DOI 10.1039/D4FD00093E; полный текст [57]):
  - Пересчитанные top-1/top-5/top-50 на USPTO-50K: RootAligned 56,0/86,1/94,2; RetroKNN 55,3/85,0/96,6; Chemformer 55,0/73,7/76,0; Graph2Edits 54,6/82,8/91,7; GLN 52,4/81,2/93,1; LocalRetro 51,5/84,3/96,7; MHNreact 50,6/80,1/92,6; MEGAN 48,7/79,5/93,5.
  - Рейтинг меняется: «LocalRetro was originally reported to have a better top-1 accuracy than GLN, but we find that to not be the case»; причина — нестрогое сравнение: «LocalRetro (and by extension RetroKNN) used a relaxed notion of success, and we see that the results deteriorate significantly» (53,4 → 51,5 и 57,2 → 55,3).
  - Дедупликация поднимает top-k при k>1 (GLN top-5 75,4% → 81,2%).
  - Обобщаемость: модели, обученные на USPTO-50K и проверенные на Pistachio, дают «in terms of top-50 accuracy all models still fall below 55%, compared to nearly 100% on USPTO» (top-1 Chemformer 26,1%).
  - Многостадийный тест: 190 «Retro* Hard» целей, 23 081 629 building blocks, 10 минут на молекулу. «we also find that the difference between Retro* and our MCTS reimplementation is small, which is in line with the results by Genheden & Bjerrum (2022), but contrasts the results from the original Retro* paper». Авторы подчёркивают, что solve rate вводит в заблуждение: допускающая модель даёт «решения», которые нереалистичны.
- **Конвейер:** выбор обёртки одностадийной модели (единый API, дедупликация и фильтр валидности) → одностадийная оценка (top-k exact match, MRR, скорость) на USPTO-50K/Pistachio → подключение инвентаря и алгоритма поиска → многостадийный прогон под бюджет вызовов/времени → метрики (время до первого решения, число неперекрывающихся маршрутов, число вызовов модели) → отчёт на дефолтных best practices [57].
- **Сильные стороны:** де-факто стандарт честного сравнения; разделяет вклад модели, поиска и инвентаря; уже переиспользуется третьими сторонами. Для нашего `eval/` это готовая опора.
- **Слабые стороны (по словам авторов):** метрики solve rate и recall «not ideal»; модель реализуемости не поставляется; и ключевое для нас: «the lack of information on reaction conditions, required quality of the starting materials, required equipment, and purification… is a significant barrier… which syntheseus does not address».

### 2.4 RetroBioCat / rbc2 (Манчестер)

- **Категория:** биокаталитический (ферментативный) ретросинтез с базой ферментных прецедентов; v2 допускает смешанные химико-ферментативные маршруты.
- **Доступ:** веб-приложение бесплатно (версия v2025.10.16; хостинг Disyn Biotec) [58]; код v1 под MIT, но репозиторий не обновлялся с 2023; **v2 (`rbc2`) под CC BY-NC 4.0** (некоммерческая) и без веб-части: «rbc2 does not feature a web-app element, and is instead designed to be used as soley a python package», 5 звёзд [60].
- **Ключевые возможности:** экспертно закодированные правила биокатализа в виде reaction SMARTS; сопоставление ферментных прецедентов по сходству субстрата; метрика молекулярной сложности; Network explorer (ручной режим) и Pathway explorer (автоматическое расширение с взвешенным скорингом); флаги сообщества о нереалистичных предложениях; в v2 — модульные расширители (RetroBioCat, EnzymeMap, BKMS, RetroRules) и химические расширители с опорой на AiZynthFinder/ASKCOS, плюс модуль MCTS [58], [60].
- **Эффективность (`DEV`, Nat Catal 2021) [59]:** «The current rule set consists of 99 reactions, described using 135 reaction SMARTS»; на тестовом наборе из 52 литературных каскадов «Except for C-H oxidation by P450 enzymes, all of the reactions in the test-set were correctly predicted by RetroBioCat», и «the majority of pathways were suggested within the top few suggestions using pathway explorer with only the default settings for the weighted score». База ферментных прецедентов описана отдельной статьёй с ролями и ревью записей, автоматическим BLAST против UniRef50 [61]; число записей в тексте не указано — «не подтверждено». Рецензируемой статьи по RetroBioCat 2 найти не удалось — «не подтверждено».
- **Конвейер:** SMILES цели → применение курированных ферментативных SMARTS → поиск литературного прецедента фермента для каждой стадии (с флагом «может потребоваться инженерия белка») → скоринг узлов (прецедент, изменение сложности, покупаемость, число стадий) → расширение сети автоматически или интерактивно → перечисление и взвешенное ранжирование путей [59].
- **Сильные стороны:** единственный широко используемый планировщик с биокатализом; экспертные правила + ферментный прецедент; бесплатный веб-UI; в v2 можно смешивать химию и ферменты.
- **Слабые стороны:** v2 некоммерческая лицензия, без веб-части и с незрелой документацией; правил мало (99) и они поддерживаются вручную; v1 не развивается с 2023; авторы сами отмечают риск, что ферментативные варианты «утонут» среди более многочисленных химических.

### 2.5 Коротко: остальные открытые компоненты

- **Retro*** (Chen et al., ICML 2020) [62]: best-first поиск по AND/OR-дереву с обученной функцией ценности; при бюджете 500 вызовов одностадийной модели success rate 86,84% против 55,26% у DFPN-E и 33,68% у MCTS в их постановке. Референс-реализация MIT, не поддерживается с 2022, но переиспользована в AiZynthFinder и Syntheseus.
- **LocalRetro** (JACS Au 2021) [63]: локальные атомные и связевые шаблоны + глобальное внимание; top-1 на USPTO-50K 53,4%, round-trip 89,5%/99,2% (top-1/top-5). Под независимой строгой оценкой — 51,5% [57]. Лицензия с 2026 — CC BY-NC-SA 4.0, то есть коммерческое использование требует разрешения.
- **Chemformer** (MolecularAI, Apache-2.0): предобученный seq2seq; независимая оценка — top-1 55,0% на USPTO-50K [57]; используется как плагин расширения AiZynthFinder. Журнальные детали (MLST 2022) подтвердить не удалось — издательская страница блокирует ботов.
- **RXNMapper** (Sci Adv 2021) [64]: безнадзорное картирование атомов по вниманию; «99.4% correct full atom-mappings on a test set of 49k strongly unbalanced patent reactions», 7,7 мс на реакцию на GPU. MIT. Для нас это инфраструктура проверки баланса и извлечения шаблонов.
- **SynPlanner** (JCIM 2025) [65]: сквозной стек «данные → картирование → извлечение правил → обучение policy/value GNN (supervised + RL) → MCTS-планирование», MIT, GUI и CLI, релиз v1.7.0 от 25.08.2026. Самый близкий аналог «собери свой планировщик из сырых данных».
- **DirectMultiStep** (JCIM 2025) [66]: генерация целого многостадийного маршрута одной строкой (mixture-of-experts трансформер); заявлены «1.9x and 3.1x improvements in Top-1 accuracy on the n1 and n5 test sets» PaRoutes. MIT.
- **Open Reaction Database (ORD)** [67], [68]: открытая схема и инфраструктура для структурированных данных о реакциях; данные под CC BY-SA 4.0, формат Parquet + зеркало на Hugging Face, порядок величины — от 1 до 10 млн реакций (точное число не заявлено, крупнейший отдельный датасет — 1,8 млн реакций). Основной легальный источник структурированных реакций для нашего `sources/`.
- **PaRoutes / rxnutils / AiZynthTrain / route-distances** (экосистема AstraZeneca, Apache-2.0/MIT) [69]: бенчмарк маршрутов, утилиты реакций, пайплайны обучения и метрики расстояния между маршрутами. `route-distances` — готовая основа для нашей метрики strategy diversity.

## 3. LLM и агентные системы

### 3.1 ChemCrow (EPFL/Rochester/IBM) и FutureHouse Phoenix

- **Категория:** LLM-агент с инструментами. **Публикация:** Nat Mach Intell 6:525–535 (08.05.2024) [72]. **Доступ:** MIT, `pip install chemcrow`, но README предупреждает: «This package does not contain all the tools described in the ChemCrow paper because of API usage restrictions… This repo will not give the same results»; в релиз вошло подмножество из 12 инструментов [73]. Продолжение как продукт — агент Phoenix на платформе FutureHouse (запуск 01.05.2025), сами авторы отмечают, что он слабее отбенчмаркен и может чаще ошибаться [74].
- **Ключевые возможности:** GPT-4 при температуре 0,1 под управлением LangChain, формат «Thought, Action, Action Input, Observation» (ReAct); в статье заявлено «18 expert-designed tools» в семействах: общие (веб-поиск, поиск по литературе, Python REPL, обращение к человеку), молекулярные (имя → SMILES, цена, патентный чек, функциональные группы), **безопасность** (проверка контролируемых веществ, взрывоопасности, сводка по безопасности), реакционные (именование, предсказание, планирование через RXN4Chemistry, исполнение на роботе) [72].
- **Эффективность (`DEV`):** 14 сценариев, базовая линия — GPT-4 без инструментов; эксперты оценивали «(1) correctness of the chemistry, (2) quality of reasoning and (3) degree of task completion», по 4 оценщика на задачу, всего 56 оценок. **Ключевой вывод для нашего протокола:** «EvaluatorGPT favours GPT-4, typically basing its evaluation on the fluency and apparent completeness of GPT-4's responses» и «LLM-based methods like EvaluatorGPT, for now, cannot replace expert human assessment»; в аннотации препринта это сформулировано как «GPT-4 as an evaluator cannot distinguish between clearly wrong GPT-4 completions and Chemcrow's performance». Там же: «GPT-4 systematically fails to provide factually accurate information». Процентных предпочтений в тексте нет [72].
- **Конвейер:** запрос пользователя → ReAct-цикл LLM (Thought → Action) → вызов инструмента (RXN, PubChem, RDKit-обёртки, проверки безопасности) → Observation возвращается в цикл → финальный ответ (опционально исполнение на роботизированной платформе) [72].
- **Сильные стороны:** заземление ответов на детерминированные инструменты; явные инструменты безопасности и проверки контролируемых веществ; открытый код.
- **Слабые стороны:** авторы сами отмечают «lack of reproducibility… under the current API-based approach»; зависимость от закрытой модели и проприетарных инструментов; «validity of ChemCrow's responses depends on the quality and quantity of the tools»; **нет provenance и статуса проверки на уровне отдельного факта и нет валидатора маршрута целиком**.

### 3.2 Coscientist (CMU)

- **Категория:** многомодульный LLM-агент с лабораторной автоматизацией. **Публикация:** Nature 624:570–578 (2023) [75]. **Доступ:** частичный релиз, Apache 2.0 с Commons Clause (коммерческое использование ограничено) [76]; авторы прямо пишут: «Because of safety concerns, data, code and prompts will be only fully released after the development of US regulations in the field of artificial intelligence and its scientific applications» [75].
- **Архитектура (подтверждена):** Planner — инстанс GPT-4, команды GOOGLE, PYTHON, DOCUMENTATION, EXPERIMENT; веб-поисковик «is another LLM itself»; код исполняется «in an isolated Docker container»; модуль документации извлекает и суммирует описания API; EXPERIMENT запускает код на оборудовании [75].
- **Эффективность (`DEV`):** тест на планирование синтеза для 7 широко известных безрецептурных соединений по шкале 1–5 (ниже 3 — провал), сравнение GPT-3.5, GPT-4, Claude 1.3, Falcon-40B-Instruct и версий с веб-поиском. Версия GPT-4 с веб-поиском получила максимум по 4 соединениям и была единственной, преодолевшей порог на самом сложном из них; «All non-browsing models incorrectly synthesized ibuprofen»; вывод — «importance of grounding LLMs to avoid 'hallucinations'». Авторы признают, что «labelling is inherently subjective» [75].
- **Конвейер:** запрос → Planner (GPT-4) → GOOGLE/DOCUMENTATION (суммаризация LLM) → PYTHON в песочнице → EXPERIMENT (API робота) → Observation назад в Planner [75].
- **Сильные стороны:** чётко показано, что веб-заземление сильнее параметрической памяти; цикл замкнут на реальное оборудование.
- **Слабые стороны:** субъективная оценка на 7 объектах; извлечённые тексты суммирует LLM, структурной проверки химии нет; полная система не выложена, результат невоспроизводим.

### 3.3 Strategy-aware планирование: Bran et al. / steer (EPFL)

- **Категория:** LLM как оценщик/судья маршрутов поверх классического поиска. **Публикация:** Matter, 24.04.2026, DOI 10.1016/j.matt.2026.102812 [77]; препринт arXiv:2503.08537 v2 [78]. **Код:** `steer`, MIT [79].
- **Ключевая идея:** LLM не генерирует структуры — «We employed the AiZynthfinder software as the underlying retrosynthesis engine», а оценивает и отбирает маршруты по стратегии, заданной естественным языком [78].
- **Эффективность (`DEV`):** бенчмарк из 13 стратегических запросов на 4 целях; лучший результат у Gemini-2.5-pro, «improving over 50% relative to the next best model»; у малых моделей «performance is indistinguishable from random choice even for short routes»; на маршрутах до 50 реакций все модели, кроме Gemini-2.5-pro, «struggle to distinguish and select aligned routes». Отдельный бенчмарк на механизмы: 12 реакций, случайный baseline 17%, разброс между моделями огромный (у GPT-4o-mini до 5%). В пресс-релизе EPFL: «36 chemists provided 368 valid evaluations», их суждения совпали с оценками системы «71.2% of the time on average» [77].
- **Конвейер:** цель + стратегия на естественном языке → MCTS AiZynthFinder генерирует маршруты-кандидаты → сериализация маршрутов в текст → LLM оценивает каждый и пишет обоснование → ранжирование или направление поиска [78].
- **Сильные стороны:** разделение ролей ровно как в нашем ADR-0002 (LLM предлагает/оценивает, детерминированный движок обеспечивает валидность); открытый код; есть человеческая калибровка судьи.
- **Слабые стороны:** качество ограничено «the quality and diversity of synthetic routes generated by the backend»; типичные сбои — «grouping reactions» и разбор реакций «in an inverse sense»; сам судья остаётся непроверенной LLM.

### 3.4 LLM-Syn-Planner (ICML 2025)

- **Подход:** LLM генерирует маршрут целиком, эволюционный поиск его дорабатывает; каждая реакция сверяется с базой реакций, несопоставленные стадии помечаются «non-existent», молекулы обязаны парситься RDKit и находиться среди 23 млн building blocks eMolecules [80].
- **Эффективность (`DEV`):** при бюджете N=100 вызовов solve rate (GPT-4o / DeepSeek-V3): USPTO-190 — 64,7 / 62,1 против 86,8 у RootAligned+Retro*; Pistachio Hard — 72,0 / 74,0 против 83,0. При N=500 USPTO-190 вырастает до 92,1 / 92,6. LLM в роли простой одностадийной модели даёт 0,0 на Pistachio Hard [80].
- **Конвейер:** поиск похожих маршрутов → генерация маршрута LLM → сверка с базой/шаблонами и проверки RDKit → оценка приспособленности → мутации и отбор.
- **Вывод для нас:** без детерминированной сверки LLM-маршрут нежизнеспособен, а с ней при большом бюджете он догоняет специализированные модели. Код на момент проверки не выложен — «не подтверждено».

### 3.5 AOT* (Findings of ACL 2026)

- **Подход:** LLM управляет AND/OR-поиском; валидация сверкой с библиотекой более 270 тыс. шаблонов USPTO, несопоставленные реакции помечаются «non-existent» [81].
- **Эффективность (`DEV`):** при N=100 — 86,3 на USPTO-190 и 86,0 на Pistachio Hard против 86,8 и 78,0 у RootAligned+Retro*; при N=300 — 93,1; заявлено «3-5× fewer iterations» по сравнению с предыдущими LLM-методами [81].
- **Осторожно:** галлюцинации устраняются конструкцией, а не измеряются; числа LLM-Syn-Planner в сравнительной таблице совпадают с оригинальными, то есть перенесены, а не перепроверены.

### 3.6 DeepRetro (препринт, не рецензирован)

- **Подход:** сначала пробуется AiZynthFinder, при отказе LLM предлагает разрыв, затем фильтры валидности/стабильности/«галлюцинаций», рекурсия по предшественникам и правки человеком в цикле [82].
- **Эффективность (`DEV`, сами авторы просят считать числа качественными):** одностадийно на 250 реакциях USPTO-50k «Any Correct»: DeepRetro + Claude 4 Opus + Pistachio — 135 (54%), ASKCOS — 115, AiZynthFinder (Pistachio) — 83. Многостадийно на USPTO-190 — 183/190 против 177 у PDVN и 139 у Retro*. Химики оценили точность метаданных в 40% (Claude 3 Opus) и 80% (Claude 4 Opus). Стоимость «over $1 USD per molecule». Авторы признают, что обвязка проверок «still misses many edge cases» [82].
- **Вывод для нас:** это ближайший по идее прототип (LLM + детерминированные фильтры + человек в цикле), и он же показывает, насколько рыхло сегодня определяются «проверки» — именно это мы формализуем кодами диагностик. Оценка «метаданных» в 40–80% — прямой аргумент за citation grounding.

### 3.7 Остальные LLM-системы кратко

- **Llamole** (ICLR 2025) [83]: мультимодальная LLM, где реакции порождает GNN поверх top-50 шаблонов (поэтому «выдуманных» реакций нет); «increases the success ratio from 5% to 35% for drugs and to 17.9% for polymers» (успех = маршрут до покупаемых building blocks Enamine). Там же базовые LLM не выдают валидный формат реакции или шаблон в 68,4% (in-context) и 57,6% (fine-tuned) случаев. Apache-2.0.
- **Chemma** (Nat Mach Intell, онлайн 01.07.2025) [84]: LLM, дообученная на «1.28 million pairs of Q&A about reactions»; заявлен top-1 на USPTO-50k 72,2% против «the best reported Top-1 accuracy of 57.7%» и R² выхода 0,88. DOI и код подтвердить не удалось — «не подтверждено».
- **SynAsk** (Chem Sci 2024) [85]: дообученный Qwen-1.5 + LangChain, 12 внутренних и 10 внешних инструментов; на 11 549 препаратах ChEMBL выдал маршруты для 6 358 (55%) против 3 118 (27%) у AiZynthFinder — но это именно «выдал», а не «валидировал»; MAE прогноза выхода 14,1% на 60 литературных реакциях. Анализа галлюцинаций нет.
- **ether0** (FutureHouse, открытые веса Apache-2.0) [86]: 24B на базе Mistral, RL на 640 730 задачах; награда за реакции — «exact molecule match with RDKit», за ретросинтез — «reactants must all be purchasable» плюс проверка прямой моделью; для прямого предсказания «70% accuracy after 46,000 examples, compared to MT's 64.1%». Точность ретросинтеза не приводится; сами авторы называют модель «fundamentally a research model» с малой пользой для условий реакций.
- **Retro-R1** (NeurIPS 2025) [87]: RL-агент, который «interacts dynamically with plug-in single-step retrosynthesis tools»; заявлено «55.79% pass@1», на 8,95 пункта выше предыдущего SOTA на наборе Retro*-190. MIT.
- **Общий вывод по разделу:** все числа качества маршрутов в разделе 3 — self-reported. Независимые измерения (раздел 4) показывают, что LLM без обвязки заметно слабее специализированных инструментов, а архитектурная конвергенция 2025–2026 однозначна: **LLM предлагает или судит, детерминированный слой ограничивает**. Ни одна из систем не привязывает к каждому факту источник и статус проверки и не проверяет литературные ссылки и условия.

## 4. Процессная сторона: симуляторы, зелёные метрики, регуляторные проверки

> Общий факт, важный для позиционирования: **ни один из симуляторов не принимает маршрут как вход.** Всем нужна собранная пользователем схема/рецепт плюс стехиометрия, выходы или кинетика. Это вывод по их страницам возможностей; импорт маршрута не заявляет ни один из них.

### 4.1 DWSIM (открытый симулятор процессов)

- **Доступ:** Core Edition «Free to download and use, source code available», GPL v3; Patreon Edition добавляет функции при подписке (Explorer 7,49 / Premium 29,99 / Premium+ 59,99 USD в месяц); MCP-сервер «Free and open-source (GPL-3)» [103]. Версия 10.2.11 от 08.10.2026. **Риск:** публичный репозиторий «was archived by the owner on Aug 11, 2026. It is now read-only» [104].
- **Возможности, важные для нас** [105]: «Fluent API in Python/VB.NET for programmatic flowsheet automation» (04.2026) и **MCP-сервер, который отдаёт схемы LLM-агентам** (05.2026); AI-подсказки кода и AI-ускоритель сходимости; режим BioReactor (batch/fed-batch) как «cycle-averaged steady state»; термопакеты GERG2008, PC-SAFT, CoolProp, Reaktoro; Python-консоль. Фарма-специфичных функций и рецептурной логики не найдено.
- **Эффективность:** метрик нет; единственный косвенный показатель распространённости — около 800 загрузок в неделю на SourceForge [106].
- **Конвейер:** компоненты и термопакет → схема аппаратов и реакторов → реакции и кинетика → расчёт (стационарный или динамический) → автоматизация через Python/Fluent API/MCP → результаты.
- **Сильные стороны:** бесплатен, кроссплатформенный, скриптуемый; MCP-эндпоинт — готовая точка интеграции «наш маршрут → модель установки».
- **Слабые стороны:** ориентация на непрерывные процессы, слабая поддержка многостадийных периодических процессов АФИ (наш вывод); архивированный репозиторий — риск поддержки; часть функций за подпиской.

### 4.2 Коммерческие симуляторы и инструменты масштабирования

- **Aspen Plus (batch modelling), AspenTech.** Владелец — Emerson: выкуп остальных акций AspenTech завершён 12.03.2025 [109]. Доступ коммерческий, цены по запросу — «не подтверждено». Возможности: «Simulate batch, semi-batch and continuous processes involving reaction, distillation, crystallization, filtering and drying», «extensive and customizable library of kinetic models» [107]; исторически — консоль разработки процесса, модели растворимости NRTL-SAC для подбора растворителя и автоматические записи партий для пилота [108]. Доказательства — только качественные отзывы GSK и AstraZeneca 2009 года без чисел [108].
- **gPROMS FormulatedProducts (PSE, Siemens).** «an end-to-end solution for modeling and simulation of pharmaceutical processes», цены «Contact us» [110]. Числовых доказательств нет; текущая версия — «не подтверждено».
- **Dynochem / Scale-up Suite (Scale-up Systems).** Владелец — METTLER TOLEDO с октября 2021: «In October 2021, we also acquired Scale-up Systems Inc., a leading software provider for scale-up and reaction modeling … The initial cash payment was $20.2 million» [112]. Возможности: подгонка кинетики, инструменты перемешивания и теплопередачи, кристаллизация, замена растворителя, **утилита стоимости и «зелёности» процесса**, автоматизация RunScript, Reaction Lab («Kinetics Meets ELN») [111]. Доказательства — кейсы клиентов, размещённые вендором (`VENDOR`): «Run 81 virtual experiments in 5 minutes, saving >30 days compared to a lab DOE»; у Lilly «average per project savings were ~10x API use and 20% FTE time»; у Siegfried «enabled directly scale up from 1 L to 4000 L» [111].
- **SuperPro Designer (Intelligen).** Единственный с публичной ценой: «$ 7,000 per copy / per year» за фиксированную лицензию, комплект со SchedulePro — 11 000 USD/год, бессрочная лицензия «has been discontinued», есть бесплатная ознакомительная версия и академические скидки [113]. Возможности: двухуровневое представление периодического процесса, база более 1 200 материалов, оценка CAPEX/OPEX, диаграммы Ганта и загрузки оборудования, поиск «узких мест», **оценка воздействия на среду**, отчёты по выбросам и стокам [114]; `VENDOR`: «More than 500 companies» и «more than 1000 colleges and universities».
- **Общий вывод:** это слой «после выбора маршрута». Для платформы они интересны как **потребители экспорта** (стехиометрия, рецепт, масштаб), а не как конкуренты.

### 4.3 Зелёные метрики: инструменты ACS GCI Pharmaceutical Roundtable

- **Доступ:** все перечисленные инструменты бесплатны (Excel или веб), индекс — [115]. API не найдено — «не подтверждено».
- **PMI Calculator (линейный):** Excel, бесплатно, «In 2011, the ACS GCI Pharmaceutical Roundtable released a free, publicly available linear PMI calculator»; PMI = кг всех входных материалов на кг готовой субстанции, вода включается. Бенчмарк по данным 2008 года: растворители 58%, вода 28%, реагенты 8%, прочее 6% от PMI [116].
- **Convergent PMI Calculator:** Excel, бесплатно, 2014 год; «Up to 11 step linear sequence» и «Up to 3 branches for convergent synthesis» [116].
- **PMI Prediction Calculator (PMI Predictor):** веб-приложение; статья Borovika et al., Nature Sustainability 2019, 2(11), 1034–1040 [117]. Монте-Карло по историческим межкорпоративным данным PMI, назначение — «predict the probable efficiencies of proposed synthetic routes before their evaluation in the laboratory». **Это самая прямо переиспользуемая метрика для оценки предложенного маршрута до лаборатории.** Объём обучающих данных (порядка 2 000 точек) — «не подтверждено».
- **Solvent Selection Tool:** бесплатный веб-инструмент, основан на Diorazio, Hose, Adlington, Org Process Res Dev 2016, 20, 760–773; «User identifies the necessary properties (from ~100 options)», «shortlists appropriate solvents (from set of 272 candidates)», «PCA identified 5 Principal Components», фильтры включают класс растворителя по ICH [118].
- **Reagent Guides:** веб, 28 руководств в навигации (на странице инструментов указано «over 25 transformations») [119].
- **iGAL 2.0 (Green Chemistry Innovation Scorecard):** веб-калькулятор, «Version 2.0 released August 6, 2021», основан на «64 bulk active pharmaceutical manufacturing processes encompassing 703 steps across 12 companies»; входы — бессолевая молекулярная масса, фаза разработки, % выхода, % конвергентности и cEF = PMI − 1; выход — относительный показатель «зелёности» [120].
- **CHEM21 solvent guide:** Prat et al., Green Chem 2016, 18, 288–296; оценки безопасности, здоровья и среды по шкале 1–10 («1 to 3: green, 4 to 6: yellow, 7 to 10: red»), категории Recommended / Problematic / Hazardous, интерактивный скорер + Excel для растворителей вне списка [121].
- **Сильные стороны:** бесплатно, это де-факто отраслевой стандарт метрик, легко встраивается в платформу как расчёт по RouteSpec.
- **Слабые стороны:** ввод данных ручной (Excel/веб-формы), API нет, PMI игнорирует опасность, часть эталонных данных относится к 2008–2010 годам.

### 4.4 Регуляторные и safety-инструменты (ICH M7 и опасности)

- **Mirabilis (Lhasa Limited)** — **единственный подтверждённый инструмент, который принимает маршрут синтеза как вход для регуляторной оценки.** Запущен 20.01.2015 консорциумом (AbbVie, AstraZeneca, Lilly, GSK, Roche, Novartis, Pfizer) [124]; SaaS на AWS с 2018 года; охват расширен на N-нитрозамины. Конвейер (подтверждён) [123]: пользователь «enter their synthesis scheme(s), highlight the impurities of concern» → модель предсказывает purge factor «made up of reactivity, solubility and volatility purge factors» → требуемый purge factor считается из дозы, исходной концентрации примеси и предела контроля → purge ratio = предсказанный / требуемый → отображение в опцию контроля ICH M7 (PR > 1000 — поддерживается опция 4 с указанием ratio; 1000 > PR > 100 — опция 4 с полным расчётом и литературой; 100 > PR > 1 — опция 4 только при сильных данных; PR < 1 — нужны опции 3, 2 или 1). `VENDOR`-вебинар со ссылкой на опрос IQ: по 11 производителям 59% из 260 принятых примесей использовали стратегию опции 4, доля регуляторного одобрения опции 4 — 96% FDA, 95% EMA, 97% PMDA; модель «typically under-predicting by a factor of 10», то есть сознательно консервативна [125]. Цены — «не подтверждено».
- **Derek Nexus (экспертные правила) и Sarah Nexus (статистика), Lhasa.** Вместе «satisfy the two-methodology requirement in ICH M7» [126]. Рецензируемая оценка (авторы из Lhasa): две системы «showed concordance in 70–85% of predictions with accuracy as high as 90% for concordant results»; на специально подобранном сложном наборе экспертная проверка оказывалась точнее обеих систем [127]. Цены — «не подтверждено».
- **CHETAH 11.0 (ASTM), 2020.** Групповая аддитивность Бенсона; назначение — «classifying materials for their ability to decompose with violence», оценки теплот реакции и пределов воспламеняемости; лицензия на одного пользователя, цена по запросу [128].
- **Корреляция Yoshida:** отдельного ПО не найдено, применяется к экспериментальным данным ДСК — «не подтверждено». **Bretherick's:** не проверено.
- **Есть ли регуляторные проверки внутри CASP:** ChemAIRS предсказывает примеси стадии, но ICH M7 не упоминает [129]; ASKCOS предсказывает примеси (минорные продукты, переокисление, димеризация, аддукты растворителя), но модулей токсикологии и мутагенности в списке нет [130]; у SYNTHIA подтверждены исключение реагентов и поиск более зелёных альтернатив, фильтр по ICH M7 — «не подтверждено». **Итог: ни один CASP не объединяет генерацию маршрута с (Q)SAR-скринингом по ICH M7 и оценкой выведения примесей. Mirabilis и Derek/Sarah работают только после того, как маршрут нарисован человеком.**

## 5. Бенчмарки и доказательная база

### 5.1 USPTO-50K: одностадийный top-k

- **Происхождение:** Liu et al. 2017 (ACS Cent Sci, DOI 10.1021/acscentsci.7b00303): «50,000 atom-mapped reactions that have been classified into 10 broad reaction types», извлечены из патентов (датасет Lowe), классы по Schneider et al. 2016; сплит «into training, validation and test datasets (8:1:1)»; в исходной постановке класс реакции подавался модели на вход. Их seq2seq давал top-1/10/50 = 34,1/62,0/71,9% против 34,8/65,7/69,8% у правилового baseline [102].
- **Протокол сегодня:** top-k exact match набора реагентов при неизвестном классе реакции; тестовая часть ~5 тыс. реакций.
- **Представительные top-1 (сводная таблица [95], если не указано иное):** LocalRetro 53,4; R-SMILES 56,3; Graph2Edits 55,1; EditRetro 60,8 (Nat Commun 2024, «top-1 accuracy of 60.8% on the standard benchmark dataset USPTO-50 K» [97]); RetroSynFlow 60,0; RSGPT 63,4 (Nat Commun 2025, «Top-1 accuracy of 63.4%, substantially outperforming previous models» [96]); RetroDFM-R 60,4 (66,1% при полном инференсе) [98]. На USPTO-FULL (~1 млн реакций) top-1: RSGPT 59,2; R-SMILES 48,9; NAG2G 49,7; GLN 39,3; LocalRetro 39,1 [95].
- **Важный контекст по RSGPT:** ~3,2 млрд параметров, более 10 млрд синтетических реакций в предобучении, многоступенчатый пайплайн (предобучение → RLAIF → SFT), инференс с 20-кратной аугментацией; в сводной работе его трактуют как «upper-bound baseline» [95]. Проверял ли кто-нибудь пересечение синтетических данных с тестом — «не подтверждено».
- **Критика метрики:**
  - Дедупликация меняет результаты: top-5 GLN «can be increased by as much as 5.8% with simple deduplication» [57].
  - Нестрогое сравнение стерео завышало результаты LocalRetro на +1,3 п.п. top-1, и эти числа копировались дальше [57].
  - Top-k измеряет только recall эталона и ничего не говорит о качестве остальных предложений; эталон шумный, а валидные альтернативы считаются ошибкой [43], [57].
  - USPTO-50K слишком узок: в независимой работе «Models Matter» он назван «insufficient», а выбор одностадийной модели меняет успех многостадийного поиска «by up to +28%» [71].

### 5.2 PaRoutes: многостадийный бенчмарк

- **Что это:** два набора по 10 000 маршрутов, извлечённых из патентной литературы (n1 и n5), списки стока как критерий остановки и курированный набор реакций для обучения одностадийных моделей [70], [69].
- **Метрики:** число решённых целей и восстановление эталонного патентного маршрута в top-1/5/10; разнообразие через кластеризацию маршрутов.
- **Результаты версии 2.0** (таблица в репозитории, [69]):

| Метод | Набор | Решено (из 10 000) | Top-1 | Top-5 | Top-10 |
|---|---|---|---|---|---|
| MCTS | n1 | 9716 | 0,2372 | 0,5107 | 0,5414 |
| MCTS | n5 | 9689 | 0,1237 | 0,3584 | 0,4056 |
| Retro* | n1 | 9728 | 0,2027 | 0,4516 | 0,4847 |
| Retro* | n5 | 9729 | 0,1143 | 0,3365 | 0,3897 |
| DFPN | n1 | 7786 | 0,1705 | 0,2456 | 0,2460 |
| DFPN | n5 | 6730 | 0,0753 | 0,1146 | 0,1151 |

- **Главный вывод:** при доле решённых целей ~97% известный патентный маршрут оказывается на первом месте лишь в 12–24% случаев. «Решено» не означает «так и делают на практике». Метрику разнообразия на основе кластеризации независимые авторы называют немонотонной [57].

### 5.3 Переоценка через Syntheseus — ключевой независимый источник

Числа приведены в разделе 2.3. Для статьи важны три вывода [57]:
1. Рейтинги моделей меняются при унификации протокола (дедупликация, строгий exact match) — значит, цитировать чужие таблицы без перепроверки нельзя.
2. Обобщаемость резко падает за пределами домена обучения: top-50 ниже 55% на Pistachio против почти 100% на USPTO.
3. Solve rate может вводить в заблуждение: «допускающая» модель даёт больше формальных решений за счёт нереалистичных реакций. То есть нужна метрика реализуемости и происхождения, а не только решаемости.

### 5.4 Что ещё измеряют и чего не хватает

- **Round-trip accuracy, coverage, class diversity** [100], [30]: обратная проверка предсказанных предшественников прямой моделью — ровно та идея, которую мы реализуем детерминированно.
- **Retro-fallback** (ICLR 2024) [99]: существующие планировщики «overlook the fact that we have imperfect knowledge of the space of possible reactions»; предлагается стохастическая модель реализуемости и максимизация вероятности, что хотя бы один план сработает; результат «generally produces better sets of synthesis plans than the popular MCTS and retro*».
- **SDDBench** [101]: round-trip оценка маршрута через сходство цели с продуктом, предсказанным прямой моделью из найденного сырья; мотивация — SA score «falls short of guaranteeing that synthetic routes can actually be found».
- **Экспертные оценки маршрутов:** двойной слепой AB-тест (компьютерные маршруты эквивалентны литературным) [21]; Turing-подобный тест (маршруты «largely indistinguishable») [6]; 99 химиков с PhD и 599 парных сравнений в пользу предсказаний RetroChimera «(P<0.05, mean preference rate ≈64%)» [43]; 4-градационный протокол RetroTrim на 32 целях [31]; 36 химиков и 368 оценок при согласии с LLM-судьёй «71.2% of the time on average» [77].
- **Люди против LLM как судей маршрутов** (`IND`, Voinarovska et al., Digital Discovery 2026, 5, 3648–3660) [94]: 17 химиков-экспертов оценивали 50 ретросинтетических путей AiZynthFinder, им противопоставлены Claude Opus 4.8, GPT-5.5, Llama 3.1 70B и Gemini 3.1 Pro. Gemini 3.1 Pro ближе всего к мнению человеческого большинства, GPT-5.5 и Opus систематически пессимистичнее, Llama 3.1 70B имеет «pronounced optimistic bias». Значений каппы в аннотации нет — «не подтверждено». Вывод: LLM-судья по маршрутам пригоден только при калибровке и указании модели, иначе смещение переносится в метрику.

### 5.5 LLM в химии: что показывают независимые бенчмарки

- **Guo et al., NeurIPS 2023 D&B** (`IND`, 100 тестовых примеров USPTO-50k) [88]: top-1 ретросинтеза — Chemformer 0,536 при 0% невалидных SMILES; GPT-4 zero-shot 0,006 при **20,6% невалидных SMILES**; лучший few-shot GPT-4 0,114 при 11,0%; Llama2-13B 0 при 27,2%. Прямое предсказание на USPTO-MIT: Chemformer 0,938 против GPT-4 zero-shot 0,004 при 17,4% невалидных. Вывод авторов — «less competitive performance in tasks demanding precise understanding of molecular SMILES».
- **Microsoft Research AI4Science, отчёт по GPT-4** [89]: на первых 500 примерах USPTO-50K «accuracy of GPT-4 (20.6%) is lower than that of the domain-specific model (53.6%)»; доля невалидных SMILES 17,8% в zero-shot и 4,8% при few-shot по отпечаткам; отмечено, что для докинга модель «merely fabricates a score».
- **LlaSMol** [93]: ретросинтез на USPTO-full — SOTA-модель 47,0% exact match при валидности 99,7%; GPT-4 0,0% при валидности 42,6%; Claude 3 Opus 1,1% при 94,8%; дообученная LlaSMol-Mistral 7B 32,9% при валидности 100%.
- **«Evaluating LLMs in Scientific Discovery»** (`IND`, 2025) [90]: таблица «Retrosynthesis solve rate comparison on Pistachio Hard (100 targets)»: gpt-4o 60,0; gpt-5 53,0; claude-sonnet-4.5 53,0; deepseek-R1 42,0; RootAligned (MCTS) 83,0. Причина отставания названа прямо: «Due to frequent failures in molecule or reaction validity checks», модели «fail to outperform traditional retrosynthesis models on established benchmarks».
- **ChemBench** (`IND`, Nat Chem 2025) [91]: «2788 question-answer pairs», человеческий baseline — «19 experts in chemistry»; лучшая модель «outperforms the best human in our study in this overall metric by almost a factor of two», но «most models are not well-calibrated and provide misleading confidence estimates»; провалы на подсчёте сигналов ЯМР («22 percent correct answers for o1») и на оценке предпочтительности структур («often indistinguishable from random guessing»). Задач по планированию синтеза в наборе нет.
- **Выдуманные ссылки** (`IND`, Walters & Wilder, Sci Rep 2023) [92]: «55% of the GPT-3.5 citations but just 18% of the GPT-4 citations are fabricated» (42 темы, не только химия). Исследования, которое измеряло бы долю выдуманных DOI именно в химических ответах и в описаниях условий, найти не удалось — **«не подтверждено», и это прямая ниша для нашей метрики citation grounding rate (RQ3)**.

## 6. Матрица возможностей

Обозначения: ✓ — есть и подтверждено источником; ~ — частично (ограниченно, только в одном модуле, или вручную); ✗ — нет; **?** — не подтверждено.

Столбцы: **Retro** — движок ретросинтеза; **Усл.** — предсказание условий реакции; **Лит.** — литературное заземление со ссылками на источник стадии; **Пров.** — явный статус проверки / происхождения у каждого факта; **Масшт.** — процессный вид и масштаб (lab/pilot/plant); **Зелён.** — зелёные метрики (PMI и аналоги); **Безоп.** — флаги безопасности и регуляторики (ICH, опасности); **Чат** — интерактивная правка через диалог; **Diff** — версии и семантический diff маршрута; **Эксп.** — экспорт отчёта (HTML/PDF/SVG); **OSS** — открытый код.

| Решение | Retro | Усл. | Лит. | Пров. | Масшт. | Зелён. | Безоп. | Чат | Diff | Эксп. | OSS |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Ручной baseline (химик + SciFinder/Reaxys) | ✓ | ✓ | ✓ | ~ | ✓ | ~ | ✓ | ✓ | ✗ | ✓ | ✗ |
| SYNTHIA [1–7] | ✓ | ? | ? | ✗ | ✗ | ~ | ~ | ✗ | ✗ | ~ | ✗ |
| CAS SciFinder Retrosynthesis [8–12] | ✓ | ~ | ✓ | ~ | ✗ | ✗ | ✗ | ~ | ✗ | ✓ | ✗ |
| Reaxys Predictive Retrosynthesis [13–20] | ✓ | ~ | ✓ | ~ | ✗ | ✗ | ✗ | ✗ | ✗ | ~ | ✗ |
| Iktos Spaya [22–24] | ✓ | ✗ | ? | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ? | ✗ |
| IBM RXN / rxn-sandbox [25–30] | ✓ | ~ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ~ | ~ |
| ChemAIRS [32–35, 129] | ✓ | ✓ | ~ | ✗ | ✓ | ✗ | ~ | ✗ | ? | ? | ✗ |
| PostEra Manifold [36–39] | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ? | ✗ |
| Molecule.one RetroTrim / Maria [31, 40–42] | ✓ | ~ | ~ | ~ | ~ | ✗ | ✗ | ✗ | ✗ | ? | ✗ |
| RetroChimera [43, 44] | ~ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ |
| AiZynthFinder [48–52] | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ~ | ✓ |
| ASKCOS v2 [53–55, 130] | ✓ | ✓ | ✗ | ~ | ✗ | ✗ | ~ | ~ | ✗ | ✓ | ✓ |
| Syntheseus [56, 57] | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ |
| RetroBioCat / rbc2 [58–61] | ✓ | ✗ | ✓ | ~ | ✗ | ~ | ✗ | ✗ | ✗ | ~ | ~ |
| ChemCrow / Phoenix [72–74] | ~ | ~ | ~ | ✗ | ✗ | ✗ | ✓ | ✓ | ✗ | ✗ | ✓ |
| Coscientist [75, 76] | ~ | ✓ | ~ | ✗ | ✗ | ✗ | ✗ | ✓ | ✗ | ✗ | ~ |
| steer / Bran et al. [77–79] | ✓ | ✗ | ✗ | ~ | ✗ | ✗ | ✗ | ✓ | ✗ | ✗ | ✓ |
| DeepRetro [82] | ✓ | ~ | ~ | ~ | ✗ | ✗ | ~ | ✓ | ✗ | ✗ | ✓ |
| Симуляторы (DWSIM, Aspen, Dynochem, SuperPro) [103–114] | ✗ | ✗ | ✗ | ✗ | ✓ | ~ | ~ | ✗ | ~ | ✓ | ~ |
| ACS GCI tools (PMI, iGAL, solvents) [115–122] | ✗ | ✗ | ✓ | ✗ | ~ | ✓ | ~ | ✗ | ✗ | ~ | ~ |
| Mirabilis + Derek/Sarah [123–127] | ✗ | ✗ | ✓ | ✓ | ✗ | ✗ | ✓ | ✗ | ✗ | ✓ | ✗ |
| **synthroute (цель проекта)** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

Пояснения к спорным клеткам:
- «Лит.» = ✓ только там, где источник конкретной стадии показывается пользователю со ссылкой (CAS [9], Reaxys [18], RetroBioCat [59], Mirabilis/Derek как регуляторные отчёты). У ML-движков без литературной базы столбец пуст по существу, а не по недосмотру.
- «Пров.» = ✓ только у Mirabilis: это единственный найденный инструмент, который по входному маршруту выдаёт формализованный вердикт с градацией и привязкой к регуляторной опции [123].
- «Чат» у ChemCrow, Coscientist, steer, DeepRetro означает диалоговый интерфейс агента, а не редактирование маршрута как объекта с версиями.
- «Diff» не реализован нигде из проверенного: у симуляторов есть сравнение сценариев, но не семантический diff маршрута.
- Строка synthroute — **целевое состояние по ТЗ**, а не измеренный факт.

## 7. Что работает эффективно, а что нет

### Работает

1. **Шаблонный/ML-ретросинтез как генератор идей.** Доля целей, для которых находится формально замкнутый маршрут, высокая: 80–86% на внутренних наборах AstraZeneca, 71% на ChEMBL [50], ~97% на PaRoutes [69], 94%/82% у PostEra в независимой проверке [38]. Для drug-like целей из литературного пространства это рабочий инструмент.
2. **Одностадийное предсказание прямой реакции.** Трансформер превосходит средний результат людей на контрольном наборе: 87,5% против 76,5% top-1 [29]. Это надёжная основа для обратной проверки (round-trip).
3. **Правиловые системы с лабораторной валидацией.** Единственные подтверждённые случаи «спланировано машиной — сделано в лаборатории» описаны для SYNTHIA/Chematica [5], [6].
4. **Экспертная оценка вслепую как метрика.** Двойные слепые AB-тесты [21], Turing-подобный тест [6], парные сравнения [43] и 4-градационный протокол [31] работают и дают интерпретируемые результаты. Это лучший доступный способ измерять «технически осмысленно или нет».
5. **Разделение ролей «LLM предлагает / детерминированный слой ограничивает».** Все сильные результаты 2025–2026 построены так: шаблонная сверка [80], [81], AiZynthFinder как движок [78], [82], RDKit + проверка покупаемости [83], [86]. Там, где LLM работает как судья с калиброванной человеческой проверкой, согласие с большинством экспертов достигает ~71% [77].
6. **Открытая инфраструктура оценки.** Syntheseus [57], PaRoutes [69], ORD [67] и RXNMapper [64] дают воспроизводимую базу, которой пять лет назад не было.
7. **Бесплатные отраслевые метрики «зелёности».** PMI-калькуляторы, PMI Predictor, iGAL 2.0, CHEM21 — готовые, признанные консорциумом формулы, которые можно считать по маршруту до лаборатории [116]–[121].

### Не работает

1. **LLM без обвязки.** Независимые измерения единодушны: top-1 ретросинтеза GPT-4 0,006 против 0,536 у Chemformer при 20,6% невалидных SMILES [88]; 20,6% против 53,6% у специализированной модели [89]; 0,0% exact match при валидности 42,6% [93]; solve rate 42–60 против 83 у RootAligned+MCTS [90]. Базовые LLM не выдают валидный формат реакции в 57,6–68,4% случаев [83].
2. **Метрика top-k exact match.** Завышается дедупликацией и нестрогим сравнением, меняет рейтинги при унификации протокола, не отражает качество альтернатив, рушится вне домена обучения (top-50 < 55% на Pistachio) [57], [71].
3. **Solve rate как критерий пригодности.** При 97% «решённых» целей реальный патентный маршрут оказывается первым лишь в 12–24% случаев [69]; «допускающие» модели набирают решения за счёт нереалистичных реакций [57]. На сложных drug-like целях экспертная оценка показывает большую долю «No pathway» и «Nonsense» даже у сильных систем [31].
4. **LLM как автоматический судья без калибровки.** EvaluatorGPT предпочитает беглость правильности и «cannot distinguish between clearly wrong GPT-4 completions» [72]; разные модели систематически смещены в пессимизм или оптимизм [94]. Для нашего протокола это запрет на LLM-as-judge в основной метрике.
5. **Условия, выделение и очистка.** Прямая цитата авторов Syntheseus: «the lack of information on reaction conditions, required quality of the starting materials, required equipment, and purification… is a significant barrier… which syntheseus does not address» [57]. Авторы ASKCOS добавляют, что оценка выделения и очистки «remains elusive» [53].
6. **Происхождение и проверяемость фактов.** Ни одна из проверенных систем не привязывает к каждой стадии источник плюс статус проверки. Литературные ссылки есть у CAS и Reaxys, но они внутри платной закрытой платформы и не выгружаются в открытый формат; у ML-движков ссылок нет вовсе.
7. **Регуляторика и безопасность внутри планирования.** Проверки ICH M7 (мутагенность по двум методологиям, purge factor) существуют только как отдельные платные инструменты, которым нужен уже готовый маршрут [123]–[127]. CASP-системы их не включают.
8. **Сопоставимость коммерческих систем.** Воспроизводимого независимого сравнения SYNTHIA / CAS / Reaxys / Spaya / ChemAIRS не существует: лицензии запрещают публикацию результатов, и у ChemAIRS, например, все числа вендорские, вплоть до «бенчмарка 9 инструментов» без названий конкурентов и без публикации [32].
9. **Устойчивость бесплатного облачного доступа.** Самый цитируемый бесплатный облачный CASP отключается 28.10.2026 [25], PostEra больше не продвигает Manifold [36], Molecule.one ушла в автономную лабораторию [40], v2 RetroBioCat стала некоммерческой [60]. Публичный слой ниши сжимается.

## 8. Пробел, который закрывает наш проект

**Формулировка.** Сегодня существуют (а) движки, которые генерируют много формально замкнутых маршрутов, но без источников, условий, масштаба и статуса проверки; (б) закрытые базы, где у стадий есть ссылки на литературу, но результат нельзя выгрузить и проверить программно; (в) отдельные процессные и регуляторные инструменты, которым нужен уже готовый маршрут на входе; (г) LLM-агенты, которые красиво разговаривают и систематически ошибаются, причём их собственный LLM-судья этого не замечает. **Связующего слоя — маршрута как проверяемого объекта с происхождением каждого факта — нет ни у кого.**

**Из каких подтверждённых фактов это следует:**

| Элемент пробела | Доказательство |
|---|---|
| Статуса проверки на уровне факта нет ни в одном CASP | Матрица в разделе 6; единственный ✓ в столбце «Пров.» — Mirabilis, который сам маршрут не генерирует [123] |
| Условия, сырьё, оборудование и очистка — признанный барьер | Прямое признание авторов Syntheseus [57] и ASKCOS [53] |
| Solve rate и top-k не доказывают пригодность | PaRoutes: top-1 восстановления 12–24% при 97% решённых [69]; критика Syntheseus [57] |
| LLM без проверок непригодна, с проверками — конкурентна | 0,006 против 0,536 top-1 [88]; solve rate 42–60 против 83 [90]; с шаблонной сверкой и бюджетом — 86,3 против 86,8 [81] |
| LLM-судья нельзя использовать как метрику | «cannot distinguish between clearly wrong GPT-4 completions» [72]; смещения моделей [94] |
| Доля выдуманных ссылок в химии не измерена | Общие данные по дисциплинам есть (18–55% [92]), химико-специфичных нет — «не подтверждено» |
| Зелёные и регуляторные проверки существуют, но не встроены | Инструменты ACS GCI бесплатны и считаются по маршруту [116]–[121]; ICH M7 только отдельными продуктами [123]–[127] |
| Сопоставимость закрыта лицензиями | Отсутствие независимых бенчмарков коммерческих систем (раздел 7, п. 8) |

**Что именно делаем мы и чего нет у других (по пунктам ТЗ и инвариантам):**

1. **Маршрут как контракт с происхождением.** RouteSpec (ADR-0003) хранит вместе структуру, условия, масштаб, источник и статус проверки каждого факта. Ни один из форматов конкурентов (вывод AiZynthFinder, ASKCOS, ORD) этого не делает: ORD описывает отдельные реакции, а не маршрут с масштабом и статусами.
2. **Проверка до показа (TRUST-001).** Детерминированные проверки с кодами диагностик и цикл «проверка → ремонт» (ADR-0002). Ближайший аналог — MetaScorer в RetroTrim [31] (три скорера, но все обученные и внутри вендора) и фильтры DeepRetro [82], про которые авторы сами пишут, что те «still misses many edge cases». Наша версия — открытая, с версионированными проверками и воспроизводимым прогоном.
3. **Проверка цитат как измеримая метрика.** Никто из проверенных не проверяет существование DOI и наличие цитаты в тексте источника. Это закрывает RQ3 и даёт число, которого в литературе нет (раздел 5.5).
4. **Процессный и масштабный вид + зелёные метрики по маршруту.** Считаем PMI/cEF и аналоги iGAL прямо из RouteSpec [116]–[121]; симуляторы остаются потребителями нашего экспорта (точка интеграции — MCP-сервер DWSIM и Fluent API [105]).
5. **Регуляторные флаги как справка с источником (SAFE-003, SAFE-005).** Ссылки на ICH Q3A/Q3C/Q3D/M7 и отметки о необходимости внешней оценки там, где покупные (Q)SAR-инструменты обязательны [123]–[127]. Не заменяем их, а делаем явным требование.
6. **Диалоговая правка с версиями и семантическим diff.** Столбец «Diff» в матрице пуст у всех; у агентных систем есть чат, но нет маршрута как версионируемого объекта.
7. **Открытость и воспроизводимость как стратегия.** Коммерческие числа невоспроизводимы по лицензии, а бесплатный облачный слой сжимается [25], [36], [40], [60]. Открытый формат + линтер + бенчмарк занимают освобождающееся место и дают площадку для статьи.

**Чего мы сознательно не делаем:** не конкурируем за SOTA в одностадийном ретросинтезе (там 60–63% top-1 у моделей с миллиардами параметров [95]–[98]) и не строим автономную лабораторию (Chemify, Molecule.one, Iktos Robotics). Наш вклад — слой проверяемости поверх существующих движков, что согласуется с north-star (`route-lint`, RouteSpec, SynthBench).

## 9. Открытые вопросы

### Для самостоятельного поиска
1. Извлечь точные значения по градациям Safe bet / Worthwhile / Rather not / Nonsense из рисунка 3 RetroTrim [31] или дождаться публикации их набора из 500 реакций и 32 целей — это лучший готовый протокол для нашей экспертной оценки.
2. Проверить лицензионные условия на модели и данные ASKCOS v2 по каждому компоненту (у v1 данные были CC BY-NC-SA) [53] — от этого зависит, можем ли мы использовать их как baseline в публикуемом бенчмарке.
3. Проверить работоспособность и лицензию `rxn-sandbox` после 28.10.2026 [26]: это наш кандидат на роль прямой модели для round-trip проверки без облака.
4. Уточнить статус PostEra Manifold API в 2026 (поддомены не разрешались из песочницы) [36] и доступность Spaya trial [22].
5. Найти или измерить самим долю выдуманных DOI и несуществующих цитат именно в химических ответах LLM — в литературе этого нет (раздел 5.5).
6. Проверить, есть ли у ACS GCI PMI Predictor машинный интерфейс; если нет, формулы придётся реализовать по статье [117] с указанием источника.
7. Не проверено из-за исчерпания бюджета поиска: Lilly TuneLab, ReactWise, Optibrium как планировщик, AIDDISON отдельно, ChemPlanner, Bretherick's, число редизайнов маршрута на программу, стоимость route scouting в CDMO.
8. Уточнить период подписки SYNTHIA Lab (цена 1 049 EUR указана без периода) [2].

### Для эксперта (перенести в `docs/expert/questions.md`, DOC-005)
1. **Q-004 · Какая шкала оценки маршрута ближе к практике: 4 градации RetroTrim (Safe bet / Worthwhile / Rather not / Nonsense) или оценка по стадиям?** Контекст: нужен воспроизводимый протокол слепой оценки (RQ4, `docs/paper/protocol.md`). Наша гипотеза: градация по худшей стадии маршрута, как в [31], плюс отдельная отметка «нет маршрута».
2. **Q-005 · Какие проверки обязательны до показа маршрута технологу, а какие можно оставить предупреждением?** Контекст: от этого зависит набор кодов диагностик `route-lint` и строгость гейта (TRUST-002). Гипотеза: баланс реакции, существование и покупаемость сырья, соответствие стадии прецеденту — блокирующие; оценки «зелёности» — предупреждения.
3. **Q-006 · Доверяют ли на практике метрике PMI Predictor для ещё не сделанного маршрута, и какие ещё метрики смотрят до лаборатории?** Контекст: [117] и iGAL 2.0 [120] — единственные отраслевые формулы, применимые до эксперимента.
4. **Q-007 · Нужна ли в отчёте привязка к опциям контроля ICH M7 (как в Mirabilis) или достаточно флага «нужна оценка мутагенных примесей»?** Контекст: SAFE-005 запрещает юридические выводы, но технологу нужен понятный сигнал [123].
5. **Q-008 · Как технолог относится к маршруту без литературных ссылок, но прошедшему расчётные проверки?** Контекст: соотношение статусов `literature` и `computed` в UI. Гипотеза: такие маршруты годны как идея, но не как план работы.
6. **Q-009 · Какие артефакты экспорта реально используются дальше: PDF для совещания, схема для презентации или машинный формат для симулятора?** Контекст: приоритет между HTML/PDF и экспортом стехиометрии для DWSIM/Dynochem [105], [111].

## 10. Выводы для архитектуры (отдельно от фактов)

- Строки `B1` (шаблонный ретросинтез) и `B0`/`B2` (LLM без обвязки, LLM+RAG) из `docs/paper/protocol.md` имеют конкретные опорные реализации: AiZynthFinder [48] для `B1`, а для `B0`/`B2` — числа независимых бенчмарков [88], [90] как ожидаемый порядок величины.
- Для метрики strategy diversity лучше взять `route-distances` [69] и не повторять кластеризационную метрику PaRoutes, которую независимые авторы назвали немонотонной [57].
- Оценку качества нельзя строить на LLM-судье (раздел 7, п. 4). Основная метрика — детерминированные проверки, человеческая оценка вслепую вторична, LLM-судья допустим только как дополнительный сигнал с указанием модели и измеренным смещением [94].
- Прямая модель для round-trip проверки нужна локальная и воспроизводимая: `rxn-sandbox` [26] или Chemformer как плагин [48], но не облачный API, который отключается [25].
- Экспорт стоит проектировать в двух режимах: человекочитаемый отчёт (HTML/PDF с дисклеймером, SAFE-004) и машинный RouteSpec для внешних потребителей (симуляторы, ELN, MCP-клиенты).
