# Contributing

Contributions are welcome when they improve the scientific reliability of the catalogue.

## Inclusion criteria

- Direct relevance to oral medicine, oral pathology, oral cancer, OPMDs, oral cytology or clinically adjacent multimodal oral-health AI.
- A traceable primary source such as an institutional repository, Zenodo, Figshare, Mendeley Data or an official project repository.
- Sufficient documentation to identify modality, task, labels and access conditions.

## Required checks

1. Confirm whether the release contains original patient data or only augmented/repackaged images.
2. Record patients/cases separately from images, patches or visits.
3. Determine whether patient/case identifiers permit leakage-free splitting.
4. State access restrictions and licence exactly as the primary record reports them.
5. Link the primary publication when available.
6. Describe missing metadata and limitations explicitly.

Please update `last_verified` using ISO format (`YYYY-MM-DD`) and run:

```bash
python scripts/validate_catalog.py
python scripts/check_links.py
```

Do not upload or redistribute source dataset files unless their licence and governance explicitly permit it.
