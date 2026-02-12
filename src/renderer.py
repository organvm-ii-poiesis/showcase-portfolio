"""Render galleries to various output formats."""

from __future__ import annotations

from .gallery import Gallery


def render_markdown(gallery: Gallery) -> str:
    """Render a gallery as Markdown."""
    lines = [f"# {gallery.name}", "", gallery.description, ""]

    featured = gallery.featured_works()
    if featured:
        lines.append("## Featured Works")
        lines.append("")
        for work in featured:
            lines.append(f"### {work.title}")
            lines.append(f"*{work.medium.value}* | {work.organ}")
            lines.append("")
            lines.append(work.description)
            if work.tags:
                lines.append(f"\nTags: {', '.join(work.tags)}")
            lines.append("")

    lines.append("## All Works")
    lines.append("")
    lines.append(f"Total: {len(gallery.works)} works")
    lines.append("")

    for work in gallery.works:
        lines.append(f"- **{work.title}** ({work.medium.value}) — {work.organ}")

    return "\n".join(lines)


def render_summary(gallery: Gallery) -> dict:
    """Generate a summary dict of the gallery."""
    medium_counts: dict[str, int] = {}
    organ_counts: dict[str, int] = {}

    for work in gallery.works:
        medium_counts[work.medium.value] = medium_counts.get(work.medium.value, 0) + 1
        organ_counts[work.organ] = organ_counts.get(work.organ, 0) + 1

    return {
        "total_works": len(gallery.works),
        "featured_count": len(gallery.featured_works()),
        "by_medium": medium_counts,
        "by_organ": organ_counts,
    }
