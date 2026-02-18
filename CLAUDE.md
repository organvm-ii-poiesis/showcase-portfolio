# CLAUDE.md — showcase-portfolio

**ORGAN II** (Art) · `organvm-ii-poiesis/showcase-portfolio`
**Status:** ACTIVE · **Branch:** `main`

## What This Repo Is

Living portfolio aggregating all ORGAN-II generative art, interactive installations, and AI-human collaborative works

## Stack

**Languages:** Python
**Build:** Python (pip/setuptools)
**Testing:** pytest (likely)

## Directory Structure

```
📁 .github/
📁 data/
📁 docs/
    adr
    source-materials
📁 src/
    __init__.py
    __main__.py
    collector.py
    gallery.py
    renderer.py
📁 tests/
    __init__.py
    test_collector.py
    test_gallery.py
    test_renderer.py
  .gitignore
  CHANGELOG.md
  LICENSE
  README.md
  pyproject.toml
  seed.yaml
```

## Key Files

- `README.md` — Project documentation
- `pyproject.toml` — Python project config
- `seed.yaml` — ORGANVM orchestration metadata
- `src/` — Main source code
- `tests/` — Test suite

## Development

```bash
pip install -e .    # Install in development mode
pytest              # Run tests
```

## ORGANVM Context

This repository is part of the **ORGANVM** eight-organ creative-institutional system.
It belongs to **ORGAN II (Art)** under the `organvm-ii-poiesis` GitHub organization.

**Registry:** [`registry-v2.json`](https://github.com/meta-organvm/organvm-corpvs-testamentvm/blob/main/registry-v2.json)
**Corpus:** [`organvm-corpvs-testamentvm`](https://github.com/meta-organvm/organvm-corpvs-testamentvm)
