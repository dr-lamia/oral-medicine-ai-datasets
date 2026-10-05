# Oral Medicine AI Datasets

A curated, research-focused catalogue of public datasets for artificial intelligence in oral medicine, oral pathology, oral cancer, oral potentially malignant disorders (OPMDs), clinical photography, cytology, histopathology, CBCT and multimodal oral-health records.

> This repository contains **metadata and links only**. It does not redistribute clinical images or patient data. Researchers must follow each source dataset's licence, ethics approval and data-use conditions.

## Why this catalogue is different

- Identifies original datasets versus augmented or repackaged copies.
- Records patient counts separately from image counts.
- Prioritizes patient/case identifiers for leakage-free splitting.
- Highlights external-validation readiness.
- Documents access and metadata limitations.
- Suggests publishable research uses rather than only listing downloads.

The machine-readable catalogue is in [`datasets.csv`](datasets.csv). It currently tracks **26 resources**, including core oral-specific datasets, adjacent head-and-neck multimodal cohorts, evolving repositories, and derivative resources that require provenance caution.

## Recommended datasets by research task

| Research task | Recommended datasets | Key opportunity |
|---|---|---|
| Egyptian multicentre OSCC histopathology | Alexandria OSCC + SinaiU-OMP | Patient-level development followed by cross-centre external validation |
| OSCC prognosis | Multi-OSCC | Recurrence, lymph-node metastasis and histological-risk prediction |
| Smartphone OPMD/cancer referral | MeMoSA + SMART-OM + BMIOCD | Geographic external validation and uncertainty-aware triage |
| Oral cytology | Multicentre Oral Cytology | Nucleus detection, slide classification and stain-domain generalization |
| Odontogenic lesions | DOLCHID | CBCT segmentation and pathology-informed diagnosis |
| Multimodal dental AI | COde | Longitudinal vision-language modelling and patient-level leakage analysis |
| Dysplasia and OPMD histopathology | NDB-UFES + IISc OPMD WSI | Case-level dysplasia grading and progression-risk research |
| Tumour segmentation | OCDC | WSI-held-out OSCC tumour segmentation |
| Multimodal cancer prognosis | TCGA-HNSC + CPTAC-HNSCC + HANCOCK | Oral-subsite-filtered external validation and survival modelling |

## Current priority project

### Egyptian multicentre OSCC histopathology AI

1. Develop on the Alexandria dataset using strict patient-level splitting.
2. Evaluate the common OSCC/normal task on SinaiU-OMP only after checking case grouping and duplicates.
3. Add an independent MSA/Cairo University cohort as the locked external test.
4. Compare single- and dual-magnification models, pathology-foundation embeddings, calibration and uncertainty-based abstention.

Recommended title:

> **External multicentre validation of an uncertainty-aware dual-magnification foundation model for oral squamous cell carcinoma histopathology in Egypt**

## Dataset catalogue

### Oral mucosal clinical photography

- **BMIOCD** — 800 original oral-cavity photographs (330 cancer, 470 non-cancer) from four Bangladeshi institutions; released 29 September 2026 under CC BY 4.0. Patient counts, identifiers, per-image centre labels and bounding boxes are unverified; confirm these before patient- or institution-held-out testing. Possible overlap with the related 2024 study remains unresolved. [Dataset](https://doi.org/10.17632/x4rkbb9zbk.1) · [Related paper](https://ieeexplore.ieee.org/document/10499560)
- **MeMoSA** — 30,039 images from 6,426 individuals across five Asian countries, with patient- and lesion-level metadata. [Paper](https://doi.org/10.1038/s41597-026-06998-7)
- **SMART-OM** — 2,469 smartphone images spanning normal, variations from normal, OPMD and oral cancer. [Paper](https://doi.org/10.1038/s41597-026-06954-5)

### Histopathology

- **Alexandria OSCC** — 1,714 H&E fields from 115 cases at 100× and 400×. [Dataset](https://doi.org/10.17632/7m9zkcx539.1) · [Descriptor](https://doi.org/10.59275/j.melba.2026-273d)

  **DOI correction:** the MELBA webpage/PDF may display `10.17632/7m9zkcx539.1.163`. That string is malformed and returns “DOI not found.” The verified dataset DOI is [`10.17632/7m9zkcx539.1`](https://doi.org/10.17632/7m9zkcx539.1).
- **SinaiU-OMP** — 300 images across normal mucosa, OSCC, odontogenic keratocyst, plexiform ameloblastoma and pleomorphic adenoma. [Dataset](https://doi.org/10.17632/y9cjhmf8rz.1) · [Paper](https://doi.org/10.1038/s41598-026-70053-z)
- **Multi-OSCC** — 1,325 patients with multiscale tumour-core/edge images and six diagnostic/prognostic endpoints; the full release is approximately **34 GB**. [Dataset](https://doi.org/10.5281/zenodo.16842637) · [Paper](https://doi.org/10.1038/s41597-026-06736-z) · [Code](https://github.com/guanjinquan/OSCC-PathologyImageDataset)

### Cytology

- **Multicentre Oral Cytology** — Pap- and MGG-stained whole-slide images, patches, patient/slide metadata and expert nucleus annotations. [Dataset](https://zenodo.org/records/20686132)

### CBCT–histopathology

- **DOLCHID** — paired CBCT and H&E data from 262 patients with four odontogenic-lesion diagnoses. [Dataset](https://doi.org/10.6084/m9.figshare.30156622) · [Paper](https://doi.org/10.1038/s41597-026-07112-7) · [Code](https://github.com/ZimoHZM/DOLCHID)

### Longitudinal multimodal records

- **COde** — 8,775 checkups from 4,800 patients, approximately 50,000 intraoral photographs, 8,056 radiographs and bilingual clinical records. [Dataset](https://huggingface.co/datasets/zirak-ai/COde) · [Paper](https://doi.org/10.1038/s41597-026-07342-9) · [Code](https://github.com/zirak-ai/COde)

## Additional collected resources

### Clinical photography and referral

- **Annotated Oral Cavity Images (Sri Lanka)** — 3,000 images from 714 patients with healthy, benign, OPMD and oral-cancer labels plus polygon/COCO annotations. [Dataset](https://zenodo.org/records/10664056) · [Paper](https://doi.org/10.1016/j.oraloncology.2024.106946)
- **Cairo Annotated Oral Lesions** — 9,201 normal, low-risk and high-risk intraoral images with LabelMe annotations. [Dataset](https://zenodo.org/records/14571990) · [Paper](https://doi.org/10.1038/s41415-025-9007-6)
- **Oral Images Dataset** — 323 primary benign/malignant images plus augmented derivatives; patient grouping needs verification. [Dataset](https://data.mendeley.com/datasets/mhjyrn35p4/2)

### Histopathology and segmentation

- **ORCHID** — approximately 300,000 multicentre Indian patches spanning normal, OSMF and three OSCC differentiation grades. [Training set](https://zenodo.org/records/12636426) · [Validation/test](https://zenodo.org/records/12646943) · [Paper](https://pubmed.ncbi.nlm.nih.gov/39333529/)
- **NDB-UFES** — 237 Brazilian H&E images of leukoplakia with/without dysplasia and OSCC, with clinical-demographic variables. [Dataset](https://data.mendeley.com/datasets/bbmmm4wgr8) · [Paper](https://doi.org/10.1016/j.dib.2023.109033)
- **Rahman Oral Histopathology** — 1,224 normal/OSCC images from 230 patients at 100× and 400×. [Dataset](https://data.mendeley.com/datasets/ftmp4cvtmb/2) · [Paper](https://doi.org/10.1016/j.dib.2020.105114)
- **OCDC** — 1,020 pixel-annotated patches from 15 source WSIs; evaluation must split by WSI, never by patch. [Dataset](https://data.mendeley.com/datasets/9bsc36jyrt/1) · [Paper](https://arxiv.org/abs/2303.10172)
- **IISc OPMD WSI Repository** — oral-pathology whole-slide repository for OPMDs; counts and access conditions require confirmation. [Repository](https://www.midas.iisc.ac.in/fe/datasets/oral/oral-pathology-a-whole-slide-imaging-repository-for-opmd)
- **COOP** — de-identified scanned oral-pathology cases; useful as a case repository, not a fixed benchmark. [Repository](https://openoralpathology.org/)

### Clinical and multimodal cancer cohorts

- **AIKosh Oral Cancer Imaging and Clinical Dataset** — Indian clinical, radiological and histopathological data; detailed counts and licence require portal-level verification. [Dataset](https://aikosh.indiaai.gov.in/home/datasets/details/oral_cancer_imaging_and_clinical_dataset.html)
- **lyDATA KSA Oral Cavity** — 66 Saudi oral-cavity OSCC patient records focused on lymphatic metastatic progression. [Dataset](https://zenodo.org/records/18231357)
- **TCGA-HNSC** — 528 head-and-neck cancer cases with molecular, pathology and clinical data. Oral research must filter by anatomical subsite. [Dataset](https://portal.gdc.cancer.gov/projects/TCGA-HNSC)
- **CPTAC-HNSCC** — 207 patients with radiology, pathology, clinical, genomic and proteomic modalities. [Dataset](https://www.cancerimagingarchive.net/collection/cptac-hnscc/)
- **HANCOCK** — 763 patients and 13,684 pathology images with linked clinical/laboratory information. [Dataset](https://doi.org/10.7937/rcty-5h16)

### Evolving, derivative or limited-provenance resources

- **SMART/SMITA evolving release** — versioned smartphone-image resource that may overlap SMART-OM; deduplicate before combining. [Dataset](https://zenodo.org/records/16313710)
- **Oral AI Prediction Outputs** — prediction CSVs, not a new patient or image cohort. [Repository](https://doi.org/10.5281/zenodo.19551358)
- **Kaggle Oral Cancer Lips and Tongue** — retained only as a provenance-warning record. It should not support clinical claims until original sources, patient grouping and duplicates are verified. [Page](https://www.kaggle.com/datasets/shivam17299/oral-cancer-lips-and-tongue-images)

The catalogue deliberately records uncertain resources instead of silently presenting them as equivalent to original, patient-linked clinical cohorts. Filter `original_data` and `patient_level_split` in `datasets.csv` before selecting data for a study.

## Quality rules

A dataset is included only when its primary source can be identified. Kaggle mirrors, augmented derivatives and collections with unclear provenance are not treated as new primary datasets. Where patient grouping is unknown, the catalogue marks patient-level splitting as unverified.

## Automated maintenance

The repository includes a weekly workflow that validates the catalogue schema and checks primary URLs. It does not automatically change scientific metadata; all substantive updates require source verification and review.

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md). Please cite a primary repository and a peer-reviewed publication when available.

## Licence

Catalogue metadata and repository code are released under [CC BY 4.0](LICENSE). Source datasets retain their original licences.
