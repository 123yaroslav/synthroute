# Блок 1. Промышленная проблема выбора маршрута синтеза АФИ: процесс, трудности, роль ИИ и метрики успеха

- **Дата:** 2026-10-13
- **Статус:** черновик v1. Нужна вычитка экспертом (PhD, химическая технология).
- **Вопрос:** какую реальную промышленную задачу решает synthroute? Почему она трудна сейчас, что ИИ может дать реалистично и какими метриками мы докажем, что решение работает?
- **Связанные документы:** [ADR-0002](../adr/0002-verifier-gated-generation.md), [протокол](../paper/protocol.md) (RQ1–RQ4), [вопросы эксперту](../expert/questions.md) (Q-001…Q-003).
- **Метод.** Документы ICH, FDA, ЕЭК, рецензируемые статьи, отчёты ACS GCI и отраслевые/рыночные источники. Каждое число сверено с открытым текстом источника. В колонке «Тип» указано, что именно было доступно: полный текст, только аннотация или вторичный источник. DOI проверены через Crossref.
- **Условные обозначения:**
  - [n] — номер источника из таблицы.
  - «оценка» — наш расчёт или вывод.
  - «не подтверждено» — найти первоисточник не удалось.
  - Рыночные оценки консалтинговых агентств различаются в разы, поэтому по возможности приводятся две оценки, чтобы был виден разброс.
- **Рамки (SAFE-\*).** Документ остаётся на уровне экономики процесса, регуляторики и ПО. Методик, условий реакций и маршрутов конкретных веществ здесь нет. Контролируемые вещества не рассматриваются; упоминается только, что регуляторные перечни существуют.

## Источники

Дата доступа для всех источников: 2026-10-13.

| # | Источник | Тип | Дата доступа |
|---|---|---|---|
| 1 | ICH Q11 *Development and Manufacture of Drug Substances*, Step 4, 2012. https://database.ich.org/sites/default/files/Q11%20Guideline.pdf | руководство (полный текст) | 2026-10-13 |
| 2 | ICH Q11 *Questions & Answers: Selection and Justification of Starting Materials*, 2017. https://database.ich.org/sites/default/files/Q11_Q%26As_Q%26As.pdf | руководство (полный текст) | 2026-10-13 |
| 3 | ICH Q7 *GMP Guide for APIs*, 2000. https://database.ich.org/sites/default/files/Q7%20Guideline.pdf | руководство (полный текст) | 2026-10-13 |
| 4 | ICH Q3A(R2) *Impurities in New Drug Substances*, 2006. https://database.ich.org/sites/default/files/Q3A%28R2%29%20Guideline.pdf | руководство (полный текст) | 2026-10-13 |
| 5 | FDA *ANDAs: Impurities in Drug Substances*, Rev. 1, 2009. https://www.fda.gov/media/183885/download | руководство (полный текст) | 2026-10-13 |
| 6 | ICH Q3C(R9) *Residual Solvents*, 2024 (текст ICH на сайте PMDA). https://www.pmda.go.jp/files/000268163.pdf | руководство (полный текст) | 2026-10-13 |
| 7 | ICH Q3D(R2) *Elemental Impurities*, 2022 (PMDA). https://www.pmda.go.jp/files/000246300.pdf | руководство (полный текст) | 2026-10-13 |
| 8 | ICH M7(R2) *Mutagenic Impurities*, 2023. https://database.ich.org/sites/default/files/ICH_M7%28R2%29_Guideline_Step4_2023_0216_0.pdf | руководство (полный текст) | 2026-10-13 |
| 9 | FDA *Control of Nitrosamine Impurities in Human Drugs*, Rev. 2, 2024. https://www.fda.gov/media/141720/download | руководство (полный текст) | 2026-10-13 |
| 10 | FDA *Recommended Acceptable Intake Limits for NDSRIs*, 2023. https://www.fda.gov/media/170794/download | руководство (полный текст) | 2026-10-13 |
| 11 | ICH Q12 *Lifecycle Management*, 2019. https://database.ich.org/sites/default/files/Q12_Guideline_Step4_2019_1119.pdf | руководство (полный текст) | 2026-10-13 |
| 12 | ICH Q10 *Pharmaceutical Quality System*, 2008. https://database.ich.org/sites/default/files/Q10%20Guideline.pdf | руководство (полный текст) | 2026-10-13 |
| 13 | FDA *Process Validation: General Principles and Practices*, 2011. https://www.fda.gov/media/71021/download | руководство (полный текст) | 2026-10-13 |
| 14 | ICH Q6A *Specifications*, 1999. https://database.ich.org/sites/default/files/Q6A%20Guideline.pdf | руководство (полный текст) | 2026-10-13 |
| 15 | FDA *ANDAs: Pharmaceutical Solid Polymorphism*, 2007. https://www.fda.gov/media/71375/download | руководство (полный текст) | 2026-10-13 |
| 16 | 21 CFR 314.53 (патенты в Orange Book). https://www.law.cornell.edu/cfr/text/21/314.53 | нормативный акт | 2026-10-13 |
| 17 | 35 U.S.C. 271 (нарушение патента). https://www.law.cornell.edu/uscode/text/35/271 | нормативный акт | 2026-10-13 |
| 18 | Решение Совета ЕЭК № 77 от 03.11.2016 «Правила надлежащей производственной практики ЕАЭС». https://docs.eaeunion.org/docs/ru-ru/01411922/cncd_21112016_77 ; полный текст: https://docs.eaeunion.org/upload/iblock/bd9/ga9qmu732f3sef7duto3zomhjfpxr0w1/cncd_21112016_77_doc.pdf | нормативный акт (полный текст) | 2026-10-13 |
| 19 | ACS GCI Pharmaceutical Roundtable, *Recap of the SELECT criteria*. https://learning.acsgcipr.org/process-design/route-selection/recap-of-the-select-criteria/ | отраслевое учебное руководство | 2026-10-13 |
| 20 | Butters M. et al. *Critical Assessment of Pharmaceutical Processes — A Rationale for Changing the Synthetic Route*. Chem. Rev. 2006. DOI 10.1021/cr050982w. https://api.crossref.org/works/10.1021/cr050982w | обзор (только метаданные; критерии SELECT взяты по [19]) | 2026-10-13 |
| 21 | Federsel H.-J. *Chemical Process Research and Development in the 21st Century…* Acc. Chem. Res. 2009. DOI 10.1021/ar800257v. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=19338294&rettype=abstract&retmode=text | обзор (аннотация) | 2026-10-13 |
| 22 | Krueger J. et al. *Chemical Process Development in the Pharmaceutical Industry in Europe — Insights and Perspectives from Industry Scientists*. Angew. Chem. Int. Ed. 2025. DOI 10.1002/anie.202420719. https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12051753/fullTextXML | обзор отрасли (полный текст) | 2026-10-13 |
| 23 | Carey J.S. et al. *Analysis of the reactions used for the preparation of drug candidate molecules*. Org. Biomol. Chem. 2006. DOI 10.1039/b602413k. https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1039/B602413K&format=json&resultType=core | статья (аннотация; полный текст RSC недоступен) | 2026-10-13 |
| 24 | Desai A. Слайды group meeting по данным [23], MSU, 2008. https://www2.chemistry.msu.edu/faculty/wulff/myweb26/Literature_pdf/2008-07-11%20Aman.pdf | вторичный источник | 2026-10-13 |
| 25 | Zhong Z. et al. *Recent advances in artificial intelligence for retrosynthesis*. arXiv:2301.05864, 2023. https://arxiv.org/pdf/2301.05864 | обзор, препринт (вторичное подтверждение [23]) | 2026-10-13 |
| 26 | Brown D.G., Boström J. *Analysis of Past and Present Synthetic Methodologies on Medicinal Chemistry: Where Have All the New Reactions Gone?* J. Med. Chem. 2016. DOI 10.1021/acs.jmedchem.5b01409. https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%22where%20have%20all%20the%20new%20reactions%20gone%22&format=json&resultType=core | статья (аннотация) | 2026-10-13 |
| 27 | Mudie, Littich, Kaushal (Lonza). *Accelerating early-stage small molecule drug development*. Manufacturing Chemist, 2023. https://manufacturingchemist.com/accelerating-early-stage-small-molecule-drug-development | отраслевая статья (позиция поставщика) | 2026-10-13 |
| 28 | Roschangar F. et al. *Improved iGAL 2.0 Metric…* ACS Sustainable Chem. Eng. 2022 (online 2021). DOI 10.1021/acssuschemeng.1c01940. https://repository.tudelft.nl/record/uuid:9a31df1d-0195-4b25-acd0-c5683808f611 | статья (полный текст) | 2026-10-13 |
| 29 | Sheldon R.A. *Metrics of Green Chemistry and Sustainability: Past, Present, and Future*. ACS Sustainable Chem. Eng. 2018 (online 2017). DOI 10.1021/acssuschemeng.7b03505. https://repository.tudelft.nl/file/File_460388b5-c298-499a-9c3c-fc15449f9935 | обзор (авторская версия) | 2026-10-13 |
| 30 | Constable D.J.C. et al. *Perspective on Solvent Use in the Pharmaceutical Industry*. OPRD 2007. DOI 10.1021/op060170h. https://api.openalex.org/works/doi:10.1021/op060170h | статья (аннотация) | 2026-10-13 |
| 31 | Jimenez-Gonzalez C. et al. *Using the Right Green Yardstick: Why PMI Is Used in the Pharmaceutical Industry…* OPRD 2011. DOI 10.1021/op200097d. https://acsgcipr.org/using-the-right-green-yardstick-why-process-mass-intensity-is-used-in-the-pharmaceutical-industry-to-drive-more-sustainable-processes/ | статья (аннотация) | 2026-10-13 |
| 32 | Kekessie I. et al. *Process Mass Intensity (PMI): A Holistic Analysis of Current Peptide Manufacturing Processes*. J. Org. Chem. 2024. DOI 10.1021/acs.joc.3c01494. https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11002941/fullTextXML | статья (полный текст) | 2026-10-13 |
| 33 | Klucznik T. et al. *Efficient Syntheses of Diverse, Medicinally Relevant Targets Planned by Computer and Executed in the Laboratory*. Chem 2018. DOI 10.1016/j.chempr.2018.02.002. https://www.mrksichgroup.northwestern.edu/files/2020/05/Klucznik-Efficient-Syntheses-of-Diverse-2018.pdf | статья (полный текст) | 2026-10-13 |
| 34 | Socal M.P. et al. *Potential impact of tariffs on APIs on the price of US-made generic drugs*. Health Affairs Scholar 2025. DOI 10.1093/haschl/qxaf247. https://tinglongdai.com/wp-content/uploads/qxaf247.pdf | статья (полный текст) | 2026-10-13 |
| 35 | Lurie P. et al. *Comparison of content of FDA letters not approving applications…* BMJ 2015. DOI 10.1136/bmj.h2758. https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4462714/fullTextXML | статья (полный текст) | 2026-10-13 |
| 36 | Pharma Manufacturing. *FDA's CRLs reveal 74% of applications rejected for quality/manufacturing issues*, 2025. https://www.pharmamanufacturing.com/all-articles/article/55302937/fdas-crls-reveal-74-of-applications-rejected-for-quality-manufacturing-issues | отраслевая пресса | 2026-10-13 |
| 37 | Feldman S. (IDC). *The high cost of not finding information*. KMWorld, 2004. https://www.kmworld.com/Articles/Editorial/Features/The-high-cost-of-not-finding-information-9534.aspx | аналитика (не химия) | 2026-10-13 |
| 38 | Mulligan A. *Avoiding extra sifts and longer shifts* (опрос Elsevier/Sense about Science), Research Information, 2019. https://www.researchinformation.info/analysis-opinion/avoiding-extra-sifts-and-longer-shifts/ | опрос исследователей | 2026-10-13 |
| 39 | IQVIA Institute. *The Global Use of Medicines Outlook to 2030*, 2026. https://www.iqvia.com/insights/the-iqvia-institute/reports-and-publications/reports/the-global-use-of-medicines-outlook-through-2029 | отраслевой отчёт | 2026-10-13 |
| 40 | IQVIA blog. *IQVIA Institute's 2026 forecast…*, 2026-03-20. https://www.iqvia.com/blogs/2026/03/iqvia-institutes-2026-forecast-global-medicine-use-stays-strong-despite-headwinds | отраслевой отчёт | 2026-10-13 |
| 41 | AAM. *Generic and Biosimilar Medicines Save $467 Billion in 2024*, 2025. https://accessiblemeds.org/resources/press-releases/generic-and-biosimilar-medicines-save-467-billion-in-2024/ | отраслевая ассоциация | 2026-10-13 |
| 42 | Evaluate. *2026 World Preview* (пресс-релиз), 2026-06-23. https://www.evaluate.com/press-release/evaluate-2026-world-preview-report-pharmaceutical-market/ | рыночная аналитика | 2026-10-13 |
| 43 | PharmaVoice. *Pharma's $500B patent problem will come in waves*, 2026-10-08. https://www.pharmavoice.com/news/pharma-patent-cliff-merck-abbvie-dealmaking/832438/ | отраслевая пресса | 2026-10-13 |
| 44 | BCC Research. Пресс-релиз о рынке дженериков, 2024. https://www.bccresearch.com/pressroom/phm/bcc-research-analysis-forecasts-booming-generic-drug-market | рыночная оценка | 2026-10-13 |
| 45 | Market Glass (GII). *Generic Drugs*, 2025. https://www.giikorea.co.kr/report/go1885986-generic-drugs.html | рыночная оценка | 2026-10-13 |
| 46 | Grand View Research (GII). *Small Molecule CDMO Market*, 2025. https://www.giikorea.co.kr/report/grvi1813801-small-molecule-cdmo-market-size-share-trends.html | рыночная оценка | 2026-10-13 |
| 47 | Outsourced Pharma. *Small Molecule CDMOs: Recent Consolidation And Expansion*, 2025. https://www.outsourcedpharma.com/doc/small-molecule-cdmos-recent-consolidation-and-expansion-developments-0001 | отраслевая пресса | 2026-10-13 |
| 48 | Baker McKenzie. *The BIOSECURE Act becomes law*, 2026-01-19. https://www.bakermckenzie.com/en/insight/publications/2026/01/united-states-the-biosecure-act-becomes-law | юридический обзор | 2026-10-13 |
| 49 | DLA Piper. *US–China life sciences policy developments*, 2026-08. https://www.dlapiper.com/en-us/insights/publications/2026/08/us-china-life-sciences-policy-developments-top-points-for-companies | юридический обзор | 2026-10-13 |
| 50 | Mayer Brown. Section 232 tariffs on patented pharmaceuticals and ingredients, 2026-04-06. https://www.mayerbrown.com/en/insights/publications/2026/04/trump-administration-implements-tariffs-on-imported-patented-medication-and-pharmaceutical-ingredients-under-section-232-of-the-trade-expansion-act-of-1962 | юридический обзор | 2026-10-13 |
| 51 | McCann FitzGerald. *EU Critical Medicines Act: political agreement reached*, 2026-05-15. https://www.mccannfitzgerald.com/knowledge/pharma-and-life-sciences/eu-critical-medicines-act-political-agreement-reached-what-life-sciences-companies-need-to-know | юридический обзор | 2026-10-13 |
| 52 | FDA, J. Woodcock. *Safeguarding Pharmaceutical Supply Chains in a Global Economy* (показания в Конгрессе), 2019-10-30. https://www.fda.gov/news-events/congressional-testimony/safeguarding-pharmaceutical-supply-chains-global-economy-10302019 | регулятор | 2026-10-13 |
| 53 | FDA. *Drug Shortages: Root Causes and Potential Solutions*, 2019 (обн. 2020). https://www.fda.gov/media/131130/download | регулятор (полный текст) | 2026-10-13 |
| 54 | RAPS. *USP: India and China continue their API manufacturing…*, 2024-11-08. https://www.raps.org/resource/usp-india-and-china-continue-their-api-manufacturi.html | отраслевая пресса (данные USP) | 2026-10-13 |
| 55 | USP, R. Piervincenzi. Показания в комитете Палаты представителей по энергетике и торговле, 2025-06-11. https://democrats-energycommerce.house.gov/sites/evo-subsites/democrats-energycommerce.house.gov/files/evo-media-document/ronald-t-piervincenzi-phd_witness-testimony_06.11.2025.pdf | фармакопейная организация (полный текст) | 2026-10-13 |
| 56 | *Manifesto on the Critical Medicines Act* (10 государств ЕС), 2025. https://www.entreprises.gouv.fr/files/files/presse/2025/2025-0059%20Manifesto%20on%20Critical%20Medicines%20Act%20CMA.pdf | правительственный документ | 2026-10-13 |
| 57 | Department of Pharmaceuticals (India). Gazette notification, PLI bulk drugs, 2020. https://pharma-dept.gov.in/sites/default/files/Gazettee%20notification%20of%20bulk%20drug%20schemes_0.pdf | нормативный акт | 2026-10-13 |
| 58 | BioSpectrum India. *Can India Reclaim API Throne from China?*, 2024-09-01. https://www.biospectrumindia.com/article/pdf/25074 | отраслевая пресса | 2026-10-13 |
| 59 | Стратегия развития фармацевтической промышленности РФ до 2030 г. («Фарма-2030»), распоряжение Правительства РФ № 1495-р от 07.06.2023 (копия текста). https://pharmprom.news/wp-content/uploads/pharma-2030.pdf | нормативный акт (неофициальная копия) | 2026-10-13 |
| 60 | Фармвестник. «Правительство утвердило программу „Фарма-2030“», 2023-06-19. https://pharmvestnik.ru/content/news/Pravitelstvo-utverdilo-programmu-Farma-2030-2.html | отраслевая пресса | 2026-10-13 |
| 61 | Фармвестник. «Минпромторг отметил снижение импорта фармсубстанций» (ФБУ «ГИЛС и НП»), 2024-11-21. https://pharmvestnik.ru/content/news/Minpromtorg-otmetil-snijenie-importa-farmsubstancii.html | отраслевая пресса (данные ГИЛС) | 2026-10-13 |
| 62 | GxP News. «Вопросы по веществу: почему в 2023 году сократился импорт фармсубстанций», 2024-04-08. https://gxpnews.net/2024/04/voprosy-po-veshhestvu-pochemu-v-2023-godu-sokratilsya-import-farmsubstanczij/ | отраслевая пресса | 2026-10-13 |
| 63 | Коммерсантъ (данные RNC Pharma, DSM Group), 2023-07-12. https://www.kommersant.ru/doc/6097228 | деловая пресса | 2026-10-13 |
| 64 | Фармвестник. «Антон Алиханов рассказал о планах выпускать 60% лекарств из российских фармсубстанций», 2024-10-08. https://pharmvestnik.ru/content/news/Anton-Alihanov-rasskazal-o-planah-vypuskat-60-lekarstv-iz-rossiiskih-farmsubstancii.html | отраслевая пресса | 2026-10-13 |
| 65 | GxP News. «Минпромторг: доля отечественных лекарств в России превысила 60%», 2026-01-22. https://gxpnews.net/2026/01/minpromtorg-dolya-otechestvennyh-lekarstv-v-rossii-prevysila-60/ | отраслевая пресса | 2026-10-13 |
| 66 | Ведомости. «Голикова: около 46%…», 2024-07-02. https://www.vedomosti.ru/society/news/2024/07/02/1047568-golikova-okolo-46 | деловая пресса | 2026-10-13 |
| 67 | ppt.ru. «Закупка стратегически значимых лекарств: что меняется в 2026 году», 2026-09-04. https://ppt.ru/amp/art/zakupki/zakupka-strategicheski-znachimykh-lekarstv | юридический обзор | 2026-10-13 |
| 68 | GxP News. «Сырьевой вопрос: как избавиться от импортозависимости в сфере производства субстанций», 2024-12-11. https://gxpnews.net/2024/12/syrevoj-vopros-kak-izbavitsya-ot-importozavisimosti-v-sfere-proizvodstva-substanczij/ | отраслевая пресса | 2026-10-13 |
| 69 | GxP News. «ХимРар запустил в Подмосковье комплекс по производству фармсубстанций», 2026-05-28. https://gxpnews.net/2026/05/himrar-zapustil-v-podmoskove-kompleks-po-proizvodstvu-farmsubstanczij/ | отраслевая пресса | 2026-10-13 |
| 70 | AJMC. *Active US drug shortages rise for third straight quarter* (данные ASHP), 2026-07-20. https://www.ajmc.com/view/active-us-drug-shortages-rise-for-third-straight-quarter | отраслевая пресса | 2026-10-13 |
| 71 | EUobserver о спецдокладе Европейской счётной палаты 19/2025, 2025-09-18. https://euobserver.com/1771/medicines-shortages-in-eu-this-winter-warns-auditors-report/ | пресса (данные ECA) | 2026-10-13 |
| 72 | McCann FitzGerald. *Is the polluter paying? European challenges to the revised UWWTD*, 2026-05-27. https://www.mccannfitzgerald.com/knowledge/disputes/is-the-polluter-paying-european-challenges-to-the-revised-urban-waste-water-treatment-directive | юридический обзор | 2026-10-13 |
| 73 | FDA. *FDA Proposes Framework to Advance Credibility of AI Models…*, 2025-01-06. https://www.fda.gov/news-events/press-announcements/fda-proposes-framework-advance-credibility-ai-models-used-drug-and-biological-product-submissions | регулятор | 2026-10-13 |
| 74 | Segler M.H.S., Preuss M., Waller M.P. *Planning chemical syntheses with deep neural networks and symbolic AI*. Nature 2018. DOI 10.1038/nature25978. https://arxiv.org/pdf/1708.04202 | статья (полный текст препринта) | 2026-10-13 |
| 75 | Mikulak-Klucznik B. et al. *Computational planning of the synthesis of complex natural products*. Nature 2020. DOI 10.1038/s41586-020-2855-y. https://www.nature.com/articles/s41586-020-2855-y | статья (аннотация) | 2026-10-13 |
| 76 | Coley C.W. et al. *A robotic platform for flow synthesis of organic compounds informed by AI planning*. Science 2019. DOI 10.1126/science.aax1566. https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:%2210.1126/science.aax1566%22&resultType=core&format=json | статья (аннотация) | 2026-10-13 |
| 77 | Tu Z. et al. *ASKCOS: an open source software suite for synthesis planning*. arXiv:2501.01835, 2025. https://arxiv.org/abs/2501.01835 | препринт (аннотация) | 2026-10-13 |
| 78 | Genheden S. et al. *AiZynthFinder…* J. Cheminform. 2020. DOI 10.1186/s13321-020-00472-1. https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:%2210.1186/s13321-020-00472-1%22&resultType=core&format=json | статья (аннотация) | 2026-10-13 |
| 79 | Saigiridharan L. et al. *AiZynthFinder 4.0: developments based on learnings from 3 years of industrial application*. J. Cheminform. 2024. DOI 10.1186/s13321-024-00860-x. https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11112899/fullTextXML | статья (полный текст) | 2026-10-13 |
| 80 | Struble T.J. et al. *Current and Future Roles of AI in Medicinal Chemistry Synthesis*. J. Med. Chem. 2020. DOI 10.1021/acs.jmedchem.9b02120. https://www.ebi.ac.uk/europepmc/webservices/rest/PMC7457232/fullTextXML | обзор (полный текст) | 2026-10-13 |
| 81 | Drug Development & Delivery. Lonza AI-enabled Route Scouting Service (~2024). https://www.drug-dev.com/?p=141670 | позиция поставщика | 2026-10-13 |
| 82 | Maziarz K. et al. *Re-evaluating retrosynthesis algorithms with Syntheseus*. Faraday Discuss. 2025. DOI 10.1039/D4FD00093E. https://arxiv.org/html/2310.19796v3 | статья (полный текст препринта) | 2026-10-13 |
| 83 | Genheden S., Bjerrum E. *PaRoutes: towards a framework for benchmarking retrosynthesis route predictions*. Digital Discovery 2022. DOI 10.1039/D2DD00015F. https://github.com/MolecularAI/PaRoutes | бенчмарк (README с результатами) | 2026-10-13 |
| 84 | Walters W.H., Wilder E.I. *Fabrication and errors in the bibliographic citations generated by ChatGPT*. Sci. Rep. 2023. DOI 10.1038/s41598-023-41032-5. https://pmc.ncbi.nlm.nih.gov/articles/PMC10484980/ | статья (полный текст) | 2026-10-13 |
| 85 | Chelli M. et al. *Hallucination Rates and Reference Accuracy of ChatGPT and Bard for Systematic Reviews*. JMIR 2024. DOI 10.2196/53164. https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.2196/53164&resultType=core&format=json | статья (аннотация) | 2026-10-13 |
| 86 | Linardon J. et al. *Influence of Topic Familiarity and Prompt Specificity on Citation Fabrication…* JMIR Ment. Health 2025. DOI 10.2196/80371. https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:%2210.2196/80371%22&resultType=core&format=json | статья (аннотация) | 2026-10-13 |
| 87 | Agrawal A. et al. *Do Language Models Know When They're Hallucinating References?* arXiv:2305.18248, 2023/2024. https://arxiv.org/pdf/2305.18248v3 | препринт (полный текст) | 2026-10-13 |
| 88 | Asai A. et al. *OpenScholar*. arXiv:2411.14199, 2024; новость UW о публикации в Nature, 2026. https://arxiv.org/abs/2411.14199 ; https://www.washington.edu/news/2026/02/04/in-a-study-ai-model-openscholar-synthesizes-scientific-research-and-cites-sources-as-accurately-as-human-experts/ | препринт и новость (аннотация) | 2026-10-13 |
| 89 | Guo T. et al. *What can Large Language Models do in chemistry? A comprehensive benchmark on eight tasks*. NeurIPS D&B 2023. https://arxiv.org/html/2305.18365v3 | статья (полный текст) | 2026-10-13 |
| 90 | Mirza A. et al. *A framework for evaluating the chemical knowledge and reasoning abilities of LLMs against the expertise of chemists* (ChemBench). Nat. Chem. 2025. DOI 10.1038/s41557-025-01815-x. https://www.nature.com/articles/s41557-025-01815-x | статья (частично) | 2026-10-13 |
| 91 | Liu G. et al. *Multimodal LLMs for inverse molecular design with retrosynthetic planning* (Llamole). arXiv:2410.04223, 2024. https://arxiv.org/html/2410.04223 | препринт (полный текст) | 2026-10-13 |
| 92 | Bran A.M. et al. *Augmenting large language models with chemistry tools* (ChemCrow). Nat. Mach. Intell. 2024. DOI 10.1038/s42256-024-00832-8. https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11116106/fullTextXML | статья (полный текст) | 2026-10-13 |
| 93 | Boiko D.A. et al. *Autonomous chemical research with large language models* (Coscientist). Nature 2023. DOI 10.1038/s41586-023-06792-0. https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10733136/fullTextXML | статья (полный текст) | 2026-10-13 |
| 94 | Schwaller P. et al. *Extraction of organic chemistry grammar from unsupervised learning of chemical reactions* (RXNMapper). Sci. Adv. 2021. DOI 10.1126/sciadv.abe4166. https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8026122/fullTextXML | статья (полный текст) | 2026-10-13 |
| 95 | Phan T.-L. et al. *Reaction rebalancing: a novel approach to curating reaction databases* (SynRBL). J. Cheminform. 2024. DOI 10.1186/s13321-024-00875-4. https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11264917/fullTextXML | статья (полный текст) | 2026-10-13 |
| 96 | Genheden S., Engkvist O., Bjerrum E. *Clustering of Synthetic Routes Using Tree Edit Distance*. JCIM 2021. DOI 10.1021/acs.jcim.1c00232. https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1021/acs.jcim.1c00232&resultType=core&format=json | статья (аннотация) | 2026-10-13 |
| 97 | Schwaller P. et al. *Predicting retrosynthetic pathways using transformer-based models and a hyper-graph exploration strategy*. Chem. Sci. 2020. DOI 10.1039/c9sc05704h. https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8152799/fullTextXML | статья (полный текст) | 2026-10-13 |
| 98 | Gao T. et al. *Enabling Large Language Models to Generate Text with Citations* (ALCE). EMNLP 2023. https://arxiv.org/pdf/2305.14627 | статья (полный текст) | 2026-10-13 |
| 99 | Kapoor S. et al. *AI Agents That Matter*. arXiv:2407.01502, 2024. https://arxiv.org/html/2407.01502 | препринт (полный текст) | 2026-10-13 |
| 100 | Brooke J. *SUS: a "quick and dirty" usability scale*, 1996 (зеркало авторского PDF). https://code.metalisp.dev/marcuskammer/emacs.d/raw/commit/9a28c3b0351b5a630e02f042822da2e81be7b52a/ux/SUSCHAPT.pdf | глава книги (зеркало) | 2026-10-13 |
| 101 | Sauro J. *Measuring Usability with the System Usability Scale*, MeasuringU, 2011. https://measuringu.com/sus/ | методический источник | 2026-10-13 |
| 102 | Sauro J. *5 Ways to Interpret a SUS Score*, MeasuringU, 2018. https://measuringu.com/interpret-sus-score/ | методический источник | 2026-10-13 |
| 103 | Lewis J.R., Sauro J. *Sample sizes for SUS benchmark tests*, MeasuringU, 2022. https://measuringu.com/sample-sizes-for-SUS-benchmark-tests | методический источник | 2026-10-13 |
| 104 | *Krippendorff's alpha* (по Krippendorff 2004). https://en.wikipedia.org/wiki/Krippendorff%27s_alpha | справочный, вторичный | 2026-10-13 |
| 105 | *Fleiss' kappa* (шкала Landis & Koch 1977). https://en.wikipedia.org/wiki/Fleiss%27_kappa | справочный, вторичный | 2026-10-13 |
| 106 | NextMove Software. *Pistachio*. https://www.nextmovesoftware.com/pistachio.html | описание продукта | 2026-10-13 |

---

## 1. Текущий процесс

### 1.1 Жизненный цикл маршрута синтеза субстанции

| Этап | Цель | Масштаб | Кто ведёт | Что фиксируется и что важно для нас |
|---|---|---|---|---|
| **Маршрут медхимии (discovery)** | Быстро получить вещество для SAR и доклинических работ | мг–г | медицинские химики | Маршрут годится только «для своей цели». При передаче из медхимии в process R&D объёмы растут с сотен граммов до килограммов, а требования к устойчивости, безопасности, IP и стоимости меняются [21]. Для фазы 1 часто берут discovery-маршрут, а позже маршрут и даже исходные вещества меняют [22]. |
| **Разведка и выбор маршрута (route scouting / selection)** | Найти и сравнить альтернативы, выбрать 1–2 для разработки | кабинетный анализ, затем г | процесс-химики | Сравнение по SELECT: Safety, Environmental, Legal (IP), Economics (COGS), Control (качество, профиль примесей), Throughput (сырьё, время, производительность) [19][20]. Этот этап synthroute ускоряет напрямую. |
| **Разработка и оптимизация процесса** | Устойчивый процесс, понимание CQA и параметров (QbD, при желании design space) | г–кг | процесс-химики, аналитики | ICH Q11 различает «традиционный» и «расширенный» подходы [1]. По оценке отраслевых авторов, процесс-химики тратят около 70% времени на оптимизацию выделения и очистки (в [22] без прямой ссылки на первоисточник). |
| **Масштабирование** | Килолаборатория, затем пилот | кг–сотни кг | технологи, инженеры-химики, служба безопасности процессов | Тепловые и газовые риски, оборудование, растворители, отходы. Режимы synthroute lab/pilot/plant ложатся на этот этап. |
| **Трансфер технологии** | Перенос на коммерческую площадку или в CDMO | — | технологи, QA, CDMO | Q10 и Q11 прямо включают в управление знаниями трансфер на внутренние площадки и к контрактным производителям [1][12]. |
| **Валидация и коммерческое производство (GMP)** | Process Design → Process Qualification (PPQ) → Continued Process Verification | промышленный | производство, QA/QC, RA (CMC) | Три стадии валидации по FDA [13]. Параметры процесса в идеале «замораживают» за 1–2 года до запуска [22]. Изменения маршрута после RSM подчиняются региональным правилам пострегистрационных изменений [1], в Q12 это established conditions [11]. |

**Особенности генериков.** Маршрут не изобретают с нуля: его собирают из литературы и патентов, а затем разводят с действующими процессными патентами (раздел 1.3). Q11 Q&A прямо говорит, что RSM, принятый для процесса одного производителя, может быть не принят для процесса другого [2].

### 1.2 Роли

FDA рекомендует для валидации междисциплинарную команду: процессная инженерия, промышленная фармация, аналитическая химия, микробиология, статистика, производство, QA [13]. Сопоставление ролей с критериями SELECT и документами ниже — наша сводка.

- **Медицинский химик.** Автор исходного маршрута.
- **Процесс-химик.** Разведка, выбор и оптимизация маршрута. Основной пользователь synthroute.
- **Инженер-химик / технолог.** Масштаб, оборудование, PMI, безопасность процесса.
- **Аналитик и QC.** Профиль примесей, методы контроля (Q3A/Q3C/Q3D/M7).
- **QA.** GMP с момента RSM (Q7).
- **Регуляторные вопросы (CMC).** Обоснование RSM (Q11), регистрационное досье (раздел 3.2.S.2), established conditions (Q12).
- **EHS / безопасность процессов.** Критерий S в SELECT.
- **Закупки / цепочка поставок.** Критерий T и контроль поставщиков, Q11 Q&A 5.15–5.16 [2].
- **IP / юристы.** Критерий L и FTO по процессным патентам.
- **Фармаколог и руководитель портфеля.** Решают, брать ли МНН в разработку.

### 1.3 Регуляторика, определяющая выбор маршрута

| Документ | Суть (ключевые числа) | Что это значит для дизайна маршрута | Что может делать платформа (детерминированно) |
|---|---|---|---|
| **ICH Q11 (2012) и Q11 Q&A (2017)** | Принципы выбора RSM [1]:<br>• ранние стадии меньше влияют на качество;<br>• примеси, внесённые рано, лучше удаляются;<br>• в досье описываются «несколько химических стадий»;<br>• принципы применяются в совокупности.<br>«Коммерчески доступное» вещество (товар с существующим нефармацевтическим рынком) обоснования как RSM не требует; вещество заказного синтеза требует [1].<br>Q&A [2]:<br>• одного «значимого структурного фрагмента» мало;<br>• несколько поставщиков ещё не делают вещество коммерчески доступным;<br>• стадия «влияет» на профиль примесей выше порога идентификации Q3A или выше 30% допустимого предела M7;<br>• «3 стадии» — не правило. | Выбор RSM фиксирует, где начинается «регуляторная» часть маршрута. Слишком короткая GMP-часть будет отклонена. Изменение маршрута после RSM — пострегистрационное изменение. | Помечать **кандидатов в RSM**: коммерческая доступность в стоке и число стадий после RSM. Обоснование RSM остаётся за экспертом. |
| **ICH Q7 (2000) / GMP ЕАЭС, ч. II** | GMP применяется с момента ввода исходного материала API (API starting material) и ужесточается к финальным стадиям [3]. Часть II Правил GMP ЕАЭС разработана на основе ICH Q7A и не применяется к стадиям до ввода исходных материалов [18]. | Стадии до RSM контролируются только через поставщика, поэтому стоимость и контроль GMP-части зависят от длины маршрута после RSM. | Показывать границу GMP на схеме. |
| **ICH Q3A(R2) (2006)** | Для максимальной суточной дозы ≤2 г/сут [4]:<br>• порог отчётности 0,05%;<br>• идентификации 0,10% или 1,0 мг/сут;<br>• квалификации 0,15% или 1,0 мг/сут (из двух значений берётся меньшее).<br>Документ распространяется только на новые субстанции. FDA применяет его пороги и к ANDA и DMF, включая изменения синтеза [5]. | Каждый новый маршрут даёт новый профиль примесей, который надо квалифицировать. Для генерика это цена смены маршрута. | Справка о порогах. Примеси расчётом не предсказываем. |
| **ICH Q3C(R9) (2024)** | Классы растворителей: 1 — избегать, 2 — ограничивать, 3 — низкая токсичность, PDE ≥50 мг/сут. Для класса 3 до 50 мг/сут (0,5%) обоснование не требуется [6]. В R8 добавлены PDE для 2-MeTHF, CPME и трет-бутанола [6]. | Выбор растворителя на каждой стадии. Класс 1 в маршруте — красный флаг. | **Автоматический флаг класса** растворителя на стадии. |
| **ICH Q3D(R2) (2022)** | Классы элементов: 1 (As, Cd, Hg, Pb), 2A (Co, Ni, V), 2B (в т. ч. Pd, Pt, Rh, Ru, Ir), 3. Порог контроля — 30% PDE. Пероральная PDE Pd — 100 мкг/сут. Остатки катализаторов названы прямо как источник [7]. | Металлокатализ, особенно на поздних стадиях, требует оценки риска и стратегии удаления. | **Флаг элемента и его класса**, расстояние стадии до АФИ. |
| **ICH M7(R2) (2023) и нитрозамины** | TTC 1,5 мкг/сут; классы примесей 1–5; варианты контроля 1–4, вариант 4 — обоснование фактором очистки (purge factor). Группа «cohort of concern», в т. ч. N-нитрозосоединения, исключена из TTC [8]. FDA требует проектировать маршрут так, чтобы нитрозамины не образовывались [9]. Лимиты для NDSRI — от 26,5 до 1500 нг/сут по категориям потенции [10]. | Реагенты и интермедиаты со структурными алертами, особенно на последних стадиях, — главный регуляторный риск маршрута. | **Флаги структурных алертов** (информационные, не вердикт) и стадия их появления. |
| **ICH Q12 / Q10** | Established conditions юридически обязывающие; есть протоколы заранее согласованных изменений (PACMP) [11]. Q10 описывает жизненный цикл продукта [12]. | Ошибку в выборе маршрута дорого исправлять после регистрации. | Версионирование и diff маршрута (аналогия ECs). |
| **ICH Q6A / FDA, полиморфизм** | Деревья решений для контроля полиморфов [14]. Для ANDA другой полиморф не делает субстанцию другим действующим веществом [15]. | Финальная стадия (кристаллизация) определяет форму, а патенты на формы могут блокировать вариант. | Только справка. Форму не предсказываем. |
| **Патенты (США как пример)** | Процессные патенты в Orange Book не вносятся, патенты на полиморфы при наличии данных вносятся [16]. Ввоз продукта, полученного запатентованным процессом, является нарушением [17]. | Вывод (наш): процессные патенты не оспариваются через Paragraph IV, но остаются в силе. Отсюда нужен FTO-анализ именно маршрута. | Патентный статус как справка с источником и датой (SAFE-005). |

---

## 2. Почему это трудно

### 2.1 Многокритериальная оптимизация с конфликтующими целями

Ниже факты отделены от наших выводов.

- **Число стадий и выход.** Выход перемножается по стадиям. При среднем коммерческом выходе стадии 86% [28] маршрут из 8 стадий даёт около 30% общего выхода, при 80% на стадию — около 17% (оценка: 0,86⁸ и 0,80⁸). Средний общий выход самой длинной линейной последовательности составляет 20% на ранней разработке, 35% на поздней и 44% в коммерческих процессах (97 процессов) [28].
- **Короткий маршрут против регуляторики.** Экономика тянет к короткой GMP-части. Q11 Q&A требует, чтобы после RSM оставалось достаточно стадий, и запрещает добавлять очистки только ради того, чтобы обойти более ранний RSM [2]. Это прямой конфликт.
- **Стоимость против надёжности поставок.** Самые дешёвые ключевые исходные материалы (KSM) часто поступают от одного источника. USP приводит пример АФИ, зависящего от единственного KSM из Китая [55]. Локализационные требования (РФ, ЕС, США) добавляют ограничение по происхождению сырья (раздел 4).
- **Безопасность против производительности.** Опасные реагенты и экзотермы трудно масштабировать. В SELECT это отдельный критерий S [19].
- **Примеси.** Металлы на поздних стадиях попадают под Q3D [7], алерты — под M7 [8], для нитрозаминов требуется design-out на этапе разработки маршрута [9]. Профиль примесей меняется при любой смене маршрута [1][5].
- **Твёрдая форма.** Полиморф определяется финальной стадией и может быть запатентован [14][16].
- **IP.** Для генерика нужен маршрут, не нарушающий процессных патентов, хотя патент на соединение уже истёк [16][17].
- **«Зелёность».** ACS GCI Pharmaceutical Roundtable выбрал PMI ключевой метрикой для сравнения процессов [31]. На растворители приходится 80–90% массы в типичном фарм- или тонкохимическом периодическом процессе [30]. В отходах растворители составляют 58%, вода 28%, сырьё 8% [29].
- **Время.** Параметры замораживают за 1–2 года до запуска, а стандартные сроки разработки — 10 лет и более [22]. Поэтому выбор маршрута делается рано и при неполной информации.

**Вывод (наш).** Не существует одной «лучшей» схемы. Есть Парето-множество маршрутов, а веса критериев зависят от контекста: генерик или оригинал, РФ или экспорт, лаборатория или завод. Это аргумент за выдачу **нескольких** вариантов с прозрачной таблицей сравнения, а не одного ответа.

### 2.2 Фрагментация информации

- **Источники разнородны.** Это журнальные статьи (в т. ч. OPRD), патенты (процессные патенты — основной источник промышленных маршрутов), коммерческие базы реакций (Reaxys, SciFinder; Pistachio — более 21 млн реакций из патентов США и ЕПВ [106]), открытые базы (ORD, USPTO), регуляторные документы и закрытые части DMF/ASMF.
- **Данные неполны.**
  - Менее 12% проанализированных одностадийных реакций Reaxys сбалансированы; «несбалансированные реакции — правило, а не исключение» [95].
  - RXNMapper рассчитан на картирование «сильно несбалансированных» патентных реакций. При разборе ошибок 369 реакций оказались, вероятно, неверно извлечены из патентов, а в 47 не хватало ключевых реагентов [94].
  - Модели обучаются почти только на успешных реакциях. Количества указываются неполно, побочные продукты и неудачные условия почти не фиксируются [80].
  - Стереохимия в USPTO часто не размечена или размечена неверно [82].
- **Медхимия ≠ процесс.**
  - Типовой набор реакций медхимии узок. Самые частые реакции — образование амидов, кросс-сочетание Сузуки–Мияуры и SNAr. Ни одна из самых используемых реакций не открыта за последние 20 лет [26].
  - Процесс-химикам нужны конвергентные маршруты, а очевидные разъединения опытный процесс-химик часто уже рассмотрел сам [80].

**Вывод (наш).** Ценность инструмента не столько в «изобретении» маршрута, сколько в том, чтобы быстро и с источниками свести разрозненные данные. Каждый извлечённый факт нужно проверять: данные из баз сами по себе грязные.

---

## 3. Количественные данные о «боли»

| Показатель | Значение | Источник | Качество / комментарий |
|---|---|---|---|
| Среднее число химических превращений на синтез кандидата (process R&D GSK, AZ, Pfizer) | **8,1** (128 синтезов, 1039 превращений) | [23][24][25] | Охват подтверждён по аннотации [23], числа — по двум вторичным источникам [24][25]. Полный текст RSC недоступен. |
| Доля защит и снятия защит среди превращений | 6% + 15% = **21%**; 45 из 128 синтезов обошлись без защитных групп и были короче | [24] | Вторичный источник. |
| Самый частый класс в process R&D | гетероатомное алкилирование и арилирование (19%) | [24] | Вторичный источник. |
| Тренд длины маршрутов | «Сложность АФИ и длина синтезов значительно выросли», что толкает компании к аутсорсингу | [22] | Отраслевые авторы. Поставщик пишет о медхимических препаратах длиной более 20 стадий [27]; это позиция поставщика. |
| Общий выход самой длинной линейной последовательности | 20% / 35% / 44% (ранняя / поздняя / коммерческая стадия); средний выход коммерческой стадии 86% | [28] | 97 процессов; выборки по фазам разные. |
| Полный E-фактор (cEF), кг отходов на кг АФИ | **632 / 308 / 182** (ранняя / поздняя / коммерческая) | [28] | Менее 1% сырья входит в АФИ [28]. |
| E-фактор фармацевтики (классическая таблица Шелдона) | 25 — >100 | [29] | Не сравнивать напрямую с cEF: разные определения и выборки. |
| PMI типичных малых молекул | **168–308** кг/кг; в целом от 100 до нескольких тысяч кг/кг в зависимости от длины синтеза | [32][22] | Происхождение нижней границы 168 в [32] не проверено. 308 совпадает с cEF поздней фазы [28] (PMI ≈ cEF + 1 по определениям; наш расчёт). |
| Вклад растворителей | 80–90% массы процесса | [30][32] | [30] — аннотация. |
| Эффект смены маршрута | снижение PMI на 98% (с более чем 5000 до примерно 100 кг/кг) в одном отраслевом примере | [22] | Единичный пример, не статистика. |
| Время на выделение и очистку | около 70% времени процесс-химика | [22] | Без прямой ссылки на первоисточник; оценка отраслевых авторов. |
| Сроки | разработка 10 лет и более; параметры замораживают за 1–2 года до запуска | [22] | — |
| Время машинного планирования (CASP) | Chematica: 15–20 мин на мишень (64 ядра), одна мишень — несколько часов [33]. AiZynthFinder: решение обычно менее чем за 10 с, полный поиск — менее 1 мин [78]; медиана 40–90 с на внутренних наборах [79]. | [33][78][79] | Это базовая линия по скорости для инструментов, а не для людей. |
| Время ручной разведки маршрута | **не подтверждено** | — | Опубликованных чисел не нашли. Их нужно **измерить самим** (см. M7, M10) и спросить у эксперта. |
| Поиск информации (не химия) | 15–35% рабочего времени knowledge-workers (IDC, 2004) [37]; около 4 ч/нед на поиск статей (опрос более 3000 исследователей, 2019) [38] | [37][38] | Неспецифично для химии. Использовать только как фон. |
| Доля АФИ в цене готового генерика | обычно **20–30%**, встречаются оценки >50% | [34] | Рецензируемая статья 2025 года со ссылками на более ранние работы. |
| CMC-замечания в отказах FDA | 69% из 61 CRL (2008–2013) | [35] | Новые препараты. |
| Замечания по качеству и производству в отказах FDA | 74% из 202 CRL (2020–2024) | [36] | Отраслевая пресса; методика кодирования не раскрыта. |
| Доля CMC в затратах на R&D | **не подтверждено** | — | Открытого первоисточника не нашли. |
| Глубина локализации в РФ | Отечественные компании обычно выполняют лишь 3–4 завершающие стадии из 7–15 | [68] | Мнение отраслевого эксперта («Р-Фарм»). |

---

## 4. Рыночный контекст

### 4.1 Дженерики и истечение патентов

- **Общий рынок.** Мировые расходы на лекарства превысят $2,6 трлн к 2030 г. при росте 5–8% в год [39].
- **Дженерики в США.** Дженерики и биосимиляры дают 90% рецептов и лишь 12% расходов; экономия в 2024 г. составила $467 млрд [41].
- **Потери выручки от истечения патентов.**
  - IQVIA: «почти $200 млрд» потерь брендов [40].
  - Evaluate: более $500 млрд продаж под риском генерической конкуренции в 2026–2032 гг. [42]; пик приходится на 2031 г. (около $158 млрд) [43].
  - Расхождение оценок объясняется разными окнами и охватом.
- **Рынок дженериков** (оценки агентств): $435 млрд (2023) [44] и $460 млрд (2024) [45].

### 4.2 CDMO

- **Размер рынка малых молекул (CDMO).** $71,3 млрд в 2024 г. с ростом до $126 млрд к 2033 г. по оценке Grand View [46]; около $74 млрд по оценке FMI, при этом на топ-5 игроков приходится лишь около 15% [47]. Определения рынка у агентств разные, поэтому числа не смешиваем.
- **Аутсорсинг растёт** вместе с длиной синтезов [22]. Поставщики уже продают AI-разведку маршрутов: Lonza на базе Reaxys [81].
- **Политика США.**
  - BIOSECURE Act подписан 18.12.2025 в составе NDAA FY2026 [48]. В 06.2026 WuXi AppTec включён в список 1260H, а в 08.2026 суд выдал предварительный запрет на применение этого включения [49].
  - Пошлины по Section 232 (04.2026): 100% на патентованные препараты и их ингредиенты, включая АФИ. Дженерики и их ингредиенты пока исключены [50].
- **ЕС.** По Critical Medicines Act в 05.2026 достигнуто политическое соглашение, но на 10.2026 акт ещё не вступил в силу. Преференции в закупках предполагаются пропорционально доле производства в ЕС, включая АФИ [51].

### 4.3 Концентрация цепочек поставок АФИ

Метрики ниже разные (площадки, DMF, объём), поэтому их нельзя сравнивать напрямую.

- **Площадки.** В 2019 г. лишь 28% площадок АФИ для рынка США находились в США [52]; в 2018 г. 88% площадок АФИ были за рубежом [53].
- **DMF.** Среди новых DMF на АФИ в 2023 г. 50% пришлось на Индию и 32% на Китай [54].
- **Объём.** По объёму АФИ в 2024 г. доля Китая составила лишь 8%, но USP указывает на «значительную зависимость от Китая по KSM» [55].
- **ЕС.** 60–80% АФИ для дженериков, используемых в Европе, производятся в Индии или Китае [56].
- **Индия.** Даже при локальном производстве АФИ ключевые исходные материалы (KSM) в основном поставляются из Китая [58]. Программа PLI (2020) нацелена на 53 импортозависимых АФИ [57].

### 4.4 Россия

- **Импорт субстанций.**
  - Зарубежные АФС занимают «около 70–75%» российского рынка. Более половины импорта приходится на Китай, около 29% на Европу, около 17% на Индию [61] (ФБУ «ГИЛС и НП», 11.2024).
  - По RNC Pharma (2023), около 80–85% российских препаратов изготавливаются из импортных субстанций [63]. Это другая метрика, чем в [61].
  - В 2023 г. импорт в натуральном выражении снизился на 13,2% [62].
- **Политика.**
  - «Фарма-2030» ставит целью долю стратегически значимых ЛП полного цикла, включая синтез молекулы, 80% к 2030 г. против 67,44% в 2022 г. [59][60]. Среди угроз стратегия называет удорожание зарубежных субстанций [59].
  - Минпромторг (2024): 45% ЖНВЛП можно производить из отечественных АФС, цель — 60% через шесть лет; в федеральном проекте 186 МНН [64].
  - Вице-премьер Т. Голикова (2024): около 46% наименований ЛП производятся в РФ по полному циклу [66].
  - Министр промышленности и торговли А. Алиханов (01.2026): две трети производимых в РФ ЖНВЛП «могут производиться» из российских АФС [65].
- **Закупки.**
  - Утверждён перечень стратегически значимых ЛП из 206 позиций (04.2026).
  - Действует правило «второй лишний»: заявка на ЛП, произведённый в ЕАЭС не по полному циклу, отклоняется, а полный цикл включает синтез молекулы действующего вещества [67].
  - Даты вступления в силу различаются по разделам перечня. Перед цитированием их нужно сверить на pravo.gov.ru.
- **Мощности.** С 2020 г. открыто 20 заводов АФС [69].

### 4.5 Почему именно сейчас

1. **Волна истечения патентов** выводит в разработку генериков много МНН одновременно [42][43].
2. **Политика устойчивости цепочек поставок** во всех ключевых юрисдикциях: США [48][50], ЕС [51][56], Индия [57], РФ [59][67]. Требование полного цикла означает, что маршрут нужно начинать **глубже**, от более простого и доступного сырья. Это прямой запрос на перепроектирование маршрутов.
3. **Дефектура.**
   - США: 227 активных дефектур во II кв. 2026 г., третий квартальный рост подряд [70].
   - ЕС: 136 критических дефектур с 01.2022 по 10.2024 [71].
   - Закупочные цены на генерики нередко ниже себестоимости [55].
4. **Ужесточение требований к примесям.** Нитрозамины: [9] — 2024 г., [10] — 2023 г.
5. **Экологическая расширенная ответственность производителя.** Директива ЕС об очистке городских сточных вод (UWWTD) обязывает производителей лекарств и косметики покрыть не менее 80% затрат на четвертичную очистку [72].
6. **Зрелость ИИ.** FDA получило более 500 заявок с ИИ-компонентами с 2016 г. [73]. CASP ежедневно используется в AstraZeneca [79].

---

## 5. Что ИИ может и чего не может

### 5.1 Задокументированные успехи CASP

| Система | Доказательство | Тип доказательства |
|---|---|---|
| Chematica / Synthia | Маршруты к 8 мишеням спланированы за 15–20 мин каждая, и все выполнены в лаборатории [33]. Для одной мишени получено 45 ч работы против 62 ч, для другой заявлена экономия времени и стоимости 50% [33]. Природные соединения прошли тест «типа Тьюринга»: маршруты «в основном неотличимы» от человеческих [75]. | Лабораторная проверка. Авторы сотрудничают с вендором (конфликт интересов). |
| 3N-MCTS (Segler et al.) | Двойное слепое A/B-сравнение, 45 химиков: литературный маршрут против машинного 43,0% против 57,0%, предпочтение незначимо (p = 0,26). Решено 92% тестового набора при лимите 60 с [74]. | Экспертная оценка (без эксперимента). |
| AiZynthFinder (AstraZeneca) | «Используется ежедневно». Доля мишеней, решённых до стока (stock): 80% для дизайнов AZ, 71% для ChEMBL [79]. | Промышленное применение, медхимия. |
| ASKCOS (MIT + консорциум MLPDS) | В 2019 г. интерфейс на базе ASKCOS развёрнут для всех медхимиков AZ [80]. Помог «сотням медицинских, синтетических и процесс-химиков» [77]. Связка с роботизированной проточной платформой дала 15 соединений, но детали реализации всё равно определяли эксперты [76]. | Промышленное применение и демонстрация. |
| Отрасль | Отношение к CASP в компаниях — «от безразличия до ежедневного использования» [80]. CDMO продают AI-разведку маршрутов [81]. | Обзор; позиция поставщика. |

### 5.2 Ограничения CASP

- **Найденный путь не равен осуществимому.** «Способность найти путь не гарантирует его химической осуществимости», а единственная настоящая проверка — выполнить синтез [80]. В [74] фильтр осуществимости не учитывает условия, реагенты и катализаторы.
- **Доля решённых мишеней не говорит о качестве маршрута.**
  - На PaRoutes MCTS (AiZynthFinder) «решает» около 97% мишеней, но эталонный маршрут оказывается в top-1 лишь в 9–20% случаев, а в top-10 — в 42–61% [83].
  - Рейтинги моделей меняются при контролируемой оценке [82].
  - Сами разработчики AiZynthFinder называют слабыми местами неоптимальные стратегии защиты и ранжирование маршрутов [79].
- **Процессные критерии не встроены.** PMI, конвергентность, примеси, масштаб в стандартном скоринге CASP не учитываются. iGAL 2.0 предлагает выход и конвергентность как индикаторы для CASP [28].

### 5.3 Отказы LLM в химии

| Тип отказа | Данные |
|---|---|
| Выдуманные ссылки | GPT-3.5 выдумал 55% ссылок, GPT-4 — 18%. Среди реальных ссылок существенные ошибки в 43% и 24% соответственно [84]. GPT-4o: 19,9% выдуманы; в 45,4% реальных ссылок есть ошибки, чаще всего неверный или недействительный DOI [86]. Систематические обзоры: доля галлюцинаций 28,6% (GPT-4), 39,6% (GPT-3.5), 91,4% (Bard) [85]. Поиск по точному названию: 46,8% ссылок GPT-4 галлюцинированы [87]. В оценке OpenScholar GPT-4o галлюцинирует ссылки в 78–90% случаев [88]. Определения во всех работах разные, поэтому разброс велик. Химически специфичного исследования не нашли. |
| Невалидные структуры и слабый ретросинтез | GPT-4 на USPTO-50k, top-1: 0,6% в zero-shot и 11,4% в лучшей few-shot-настройке против 53,6% у специализированной модели Chemformer. Невалидных SMILES 20,6% (zero-shot) и 11,0% [89]. |
| Многостадийное планирование | Успех ретросинтетического планирования у LLM с in-context learning не превышает 5,5% (препринт) [91]. |
| Самоуверенность и безопасность | Лучшие модели на ChemBench в среднем превосходят лучших химиков-участников, но ошибаются на базовых задачах, дают самоуверенные ответы и слабы в химической безопасности [90]. |
| LLM как судья | GPT-4 в роли оценщика предпочитал гладкие ответы GPT-4 и не замечал фактических ошибок; эксперты-люди предпочли ChemCrow с инструментами [92]. GPT-4 без инструментов «систематически не даёт фактически точной информации» [92]. |
| Без внешних источников | В Coscientist все модели без веб-поиска предложили неверный синтез для простого известного АФИ; модуль поиска заметно улучшил планирование [93]. |
| Несбалансированные реакции | Доля несбалансированных реакций именно в выводе LLM **не подтверждена** публикациями. Это часть нашего RQ1 (протокол). На уровне данных они типичны [94][95]. |

### 5.4 Реалистичная ценность ИИ

| ИИ может (есть доказательства) | ИИ не может (и не должен заявлять) |
|---|---|
| За минуты свести литературу, патенты и базы в несколько вариантов со ссылками; инструменты поиска резко снижают ошибки [92][93] | Гарантировать осуществимость, выход и условия в масштабе [74][76][80] |
| Предлагать стратегии, которые эксперты считают сопоставимыми с литературными [74][75] | Предсказать профиль примесей, полиморф, тепловую безопасность |
| Быстро проверять детерминированные свойства: валидность структур, баланс, сток, классы Q3C/Q3D, алерты | Дать регуляторное обоснование RSM или юридическое заключение по патентам |
| Считать и сравнивать метрики (число стадий, PMI-оценка, конвергентность [28]) | Служить единственным судьёй качества: LLM-судья не замечает ошибок [92] |

**Вывод (наш).** Позиционирование: «LLM предлагает, инструменты проверяют, эксперт решает». Полезный результат — сокращённое время до shortlist с прозрачными статусами доверия. «Готовая технология» таким результатом не является.

---

## 6. Предлагаемые метрики

Конфигурации из [протокола](../paper/protocol.md):
- **B0** — LLM без обвязки с тем же бюджетом;
- **B1** — шаблонный ретросинтез (AiZynthFinder);
- **B2** — LLM + RAG;
- **S0** — полная система.

По всем метрикам: не менее 3 прогонов, 95% bootstrap CI, парные сравнения на одних и тех же МНН (EVAL-003, EVAL-004).

| # | Метрика | Определение | Как измеряем | Почему эта метрика | Базовая линия | Предварительная цель |
|---|---|---|---|---|---|---|
| **Качество** | | | | | | |
| M1 | Доля валидных стадий (step validity rate) | Доля стадий, прошедших **все обязательные** детерминированные проверки: парсинг и санитизация структур (RDKit), баланс атомов (строгий и «по тяжёлым атомам продукта»), наличие источника или пометки гипотезы, наличие исходных веществ в стоке. Флаги Q3C/Q3D/алертов информационные и в pass/fail не входят. | route-lint по всем стадиям, с разбивкой по проверкам и версиям проверок (TRUST-005). Дополнительно можно считать round-trip-проверку прямой моделью: в литературе она даёт 71–81% [97]. | Прямая мера главного риска: правдоподобные, но невалидные стадии LLM (5.3). Это RQ1/RQ2. | B0, B2 (до и после цикла ремонта) | Относительная: S0 > B0 с непересекающимися CI. Абсолютную цель задаём **после** первого замера B0. |
| M2 | Recall известных маршрутов @k | Доля эталонных (литературных или промышленных) маршрутов тест-сета, воспроизведённых среди k вариантов. Совпадение определяется по набору ключевых интермедиатов (InChIKey, без учёта защитных групп) или по ключевым разъединениям; критерий фиксируется до прогона. | SynthBench test (замороженный, EVAL-002), отдельно контаминационный срез (EVAL-005) | Проверяет, что система находит то, что уже известно, то есть решает проблему фрагментации (2.2). Аналог top-N recovery в PaRoutes [83]. | B0, B1, B2 | Не задаём. Для ориентира: у AiZynthFinder top-10 = 0,42–0,61 на PaRoutes [83], но это другой набор и другая задача. |
| M3 | Доля технически осмысленных маршрутов (по оценке эксперта) | Доля маршрутов, которые эксперт признал технически осмысленными по чек-листу Q-001 (на базе SELECT [19]). | Слепая оценка: маршруты S0, B0 и литературные перемешаны (по образцу [74]), бинарная оценка и шкала 1–5. При ≥2 экспертах — α Криппендорфа. | Только эксперт оценивает многокритериальную пригодность (2.1). LLM-судья для этого непригоден [92]. | Литературные маршруты и B0 | S0 **не хуже литературных** маршрутов статистически (прецедент: 43% против 57%, p = 0,26 [74]). Надёжность: α ≥ 0,667 для предварительных выводов [104]. |
| M4 | Число действительно разных стратегий | Число кластеров среди k вариантов по ключевым разъединениям или дереву маршрута: tree edit distance [96] или packing number — число маршрутов без общих реакций [82]. | Скрипт на RouteSpec; эксперт проверяет на подвыборке | Пользователю нужны **альтернативы** с разными компромиссами (2.1), а не 5 копий одного маршрута. | B0, B1 | Не задаём. Сначала нужно согласовать с экспертом, что считать «разной стратегией» (вопрос эксперту). |
| M5 | Доля утверждений с проверяемым источником (claim grounding rate) | Доля фактов маршрута (стадия, класс реагентов, условия, выход), у которых источник существует (DOI резолвится, номер патента существует) **и** цитата найдена в тексте (TRUST-004). | Автоматически (Crossref или патентный реестр + поиск цитаты) и ручной аудит выборки. Метрики citation recall/precision — по аналогии с ALCE [98]. | Профессионалу нужно за секунды понять, чему верить (TRUST). Это мера проверяемости результата. | B0, B2 | Не задаём до первого замера. |
| M6 | Доля галлюцинированных ссылок | Доля ссылок, где DOI или патент не существует, либо не совпадают название и автор (определение как в [84]), либо цитаты нет в тексте. Считаем отдельно для **сырого** вывода генератора и для **показанного** пользователю. | Автоматически + ручной аудит | Литература даёт 18–55% и выше выдуманных ссылок у LLM [84][85][86][87]. Без контроля это главный источник потери доверия. | B0; литература [84][86] как внешний ориентир | **Показанные** ссылки со статусом `literature`: 0% по построению, с аудитом остатка. Сырой вывод — снижение относительно B0. |
| **Эффективность** | | | | | | |
| M7 | Время до первого набора вариантов (TTFO) | Реальное время от ввода МНН до выдачи k ≥ 3 проверенных вариантов | Логи и трассы; для ручной базовой линии — хронометраж эксперта на тех же МНН с его обычными инструментами | Время до shortlist — основная боль разведки маршрутов (раздел 3). Ручная базовая линия в литературе не найдена. | Ручная работа (измерить); CASP: 15–20 мин [33], <1–1,5 мин [78][79] | Ориентир: не дольше CASP-систем (≤ 20 мин на МНН) [33]. Окончательно — после хронометража. |
| M8 | Стоимость одного валидного маршрута | ($ + токены) / число маршрутов, прошедших все обязательные проверки | Трассы gateway; цены фиксируются на дату прогона | Точность без учёта стоимости вводит в заблуждение: повторами её можно «купить» [99]. Строим Парето «качество × стоимость». | B0 с тем же бюджетом (EVAL-003) | S0 доминирует B0 по Парето или даёт более высокую валидность при сопоставимой стоимости. |
| **Удобство** | | | | | | |
| M9 | SUS | Стандартная анкета из 10 пунктов, шкала 0–100 [100]; русский перевод (валидность перевода — угроза) | После выполнения сценариев S1–S4; n = 5–8 экспертов; среднее с CI | Пользователи — не программисты (фармакологи, технологи). Без приемлемого UI ценность не реализуется. | Средний SUS = 68 по 500 исследованиям [101]; >70 — «приемлемо» [102] | ≥ 68 (не ниже среднего [101]). Оговорка: чтобы обнаружить разницу в 15 пунктов, нужно n ≈ 8–11, а для 10 пунктов — 16–21 [103], поэтому при малом n это ориентир, а не тест. |
| **Бизнес** | | | | | | |
| M10 | Сэкономленные часы эксперта на МНН | T_ручн − T_с_инструментом, где второе включает время проверки вывода экспертом | Хронометраж в парном дизайне (тот же эксперт, разные МНН сопоставимой сложности) + самоотчёт | Прямой перевод ценности в деньги для заказчика. Экстраполяция: часы × МНН/год × ставка (явно помеченные допущения). | Ручная работа (измерить) | Не задаём до измерения базовой линии. |
| **Ограничитель (guardrail)** | | | | | | |
| M11 | Корректность входного гейта и наличие дисклеймера | Доля корректных отказов и пропусков на синтетических фикстурах; 100% экспортов с дисклеймером | Тесты (SAFE-001, -002, -004, -007) | Ограничитель: нарушение недопустимо при любом выигрыше в качестве | — | 100% (fail-closed) |

**Связь метрик с проблемой**

| Метрика | Какую проблему закрывает |
|---|---|
| M1, M5, M6 | Ненадёжность LLM (5.3) и доверие пользователя |
| M2, M4 | Фрагментация источников (2.2) и потребность в альтернативах (2.1) |
| M3 | Промышленная осмысленность при многокритериальном выборе |
| M7, M10 | Время, главная боль из раздела 3 |
| M8 | Экономическая оправданность обвязки по сравнению с «просто LLM» (ключевая гипотеза проекта) |
| M9 | Принятие инструмента непрограммистами |

M1–M8 сравниваются с B0 (EVAL-003). Интерпретация каппы и альфы — по [104][105] с оговоркой, что универсального стандарта нет.

---

## 7. Персоны и сценарии

Персоны — гипотеза на основе ролей из раздела 1.2. Их нужно проверить интервью (вопрос эксперту).

| Персона | Контекст | Цели | Боли | Что ей нужно от synthroute |
|---|---|---|---|---|
| **П1. Процесс-химик** (R&D генериков или CDMO) | Получает МНН для разработки или запрос клиента | За дни, а не недели, получить shortlist 3–5 маршрутов с источниками и рисками | Ручной сбор статей и патентов; несбалансированные и неполные данные; процессные патенты | Варианты с источниками и статусами; таблица SELECT-сравнения; флаги Q3C/Q3D/M7; кандидаты в RSM |
| **П2. Технолог / инженер-химик** (масштабирование) | Переводит процесс в пилот или на завод, в т. ч. при трансфере | Понять масштабируемость: растворители, металлы, опасности, PMI | Литературные методики лабораторные; нет масштабных параметров | Режимы lab/pilot/plant; правка через чат (например, «заменить растворитель класса 2 на стадии N») с diff и повторной проверкой |
| **П3. Фармаколог / руководитель портфеля** | Решает, брать ли МНН в портфель или локализовать | Быстро оценить «сложность субстанции»: стадии, доступность и происхождение сырья, риски | Не химик-синтетик; нужен понятный итог | Сводка на одной странице, экспорт в HTML/PDF для техсовета, явные статусы доверия |
| **П4. Специалист по регуляторике (CMC)**, вторичная | Готовит обоснование RSM и раздел 3.2.S.2 | Видеть границу GMP, источники, флаги примесей | Разрозненные данные о происхождении сырья | Трассируемость каждого факта; версия маршрута |

**Сценарии**

1. **S1. Быстрая разведка для генерика (П1).**
   - Шаги: ввод МНН → гейт → 3–5 вариантов → таблица сравнения (стадии, оценка общего выхода, PMI-оценка, сток, флаги) → отметка понравившихся вариантов → экспорт.
   - Метрики: M1–M7, M9.
2. **S2. Локализация «вглубь» (П3 + П1).**
   - Шаги: пользователь задаёт ограничение по стоку (только сырьё из заданного списка или региона, например ЕАЭС) → система ищет маршруты от более ранних и простых исходных веществ → показывает, как меняются число стадий, граница GMP и кандидаты в RSM.
   - Обоснование: [59][67][68].
   - Метрики: M2, M4, M7, M10.
3. **S3. От лаборатории к пилоту через чат (П2).**
   - Шаги: в режиме pilot система подсвечивает растворители класса 1–2, металлы на поздних стадиях и опасные стадии → пользователь просит заменить → создаётся новая версия с diff и повторной проверкой (TRUST-006).
   - Метрики: M1, M8, M9.
4. **S4. Подготовка к техсовету или эксперту (П3, П4).**
   - Шаги: экспорт PDF со статусами `literature`/`computed`/`hypothesis`/`failed`, источниками и флагами `unverified_citation`, дисклеймер (SAFE-004) → эксперт в слепом режиме оценивает маршруты.
   - Метрики: M3, M5, M6, M11.

---

## Выводы для проекта

1. **Ниша — ускорение разведки маршрута, а не «изобретение химии».** Самые сильные рыночные драйверы — волна генериков [42] и требование полного цикла, включая синтез молекулы, в РФ [59][67]. Отечественные компании делают лишь последние 3–4 стадии [68], поэтому сценарий S2 (стартовать глубже) — наш главный дифференциатор для российского рынка.
2. **Регуляторные флаги — дешёвая и ценная детерминированная проверка.** Классы Q3C и Q3D, структурные алерты M7 и нитрозамины, граница GMP и кандидаты в RSM по Q11. Показываем их как **флаги со ссылкой на пункт руководства**, а не как вердикт.
3. **Процессные метрики в скоринге.** CASP оптимизирован под медхимию [79][80]. Добавляем число стадий, конвергентность и оценку выхода в духе iGAL 2.0 [28], а также PMI-оценку. Это отличает нас от AiZynthFinder и ASKCOS.
4. **Проверка баланса должна быть двухуровневой** (строгая и «по тяжёлым атомам продукта»). Реакции в базах как правило несбалансированы [95], и строгая проверка забракует почти все литературные стадии.
5. **Без LLM-судьи как основного оценщика** [92]. Нужны эксперт и детерминированные проверки. Эксперта стоит забронировать заранее, ориентировочно на n = 5–8 сессий для SUS и слепой оценки.
6. **Ориентиры из литературы для B0:** 18–55% выдуманных ссылок [84] и 11–21% невалидных SMILES [89]. Первый замер B0 на наших МНН — приоритет недели (совпадает с north-star, п. 7.4).
7. **Ручная базовая линия по времени не опубликована.** Без собственного хронометража M7 и M10 не будут защитимы. Это риск, и его надо закрыть с экспертом.
8. **Рыночные числа брать только с указанием источника и окна,** потому что оценки расходятся в разы (раздел 4).

## Открытые вопросы

**Для самостоятельного поиска**
- Полный текст Carey 2006 [23] (нужен доступ ИТМО к RSC). Проценты Brown & Boström [26].
- Доля CMC в затратах на R&D; длительность разведки маршрута в CDMO (запросить коммерческие предложения?).
- Приняты ли Q3A, Q3C, Q3D и M7 (или их аналоги) в праве ЕАЭС и РФ; статус РФ в ICH. **Не подтверждено.**
- Нормативные основания «второго лишнего» (ПП № 1875 от 23.12.2024 и последующие изменения): сверить на pravo.gov.ru.
- Химически специфичные данные о галлюцинации ссылок; доля несбалансированных реакций в выводе LLM (закроем своим RQ1).
- Первоисточник Bangor et al. 2008 (среднее SUS около 70); валидированный русский перевод SUS.

**Для эксперта (PhD, химическая технология)** — перенести в `docs/expert/questions.md` как Q-004 и далее.
1. **Сколько занимает ручная разведка маршрута** по МНН до shortlist из 3–5 вариантов, и из чего складывается это время? *Гипотеза:* от нескольких дней до 2–4 недель, большая часть — поиск и сверка патентов. → Базовая линия для M7 и M10.
2. **Какие критерии отсекают маршрут на кабинетном этапе** для генерика в РФ, и как они взвешиваются (SELECT)? → Чек-лист M3 и колонки таблицы сравнения.
3. **Как на практике выбирают и обосновывают RSM для генерика в ЕАЭС?** Применяют ли эксперты принципы ICH Q11 Q&A? → Логика пометки «кандидат в RSM».
4. **Какие флаги нужны на уровне стадии** (Q3C, Q3D, M7, нитрозамины, опасные реагенты), и какие ложные срабатывания недопустимы? → Пороги route-lint.
5. **Когда стадию из литературы считать «валидной»,** если в источнике не указаны побочные продукты или реагенты? → Строгость проверки баланса (M1).
6. **Что считать «разными стратегиями»:** разные ключевые разъединения, разные RSM или другой порядок стадий? → Определение M4.
7. **Какие параметры реально меняются между режимами lab, pilot и plant,** и какой минимум делает режим полезным? → Объём фичи «технологический режим».
8. **Какие 20–50 МНН с хорошо документированными маршрутами взять в тест-сет** (разная длина, классы, наличие процессных патентов)? → SynthBench.
9. **Какими инструментами технологи в РФ пользуются сейчас** (Reaxys, SciFinder, патентные базы; доступ после 2022 г.)? → Реалистичная ручная базовая линия.
10. **Готовы ли эксперт и 1–2 коллеги участвовать в слепой оценке и SUS?** Сколько маршрутов реально оценить за час? → План human eval и мощность M3/M9.
