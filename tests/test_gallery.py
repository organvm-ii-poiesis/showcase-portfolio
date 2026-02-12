"""Tests for the gallery model."""

from src.gallery import Gallery, Medium, Work


def _sample_work(**overrides) -> Work:
    defaults = {
        "title": "Test Work",
        "description": "A test creative work",
        "medium": Medium.GENERATIVE_ART,
        "organ": "organvm-ii-poiesis",
        "repo": "test-repo",
    }
    defaults.update(overrides)
    return Work(**defaults)


class TestWork:
    def test_slug_generation(self):
        work = _sample_work(title="My Creative Work")
        assert work.slug == "my-creative-work"

    def test_default_not_featured(self):
        work = _sample_work()
        assert work.featured is False

    def test_tags_default_empty(self):
        work = _sample_work()
        assert work.tags == []


class TestGallery:
    def test_add_work(self):
        gallery = Gallery(name="Test", description="Test gallery")
        gallery.add_work(_sample_work())
        assert len(gallery.works) == 1

    def test_featured_works(self):
        gallery = Gallery(name="Test", description="")
        gallery.add_work(_sample_work(featured=True))
        gallery.add_work(_sample_work(featured=False))
        assert len(gallery.featured_works()) == 1

    def test_by_medium(self):
        gallery = Gallery(name="Test", description="")
        gallery.add_work(_sample_work(medium=Medium.GENERATIVE_ART))
        gallery.add_work(_sample_work(medium=Medium.PERFORMANCE))
        gallery.add_work(_sample_work(medium=Medium.GENERATIVE_ART))
        assert len(gallery.by_medium(Medium.GENERATIVE_ART)) == 2

    def test_by_organ(self):
        gallery = Gallery(name="Test", description="")
        gallery.add_work(_sample_work(organ="organvm-i-theoria"))
        gallery.add_work(_sample_work(organ="organvm-ii-poiesis"))
        assert len(gallery.by_organ("organvm-i-theoria")) == 1

    def test_search(self):
        gallery = Gallery(name="Test", description="")
        gallery.add_work(_sample_work(title="Recursive Engine", tags=["recursion"]))
        gallery.add_work(_sample_work(title="Other Thing"))
        assert len(gallery.search("recursive")) == 1
        assert len(gallery.search("recursion")) == 1

    def test_search_case_insensitive(self):
        gallery = Gallery(name="Test", description="")
        gallery.add_work(_sample_work(title="Recursive Engine"))
        assert len(gallery.search("RECURSIVE")) == 1
