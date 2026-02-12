"""CLI entry point for showcase-portfolio.

Usage:
    python -m src generate [--output PATH]
    python -m src summary
    python -m src search QUERY
    python -m src featured
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .collector import collect_from_works_file
from .renderer import render_html, render_json, render_markdown, render_summary


DEFAULT_WORKS_PATH = Path(__file__).parent.parent / "data" / "works.json"


def cmd_generate(args: argparse.Namespace) -> None:
    """Generate portfolio from works.json and output as markdown, HTML, or JSON."""
    works_path = Path(args.works) if args.works else DEFAULT_WORKS_PATH
    gallery = collect_from_works_file(works_path)

    if args.format == "html":
        output = render_html(gallery)
    elif args.format == "json":
        output = render_json(gallery)
    else:
        output = render_markdown(gallery)

    if args.output:
        Path(args.output).write_text(output, encoding="utf-8")
        print(f"Portfolio written to {args.output}")
    else:
        print(output)


def cmd_summary(args: argparse.Namespace) -> None:
    """Print portfolio statistics."""
    works_path = Path(args.works) if args.works else DEFAULT_WORKS_PATH
    gallery = collect_from_works_file(works_path)
    summary = render_summary(gallery)

    print(f"Portfolio: {gallery.name}")
    print(f"Total works: {summary['total_works']}")
    print(f"Featured: {summary['featured_count']}")
    print()
    print("By medium:")
    for medium, count in sorted(summary["by_medium"].items()):
        print(f"  {medium}: {count}")
    print()
    print("By organ:")
    for organ, count in sorted(summary["by_organ"].items()):
        print(f"  {organ}: {count}")


def cmd_search(args: argparse.Namespace) -> None:
    """Search works by keyword."""
    works_path = Path(args.works) if args.works else DEFAULT_WORKS_PATH
    gallery = collect_from_works_file(works_path)
    results = gallery.search(args.query)

    if not results:
        print(f"No works found matching '{args.query}'")
        sys.exit(0)

    print(f"Found {len(results)} work(s) matching '{args.query}':")
    print()
    for work in results:
        featured_mark = " [FEATURED]" if work.featured else ""
        print(f"  {work.title} ({work.medium.value}) — {work.organ}{featured_mark}")
        print(f"    {work.description[:100]}...")
        print()


def cmd_featured(args: argparse.Namespace) -> None:
    """List only featured works."""
    works_path = Path(args.works) if args.works else DEFAULT_WORKS_PATH
    gallery = collect_from_works_file(works_path)
    featured = gallery.featured_works()

    if not featured:
        print("No featured works found.")
        sys.exit(0)

    print(f"Featured works ({len(featured)}):")
    print()
    for work in featured:
        print(f"  {work.title}")
        print(f"    {work.medium.value} | {work.organ} | {work.repo}")
        print(f"    {work.description[:120]}...")
        print()


def main() -> None:
    """Parse arguments and dispatch to subcommands."""
    parser = argparse.ArgumentParser(
        prog="showcase-portfolio",
        description="Portfolio aggregation engine for the ORGAN creative system",
    )
    parser.add_argument(
        "--works",
        default=None,
        help=f"Path to works.json (default: {DEFAULT_WORKS_PATH})",
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # generate
    gen_parser = subparsers.add_parser("generate", help="Generate portfolio output")
    gen_parser.add_argument("--output", "-o", help="Output file path (default: stdout)")
    gen_parser.add_argument(
        "--format", "-f",
        choices=["markdown", "html", "json"],
        default="markdown",
        help="Output format (default: markdown)",
    )

    # summary
    subparsers.add_parser("summary", help="Print portfolio statistics")

    # search
    search_parser = subparsers.add_parser("search", help="Search works by keyword")
    search_parser.add_argument("query", help="Search query")

    # featured
    subparsers.add_parser("featured", help="List featured works")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    commands = {
        "generate": cmd_generate,
        "summary": cmd_summary,
        "search": cmd_search,
        "featured": cmd_featured,
    }
    commands[args.command](args)


if __name__ == "__main__":
    main()
