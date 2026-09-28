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

The machine-readable catalogue is in [`datasets.csv`](datasets.csv).

## Recommended datasets by research task

| Research task | Recommended datasets | Key opportunity |
|---|---|---|
| Egyptian multicentre OSCC histopathology | Alexandria OSCC + SinaiU-OMP | Patient-level development followed by cross-centre external validation |
| OSCC prognosis | Multi-OSCC | Recurrence, lymph-node metastasis and histological-risk prediction |
| Smartphone OPMD/cancer referral | MeMoSA + SMART-OM | Geographic external validation and uncertainty-aware triage |
| Oral cytology | Multicentre Oral Cytology | Nucleus detection, slide classification and stain-domain generalization |
| Odontogenic lesions | DOLCHID | CBCT segmentation and pathology-informed diagnosis |
| Multimodal dental AI | COde | Longitudinal vision-language modelling and patient-level leakage analysis |

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

- **MeMoSA** — 30,039 images from 6,426 individuals across five Asian countries, with patient- and lesion-level metadata. [Paper](https://doi.org/10.1038/s41597-026-06998-7)
- **SMART-OM** — 2,469 smartphone images spanning normal, variations from normal, OPMD and oral cancer. [Paper](https://doi.org/10.1038/s41597-026-06954-5)

### Histopathology

- **Alexandria OSCC** — 1,714 H&E fields from 115 cases at 100× and 400×. [Dataset](https://doi.org/10.17632/7m9zkcx539.1) · [Descriptor](https://doi.org/10.59275/j.melba.2026-273d)

  **DOI correction:** the MELBA webpage/PDF may display `10.17632/7m9zkcx539.1.163`. That string is malformed and returns “DOI not found.” The verified dataset DOI is [`10.17632/7m9zkcx539.1`](https://doi.org/10.17632/7m9zkcx539.1).
- **SinaiU-OMP** — 300 images across normal mucosa, OSCC, odontogenic keratocyst, plexiform ameloblastoma and pleomorphic adenoma. [Dataset](https://doi.org/10.17632/y9cjhmf8rz.1) · [Paper](https://doi.org/10.1038/s41598-026-70053-z)
- **Multi-OSCC** — 1,325 patients with multiscale tumour-core/edge images and six diagnostic/prognostic endpoints. [Dataset](https://doi.org/10.5281/zenodo.16842637) · [Paper](https://doi.org/10.1038/s41597-026-06736-z) · [Code](https://github.com/guanjinquan/OSCC-PathologyImageDataset)

### Cytology

- **Multicentre Oral Cytology** — Pap- and MGG-stained whole-slide images, patches, patient/slide metadata and expert nucleus annotations. [Dataset](https://zenodo.org/records/20686132)

### CBCT–histopathology

- **DOLCHID** — paired CBCT and H&E data from 262 patients with four odontogenic-lesion diagnoses. [Dataset](https://doi.org/10.6084/m9.figshare.30156622) · [Paper](https://doi.org/10.1038/s41597-026-07112-7) · [Code](https://github.com/ZimoHZM/DOLCHID)

### Longitudinal multimodal records

- **COde** — 8,775 checkups from 4,800 patients, approximately 50,000 intraoral photographs, 8,056 radiographs and bilingual clinical records. [Dataset](https://huggingface.co/datasets/zirak-ai/COde) · [Paper](https://doi.org/10.1038/s41597-026-07342-9) · [Code](https://github.com/zirak-ai/COde)

## Quality rules

A dataset is included only when its primary source can be identified. Kaggle mirrors, augmented derivatives and collections with unclear provenance are not treated as new primary datasets. Where patient grouping is unknown, the catalogue marks patient-level splitting as unverified.

## Automated maintenance

The repository includes a weekly workflow that validates the catalogue schema and checks primary URLs. It does not automatically change scientific metadata; all substantive updates require source verification and review.

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md). Please cite a primary repository and a peer-reviewed publication when available.

## Licence

Catalogue metadata and repository code are released under [CC BY 4.0](LICENSE). Source datasets retain their original licences.
