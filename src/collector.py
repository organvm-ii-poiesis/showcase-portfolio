"""Collector that aggregates works from registry data."""

from __future__ import annotations

import json
from pathlib import Path

from .gallery import Gallery, Medium, Work


ORGAN_MEDIUM_MAP: dict[str, Medium] = {
    "organvm-i-theoria": Medium.SOFTWARE,
    "organvm-ii-poiesis": Medium.MIXED_MEDIA,
    "organvm-iii-ergon": Medium.SOFTWARE,
    "organvm-iv-taxis": Medium.SOFTWARE,
    "organvm-v-logos": Medium.LITERARY,
    "organvm-vi-koinonia": Medium.INTERACTIVE,
    "organvm-vii-kerygma": Medium.MIXED_MEDIA,
}


def collect_from_registry(registry_path: Path) -> Gallery:
    """Build a gallery from a registry-v2.json file."""
    with open(registry_path) as f:
        data = json.load(f)

    gallery = Gallery(
        name="ORGAN System Portfolio",
        description="Complete portfolio of creative and technical works across all 8 organs",
    )

    repos = data.get("repositories", data.get("repos", []))
    for repo in repos:
        org = repo.get("org", "")
        medium = ORGAN_MEDIUM_MAP.get(org, Medium.SOFTWARE)
        relevance = repo.get("portfolio_relevance", "LOW")

        work = Work(
            title=repo.get("name", ""),
            description=repo.get("description", ""),
            medium=medium,
            organ=org,
            repo=repo.get("name", ""),
            tags=repo.get("topics", []),
            featured=relevance in ("CRITICAL", "HIGH"),
        )
        gallery.add_work(work)

    return gallery


def collect_from_works_file(works_path: Path) -> Gallery:
    """Build a gallery from a curated works.json file."""
    with open(works_path) as f:
        data = json.load(f)

    gallery = Gallery(
        name=data.get("gallery_name", "Portfolio"),
        description=data.get("description", ""),
    )

    for item in data.get("works", []):
        work = Work(
            title=item["title"],
            description=item.get("description", ""),
            medium=Medium(item.get("medium", "software")),
            organ=item.get("organ", ""),
            repo=item.get("repo", ""),
            tags=item.get("tags", []),
            featured=item.get("featured", False),
        )
        gallery.add_work(work)

    return gallery
