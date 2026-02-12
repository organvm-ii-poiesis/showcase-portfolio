"""Gallery model for organizing creative works."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from enum import Enum


class Medium(str, Enum):
    """Creative medium categories."""
    GENERATIVE_ART = "generative-art"
    PERFORMANCE = "performance"
    INTERACTIVE = "interactive"
    LITERARY = "literary"
    MUSICAL = "musical"
    MIXED_MEDIA = "mixed-media"
    SOFTWARE = "software"


@dataclass
class Work:
    """A single creative work in the portfolio."""
    title: str
    description: str
    medium: Medium
    organ: str
    repo: str
    date_created: date | None = None
    tags: list[str] = field(default_factory=list)
    url: str = ""
    featured: bool = False

    @property
    def slug(self) -> str:
        return self.title.lower().replace(" ", "-").replace("'", "")


@dataclass
class Gallery:
    """A curated collection of works."""
    name: str
    description: str
    works: list[Work] = field(default_factory=list)

    def add_work(self, work: Work) -> None:
        self.works.append(work)

    def featured_works(self) -> list[Work]:
        return [w for w in self.works if w.featured]

    def by_medium(self, medium: Medium) -> list[Work]:
        return [w for w in self.works if w.medium == medium]

    def by_organ(self, organ: str) -> list[Work]:
        return [w for w in self.works if w.organ == organ]

    def search(self, query: str) -> list[Work]:
        q = query.lower()
        return [
            w for w in self.works
            if q in w.title.lower()
            or q in w.description.lower()
            or any(q in tag.lower() for tag in w.tags)
        ]
