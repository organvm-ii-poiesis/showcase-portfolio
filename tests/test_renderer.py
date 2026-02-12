"""Tests for the renderer module."""

from __future__ import annotations

import json

from src.gallery import Gallery, Medium, Work
from src.renderer import render_html, render_json, render_markdown, render_summary


def _sample_work(**overrides) -> Work:
    defaults = {
        "title": "Test Work",
        "description": "A test creative work for rendering",
        "medium": Medium.GENERATIVE_ART,
        "organ": "organvm-ii-poiesis",
        "repo": "test-repo",
    }
    defaults.update(overrides)
    return Work(**defaults)


def _populated_gallery() -> Gallery:
    """Build a gallery with diverse works for testing."""
    gallery = Gallery(
        name="Test Portfolio",
        description="A test portfolio for renderer validation",
    )
    gallery.add_work(_sample_work(
        title="Featured Art",
        medium=Medium.GENERATIVE_ART,
        organ="organvm-ii-poiesis",
        featured=True,
        tags=["generative", "art"],
    ))
    gallery.add_work(_sample_work(
        title="Featured Software",
        medium=Medium.SOFTWARE,
        organ="organvm-i-theoria",
        featured=True,
        tags=["recursion"],
    ))
    gallery.add_work(_sample_work(
        title="Regular Performance",
        medium=Medium.PERFORMANCE,
        organ="organvm-ii-poiesis",
        featured=False,
        tags=["performance", "live"],
    ))
    gallery.add_work(_sample_work(
        title="Musical Piece",
        medium=Medium.MUSICAL,
        organ="organvm-ii-poiesis",
        featured=False,
    ))
    return gallery


class TestRenderMarkdown:
    def test_contains_gallery_name(self):
        gallery = _populated_gallery()
        md = render_markdown(gallery)
        assert "# Test Portfolio" in md

    def test_contains_description(self):
        gallery = _populated_gallery()
        md = render_markdown(gallery)
        assert "A test portfolio for renderer validation" in md

    def test_featured_section_present(self):
        gallery = _populated_gallery()
        md = render_markdown(gallery)
        assert "## Featured Works" in md
        assert "### Featured Art" in md
        assert "### Featured Software" in md

    def test_all_works_section_with_count(self):
        gallery = _populated_gallery()
        md = render_markdown(gallery)
        assert "## All Works" in md
        assert "Total: 4 works" in md

    def test_all_works_listed(self):
        gallery = _populated_gallery()
        md = render_markdown(gallery)
        assert "**Featured Art**" in md
        assert "**Regular Performance**" in md
        assert "**Musical Piece**" in md

    def test_empty_gallery(self):
        gallery = Gallery(name="Empty", description="Nothing here")
        md = render_markdown(gallery)
        assert "# Empty" in md
        assert "Total: 0 works" in md
        assert "## Featured Works" not in md

    def test_tags_rendered(self):
        gallery = _populated_gallery()
        md = render_markdown(gallery)
        assert "generative" in md
        assert "art" in md


class TestRenderSummary:
    def test_total_works_count(self):
        gallery = _populated_gallery()
        summary = render_summary(gallery)
        assert summary["total_works"] == 4

    def test_featured_count(self):
        gallery = _populated_gallery()
        summary = render_summary(gallery)
        assert summary["featured_count"] == 2

    def test_counts_by_medium(self):
        gallery = _populated_gallery()
        summary = render_summary(gallery)
        by_medium = summary["by_medium"]
        assert by_medium["generative-art"] == 1
        assert by_medium["software"] == 1
        assert by_medium["performance"] == 1
        assert by_medium["musical"] == 1

    def test_counts_by_organ(self):
        gallery = _populated_gallery()
        summary = render_summary(gallery)
        by_organ = summary["by_organ"]
        assert by_organ["organvm-ii-poiesis"] == 3
        assert by_organ["organvm-i-theoria"] == 1

    def test_empty_gallery_summary(self):
        gallery = Gallery(name="Empty", description="")
        summary = render_summary(gallery)
        assert summary["total_works"] == 0
        assert summary["featured_count"] == 0
        assert summary["by_medium"] == {}
        assert summary["by_organ"] == {}


class TestRenderHtml:
    def test_valid_html_structure(self):
        gallery = _populated_gallery()
        html = render_html(gallery)
        assert "<!DOCTYPE html>" in html
        assert "<html" in html
        assert "</html>" in html
        assert "<head>" in html
        assert "<body>" in html

    def test_contains_title(self):
        gallery = _populated_gallery()
        html = render_html(gallery)
        assert "<title>Test Portfolio</title>" in html
        assert "<h1>Test Portfolio</h1>" in html

    def test_featured_section(self):
        gallery = _populated_gallery()
        html = render_html(gallery)
        assert "<h2>Featured Works</h2>" in html
        assert "featured" in html  # CSS class for featured works

    def test_all_works_listed(self):
        gallery = _populated_gallery()
        html = render_html(gallery)
        assert "<strong>Featured Art</strong>" in html
        assert "<strong>Regular Performance</strong>" in html
        assert "<strong>Musical Piece</strong>" in html
        assert "<strong>Featured Software</strong>" in html

    def test_includes_medium_and_organ(self):
        gallery = _populated_gallery()
        html = render_html(gallery)
        assert "generative-art" in html
        assert "organvm-ii-poiesis" in html

    def test_empty_gallery_html(self):
        gallery = Gallery(name="Empty", description="Nothing")
        html = render_html(gallery)
        assert "<h1>Empty</h1>" in html
        assert "Total: 0 works" in html
        assert "<h2>Featured Works</h2>" not in html

    def test_tags_in_html(self):
        gallery = _populated_gallery()
        html = render_html(gallery)
        assert "generative" in html
        assert "recursion" in html


class TestRenderJson:
    def test_valid_json(self):
        gallery = _populated_gallery()
        output = render_json(gallery)
        data = json.loads(output)
        assert isinstance(data, dict)

    def test_gallery_metadata(self):
        gallery = _populated_gallery()
        output = render_json(gallery)
        data = json.loads(output)
        assert data["gallery"]["name"] == "Test Portfolio"
        assert data["gallery"]["total_works"] == 4
        assert data["gallery"]["featured_count"] == 2

    def test_works_count(self):
        gallery = _populated_gallery()
        output = render_json(gallery)
        data = json.loads(output)
        assert len(data["works"]) == 4

    def test_preserves_all_fields(self):
        gallery = _populated_gallery()
        output = render_json(gallery)
        data = json.loads(output)
        first_work = data["works"][0]
        assert "title" in first_work
        assert "description" in first_work
        assert "medium" in first_work
        assert "organ" in first_work
        assert "repo" in first_work
        assert "tags" in first_work
        assert "featured" in first_work
        assert "slug" in first_work

    def test_featured_flag_preserved(self):
        gallery = _populated_gallery()
        output = render_json(gallery)
        data = json.loads(output)
        featured_works = [w for w in data["works"] if w["featured"]]
        assert len(featured_works) == 2

    def test_empty_gallery_json(self):
        gallery = Gallery(name="Empty", description="")
        output = render_json(gallery)
        data = json.loads(output)
        assert data["gallery"]["total_works"] == 0
        assert data["works"] == []

    def test_slug_generated(self):
        gallery = Gallery(name="Test", description="")
        gallery.add_work(_sample_work(title="My Great Work"))
        output = render_json(gallery)
        data = json.loads(output)
        assert data["works"][0]["slug"] == "my-great-work"
