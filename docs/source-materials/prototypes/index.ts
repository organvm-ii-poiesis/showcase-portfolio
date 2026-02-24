import type { CanonicalSection } from "@/types/content";

/**
 * Generates a URL-friendly slug from a string.
 * @param value The string to slugify.
 * @returns A normalized kebab-case slug.
 */
export function slugify(value: string): string {
  return value
    .toLowerCase()
    .replace(/[^a-z0-9\s-]/g, "")
    .trim()
    .replace(/\s+/g, "-")
    .replace(/-+/g, "-");
}

/**
 * Normalizes raw text from PDF extraction for Markdown consistency.
 * Handles line endings, trailing whitespace, and thesis-specific markers.
 * @param raw The raw text string from extraction.
 * @returns Normalized Markdown-ready text.
 */
export function normalizeText(raw: string): string {
  const withUnixLines = raw.replace(/\r\n?/g, "\n").replace(/\f/g, "\n\n");
  const noTrailing = withUnixLines
    .split("\n")
    .map((line) => line.replace(/[ \t]+$/g, ""))
    .join("\n");

  const sectionized = noTrailing
    .split("\n")
    .map((line) => {
      // Look for markers like " > TITLE < " which often indicate cycle or section breaks in the thesis
      const markerMatch = line.match(/^[-—\s]*>\s*(.+?)\s*<\s*[-—\s]*$/);
      if (markerMatch) {
        return `## ${markerMatch[1]}`;
      }
      return line;
    })
    .join("\n");

  return sectionized.replace(/\n{3,}/g, "\n\n").trim();
}

/**
 * Parses normalized Markdown text into structured CanonicalSections.
 * Ensures unique anchors and IDs using a document-level prefix.
 * @param markdown The document content in Markdown format.
 * @param docSlug The unique slug for the document (used for ID prefixing).
 * @returns An array of parsed sections with unique IDs and anchors.
 */
export function parseSections(markdown: string, docSlug: string): CanonicalSection[] {
  const lines = markdown.replace(/\r\n?/g, "\n").split("\n");

  const sections: CanonicalSection[] = [];
  const anchorCounts = new Map<string, number>();
  let currentTitle = "Full Text";
  let buffer: string[] = [];
  let order = 1;

  const commitSection = () => {
    const body = buffer.join("\n").trim();
    if (!body) {
      return;
    }

    const baseAnchor = slugify(currentTitle || `section-${order}`) || `section-${order}`;
    const currentCount = anchorCounts.get(baseAnchor) ?? 0;
    const nextCount = currentCount + 1;
    anchorCounts.set(baseAnchor, nextCount);
    
    // Create a unique anchor within the document
    const anchor = nextCount > 1 ? `${baseAnchor}-${nextCount}` : baseAnchor;
    
    // Create a unique ID across the entire project (doc-anchor-order)
    const id = `${docSlug}-${anchor}-${order}`;

    sections.push({
      id,
      title: currentTitle,
      order,
      anchor,
      body,
    });
    order += 1;
  };

  for (const line of lines) {
    // Skip the main document title (h1)
    if (line.startsWith("# ")) {
      continue;
    }

    // Treat h2 as a section separator
    if (line.startsWith("## ")) {
      commitSection();
      currentTitle = line.replace(/^##\s+/, "").trim();
      buffer = [];
      continue;
    }

    buffer.push(line);
  }

  commitSection();
  return sections;
}
