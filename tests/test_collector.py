"""Tests for the collector module."""

import json
import tempfile
from pathlib import Path

from src.collector import collect_from_works_file


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
