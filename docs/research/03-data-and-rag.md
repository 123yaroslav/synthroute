# Данные и RAG: инвентаризация источников, дизайн бенчмарка, хранилище знаний

- **Дата:** 2026-10-13
- **Блоки недельного плана:** 5 (данные) и 6 (RAG)
- **Вопрос:** какие датасеты закрывают задачу «МНН → несколько проверенных вариантов маршрута», можно ли их использовать в открытом бенчмарке, как отобрать 30–50 препаратов и как устроить хранилище документов для RAG.
- **Рамки:** документ работает на уровне данных и ПО (состав, объём, версия, лицензия, способ доступа). Процедуры синтеза, условия реакций и маршруты конкретных веществ здесь не приводятся (SAFE-004, RESPONSIBLE_USE.md). Регуляторные перечни упоминаются только как источники данных для входного гейта.
- **Правило точности:** каждое число, лицензия и утверждение о доступе снабжены ссылкой из таблицы «Источники». Где факт не удалось подтвердить первоисточником, стоит «не подтверждено» (CORE-005, DOC-004).
- **Как собирали:** прямые загрузки официальных страниц, API (figshare, Zenodo, GitHub, PyPI, Crossref, OpenAlex, Europe PMC, PubChem, ChEMBL, HF datasets-server) и FTP-листинги 2026-10-13. Пометка **[подсчёт]** означает, что число получено нами по скачанному файлу, а не взято со страницы.

## Источники

Все даты доступа — 2026-10-13.

| # | Источник (URL) | Тип | Дата доступа |
|---|---|---|---|
| 1 | https://api.figshare.com/v2/articles/5104873 (DOI 10.6084/m9.figshare.5104873.v1) | датасет (метаданные + файлы) | 2026-10-13 |
| 2 | https://nextmovesoftware.com/blog/?p=2975 | блог вендора | 2026-10-13 |
| 3 | https://github.com/connorcoley/retrosim , https://raw.githubusercontent.com/connorcoley/retrosim/master/retrosim/data/data_processed.csv | репозиторий + файл данных | 2026-10-13 |
| 4 | https://api.crossref.org/works/10.1021/acs.jcim.6b00564 | метаданные статьи | 2026-10-13 |
| 5 | https://github.com/wengong-jin/nips17-rexgen , https://arxiv.org/pdf/1711.04810 | репозиторий + статья | 2026-10-13 |
| 6 | https://github.com/Hanjun-Dai/GLN , https://arxiv.org/pdf/2001.01408 | репозиторий + статья | 2026-10-13 |
| 7 | https://raw.githubusercontent.com/open-reaction-database/ord-data/main/README.md , https://api.github.com/repos/open-reaction-database/ord-data | README + метаданные репозитория | 2026-10-13 |
| 8 | https://datasets-server.huggingface.co/size?dataset=open-reaction-database/ord-data , https://huggingface.co/datasets/open-reaction-database/ord-data | API размеров датасета | 2026-10-13 |
| 9 | https://raw.githubusercontent.com/open-reaction-database/ord-schema/main/README.md , https://pypi.org/pypi/ord-schema/json , https://docs.open-reaction-database.org/en/latest/ | схема, пакет, документация | 2026-10-13 |
| 10 | https://api.crossref.org/works/10.1021/jacs.1c09820 | метаданные статьи (ORD, JACS 2021) | 2026-10-13 |
| 11 | https://api.crossref.org/works/10.1021/acs.jcim.4c00292 , https://api.figshare.com/v2/articles/23298467 , https://github.com/sustainable-processes/ORDerly , Europe PMC PMC11094788 | статья + датасет + репозиторий (ORDerly) | 2026-10-13 |
| 12 | https://github.com/MolecularAI/PaRoutes , https://zenodo.org/api/records/7341155 , https://zenodo.org/api/records/6275421 , https://api.crossref.org/works/10.1039/D2DD00015F | репозиторий + датасеты + статья | 2026-10-13 |
| 13 | https://www.nextmovesoftware.com/pistachio.html | страница продукта | 2026-10-13 |
| 14 | https://www.elsevier.com/products/reaxys , https://www.elsevier.com/products/reaxys/predictive-retrosynthesis | страницы продукта | 2026-10-13 |
| 15 | https://www.cas.org/cas-data/cas-reactions , https://www.cas.org/legal , https://brandcdn.cas.org/G2HB3KG8/as/k4sp5c4wz3cvqpf5jcpn96/Info-Use-Policy-7122024 | страница продукта + Information Use Policy | 2026-10-13 |
| 16 | https://api.crossref.org/works/10.1038/s41929-020-00556-z , https://api.figshare.com/v2/articles/12696482 , https://api.github.com/repos/willfinnigan/retrobiocat , Europe PMC PMC7116764, PMC10476152 | статья + датасет + репозиторий (RetroBioCat) | 2026-10-13 |
| 17 | https://zenodo.org/api/records/8254726 , https://api.github.com/repos/hesther/enzymemap , Europe PMC PMC10718068 | датасет + репозиторий + статья (EnzymeMap) | 2026-10-13 |
| 18 | https://raw.githubusercontent.com/rxn4chemistry/biocatalysis-model/main/data/ecreact-1.0.csv , https://raw.githubusercontent.com/rxn4chemistry/biocatalysis-model/main/LICENSE , Europe PMC PMC8857209 | данные + лицензия + статья (ECREACT) | 2026-10-13 |
| 19 | https://www.brenda-enzymes.org/download.php | страница загрузок БД | 2026-10-13 |
| 20 | https://api.figshare.com/v2/articles/24797220 , Europe PMC PMC11316731 | датасет + статья (mech-USPTO-31K) | 2026-10-13 |
| 21 | https://arxiv.org/pdf/2601.01943 , https://api.github.com/repos/TieuLongPhan/SynRXN , https://zenodo.org/api/records/17297258 , https://pypi.org/pypi/synrxn/json | статья + репозиторий + датасет (SynRXN) | 2026-10-13 |
| 22 | https://api.figshare.com/v2/articles/28230053 | датасет (CRD 1.37M) | 2026-10-13 |
| 23 | https://github.com/microsoft/syntheseus , https://pypi.org/pypi/syntheseus/json , https://raw.githubusercontent.com/microsoft/syntheseus/main/docs/single_step.md , https://api.crossref.org/works/10.1039/D4FD00093E | репозиторий + пакет + документация + статья | 2026-10-13 |
| 24 | https://arxiv.org/pdf/2006.15820 , https://raw.githubusercontent.com/binghong-ml/retro_star/master/README.md , https://arxiv.org/pdf/2310.19796 | статьи + README (Retro*, USPTO-190) | 2026-10-13 |
| 25 | https://api.github.com/repos/MolecularAI/aizynthfinder , https://raw.githubusercontent.com/MolecularAI/aizynthfinder/master/aizynthfinder/tools/download_public_data.py , https://zenodo.org/api/records/7797465 , https://api.figshare.com/v2/articles/12334577 , https://pypi.org/pypi/aizynthfinder/json , Europe PMC PMC11112899, PMC7672904 | ПО + модели + сток + статьи | 2026-10-13 |
| 26 | https://gitlab.com/mlpds_mit/askcosv2/askcos2_core/-/raw/main/LICENSE , https://arxiv.org/pdf/2501.01835 , https://askcos-docs.mit.edu/guide/6-Customization/6.1-Buyables-Postprocessing.html | лицензия + статья + документация (ASKCOS) | 2026-10-13 |
| 27 | https://pubchem.ncbi.nlm.nih.gov/docs/programmatic-access (исходник .md: /pcfe/docs/markdown/programmatic-access.md) | документация API | 2026-10-13 |
| 28 | https://pubchem.ncbi.nlm.nih.gov/docs/dynamic-request-throttling | документация API | 2026-10-13 |
| 29 | https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest , https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/imatinib/property/SMILES,ConnectivitySMILES,InChIKey/JSON | документация + живой запрос | 2026-10-13 |
| 30 | https://pubchem.ncbi.nlm.nih.gov/docs/pug-view , https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/compound/2244/JSON?heading=GHS+Classification | документация + живой запрос | 2026-10-13 |
| 31 | https://pubchem.ncbi.nlm.nih.gov/docs/lcss | документация (LCSS) | 2026-10-13 |
| 32 | https://pubchem.ncbi.nlm.nih.gov/docs/downloads , https://ftp.ncbi.nlm.nih.gov/pubchem/Compound/Extras/ | документация + FTP-листинг | 2026-10-13 |
| 33 | https://pubchem.ncbi.nlm.nih.gov/data/gear.cgi?q=stats&outfmt=json | статистика (бэкенд /docs/statistics) | 2026-10-13 |
| 34 | https://www.ncbi.nlm.nih.gov/home/about/policies/ | политика использования | 2026-10-13 |
| 35 | https://www.ebi.ac.uk/chembl/api/data/status.json , https://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/latest/ (release notes, LICENSE, REQUIRED.ATTRIBUTION, schema_documentation.txt), https://www.ebi.ac.uk/chembl/api/data/molecule.json , https://chembl.gitbook.io/chembl-interface-documentation/ | API + FTP + документация (ChEMBL 37) | 2026-10-13 |
| 36 | https://www.who.int/teams/health-product-and-policy-standards/inn/inn-lists , https://www.who.int/publications/m/item/inn-pl-135 , https://cdn.who.int/media/docs/default-source/international-nonproprietary-names-%28inn%29/pl135.pdf , https://www.who.int/teams/health-product-and-policy-standards/inn/guidance-on-inn , https://extranet.who.int/soinn/ , https://www.who.int/about/policies/terms-of-use | списки INN + условия WHO | 2026-10-13 |
| 37 | https://go.drugbank.com/releases/latest , https://trust.drugbank.com/drugbank-trust-center/terms-of-use , https://trust.drugbank.com/drugbank-trust-center/drugbank-terms-of-service | релизы + условия | 2026-10-13 |
| 38 | https://www.fda.gov/drugs/drug-approvals-and-databases/orange-book-data-files , https://www.fda.gov/drugs/drug-approvals-and-databases/approved-drug-products-therapeutic-equivalence-evaluations-orange-book , https://www.fda.gov/about-fda/about-website/website-policies | файлы данных + политика сайта | 2026-10-13 |
| 39 | https://www.fda.gov/drugs/drug-approvals-and-databases/drugsfda-data-files | файлы данных | 2026-10-13 |
| 40 | https://www.ema.europa.eu/en/medicines/download-medicine-data , https://www.ema.europa.eu/en/documents/report/medicines-output-medicines_json-report_en.json , https://www.ema.europa.eu/en/scientific-guidelines/download-website-data-json-data-format , https://www.ema.europa.eu/en/about-us/legal-notice | таблицы + JSON + правовая справка | 2026-10-13 |
| 41 | https://grls.rosminzdrav.ru/GRLS.aspx , https://grls.rosminzdrav.ru/robots.txt , https://www.consultant.ru/document/cons_doc_LAW_99350/cc6d28ea3b6e9b84fe7b623b8a0b3c745a8f34c0/ (61-ФЗ, ст. 33), https://minzdrav.gov.ru/opendata | реестр + норма права | 2026-10-13 |
| 42 | https://www.incb.org/incb/en/narcotic-drugs/Yellowlist/yellow-list.html , https://www.incb.org/incb/en/psychotropics/green-list.html , https://www.incb.org/incb/en/precursors/Red_Forms/red-list.html | регуляторные перечни (INCB) | 2026-10-13 |
| 43 | https://base.garant.ru/12112176/ (ПП РФ от 30.06.1998 № 681) | нормативный акт | 2026-10-13 |
| 44 | https://www.ecfr.gov/api/versioner/v1/versions/title-21.json?part=1308 , https://www.deadiversion.usdoj.gov/schedules/orangebook/c_cs_alpha.pdf | нормативный акт (API) + перечень | 2026-10-13 |
| 45 | https://www.opcw.org/resources/declarations/online-scheduled-chemicals-database , https://scdb.opcw.org/ | база перечней (CWC) | 2026-10-13 |
| 46 | https://open.fda.gov/apis/authentication/ , https://open.fda.gov/license/ | API + лицензия | 2026-10-13 |
| 47 | https://dailymed.nlm.nih.gov/dailymed/spl-resources-all-drug-labels.cfm , https://dailymed.nlm.nih.gov/dailymed/app-support-web-services.cfm | выгрузки + API | 2026-10-13 |
| 48 | https://precision.fda.gov/uniisearch/archive , https://www.fda.gov/industry/fda-data-standards-advisory-board/fdas-global-substance-registration-system | архив UNII + описание GSRS | 2026-10-13 |
| 49 | https://www.nlm.nih.gov/research/umls/rxnorm/docs/rxnormfiles.html , https://www.nlm.nih.gov/research/umls/rxnorm/docs/termsofservice.html , https://lhncbc.nlm.nih.gov/RxNav/TermsofService.html | релизы + условия | 2026-10-13 |
| 50 | https://pmc.ncbi.nlm.nih.gov/articles/PMC8284596 (ZINC20, DOI 10.1021/acs.jcim.0c00675), https://wiki.docking.org/index.php/Smallworld_and_Arthor_Databases | статья + вики подмножеств | 2026-10-13 |
| 51 | https://pmc.ncbi.nlm.nih.gov/articles/PMC9976280 (ZINC-22, DOI 10.1021/acs.jcim.2c01253) | статья | 2026-10-13 |
| 52 | https://wiki.docking.org/index.php/UCSF_ZINC_License , https://wiki.docking.org/index.php/Terms_And_Conditions | лицензия и условия | 2026-10-13 |
| 53 | https://www.emolecules.com/data-downloads , https://downloads.emolecules.com/free/2026-10-01/ , https://downloads.emolecules.com/free-extended/2026-10-01/ , https://search.emolecules.com/info/terms-of-service.html , https://www.emolecules.com/ | выгрузки + условия | 2026-10-13 |
| 54 | https://enamine.net/building-blocks/building-blocks-catalog , https://enamine.net/building-blocks/made-building-blocks , https://enamine.net/compound-collections/real-compounds/real-database , https://enamine.net/terms-of-use | каталоги + условия (v8) | 2026-10-13 |
| 55 | https://huggingface.co/datasets/molport/In-stock-Building-Block-Database , https://huggingface.co/datasets/molport/In-stock-Database , https://blog.molport.com/database/ftp-database-download/ | датасеты + описание FTP | 2026-10-13 |
| 56 | https://mcule.com/database , https://mcule.com/terms/ | выгрузки + условия | 2026-10-13 |
| 57 | https://molecularai.github.io/aizynthfinder/stocks.html , https://molecularai.github.io/aizynthfinder/configuration.html | документация стока | 2026-10-13 |
| 58 | https://askcos-docs.mit.edu/guide/11-References/11.1-ASKCOS-related-papers.html | документация (модули, buyables) | 2026-10-13 |
| 59 | https://www.ema.europa.eu/en/documents/scientific-guideline/ich-q3c-r9-guideline-impurities-guideline-residual-solvents-step-5_en.pdf , https://www.ema.europa.eu/en/ich-q3c-r8-residual-solvents-scientific-guideline | руководство ICH Q3C(R9) | 2026-10-13 |
| 60 | https://database.ich.org/sites/default/files/Q3D-R2_Guideline_Step4_2022_0308.pdf , https://www.ema.europa.eu/en/ich-q3d-elemental-impurities-scientific-guideline | руководство ICH Q3D(R2) | 2026-10-13 |
| 61 | https://database.ich.org/sites/default/files/ICH_M7%28R2%29_Guideline_Step4_2023_0216_0.pdf , https://www.ema.europa.eu/en/ich-m7-assessment-control-dna-reactive-mutagenic-impurities-pharmaceuticals-limit-potential-carcinogenic-risk-scientific-guideline | руководство ICH M7(R2) | 2026-10-13 |
| 62 | https://database.ich.org/sites/default/files/Q11_Guideline.pdf , https://www.ema.europa.eu/en/ich-q11-development-manufacture-drug-substances-chemical-entities-biotechnological-biological-entities-scientific-guideline | руководство ICH Q11 + Q&A | 2026-10-13 |
| 63 | https://api.crossref.org/works/10.1039/C5GC01008J (CHEM21, Green Chem. 2016) | статья | 2026-10-13 |
| 64 | https://learning.acsgcipr.org/guides-and-metrics/solvent-selection-guides/the-chem21-solvent-selection-guide/ | описание методики | 2026-10-13 |
| 65 | DOI: 10.1039/C4GC01149J, 10.1021/op4002565, 10.1039/C6GC00611F, 10.1039/C0GC00918K, 10.1039/B711717E, 10.1186/s40508-016-0051-z (проверены через api.crossref.org/works/<DOI>), https://eprints.whiterose.ac.uk/id/eprint/102544/1/art_10.1186_s40508_016_0051_z.pdf | гайды по растворителям | 2026-10-13 |
| 66 | https://acsgcipr.org/ , https://acsgcipr.org/tools/ , https://acsgcipr.org/tools/solvent-tool/ , https://acsgcipr.org/tools/process-mass-intensity-prediction-calculator/ , https://reagents.acsgcipr.org/ | инструменты ACS GCIPR | 2026-10-13 |
| 67 | https://api.crossref.org/works/10.1021/op200097d | статья о PMI | 2026-10-13 |
| 68 | https://api.crossref.org/works/10.1038/s41893-019-0400-5 | статья (PMI Predictor) | 2026-10-13 |
| 69 | https://api.crossref.org/works/10.1039/C5GC00340G , https://api.crossref.org/works/10.1021/acs.oprd.6b00015 | метрики CHEM21 + Solvent Tool | 2026-10-13 |
| 70 | https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/compound/887/JSON?heading=GHS%20Classification , https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/annotations/heading/GHS%20Classification/JSON?page=1 | агрегированные GHS-данные | 2026-10-13 |
| 71 | https://www.dguv.de/ifa/gestis/gestis-stoffdatenbank/index-2.jsp | БД GESTIS + условия | 2026-10-13 |
| 72 | https://cameochemicals.noaa.gov/ , https://cameochemicals.noaa.gov/help/reference/terms_and_conditions.htm | БД реактивности + условия | 2026-10-13 |
| 73 | https://shop.elsevier.com/books/brethericks-handbook-of-reactive-chemical-hazards/urben/978-0-08-100971-0 | коммерческий справочник | 2026-10-13 |
| 74 | https://crossref.org/documentation/retrieve-metadata/rest-api/access-and-authentication/ | документация API (лимиты) | 2026-10-13 |
| 75 | https://www.crossref.org/documentation/retrieve-metadata/rest-api/ , https://www.crossref.org/documentation/retrieve-metadata/rest-api/tips-for-using-the-crossref-rest-api/ | документация API (права, советы) | 2026-10-13 |
| 76 | https://crossref.org/blog/announcing-changes-to-rest-api-rate-limits/ , https://community.crossref.org/t/refining-rest-api-limits-for-improved-stability-and-reliability/16137 | анонс изменений лимитов | 2026-10-13 |
| 77 | https://api.openalex.org/works?per_page=1 , https://api.openalex.org/sources/issn:1083-6160 | живой запрос к API | 2026-10-13 |
| 78 | https://help.openalex.org/how-to-use-the-api/rate-limits-and-authentication | документация API | 2026-10-13 |
| 79 | https://help.openalex.org/access/pricing/ | тарифы и лицензия | 2026-10-13 |
| 80 | https://help.openalex.org/access/example-costs/ | стоимость операций | 2026-10-13 |
| 81 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=...&format=json , https://www.ebi.ac.uk/europepmc/webservices/rest/PMC7012039/fullTextXML | живые запросы к API | 2026-10-13 |
| 82 | https://europepmc.org/downloads/openaccess | описание OA-подмножества | 2026-10-13 |
| 83 | https://www.ebi.ac.uk/europepmc/annotations_api/annotationsByArticleIds?articleIds=PMC%3APMC7012039&format=JSON | Annotations API (живой запрос) | 2026-10-13 |
| 84 | https://www.semanticscholar.org/product/api | документация API | 2026-10-13 |
| 85 | https://api.unpaywall.org/v2/<DOI>?email=... (живой запрос), https://unpaywall.org/products/api | API Unpaywall | 2026-10-13 |
| 86 | https://www.elsevier.com/about/policies-and-standards/text-and-data-mining | политика TDM | 2026-10-13 |
| 87 | https://www.elsevier.com/about/policies-and-standards/text-and-data-mining/license | лицензия TDM | 2026-10-13 |
| 88 | https://solutions.acs.org/solutions/text-and-data-mining/ | услуга TDM (ACS) | 2026-10-13 |
| 89 | https://www.springernature.com/gp/researchers/text-and-data-mining | политика TDM | 2026-10-13 |
| 90 | https://cloud.google.com/blog/products/gcp/google-patents-public-datasets-connecting-public-paid-and-private-patent-data | описание датасета + атрибуция | 2026-10-13 |
| 91 | https://cloud.google.com/bigquery/docs/sandbox | бесплатные квоты BigQuery | 2026-10-13 |
| 92 | https://github.com/google/patents-public-data | репозиторий примеров (архивирован) | 2026-10-13 |
| 93 | https://ftp.ebi.ac.uk/pub/databases/chembl/SureChEMBL/bulk_data/ (README.txt, LICENCE, latest/) | bulk-данные + лицензия | 2026-10-13 |
| 94 | https://about.lens.org/policies/ | условия использования | 2026-10-13 |
| 95 | https://www.epo.org/en/searching-for-patents/data/web-services/ops | API + тарифы | 2026-10-13 |
| 96 | https://catalog.data.gov/dataset/patent-grant-full-text-1976-present | каталожная запись датасета | 2026-10-13 |
| 97 | https://api.uspto.gov/api/v1/datasets/products/ptgrxml (живой запрос, HTTP 401), https://bulkdata.uspto.gov/ (нет ответа) | проверка доступа | 2026-10-13 |
| 98 | https://api.github.com/repos/{kermitt2/grobid, docling-project/docling, datalab-to/marker, facebookresearch/nougat, pymupdf/PyMuPDF, CambridgeMolecularEngineering/chemdataextractor2, dan2097/opsin, Kohulan/DECIMER-Image_Transformer, thomas0809/MolScribe, thomas0809/RxnScribe, CrystalEye42/OpenChemIE} | лицензии репозиториев | 2026-10-13 |
| 99 | https://www.rdkit.org/docs/Cartridge.html , https://api.github.com/repos/rdkit/rdkit | документация + лицензия | 2026-10-13 |
| 100 | https://api.github.com/repos/chembl/FPSim2 | лицензия репозитория | 2026-10-13 |
| 101 | https://api.github.com/repos/rxn4chemistry/rxnmapper | лицензия репозитория | 2026-10-13 |
| 102 | https://api.github.com/repos/mrodobbe/Rxn-INSIGHT , https://api.crossref.org/works/10.1186/s13321-024-00834-z | ПО + статья | 2026-10-13 |
| 103 | https://api.github.com/repos/rsc-ontologies/rxno | онтология RXNO | 2026-10-13 |
| 104 | https://huggingface.co/api/models/{BAAI/bge-m3, nomic-ai/nomic-embed-text-v1.5, Qwen/Qwen3-Embedding-0.6B, allenai/specter2_base, intfloat/multilingual-e5-large} | лицензии моделей | 2026-10-13 |
| 105 | https://arxiv.org/abs/2005.11401 | статья (RAG) | 2026-10-13 |
| 106 | https://arxiv.org/abs/2312.05934 | статья (fine-tuning vs RAG) | 2026-10-13 |
| 107 | https://arxiv.org/abs/2405.05904 | статья (новое знание и галлюцинации) | 2026-10-13 |
| 108 | https://arxiv.org/abs/2403.01432 | статья (редкое знание) | 2026-10-13 |
| 109 | https://arxiv.org/abs/2211.08411 | статья (long-tail знание) | 2026-10-13 |
| 110 | https://arxiv.org/abs/2104.07567 | статья (retrieval снижает галлюцинации) | 2026-10-13 |
| 111 | https://api.crossref.org/works/10.1038/s41598-023-41032-5 , PubMed 37679503 | статья (выдуманные ссылки) | 2026-10-13 |
| 112 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.2196/80371 | статья (фабрикация ссылок GPT-4o) | 2026-10-13 |
| 113 | https://api.crossref.org/works/10.1038/s42256-024-00832-8 , PubMed 38799228 | статья (ChemCrow) | 2026-10-13 |
| 114 | https://api.crossref.org/works/10.1038/s41586-023-06792-0 | статья (Coscientist) | 2026-10-13 |
| 115 | https://arxiv.org/abs/2312.07559 | статья (PaperQA) | 2026-10-13 |
| 116 | https://arxiv.org/abs/2409.13740 , https://api.github.com/repos/Future-House/paper-qa | статья + репозиторий (PaperQA2) | 2026-10-13 |
| 117 | https://arxiv.org/abs/2505.07671 | статья (ChemRAG-Bench) | 2026-10-13 |
| 118 | https://api.crossref.org/works/10.1038/s41557-025-01815-x , PubMed 40394186 | статья (ChemBench) | 2026-10-13 |
| 119 | https://arxiv.org/abs/2609.05450 | препринт (верификатор маршрутов) | 2026-10-13 |
| 120 | https://arxiv.org/abs/2509.20988 | препринт (LLM + AND-OR поиск) | 2026-10-13 |
| 121 | https://arxiv.org/abs/2503.08537 | препринт (стратегическое планирование) | 2026-10-13 |
| 122 | https://arxiv.org/abs/2406.04593 | препринт (SynAsk) | 2026-10-13 |
| 123 | https://api.crossref.org/works/10.1145/1571941.1572114 | статья (RRF) | 2026-10-13 |
| 124 | https://api.crossref.org/works/10.1561/1500000019 | обзор (BM25) | 2026-10-13 |
| 125 | https://arxiv.org/abs/2104.08663 | статья (BEIR) | 2026-10-13 |
| 126 | https://www.anthropic.com/engineering/contextual-retrieval | инженерный отчёт | 2026-10-13 |
| 127 | https://arxiv.org/abs/2402.05131 | статья (структурный chunking) | 2026-10-13 |
| 128 | https://arxiv.org/abs/2309.15217 | статья (RAGAS) | 2026-10-13 |
| 129 | https://arxiv.org/abs/2305.14627 | статья (ALCE, оценка цитирований) | 2026-10-13 |
| 130 | https://arxiv.org/abs/2311.04850 | статья (контаминация, перефразировки) | 2026-10-13 |
| 131 | https://arxiv.org/abs/2310.17623 | статья (доказательство контаминации) | 2026-10-13 |
| 132 | https://api.github.com/repos/google/BIG-bench (README, canary) | практика защиты бенчмарка | 2026-10-13 |
| 133 | https://api.github.com/repos/mlcommons/croissant | формат метаданных | 2026-10-13 |
| 134 | https://api.crossref.org/works/10.1145/3458723 | статья (Datasheets for Datasets) | 2026-10-13 |
| 135 | https://api.crossref.org/works/10.1039/b602413k , PubMed 16763676 | обзор реакций процесса (Carey 2006) | 2026-10-13 |
| 136 | https://api.crossref.org/works/10.1021/jm200187y , PubMed 21504168 | обзор реакций медхимии (Roughley 2011) | 2026-10-13 |
| 137 | https://api.crossref.org/works/10.1021/acs.jmedchem.5b01409 , PubMed 26571338 | анализ методологий (Brown 2016) | 2026-10-13 |
| 138 | https://api.crossref.org/works/10.1021/acs.jmedchem.6b00153 , PubMed 27028220 | анализ патентов (Schneider 2016) | 2026-10-13 |
| 139 | https://api.crossref.org/works/10.1021/op050021j | обзор GMP-реакций (Dugger 2005) | 2026-10-13 |
| 140 | https://api.crossref.org/works/10.1038/nrd.2018.116 , PubMed 30140018 | обзор синтетического инструментария | 2026-10-13 |
| 141 | https://api.crossref.org/works/10.1021/jm501100b , PubMed 25255204 | статистика N-гетероциклов | 2026-10-13 |
| 142 | https://api.crossref.org/works/10.1021/acs.jmedchem.8b00686 , PubMed 30212196 | свойства одобренных препаратов | 2026-10-13 |
| 143 | https://api.crossref.org/works/10.1021/jm4017625 , PubMed 24471928 | статистика кольцевых систем | 2026-10-13 |
| 144 | https://api.crossref.org/works/10.1021/acsomega.0c00830 , PubMed 32455181 | статистика фторсодержащих | 2026-10-13 |
| 145 | https://api.crossref.org/works/10.1021/acs.jmedchem.3c02239 , PubMed 38344815 | статистика хиральности одобрений | 2026-10-13 |
| 146 | https://api.crossref.org/works/10.1039/C9SC04944D , Europe PMC PMC7012039 | влияние датасетов на CASP | 2026-10-13 |
| 147 | https://api.crossref.org/works/10.1186/s13321-017-0225-z , PubMed 29086048 | алгоритм функциональных групп | 2026-10-13 |
| 148 | https://api.crossref.org/works/10.1021/ci5006614 | отпечаток и классификация реакций | 2026-10-13 |
| 149 | https://api.crossref.org/works/10.1021/acs.jmedchem.6c00287 | ежегодная серия обзоров синтезов | 2026-10-13 |
| 150 | https://api.crossref.org/works/10.1038/nature11117 , https://api.crossref.org/works/10.1021/acs.oprd.8b00232 | обзоры биокатализа | 2026-10-13 |

---

## 1. Инвентаризация датасетов

### 1.1. Реакции

| Датасет | Содержимое, объём, версия | Лицензия | Открытый бенчмарк? | Доступ | Роль в проекте |
|---|---|---|---|---|---|
| **USPTO (Lowe) full** | реакции, извлечённые текст-майнингом из патентов США 1976–Sep2016; CML и reaction SMILES; grants **1 808 937** реакций, applications **1 939 253** **[подсчёт]**; уникальных строк с атом-маппингом 1 105 130 и 1 119 744 **[подсчёт]**; v1 от 2017-06-13 [1] | **CC0** [1], подтверждено вендором [2] | **Да** | figshare (bulk, 7z) [1] | база для обучения/оценки шаблонных моделей; источник шагов для сверки с эталонами |
| **USPTO-50K** | 50 016 реакций, 10 классов (распределение от 230 до 15 151 на класс) **[подсчёт]**; стандартный сплит 40 008/5 001/5 007 [3][6]; копия в репозитории retrosim (MIT), статья JCIM 2016 [4] | производная от CC0; собственная лицензия набора — **не подтверждено** | **Да, вероятно** | GitHub [3] | one-step-модели, сравнение с опубликованными метриками |
| **USPTO-MIT** | полностью картированные реакции из grants; README: «480K»; точно **479 035** = 409 035/30 000/40 000 [5]; в ORD как конфиг `uspto-mit` [8] | MIT (репозиторий) [5]; в ORD — CC BY-SA 4.0 [7] | **Да** | GitHub, ORD/HF [5][8] | прямая предсказательная задача, валидация реакций |
| **USPTO-FULL** | ~1 млн уникальных реакций из 1 808 937 сырых; сплит 800k/100k/100k [6]; 2019 | MIT (репозиторий GLN) [6] | **Да, вероятно** | Dropbox через репозиторий [6] | полномасштабное обучение шаблонов |
| **Open Reaction Database (ORD)** | структурированные записи реакций (protobuf `Reaction`), включая роли, выходы, ссылку на первоисточник; **53** Parquet-датасета, суммарно **2 428 291** реакции (uspto-grants 1 771 032 + USPTO-MIT 479 035 как подмножество тех же грантов + 178 224 прочие) **[подсчёт]** [8]; реорганизация 2026-08-30, 499 ID выведены из обращения [7] | данные **CC BY-SA 4.0**, код Apache-2.0 [7]; `ord-schema` 0.9.2 [9]; описание формата — JACS 2021 [10] | **Да, но ShareAlike**: производный датасет обязан выходить под CC BY-SA 4.0 (наш вывод) | git clone, `scripts/download_from_huggingface.py`, HF, `pip install ord-schema` [7][9] | основной структурированный источник `literature`-статуса; ключ по InChIKey; внутри есть HTE-наборы (например Buchwald–Hartwig 4 312, Suzuki 5 760, Pfizer HTE 39 347, C–N ultra-HTE 50 688, амиды 47 015, Chan-Lam 9 632) **[подсчёт]** [8] |
| **ORDerly** | очищенные производные ORD: forward 919 077, retro 939 648, condition 258 273 / 691 142, non-USPTO 29 417 / 23 334; срез ORD на 2024-02-20 [11] | датасеты заявлены **CC BY 4.0**, пакет MIT [11] | **с оговоркой**: CC BY 4.0 поверх ORD (CC BY-SA 4.0) — возможный конфликт ShareAlike, нужна юридическая проверка (наш вывод) | figshare, `pip install orderly` [11] | готовая очистка и стандартизация вместо собственной |
| **PaRoutes** | два набора по **10 000** многостадийных маршрутов из патентов + стоки и шаблоны; stock_n1 **13 432**, stock_n5 **13 328** молекул **[подсчёт]**; selected_reactions_all.csv ≈3,26 ГБ [12] | данные **CC BY 4.0** (Zenodo v1 2022-02-25, v2 «PaRoutes 2.0» 2022-11-22), код Apache-2.0; статья CC BY-NC 3.0 [12] | **Да** | Zenodo, GitHub [12] | эталон для метрик многостадийного поиска; референс распределения длин маршрутов; источник целей-прокси |
| **Pistachio** (NextMove) | реакции из патентов US и EPO; «over 21 million chemical reactions», версия 2026-06-30 (2026Q2) [13]; на практике 15,6 млн сырых / 3,4 млн после обработки [24] | коммерческая; текст лицензии и условия ML — **не подтверждено** [13] | **Нет** без отдельной лицензии | подписка | только как внешний ориентир; «most researchers do not have access» [24] |
| **Reaxys** (Elsevier) | «1B+ chemistry data points», «over 70 million reactions», «420,000+ expert rules» [14]; без даты на страницах | коммерческая; массовый доступ «via MCP, API or flat file as a separate license» [14]; TDM-политика Elsevier покрывает только полные тексты ScienceDirect [86][87] | **Нет**: разрешает ли университетская подписка массовый экспорт и обучение ML — **не подтверждено** | подписка | не используем как источник данных бенчмарка |
| **CAS** | «More than 150 million single- and multi-step reactions… since 1840» [15]; — | **Information Use Policy (07/12/2024) прямо запрещает** сбор данных «For the purposes of machine learning… or any other artificial intelligence purposes», ограничивает хранение (≤5 000 Records и 5 000 Molfiles) и запрещает интернет-редистрибуцию [15] | **Нет** | подписка | исключён из конвейера по лицензии |
| **RetroBioCat** | правила биокаталитических реакций: **99** именованных правил в rxns_yaml.yaml **[подсчёт]**; building_blocks.db (eMolecules, ZINC in-stock, MolPort) [16] | figshare v7 (2023-12-31) **CC BY 4.0**; код MIT [16] | **Да** (файлы figshare) | figshare, GitHub [16] | генерация биокаталитических альтернатив стадиям; разметка «biocatalysis candidate» |
|  | данные о литературных прецедентах; — | «available on request»; закрытые версии лицензируются через Disyn Biotec [16] | **Нет** | по запросу | — |
| **EnzymeMap** | 63 137 уникальных картированных реакций в пределах EC-класса; 47 974 без учёта EC; 234 845 записей с организмом/белком [17] | Zenodo v2 **CC BY 4.0**; код MIT [17] | **Да** | Zenodo [17] | ферментативные шаблоны, картирование |
| **ECREACT** | 62 222 уникальных комбинаций «реакция — EC» (PathBank 27 835, MetaNetX 19 176, BRENDA 8 496, Rhea 6 715) **[подсчёт]** [18] | репозиторий MIT; отдельной лицензии на данные нет [18]; источник BRENDA — CC BY 4.0 [19] | **Да, вероятно** (лицензии PathBank и MetaNetX не проверены) | GitHub [18] | биокатализ как альтернатива стадии |
| **mech-USPTO-31K** (2024) | 31 364 реакции с разметкой механизмов (MechFinder) [20] | figshare **CC BY 4.0** | **Да** | figshare [20] | объяснимость, проверка осмысленности шага |
| **SynRXN** (2026) | консолидированный набор реакций, включает USPTO_50k (50 016) и ECREACT; статья Sci Data 2026 [21] | репозиторий/Zenodo Apache-2.0, в статье теги CC BY 4.0 по поднаборам [21] | **Да, вероятно** (разнородные теги лицензий) | GitHub, Zenodo, `pip install synrxn` [21] | свежая унифицированная разметка; экономит собственную очистку |
| **CRD 1.37M** (2025) | «1.37M lines» из USPTO 1976–2024 + ~2,5% академической литературы; автор признаёт наличие ошибок [22] | figshare **CC BY 4.0** | **Да, с осторожностью** | figshare [22] | расширение покрытия, только после собственной валидации |
| **Retro\* / USPTO-190** | 299 202 обучающих маршрута, 65 274 валидационных, 189 (у Syntheseus — 190) тестовых целей; ~380K шаблонов [24] | репозиторий MIT [24] | **Да, вероятно** | Dropbox через репозиторий [24] | второй набор целей многостадийного поиска |
| **Syntheseus** (ПО + чекпойнты) | унифицированный интерфейс одностадийных моделей и алгоритмов поиска; статья Faraday Discuss. 2024 [23] | ПО **MIT**, PyPI 0.9.0 (2026-09-23); часть чекпойнтов обучена на Pistachio, лицензия наследуется от модели [23] | ПО — да; чекпойнты на Pistachio — **проверять отдельно** | GitHub, PyPI [23] | базовая линия B1 «шаблонный ретросинтез без LLM» |
| **AiZynthFinder** (ПО + публичные модели) | ONNX-модели (expansion, ringbreaker, filter) и шаблоны: USPTO **42 554**, ringbreaker **5 282** **[подсчёт]** (в статье «about 45,500») [25] | ПО **MIT**, PyPI 4.4.1 (2025-12-09); модели Zenodo **CC BY 4.0**; сток figshare — MIT [25] | **Да** | `download_public_data`, Zenodo, figshare [25] | основной ретросинтетический движок проекта |
| **ASKCOS v2** (ПО + модели) | код и веса; CAS-модели доступны только членам MLPDS, Reaxys-модель под CC BY-NC 4.0 [26] | код **MIT** [26] | ПО — да; отдельные модели — нет | GitLab [26] | второй движок для сравнения стратегий |

### 1.2. Молекулы, препараты, регуляторные данные

| Источник | Содержимое и объём | Версия/дата | Лицензия и условия | Доступ и лимиты | Роль |
|---|---|---|---|---|---|
| **PubChem** | Compounds **124 663 543**, Substances **349 330 330**, Patents **82 942 034**, Literature **45 802 641**, Data Sources **1 131** [33] | счётчик соединений от 2026-09-27, патентов от 2026-09-04 [33] | лицензия определяется источником данных; «Exceptions may exist where licensing agreements prevent… bulk downloads» [32]; NCBI «places no restrictions on the use or distribution of the data», но депозиторы «may claim patent, copyright…» [34]; по LCSS: «we are not able to give unconditional permission for reuse» [31] | PUG-REST: **≤5 запросов/с**, таймаут 30 с, «We cannot offer API keys or whitelists to exceed these limits» [27]; заголовок `X-Throttling-Control`, при превышении 503 и временная блокировка [28]; для объёмов — FTP (CID-SMILES.gz 1,4 ГБ, CID-InChI-Key.gz 6,9 ГБ, CID-Synonym-filtered.gz 931 МБ, CID-Patent.gz 6,1 ГБ, CID-LCSS.xml.gz 456 МБ) [32] | МНН/синоним → CID → `SMILES`/`ConnectivitySMILES`/`InChIKey` [29]; патентные перекрёстные ссылки (`/xrefs/PatentID`) [29]; GHS-классификация и LCSS через PUG-View (один CID на запрос; у каждой ссылки есть `LicenseNote`/`LicenseURL`) [30][31] |
| **ChEMBL** | 2 921 148 соединений, 24 527 044 активности, 18 552 цели; источники с «одними соединениями»: INN 10 742, USAN 8 230, ATC 3 488, Orange Book 2 258, EMA 1 046, Withdrawn Drugs 327 [35] | **ChEMBL 37**, release 2026-05-01 [35] | **CC BY-SA 3.0**, требование сохранять ChEMBL ID и номер релиза [35] | REST API `https://www.ebi.ac.uk/chembl/api/data/<resource>`, клиент `chembl_webresource_client`, FTP-дампы; лимиты API на странице не указаны [35] | ядро отбора: `max_phase=4` даёт **4 225** молекул (из них **3 475** small molecule), endpoint `drug` — **2 996** (агрегирован по parent); синонимы с `syn_type=INN` — **11 211** (живые запросы) [35]. Важно: `withdrawn_flag=true` при `max_phase=4` — **364** молекулы, то есть отзыв не снимает статус [35]; в ChEMBL 36 часть ATC/BNF-соединений была понижена ниже 4, в 37 вручную возвращено 169 [35] |
| **WHO INN** | записи с латинским/английским/французским/испанским названием, химическим названием, классом, брутто-формулой, CAS RN, структурой [36] | Proposed **PL 135** (публикация 2026-07-20, срок возражений 2026-11-20), Recommended **RL 96** (2026-09-29); Cumulative List No. 17 (2017) только на CD-ROM [36] | по WHO: «Since the name is available in the public domain it may be used freely» (о recommended INN); условия сайта допускают воспроизведение для «research or private study» со ссылкой, но «not for sale or… commercial purposes» [36] | только PDF; MedNet/SoINN — по логину, «free of charge to its members» [36] | справочник МНН для входного гейта и нормализации запроса. Число INN: на странице WHO «some 7000 names» (страница старая, 2017), что расходится с 10 742 записями источника INN в ChEMBL 37 — это разные метрики [35][36] |
| **DrugBank** | полный датасет; Open Data (Vocabulary CSV 1,12 МБ, Open Structures SDF 5,16 МБ) [37] | 5.1.22 (2026-06-27) [37] | полный датасет **CC BY-NC 4.0** (академическая лицензия бесплатна при условиях «student, professor, or research associate» и «solely for academic purposes»); ToU запрещают «create derivative works of the Databases», «distribute, publish», «develop another database of drug information»; Open Data — **CC0** [37] | аккаунт; **на 2026-10-13 все академические загрузки, включая Open Data, помечены «Temporarily unavailable»** [37] | не используем в публикуемом датасете; максимум — сверка идентификаторов из Open Data (CC0) |
| **FDA Orange Book** | Products.txt, Patent.txt, Exclusivity.txt (ASCII, разделитель `~`); поля `Patent Expire Date` (с продлениями), Drug Substance/Product Flag, `Exclusivity Code`, `Exclusivity Date` [38] | «Content current as of 08/18/2026»; файлы обновляются **ежемесячно** [38] | контент сайта FDA «in the public domain» [38] | ZIP-выгрузка + openFDA Orange Book API [38][46] | критерий «вне патентной защиты» (справочно, SAFE-005) |
| **Drugs@FDA** | 12 таблиц с табуляцией (Products, Applications, Submissions, MarketingStatus, TE, ApplicationDocs…) [39] | обновление **каждое утро по будням** [39] | public domain [38] | ZIP-выгрузка [39] | подтверждение факта одобрения, даты, тип заявки |
| **EMA** | таблицы xlsx + полный JSON сайта; medicines JSON — **2 748** записей, human **2 351**, из них Authorised **1 568** **[подсчёт]**; поля `international_non_proprietary_name_common_name`, `active_substance`, `atc_code_human`, `medicine_status`, `medicine_url` (EPAR) [40] | JSON-отчёт с timestamp 2026-10-13T06:02:34Z; обновления дважды в день (06:00 и 18:00 CET) [40] | «may be reproduced and / or distributed… provided that EMA is always acknowledged», включая коммерческое использование; не распространяется на контент третьих лиц [40] | xlsx, JSON-фиды [40] | второй регулятор для фильтра F1; EPAR как документы для RAG |
| **ГРЛС** | по 61-ФЗ ст. 33 реестр содержит для препаратов МНН/группировочное/химическое и торговое наименование, держателя РУ; для фармсубстанций — наименование, производителя и адрес, срок годности, условия хранения, номер ФС или НД, **отметку о включении в перечень НС/ПВ/прекурсоров** [41] | данные на 2026-10-13 [41] | условия переиспользования не опубликованы; `robots.txt`: `User-agent: * Disallow: /` — **автоматический обход запрещён** [41] | только веб-поиск; кнопки экспорта в Excel нет; есть форма заявки на доступ к БД; страница открытых данных Минздрава «находится на доработке» [41] | **в автоматический конвейер не берём** (DATA-003). Используем вручную как справку о регистрации в РФ; возможный путь — официальная заявка на доступ |
| **Регуляторные перечни** (входной гейт, SAFE-003) | INCB Yellow List (65-е изд., Updated July 2026), Green List (36-е изд., Updated December 2025 + PDF новых веществ CND March 2026), Red List (23-е изд., Updated July 2025) [42]; ПП РФ от 30.06.1998 № 681 (последнее изменение в редакции Garant — 11.06.2025) [43]; 21 CFR 1308 (Title 21 актуален на 2026-10-08, часть изменена 2026-10-06) [44]; алфавитный перечень DEA (PDF, 27-Aug-26) [44]; перечни КЗХО через OPCW SCDB версии 2026 («up to 35,941 scheduled chemicals», в Handbook 2 255) [45] | см. колонку | публикации международных организаций и нормативные акты | INCB и DEA — PDF; 21 CFR — eCFR API (XML/JSON); OPCW — онлайн-база (bulk-выгрузка **не подтверждена**); ПП 681 — HTML, официальный машиночитаемый формат **не подтверждён** | только как **данные** для fail-closed-фильтра входа и исключения из бенчмарка; хранятся с источником и датой версии, обновление через PR (SAFE-003) |
| **openFDA** | API поверх данных FDA; в `drug/drugsfda` есть `openfda.unii`, `substance_name` [46] | meta last_updated 2026-10-09 [46] | public domain, CC0 1.0 «unless otherwise noted» [46] | без ключа **240 req/min и 1 000/день** на IP; с ключом **240 req/min и 120 000/день** [46] | автоматизация фильтров F1/F4 |
| **DailyMed (SPL)** | этикетки с активными ингредиентами и UNII; ресурс `/uniis` [47] | ежедневные обновления (на 2026-10-12) [47] | — | REST + полные zip-релизы [47] | сопоставление МНН ↔ UNII ↔ структура |
| **GSRS / UNII** | UNIIs.zip и UNII_Data.zip с полями SMILES, INCHIKEY, RXCUI, PUBCHEM, **INN_ID**; **171 917** различных UNII **[подсчёт]**; в README пометка «This adaptation was not created by WHO» [48] | архив обновлён 2026-08-04 [48] | явного заявления о public domain на страницах GSRS/precisionFDA — **не подтверждено** (есть только общая политика fda.gov) [48] | zip-выгрузка [48] | мост «регуляторный идентификатор ↔ структура», важен для надёжного разрешения МНН |
| **RxNorm** | нормализованные наименования ЛС | Full Monthly Release 2026-10-05 [49] | для полного релиза нужна бесплатная **UMLS-лицензия**; имена и коды, созданные NLM, — public domain; Current Prescribable Content — «no license required» [49] | файлы + RxNav API: ≤20 req/s на IP, до 100 req/s с ключом UTS [49] | дополнительная нормализация синонимов (сопоставление с INN как функция — **не подтверждено**) |

### 1.3. Покупаемые блоки и стоки

| Источник | Объём | Версия/дата | Лицензия и ограничения | Доступ | Роль |
|---|---|---|---|---|---|
| **ZINC20** | 1,4 млрд соединений, 1,3 млрд покупаемых (310 каталогов, 150 компаний); in-stock Ro4.0 **6 136 700**; подмножества BB: BB-Now 1,6 млн, BB-All 26,7 млн (2020Q2) [50] | статья 2020 [50] | «ZINC is free to use and download for everyone»; «You may not redistribute major portions of ZINC without the written permission»; T&C датированы 2025-03-21 [52] | транши, CartBlanche, S3/Globus [51] | базовый сток доступности |
| **ZINC-22** | >37 млрд соединений в 2D, >4,5 млрд в 3D (источники: Enamine REAL, WuXi, Mcule, ZINC20 in-stock) [51] | статья 2023; текущий размер — **не подтверждено** | как выше [52] | cartblanche22.docking.org, S3/OCI/Globus [51] | сток make-on-demand (помечать отдельно от in-stock) |
| **eMolecules (free)** | version.smi.gz 350 МБ = **33 704 595** строк **[подсчёт]**; version.sdf.gz 6,6 ГБ; free-extended quote_bb.tsv.gz = **6 937 451** строка с tier и средней ценой за грамм **[подсчёт]** [53] | каталог 2026-10-01 [53] | ToS: «for your personal use only», экспорт ≤10 000 за выгрузку и ≤100 000 за 24 ч; отдельной лицензии на free-файлы нет [53] | HTTP-выгрузка по месяцам [53] | сток + грубая оценка цены (tier) |
| **Enamine building blocks** | Comprehensive Catalog **2 850 684**; Global Stock 1 173 520; US Stock 290 648; EU Stock 57 916; MADE BB 1,35 млрд; REAL >13,6 млрд [54] | каталог «September 2026» [54] | **ToU v8 §15.2 запрещает использовать, обрабатывать и моделировать Enamine Data (AI/ML, QSAR, хемоинформатика) без письменного разрешения**; §3.2 — републикация только с согласия [54] | SD-файлы по ссылкам [54] | **в автоматический конвейер не берём** без письменного разрешения; при необходимости — запрос лицензии |
| **MolPort** | HF: In-stock BB **1 258 272** строки, In-stock DB **6 307 515**; FTP: BASIC/PROFESSIONAL, full >47 млн (только SMILES) [55] | HF-датасеты обновляются ежемесячно [55] | HF-датасеты **CC BY-NC 4.0**, только внутреннее некоммерческое использование, перепродажа и редистрибуция запрещены; FTP требует корпоративный/университетский email [55] | HF, FTP [55] | альтернативный сток (NC-ограничение фиксируем в карточке датасета) |
| **Mcule** | Full **140 551 087**; In Stock **7 072 929**; Full BB **7 362 728**; Fast Delivery BB по классам 0–5 [56] | страницы 20–27.09.2026 [56] | загрузка «для собственных бизнес-целей», передача третьим лицам запрещена; §2.8 запрещает автоматизированный сбор данных [56] | выгрузки с сайта [56] | резервный сток |
| **Сток AiZynthFinder** | zinc_stock_17_04_20.hdf5, 663 232 280 Б, **17 422 831** запись **[подсчёт]** (фрагментные транши ZINC, MW ≤ 250, logP ≤ 3,5) [25] | figshare 2020-06-11 [25] | **MIT** (запись figshare) [25] | `download_public_data` [25] | сток по умолчанию; ключ поиска — InChIKey; свой сток собирается `smiles2stock` (HDF5/CSV/txt с колонкой `inchi_key`) [57] |
| **Стоки PaRoutes** | stock_n1 **13 432**, stock_n5 **13 328** **[подсчёт]** [12] | 2.0 (2022-11-22) [12] | **CC BY 4.0** [12] | Zenodo [12] | воспроизводимые метрики на PaRoutes |
| **ASKCOS buyables** | документация: «approximately 280,000 database entries from eMolecules, LabNetwork, and Sigma Aldrich» [58]; статья: «a few hundred thousand molecules from eMolecules, Sigma Aldrich, LabNetwork, Mcule, and ChemBridge» [26] | 2025–2026 | код MIT; точный состав данных — **не подтверждён** | GitLab/документация [26][58] | сравнение «доступности» между движками |

### 1.4. Процессные и зелёно-химические справочные данные

| Источник | Что содержит | Версия/дата | Переиспользование | Роль |
|---|---|---|---|---|
| **ICH Q3C(R9)** | классы растворителей и пределы: Class 1 — 5 веществ (ppm), Class 2 — 31 вещество (PDE мг/сут и ppm), Class 3 — 27 веществ (до 50 мг/сут ≈ 5000 ppm), Table 4 — 9 веществ без токсикологических данных; пересчёт Option 1: ppm = 1000 × PDE / доза при 10 г/сут [59] | Step 4 — 2024-01-24; в ЕС действует с 2024-04-29 (R8 — 2021-04-22, R6 — 2016-11-09) [59] | PDF EMA: «Reproduction is authorised provided the source is acknowledged»; ICH допускает использование, воспроизведение, адаптацию и распространение при указании копирайта ICH с пометкой изменений (логотип и материалы третьих лиц не покрываются) [59][60] | детерминированная проверка растворителей в маршруте; цитаты в отчёте |
| **ICH Q3D(R2)** | классы элементов 1 / 2A / 2B / 3 и PDE (мкг/сут) по путям введения (oral/parenteral/inhalation), Appendix 5 — кожный и транскутанный путь | принято 2022-04-26; в ЕС с 2022-09-24; ревизии новее R2 на EMA нет [60] | как выше [60] | проверка металлокатализаторов и элементных примесей |
| **ICH M7(R2)** | подход к мутагенным примесям, TTC 1,5 мкг/сут | принято 2023-04-03; в ЕС с 2023-09-30 [61] | как выше [61] | флаг «потенциально мутагенная примесь» на уровне класса |
| **ICH Q11 + Q&A** | принципы разработки и описания производства субстанции; Q&A посвящён выбору и обоснованию исходных материалов | Q11 в ЕС с 2012-11-01; Q&A (EMA/CHMP/ICH/809509/2016) с 2018-02-28 [62] | как выше [62] | критерий «где начинается регулируемая часть маршрута» для оценки осмысленности |
| **CHEM21 solvent selection guide** | оценки Safety/Health/Environment 1–10, цветовые полосы, категории Recommended / Problematic / Hazardous / Highly hazardous; ≈77 растворителей; Excel в SI для ранжирования новых растворителей [63][64] | Green Chem. 2016, 18, 288–296 (online 2015-08-13) [63] | статья — CC BY-NC (hybrid, по данным индекса); таблицы © RSC, перепечатка требует разрешения RSC [63][64] | ранжирование растворителей в метриках «зелёности» |
| Другие гайды | Prat 2014 (обзор гайдов), Sanofi 2013 (4 класса от recommended до banned), GSK 2016 (154 растворителя, 44 новых), GSK 2011, Pfizer 2008, Byrne 2016 (открытый доступ, CC BY 4.0) [65] | 2008–2016 | большинство закрыты; открыт Byrne 2016 [65] | кросс-проверка классификаций |
| **ACS GCI Pharmaceutical Roundtable** | PMI Calculator (.xls), Convergent PMI (.xlsx), PMI-LCA, PMI Prediction Calculator (веб), Solvent Tool v2.0.0 (272 растворителя, PCA по 70 свойствам), 28 Reagent Guides, Biocatalysis Guide, AMGS [66] | Solvent Tool — 11.2019; страницы 2026 [66] | Reagent Guides: «© GCI Pharmaceutical Roundtable. All rights reserved»; факт скачивания .xls через скрипт **не подтверждён** (бот-заглушка) [66] | эталонные определения PMI и методики расчёта [67][68][69] |
| **GHS и опасности** | PubChem агрегирует ECHA C&L, EU CLP 1272/2008, NITE-CMC, Safe Work Australia HCIS, HSDB (для одного вещества — сводка по тысячам нотификаций); раздел GHS Classification в PUG-View насчитывает 359 страниц аннотаций [70] | живые запросы 2026-10-13 [70] | лицензия хранится у каждой записи: ECHA (как передаёт PubChem) «may be reproduced, distributed and/or used… **for non-commercial purposes** provided that ECHA is acknowledged»; EU CLP/EUR-Lex — CC BY 4.0 [70]; GESTIS (~8 800 веществ) запрещает коммерческое использование и перенос в другие системы [71]; CAMEO Chemicals (v3.1.0 rev 1) бесплатен, но данные третьих сторон нельзя дублировать [72]; Bretherick's — коммерческое издание [73] | флаги опасности на уровне класса, с сохранением лицензии каждой записи |

### 1.5. Литература и патенты

| Источник | Что даёт | Лимиты и доступ | Лицензия | Роль |
|---|---|---|---|---|
| **Crossref REST** | метаданные, DOI-резолвинг, ссылки на лицензии и полные тексты | лимиты (страница от 2025-10-16): public — 5 запросов и concurrency 1; polite (`mailto`) — 10 и 3; Plus — 150 без ограничения concurrency [74]; с 2025-12-01 введено разделение по типам запросов (одиночная запись против списков) [76]; заголовки `x-rate-limit-*` | «almost none of the metadata is subject to copyright, and you may use it for any purpose»; оговорка: «Some abstracts… may be subject to copyright» [75] | проверка существования DOI (TRUST-004), сбор кандидатов, лицензии статей (например, по журналу OPRD: 7 069 DOI, из них CC BY 197 — живой запрос) |
| **OpenAlex** | **326 806 755** работ (живой запрос) [77] | без ключа 10 запросов/с и бюджет **$0,10/день**; бесплатный ключ — 30/с и **$1/день**; годовой план — 50/с; семантический поиск 1/с; стоимость: singleton бесплатно, list+filter $0,10 за 1000, поиск $1 за 1000, скачивание контента $10 за 1000 [78][79][80] | данные **CC0** [79] | даты публикаций для временного срезa контаминации, обогащение метаданных |
| **Europe PMC** | живые счётчики: IN_EPMC **12 147 276**, OPEN_ACCESS **8 311 508**, из них с CC BY/CC0 **5 398 009**, патентные записи SRC:PAT **4 229 296** [81]; `fullTextXML` работает (проверено); Annotations API возвращает аннотации Chemicals/GO/Organisms с указанием секции, но содержит ложные срабатывания [83] | REST, bulk OA, OAI; явных лимитов на странице нет [81][82] | OA-подмножество: статьи «still protected by copyright, but… available under a Creative Commons license… license terms are not identical for all articles» [82] | главный источник **машиночитаемого полного текста OA**. Ограничение: профильная процессная химия почти не покрыта — по журналу OPRD в Europe PMC всего **191** запись (142 OA) против 7 069 DOI в Crossref [81] |
| **Semantic Scholar** | 214 млн статей, 2,49 млрд цитирований; датасеты S2ORC/S2AG | без ключа — общий пул «1000 requests per second… shared among all unauthenticated users»; с ключом вводный лимит **1 RPS** [84] | API License Agreement (отдельный документ) [84] | поиск кандидатов, контексты цитирований |
| **Unpaywall** | статус OA и ссылки (`best_oa_location`, `license`) — проверено живым запросом [85] | требуется параметр `email`; лимит 100 000 вызовов/день — **не подтверждено напрямую** (страница не отдала текст) [85] | лицензия данных — **не подтверждено** | легальный путь к PDF OA-версий |
| **Elsevier TDM** | полные тексты ScienceDirect | только исследователи подписывающих академических организаций, некоммерческие цели, персональный API-ключ [86] | фрагменты из одной статьи — **не более 200 символов**, с DOI-ссылкой; запрещено «Substantially or systematically reproduce, retain or redistribute the Dataset» [87] | источник текстов для RAG при наличии подписки; **в индексе храним только короткие цитаты** |
| **ACS TDM** | полные тексты ACS (включая OPRD) | платная услуга «TDM customers», стоимость зависит от объёма и срока; условия не опубликованы [88] | — | ключевой профильный источник; требуется решение кураторов и/или библиотеки ИТМО |
| **Springer Nature TDM** | метаданные, OA-полные тексты, по лицензии — закрытые | через подписку организации для некоммерческих исследований; прямая загрузка — **1 запрос/с**; TDM API с ключом — **150 запросов/мин**, «incurs additional costs»; хранить на защищённом внутреннем сервере «without access for third parties» [89] | — | дополнение покрытия |
| **Google Patents Public Data (BigQuery)** | «worldwide bibliographic information on more than 90 million patent publications from 17 countries and US full text, provided by IFI CLAIMS Patent Services» [90] | BigQuery sandbox: **1 TiB** обработанных запросов в месяц и 10 GiB хранения [91] | атрибуция «"Google Patents Public Data" by IFI CLAIMS Patent Services and Google, used under **CC BY 4.0**» [90]; репозиторий примеров Apache-2.0, архивирован 2026-04-18 [92] | масштабный отбор патентов-кандидатов SQL-запросами |
| **SureChEMBL** | химия и биомедицинские сущности из полнотекстовых патентов пяти ведомств (WIPO, USPTO, EPO, JIPO, CNIPA); bulk-снапшоты каждые две недели; latest (2026-10-06): compounds.parquet 3,9 ГБ, patents.parquet 5,6 ГБ, patent_compound_map.parquet 4,7 ГБ, fpsim2_fingerprints.h5 1,3 ГБ [93] | FTP EBI, публичный API [93] | **CC BY 4.0** (файл LICENCE и README) [93] | связка «структура ↔ патент», готовые фингерпринты для структурного поиска |
| **Lens.org** | научные и патентные данные | бесплатный доступ для личного некоммерческого использования; API по отдельным условиям; краулеры запрещены [94] | условия данных построены по модели **CC BY-NC-SA**, требуется атрибуция и сохранение Lens ID; ToU v2026.06.01 [94] | только интерактивные проверки, не для публикуемого датасета |
| **EPO OPS** | библиография, правовые события, полные тексты, изображения через XML-интерфейс | регистрация + OAuth; бесплатно **до 4 ГБ в неделю**; платный план — EUR 2 800/год [95] | Fair use charter + Terms and conditions [95] | получение полных текстов EP-документов |
| **USPTO** | «Patent Grant Full Text (1976–present)»: полный текст каждой недельной выдачи без изображений; точка доступа `data.uspto.gov/bulkdata/datasets/ptgrxml` [96] | ODP API без ключа отвечает `401 Unauthorized` (живая проверка), `bulkdata.uspto.gov` не отвечает [97] | **Creative Commons Public Domain Mark 1.0** (каталожная запись, обновлена 2025-08-28) [96] | основной массив патентных полных текстов США |

### 1.6. Инструменты обработки и поиска (лицензии проверены по репозиториям)

| Инструмент | Назначение | Лицензия |
|---|---|---|
| GROBID | структурный разбор научных PDF в TEI | Apache-2.0 [98] |
| Docling | разбор PDF/DOCX/HTML в структурированный формат | MIT [98] |
| Marker | PDF → Markdown | код Apache-2.0, **веса — модифицированная OpenRAIL-M** (бесплатно для исследований и компаний с доходом/финансированием < $5 млн) [98] |
| Nougat | OCR научных документов | код MIT, **веса CC-BY-NC** [98] |
| PyMuPDF | извлечение текста и структуры | **AGPL-3.0** (несовместима с Apache-2.0-дистрибуцией без оговорок) [98] |
| ChemDataExtractor 2 | извлечение химических сущностей из текста | MIT (по файлу LICENSE; GitHub-метка NOASSERTION) [98] |
| OPSIN | химическое название → структура | MIT [98] |
| DECIMER, MolScribe, RxnScribe, OpenChemIE | распознавание структур и схем на изображениях | MIT [98] |
| RDKit (+ PostgreSQL cartridge) | химия, канонизация, отпечатки, подструктурный (`@>`) и similarity-поиск (`%`, `<%>`) в SQL | BSD-3-Clause; документация CC BY-SA 4.0 [99] |
| FPSim2 | быстрый similarity-поиск | MIT [100] |
| rxnmapper | атом-маппинг реакций | MIT [101] |
| Rxn-INSIGHT | детерминированная классификация и наименование реакций | MIT; статья J. Cheminform. 2024 [102] |
| RXNO | онтология именных реакций | **CC BY 4.0** [103] |
| bge-m3 / multilingual-e5-large | эмбеддинги (в т. ч. многоязычные) | MIT [104] |
| nomic-embed-text-v1.5 / Qwen3-Embedding-0.6B / specter2_base | эмбеддинги, в т. ч. для научных текстов | Apache-2.0 [104] |

**Вывод по лицензиям.** Публикуемое ядро бенчмарка собираем только из CC0/CC BY/CC BY-SA/public-domain источников: USPTO (Lowe) [1], ORD [7], PaRoutes [12], SureChEMBL [93], USPTO ODP [96], Google Patents Public Data [90], ChEMBL [35], PubChem (с оговорками по депозиторам) [32][34], FDA [38][39], EMA [40], ICH (с указанием источника) [59]. Данные с NC- или anti-ML-ограничениями (CAS [15], Enamine [54], MolPort на HF [55], DrugBank [37], GESTIS [71]) либо не используются, либо используются только интерактивно, без включения в публикуемые артефакты (DATA-003).

---

## 2. Дизайн бенчмарка: отбор 30–50 препаратов

Конкретные препараты и их маршруты в этом документе не перечисляются: фиксируются только критерии, источники и процедура. Итоговые списки формируются скриптом и живут в `eval/benchmark/` (тест-сплит заморожен, EVAL-002).

### 2.1. Воронка отбора

| Фильтр | Критерий | Формализация | Источник |
|---|---|---|---|
| F1 | одобрен | `max_phase = 4` в ChEMBL **и** подтверждение хотя бы одним регулятором | ChEMBL [35], Drugs@FDA [39], EMA JSON [40], ГРЛС вручную [41] |
| F2 | есть МНН | синоним с `syn_type = INN` либо запись в списках WHO | ChEMBL [35], WHO INN [36] |
| F3 | однозначная малая молекула | одна родительская структура после снятия солей и сольватов, есть InChIKey; исключаются металлокомплексы, полимеры, смеси, длинные пептиды, олигонуклеотиды, биопрепараты и изотопно-меченые | ChEMBL `molecule_type` [35], PubChem [29], RDKit [99] |
| F4 | вне патентной защиты (справочно) | нет действующих записей в Patent.txt и Exclusivity.txt на дату выгрузки | Orange Book [38] |
| F5 | хорошо документирован | не менее двух независимых открытых источников, у которых структуры всех промежуточных веществ восстановимы; приоритет тем, чьи шаги присутствуют в ORD или USPTO (есть атом-маппинг) | Crossref [75], OpenAlex [77], Europe PMC [81], SureChEMBL [93], ORD [7], PaRoutes [12], ежегодная серия обзоров синтезов [149] |
| F6 | исключение контролируемых веществ по построению | идентификаторы целевого вещества и всех веществ эталонного маршрута сверяются с перечнями; при любой неопределённости препарат исключается (fail-closed) | перечни как данные [42][43][44][45]; отметка в ГРЛС [41] |
| F7 | структурное разнообразие | MaxMin-отбор по каркасам Bemis–Murcko и кольцевым системам, не более одного препарата на кластер в тесте; балансировка по ATC | RDKit [99], ChEMBL ATC [35] |
| F8 | квоты классов задачи | см. 2.2 | разметка по разделу 3 |

Тот же модуль, что реализует F6, работает входным гейтом платформы (SAFE-001, SAFE-002); его тесты используют нейтральные синтетические фикстуры (SAFE-007).

**Что из этого реализовано на 2026-10-13** (`eval/select_benchmark.py`, числа в `eval/reports/coverage.md`): F1 и F2 — только по ChEMBL, без подтверждения вторым регулятором; F5 — прокси по числу записей Europe PMC вместо проверки восстановимости промежуточных веществ; F6 — по openFDA NDC и 21 CFR 1308.11–1308.15, перечень ПП РФ № 681 остаётся на ручную сверку; F7 — один представитель на обобщённый каркас Bemis–Murcko, балансировки по ATC нет; F8 — квоты трёх структурных классов (N-гетероцикл, фтор, стереоцентр) с окном ±5 п.п. вокруг доли референсной популяции, остальные позиции занимает жадный MaxMin. Квоты по классам уровня маршрута (защитные группы, катализ, биокатализ, длина, конвергентность) задать пока не из чего: маршруты не собраны.

### 2.2. Квоты покрытия классов задачи

Мульти-лейбловая разметка выполняется автоматически (RDKit [99], Rxn-INSIGHT [102] с отображением в RXNO [103]), спорные случаи размечает человек с записью в журнал. Допуск по каждой квоте ±10 процентных пунктов; референсные доли считаются по разделу 3.

| Класс | Признак | Ориентир и обоснование |
|---|---|---|
| Хиральность | наличие стереоцентров или осевой хиральности у цели; отдельно отмечается способ получения стереоцентра на уровне класса (хиральный пул, асимметрический катализ, разделение, биокатализ) | доля считается по ChEMBL `max_phase=4`; регуляторный контекст: EMA не одобряло рацематы с 2016 года, у FDA около одного в год в 2013–2022 [145] |
| Азотистые гетероциклы | наличие N-гетероцикла | ≈59% уникальных малых молекул, одобренных FDA, содержат N-гетероцикл [141] |
| Фтор | наличие атома F | «about 20% of the commercial pharmaceuticals are fluoro-pharmaceuticals», база из 340 веществ [144] |
| Кольцевые системы | число и новизна кольцевых систем | до 2013 года в препаратах встречалось 351 кольцевая система и 1197 каркасов; около 28% новых препаратов содержат новую кольцевую систему [143] |
| Защитные группы | наличие стадий введения и снятия защиты в эталонном маршруте | классы protection/deprotection выделены в схемах классификации реакций медицинской и процессной химии [135][136] |
| Каталитические стадии | металлокатализ (включая кросс-сочетания) и каталитическое гидрирование | среди самых частых реакций — образование амидной связи, Suzuki–Miyaura и SNAr; из современных реакций в топе только Suzuki–Miyaura и Buchwald–Hartwig [137] |
| Биокаталитические кандидаты | для хотя бы одной стадии применимо правило RetroBioCat или есть ферментативная альтернатива в открытых данных | 10–15% как целевой ориентир; обоснование — обзоры промышленного биокатализа [150] и наборы правил [16][17][18] |
| Длина маршрута | число стадий в самой длинной линейной последовательности, бины 2–3 / 4–6 / ≥7 | сверяется с распределением длин маршрутов PaRoutes [12] |
| Конвергентность | наличие двух и более ветвей сборки | нужна для осмысленных метрик PMI (convergent PMI) [66] |
| Свойства молекулы | MW, cLogP, HBD/HBA, TPSA, Fsp3 | сравнение с популяцией одобренных оральных препаратов [142] |

### 2.3. Сплиты и контроль контаминации

| Срез | Доля | Правило формирования | Назначение |
|---|---|---|---|
| dev | ≈40% | стратификация по 2.2 | отладка промптов, проверок и цикла ремонта; доступен агентам |
| test | ≈60% | scaffold-split: ни одна кольцевая система или каркас Bemis–Murcko не встречается одновременно в dev и test; хэш набора фиксируется в ADR | главные числа статьи; заморожен (EVAL-002) |
| temporal | 5–10 позиций | эталонный источник опубликован **после** даты отсечения знаний всех сравниваемых моделей; дата берётся из Crossref и OpenAlex [75][77] | срез с минимальным риском запоминания |
| perturbed | все позиции test | запрос подаётся не по МНН, а по структурному идентификатору или редкому синониму | падение метрик относительно МНН-запроса указывает на запоминание; строковая деконтаминация по n-граммам сама по себе недостаточна [130] |
| exposure-probe | все позиции | модель без RAG просят назвать источники эталона; совпадение помечается флагом `exposed` | стратификация результатов по экспонированности; родственный подход — статистическая проверка контаминации по перестановкам [131] |

Дополнительно, в конфигурациях с RAG каждый прогон делается в двух режимах: **open-book** (весь индекс) и **reference-masked** (документы эталона и всё, опубликованное позже даты отсечения, исключаются фильтром по идентификатору и дате). Без этого сравнение с базовой линией «LLM без обвязки» (EVAL-003) смещено. Публикуемые файлы бенчмарка снабжаются canary-строкой (практика BIG-bench [132]), метаданными Croissant [133] и карточкой-datasheet [134] (DATA-001).

### 2.4. Если препаратов не хватает: методика реалистичного расширения

1. **Цели-прокси из патентных маршрутов.** Берутся многостадийные маршруты PaRoutes [12], цели которых структурно близки к одобренным препаратам (ближайший сосед среди ChEMBL `max_phase=4` по Morgan-отпечаткам с порогом Tanimoto). Маршруты там уже привязаны к патентным источникам.
2. **Перевзвешивание под реальную статистику.** Веса или стратифицированная подвыборка подбираются так, чтобы распределения свойств и классов реакций совпадали с референсной популяцией (раздел 3). Расхождение измеряется и публикуется.
3. **Жёсткая изоляция.** Такие позиции помечаются `synthetic_proxy = true`, не смешиваются с основным тестом и отчитываются отдельной строкой. Эта схема допустима именно потому, что данные для неё распространяются под CC BY 4.0 [12].

---

## 3. Методика проверки покрытия реальных классов задачи

### 3.1. Референсы

| Измерение | С чем сравниваем | Что даёт источник |
|---|---|---|
| Классы реакций процессной химии | классы стадий эталонов бенчмарка | обзор химии, использованной при получении препаратов-кандидатов в подразделениях Process Chemistry R&D GlaxoSmithKline, AstraZeneca и Pfizer [135]; обзор GMP-реакций исследовательского производства 1985–2002 [139] |
| Классы реакций медицинской химии | то же | анализ реакций в публикациях [136]; анализ 2014 против 1984 с вывод о доминировании образования амида, Suzuki–Miyaura и SNAr [137]; обзор расширения инструментария [140] |
| Классы в патентах | то же | 1,15 млн уникальных реакционных схем из фармацевтических патентов 1976–2015, с ролями и выходами, и смещение в сторону отдельных классов [138] |
| Смещение самих датасетов | USPTO против внутренних ELN | модели, обученные на наборах до 17,5 млн реакций; оценка на 1731 соединении из 41 виртуальной библиотеки; вывод о влиянии специфичности шаблонов на обобщаемость [146] |
| Длина и форма маршрута | LLS и ветвление | два набора по 10 000 патентных маршрутов [12] |
| Свойства молекул | цели бенчмарка против ChEMBL `max_phase=4` | динамика MW, cLogP, HBD/HBA одобренных оральных препаратов за два десятилетия [142] |
| Кольцевые системы | каркасы целей | статистика кольцевых систем и каркасов препаратов [143] |
| Гетероциклы, фтор, хиральность | доли в наборе | [141], [144], [145] |
| Функциональные группы | FG-профиль целей | алгоритм выделения функциональных групп, давший 3080 уникальных групп на биоактивной части ChEMBL [147] |

### 3.2. Процедура

1. **Разметка стадий.** Атом-маппинг rxnmapper [101] → детерминированная классификация Rxn-INSIGHT [102] → отображение в RXNO [103]. Альтернативная схема отпечатков реакций для крупномасштабной классификации описана в [148]; коммерческий NameRxn используется только если лицензия подтверждена (сейчас — **не подтверждено**).
2. **Дескрипторы.** Одинаковая стандартизация (RDKit [99]) для целей бенчмарка и для референсной популяции ChEMBL.
3. **Статистика сравнения.** Для категориальных признаков — доли с 95% bootstrap-интервалами и χ²/точный тест Фишера; для непрерывных — KS-статистика и расстояние Вассерштейна; сводно — расхождение Йенсена–Шеннона. Критерий «покрыто»: доля в бенчмарке попадает в интервал референса либо отклоняется не более чем на 10 п.п. Пустая ячейка (класс с долей ≥5% в референсе и нулём в бенчмарке) трактуется как блокирующий дефект набора.
4. **Отчёт.** `eval/reports/coverage.md` генерируется скриптом (EVAL-001): таблица «класс × доля в бенчмарке × доля в референсе × интервал × статус» плюс проекция целей на пространство ChEMBL `max_phase=4`.
5. **Честное ограничение.** Опубликованные обзоры [135][136][139] описывают выборки 2000-х годов и внутренние портфели отдельных компаний, поэтому служат ориентиром, а не истиной. Основной количественный референс считается нами на открытых данных (ChEMBL + USPTO/ORD) и воспроизводится одной командой.

---

## 4. RAG

### 4.1. Классификация типов документов

| Тип документа | Какие факты извлекаем | Формат и доступ | Лицензия / ограничение |
|---|---|---|---|
| Статьи процессной химии (Org. Process Res. Dev. и близкие) | граф маршрута на уровне «из какого вещества получено какое», тип стадии, заявленные числовые показатели (выход, масштаб), ссылки на предшествующие работы, цитата-подтверждение | метаданные Crossref/OpenAlex; OA-полный текст Europe PMC (JATS XML); подписной — только через TDM-API | метаданные свободны [75][79]; OA — по лицензии статьи [82]; подписной текст — некоммерческий TDM, фрагменты ≤200 символов с DOI [87]; ACS TDM — платная услуга [88]. Критично: в Europe PMC по OPRD всего 191 запись против 7 069 DOI в Crossref [81] |
| Статьи медицинской химии и обзорные серии | структуры, класс стадии, указание на источник маршрута | как выше; ежегодная серия обзоров синтезов новых одобренных препаратов — удобная точка входа по годам [149] | как выше |
| Патенты, включая процессные | структуры из аннотаций, принадлежность вещества к документу, даты приоритета, семейство | USPTO ODP (XML) [96]; EPO OPS [95]; Google Patents в BigQuery [90]; аннотации SureChEMBL (bulk Parquet) [93] | USPTO — Public Domain Mark 1.0 [96]; Google Patents Public Data — CC BY 4.0 с атрибуцией [90]; SureChEMBL — CC BY 4.0 [93]; OPS — 4 ГБ/нед бесплатно [95]; Lens — некоммерческая модель CC BY-NC-SA [94] |
| Записи реакционных БД | реакция в машинном виде (SMILES, атом-маппинг), роли, выход, ссылка на первоисточник | ORD (Parquet/protobuf) [7][8]; USPTO (Lowe) [1]; PaRoutes [12]; биокаталитические наборы [16][17][18] | CC0 / CC BY / CC BY-SA (см. 1.1) |
| Регуляторные руководства | классы растворителей и пределы, PDE элементов, подход к мутагенным примесям, принципы выбора исходных материалов | PDF ICH и EMA [59][60][61][62] | воспроизведение с указанием источника [59][60] |
| Публичные оценочные отчёты регуляторов (EPAR и аналоги) | состав субстанции, идентификаторы, формальные характеристики продукта | EMA JSON + ссылки на EPAR [40]; Drugs@FDA [39] | EMA — воспроизведение с указанием источника [40]; FDA — public domain [38] |
| Гайды по растворителям и метрикам | ранг растворителя, категория, формулы метрик | статьи [63][65]; страницы инструментов [66] | CHEM21-таблицы © RSC, нужна отдельная перепечатка [64]; часть гайдов закрыта [65] |
| Данные о безопасности (GHS, реактивность) | класс опасности, предупреждения, источник классификации | PubChem PUG-View (GHS, LCSS) [30][31][70]; CAMEO [72]; GESTIS [71] | лицензия хранится у каждой записи: ECHA — некоммерческое использование с атрибуцией, EU CLP — CC BY 4.0 [70]; GESTIS — без коммерческого использования и переноса [71]; LCSS — без безусловного разрешения на переиспользование [31] |
| Нормативные перечни для гейта | идентификаторы позиций перечня и версия документа | PDF и API [42][43][44][45] | публикации регуляторов; хранятся как данные с датой версии (SAFE-003) |

### 4.2. Архитектура хранилища

1. **Загрузка.** Отдельные адаптеры (`backend/app/sources/`) на каждый источник, с персистентным кэшем, уважением лимитов (Crossref polite pool с `mailto` [74], PubChem ≤5 запросов/с [27], OpenAlex с ключом [78], Springer Nature 1 запрос/с [89]) и записью в журнал: URL, дата получения, лицензия, контрольная сумма. Источники с запретом автоматического обхода (ГРЛС [41], Lens [94]) в автоматический конвейер не включаются.
2. **Нормализация.** Для OA-статей предпочтителен готовый JATS XML Europe PMC [81] (разметка секций уже есть, разбор PDF не нужен). Для PDF — GROBID или Docling (обе разрешающие лицензии) [98]; PyMuPDF (AGPL) и веса Nougat/Marker с NC-ограничениями в публикуемый дистрибутив не попадают [98]. Патенты приходят в XML, так что структура разделов доступна без OCR [96].
3. **Чанкование по структуре документа.** Границы чанков ставятся по элементам документа (секция, подзаголовок, таблица, подпись к схеме), а не по фиксированному числу токенов: структурное чанкование повышает качество RAG по сравнению с абзацным [127]. Экспериментальные разделы и примеры патентов индексируются как отдельные чанки с повышенным весом, поскольку именно в них лежат проверяемые фактические утверждения.
4. **Метаданные чанка (обязательные).** `doc_id`, тип документа, DOI или номер патента, дата публикации (нужна для временного среза, см. 2.3), журнал/ведомство, лицензия и допустимая длина цитаты, путь к секции, идентификаторы упомянутых веществ (InChIKey) — из OPSIN для названий [98], из аннотаций SureChEMBL для патентов [93], из PubChem для синонимов [29]. Идентификаторы веществ делают возможным структурный фильтр ещё до текстового поиска.
5. **Гибридный поиск.** BM25 [124] и плотные эмбеддинги (модели с MIT/Apache-2.0 [104]) объединяются Reciprocal Rank Fusion [123], далее реранкер. Основание: BM25 остаётся устойчивой базовой линией вне домена обучения [125], а совместное использование контекстных эмбеддингов и контекстного BM25 снижает долю неудачных извлечений на 49%, с реранкингом — на 67% [126]. Третья ветвь — **структурный поиск**: подструктурный и similarity-поиск через RDKit PostgreSQL cartridge [99] и FPSim2 [100], а также готовые фингерпринты SureChEMBL [93]; запрос по InChIKey и по подструктуре находит документы, которые текстовый поиск пропускает (названия и изображения).
6. **Хранение цитат для верификации.** Каждый извлечённый факт сохраняется вместе с дословной цитатой, смещениями в исходном тексте, `doc_id` и хэшем версии документа. Это прямая реализация TRUST-004: статус `literature` выставляется только если источник существует (резолвинг DOI через Crossref [75]) и цитата найдена в его тексте. Длина сохраняемой цитаты ограничивается лицензией источника (для подписного контента Elsevier — ≤200 символов с DOI-ссылкой [87]), поэтому поле `max_quote_len` хранится в метаданных и проверяется при экспорте.
7. **Оценка самого RAG.** Отдельный контур метрик: контекстная релевантность и верность ответа контексту по методике RAGAS [128] и метрики качества цитирования по методике ALCE [129], плюс собственная метрика citation grounding rate из протокола проекта.

### 4.3. Почему RAG, а не fine-tuning и не «просто LLM»

| Аргумент | Подтверждение |
|---|---|
| Параметрическая память плохо держит редкие факты | точность ответа на вопрос коррелирует с числом релевантных документов в предобучении; чтобы вытянуть «длинный хвост» только масштабом, модели нужно увеличить на порядки; retrieval снижает эту зависимость [109] |
| Маршруты конкретных препаратов — это и есть «длинный хвост» | RAG превосходит fine-tuning особенно на наименее популярных фактах [108] |
| Fine-tuning хуже вводит новое знание | при сравнении unsupervised fine-tuning и RAG «RAG consistently outperforms it, both for existing knowledge… and entirely new knowledge» [106] |
| Fine-tuning на новом знании повышает галлюцинации | примеры с новым знанием выучиваются медленнее, а по мере выучивания линейно растёт склонность модели к галлюцинациям [107] |
| Retrieval снижает галлюцинации | архитектуры с retrieval-in-the-loop существенно сокращают галлюцинирование знания [110]; исходная постановка RAG вводит и обновляемую память, и происхождение ответа [105] |
| Ссылки без проверки недостоверны | в сгенерированных обзорах 55% ссылок GPT-3.5 и 18% ссылок GPT-4 оказались выдуманными; среди реальных 43% и 24% содержали существенные ошибки [111]; в исследовании 2025 года на GPT-4o из 176 ссылок 35 (19,9%) были фабрикованы, а среди 141 реальной 64 (45,4%) содержали ошибки, чаще всего неверный или недействительный DOI [112] |
| В химии RAG даёт измеримый выигрыш | на наборе задач ChemRAG-Bench извлечение дало среднее относительное улучшение 17,4% по сравнению с прямым выводом [117] |
| Знание ≠ надёжность | LLM в среднем превосходят химиков-экспертов на части задач ChemBench (>2 700 пар «вопрос-ответ»), но «struggle with some basic tasks and provide overconfident predictions» — поэтому нужны детерминированные проверки, а не доверие к уверенности модели [118] |
| Связка «LLM + инструменты» уже признана в домене | агент с 18 экспертными химическими инструментами [113]; автономный исследовательский агент с доступом к внешним ресурсам [114]; агенты для литературного поиска, где PaperQA2 на ряде задач сопоставим с экспертами, а репозиторий открыт под Apache-2.0 [115][116] |
| Для планирования маршрутов это рабочая линия 2025–2026 | LLM в связке с алгоритмическим поиском и извлечением контекста [120][121]; доменные платформы [122]; работы, прямо ставящие задачу подавления «химических галлюцинаций» через верификатор маршрута [119] |
| Обновляемость и лицензии | индекс пересобирается под новые релизы (ORD реорганизован 2026-08-30 [7], SureChEMBL обновляется каждые две недели [93], Orange Book — ежемесячно [38]), а лицензионные ограничения (ограничение длины цитаты [87], запрет ML-использования [15][54]) соблюдаются на уровне метаданных чанка — в весах модели это невозможно |

Fine-tuning в проекте остаётся опцией для **формы** вывода (соответствие схеме RouteSpec, стиль разметки шагов), а не для знаний о маршрутах; конфигурация с дообучением, если появится, оценивается как отдельная линия протокола.

---

## Выводы для проекта

1. **Ядро открытых данных.** USPTO (Lowe, CC0) [1] + ORD (CC BY-SA 4.0) [7] + PaRoutes (CC BY 4.0) [12] + ChEMBL 37 (CC BY-SA 3.0) [35] + PubChem [32] + Orange Book и Drugs@FDA (public domain) [38][39] + EMA (с атрибуцией) [40] + SureChEMBL и Google Patents и USPTO ODP для патентов [93][90][96] + ICH для процессных правил [59][60][61]. Этого достаточно, чтобы собрать и опубликовать бенчмарк без коммерческих баз.
2. **Лицензионная развилка требует решения до первого публичного релиза.** ORD распространяется под CC BY-SA 4.0, значит производный датасет шагов наследует ShareAlike; предложение Apache-2.0 для кода и CC BY 4.0 для данных из north-star с этим не стыкуется, если в данные попадают записи ORD. Варианты: (а) выпускать датасет под CC BY-SA 4.0, (б) хранить только ссылки на `ord_id` без содержимого, (в) строить публикуемую часть на CC0-источнике (Lowe) и CC BY (PaRoutes). Нужен ADR.
3. **Запреты, которые надо зафиксировать в коде, а не в голове.** CAS прямо запрещает использование данных для ML и ИИ [15]; Enamine ToU §15.2 запрещает ML-обработку своих данных без письменного разрешения [54]; MolPort на HF — CC BY-NC 4.0 [55]; DrugBank запрещает производные базы и сейчас вообще приостановил академические загрузки [37]; ГРЛС запрещает автоматический обход [41]. Это материал для allow-list источников в `sources/` и для карточек DATA-001.
4. **Главный технический риск RAG — не поиск, а доступ к профильным текстам.** Процессная химия публикуется в основном в подписных журналах: в Europe PMC по OPRD всего 191 запись против 7 069 DOI в Crossref [81]. Поэтому архитектура должна одинаково хорошо работать на патентных полных текстах (свободных) и на коротких лицензированных цитатах из статей, с жёстким ограничением длины цитаты в метаданных [87].
5. **Бенчмарк обязан иметь контаминационный контур с первого дня.** Временной срез, перефразированные запросы, зонд на экспонированность, canary-строка и режим reference-masked для RAG — иначе сравнение с LLM без обвязки не защитимо [130][131][132].
6. **Проверка покрытия должна считаться скриптом, а не утверждаться словами.** Референсные доли (59% N-гетероциклов [141], ~20% фтора [144], доминирование нескольких классов реакций [137][138]) задают ожидания, но основной референс считаем сами на ChEMBL и USPTO — это воспроизводимо и обновляемо.
7. **Ближайшие практические шаги.** Карточки DATA-001 для шести источников ядра; скрипт `eval/select_benchmark.py` с фильтрами F1–F8; выгрузка референсных распределений; ADR по лицензии датасета; запрос в библиотеку ИТМО о TDM-доступе к ACS и Elsevier.

## Открытые вопросы

**Для самостоятельного поиска:**
1. Юридическая совместимость CC BY-SA 4.0 (ORD) с планируемой лицензией бенчмарка; почему ORDerly заявлен как CC BY 4.0 поверх CC BY-SA 4.0 [11].
2. Есть ли у ИТМО институциональный TDM-доступ к ACS (ключевой журнал процессной химии) и Elsevier; условия ACS TDM не опубликованы [88].
3. Разрешает ли университетская подписка Reaxys массовый экспорт и обучение моделей — публичных условий найти не удалось [14].
4. Можно ли получить официальный доступ к БД ГРЛС по заявке и в каком формате выгрузка [41].
5. Машиночитаемые версии перечней: ПП РФ № 681 и bulk-выгрузка OPCW SCDB [43][45]; списки Australia Group (сайт не ответил).
6. Лицензии PathBank и MetaNetX как источников ECREACT [18]; лицензия RetroBioCat-2 [16].
7. Точный состав buyables ASKCOS и условия использования стока ZINC внутри AiZynthFinder [26][52].
8. Фактические лимиты Unpaywall и лицензия его данных (страница не отдала текст) [85].
9. Появились ли ревизии ICH новее Q3C(R9), Q3D(R2), M7(R2) [59][60][61].
10. Статус public domain для выгрузок GSRS/UNII [48].

**Для эксперта (перенести в `docs/expert/questions.md`):**
11. Какие классы стадий технолог считает обязательными в представительном наборе из 30–50 препаратов (помимо квот раздела 2.2)?
12. Какая доля биокаталитических альтернатив в наборе выглядит реалистичной, а не маркетинговой?
13. Какие источники условий вызывают больше доверия на практике — процессные статьи или процессные патенты (связано с весами источников в TRUST)?
14. Какой горизонт «off-patent» корректен для учебного бенчмарка: отсутствие записей в Orange Book или более строгий критерий?
