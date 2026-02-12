"""Render galleries to various output formats."""

from __future__ import annotations

import json as json_module
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


def render_html(gallery: Gallery) -> str:
    """Render a gallery as a simple HTML portfolio page."""
    parts: list[str] = []
    parts.append("<!DOCTYPE html>")
    parts.append("<html lang=\"en\">")
    parts.append("<head>")
    parts.append(f"  <meta charset=\"utf-8\">")
    parts.append(f"  <title>{gallery.name}</title>")
    parts.append("  <style>")
    parts.append("    body { font-family: Georgia, serif; max-width: 800px; margin: 2rem auto; padding: 0 1rem; }")
    parts.append("    .work { margin-bottom: 2rem; border-bottom: 1px solid #ddd; padding-bottom: 1rem; }")
    parts.append("    .medium { color: #666; font-style: italic; }")
    parts.append("    .tags { color: #888; font-size: 0.9em; }")
    parts.append("    .featured { border-left: 4px solid #c9a227; padding-left: 1rem; }")
    parts.append("  </style>")
    parts.append("</head>")
    parts.append("<body>")
    parts.append(f"  <h1>{gallery.name}</h1>")
    parts.append(f"  <p>{gallery.description}</p>")

    featured = gallery.featured_works()
    if featured:
        parts.append("  <h2>Featured Works</h2>")
        for work in featured:
            parts.append(f"  <div class=\"work featured\">")
            parts.append(f"    <h3>{work.title}</h3>")
            parts.append(f"    <p class=\"medium\">{work.medium.value} | {work.organ}</p>")
            parts.append(f"    <p>{work.description}</p>")
            if work.tags:
                parts.append(f"    <p class=\"tags\">Tags: {', '.join(work.tags)}</p>")
            parts.append(f"  </div>")

    parts.append("  <h2>All Works</h2>")
    parts.append(f"  <p>Total: {len(gallery.works)} works</p>")
    parts.append("  <ul>")
    for work in gallery.works:
        parts.append(f"    <li><strong>{work.title}</strong> ({work.medium.value}) &mdash; {work.organ}</li>")
    parts.append("  </ul>")
    parts.append("</body>")
    parts.append("</html>")

    return "\n".join(parts)


def render_json(gallery: Gallery) -> str:
    """Export gallery as JSON for API consumption."""
    data = {
        "gallery": {
            "name": gallery.name,
            "description": gallery.description,
            "total_works": len(gallery.works),
            "featured_count": len(gallery.featured_works()),
        },
        "works": [],
    }

    for work in gallery.works:
        work_dict = {
            "title": work.title,
            "description": work.description,
            "medium": work.medium.value,
            "organ": work.organ,
            "repo": work.repo,
            "tags": work.tags,
            "featured": work.featured,
            "slug": work.slug,
        }
        if work.date_created:
            work_dict["date_created"] = work.date_created.isoformat()
        if work.url:
            work_dict["url"] = work.url
        data["works"].append(work_dict)

    return json_module.dumps(data, indent=2)
