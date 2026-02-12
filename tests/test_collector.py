"""Tests for the collector module."""

import json
import tempfile
from pathlib import Path

from src.collector import collect_from_registry, collect_from_works_file


class TestCollectFromWorksFile:
    def test_loads_works(self):
        data = {
            "gallery_name": "Test Gallery",
            "description": "For testing",
            "works": [
                {
                    "title": "Work 1",
                    "description": "First work",
                    "medium": "software",
                    "organ": "organvm-i-theoria",
                    "repo": "test-repo",
                    "featured": True,
                },
                {
                    "title": "Work 2",
                    "description": "Second work",
                    "medium": "performance",
                    "organ": "organvm-ii-poiesis",
                    "repo": "test-repo-2",
                },
            ],
        }
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json.dump(data, f)
            path = Path(f.name)

        gallery = collect_from_works_file(path)
        assert gallery.name == "Test Gallery"
        assert len(gallery.works) == 2
        assert gallery.works[0].featured is True
        assert gallery.works[1].featured is False

    def test_empty_works(self):
        data = {"gallery_name": "Empty", "description": "", "works": []}
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json.dump(data, f)
            path = Path(f.name)

        gallery = collect_from_works_file(path)
        assert len(gallery.works) == 0

    def test_tags_loaded(self):
        data = {
            "gallery_name": "Tags Test",
            "description": "",
            "works": [
                {
                    "title": "Tagged Work",
                    "description": "Has tags",
                    "medium": "software",
                    "organ": "organvm-i-theoria",
                    "repo": "tagged-repo",
                    "tags": ["alpha", "beta", "gamma"],
                },
            ],
        }
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json.dump(data, f)
            path = Path(f.name)

        gallery = collect_from_works_file(path)
        assert gallery.works[0].tags == ["alpha", "beta", "gamma"]

    def test_missing_optional_fields(self):
        """Gracefully handle works with only required fields."""
        data = {
            "gallery_name": "Minimal",
            "description": "",
            "works": [
                {
                    "title": "Bare Minimum",
                },
            ],
        }
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json.dump(data, f)
            path = Path(f.name)

        gallery = collect_from_works_file(path)
        work = gallery.works[0]
        assert work.title == "Bare Minimum"
        assert work.description == ""
        assert work.organ == ""
        assert work.repo == ""
        assert work.tags == []
        assert work.featured is False

    def test_all_medium_types(self):
        """All medium enum values can be loaded from works.json."""
        mediums = ["generative-art", "performance", "interactive", "literary", "musical", "mixed-media", "software"]
        works = [
            {"title": f"Work {m}", "medium": m}
            for m in mediums
        ]
        data = {"gallery_name": "All Mediums", "description": "", "works": works}
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json.dump(data, f)
            path = Path(f.name)

        gallery = collect_from_works_file(path)
        assert len(gallery.works) == 7
        loaded_mediums = {w.medium.value for w in gallery.works}
        assert loaded_mediums == set(mediums)


class TestCollectFromRegistry:
    def test_basic_registry(self):
        """Collect works from a minimal registry structure."""
        registry = {
            "repositories": [
                {
                    "name": "recursive-engine",
                    "org": "organvm-i-theoria",
                    "description": "A recursive engine",
                    "portfolio_relevance": "CRITICAL",
                    "topics": ["recursion"],
                },
            ],
        }
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json.dump(registry, f)
            path = Path(f.name)

        gallery = collect_from_registry(path)
        assert len(gallery.works) == 1
        assert gallery.works[0].title == "recursive-engine"
        assert gallery.works[0].featured is True

    def test_medium_mapping_for_all_organs(self):
        """Each organ maps to the correct default medium."""
        organs = [
            ("organvm-i-theoria", "software"),
            ("organvm-ii-poiesis", "mixed-media"),
            ("organvm-iii-ergon", "software"),
            ("organvm-iv-taxis", "software"),
            ("organvm-v-logos", "literary"),
            ("organvm-vi-koinonia", "interactive"),
            ("organvm-vii-kerygma", "mixed-media"),
        ]
        repos = [
            {"name": f"repo-{org}", "org": org, "description": "test"}
            for org, _ in organs
        ]
        registry = {"repositories": repos}
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json.dump(registry, f)
            path = Path(f.name)

        gallery = collect_from_registry(path)
        for i, (org, expected_medium) in enumerate(organs):
            assert gallery.works[i].medium.value == expected_medium, (
                f"Organ {org} expected medium {expected_medium}, got {gallery.works[i].medium.value}"
            )

    def test_featured_from_portfolio_relevance(self):
        """CRITICAL and HIGH relevance become featured; others do not."""
        registry = {
            "repositories": [
                {"name": "critical-repo", "org": "organvm-i-theoria", "description": "", "portfolio_relevance": "CRITICAL"},
                {"name": "high-repo", "org": "organvm-i-theoria", "description": "", "portfolio_relevance": "HIGH"},
                {"name": "medium-repo", "org": "organvm-i-theoria", "description": "", "portfolio_relevance": "MEDIUM"},
                {"name": "low-repo", "org": "organvm-i-theoria", "description": "", "portfolio_relevance": "LOW"},
            ],
        }
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json.dump(registry, f)
            path = Path(f.name)

        gallery = collect_from_registry(path)
        assert gallery.works[0].featured is True   # CRITICAL
        assert gallery.works[1].featured is True   # HIGH
        assert gallery.works[2].featured is False  # MEDIUM
        assert gallery.works[3].featured is False  # LOW

    def test_missing_fields_graceful(self):
        """Registry entries with missing optional fields are handled gracefully."""
        registry = {
            "repositories": [
                {"name": "bare-repo"},
            ],
        }
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json.dump(registry, f)
            path = Path(f.name)

        gallery = collect_from_registry(path)
        work = gallery.works[0]
        assert work.title == "bare-repo"
        assert work.organ == ""
        assert work.description == ""
        assert work.featured is False

    def test_empty_registry(self):
        """Empty repositories list produces empty gallery."""
        registry = {"repositories": []}
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json.dump(registry, f)
            path = Path(f.name)

        gallery = collect_from_registry(path)
        assert len(gallery.works) == 0
        assert gallery.name == "ORGAN System Portfolio"

    def test_repos_key_fallback(self):
        """Registry with 'repos' key instead of 'repositories' still works."""
        registry = {
            "repos": [
                {"name": "fallback-repo", "org": "organvm-ii-poiesis", "description": "test"},
            ],
        }
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json.dump(registry, f)
            path = Path(f.name)

        gallery = collect_from_registry(path)
        assert len(gallery.works) == 1
        assert gallery.works[0].title == "fallback-repo"

    def test_unknown_org_defaults_to_software(self):
        """An org not in ORGAN_MEDIUM_MAP defaults to SOFTWARE medium."""
        registry = {
            "repositories": [
                {"name": "unknown-org-repo", "org": "organvm-viii-meta", "description": "meta repo"},
            ],
        }
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json.dump(registry, f)
            path = Path(f.name)

        gallery = collect_from_registry(path)
        assert gallery.works[0].medium.value == "software"
