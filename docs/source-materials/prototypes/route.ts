import { NextResponse } from "next/server";

import { getCanonicalManifest } from "@/lib/content";
import type { CanonicalManifestApiResponse } from "@/types/api";

export async function GET() {
  const items = getCanonicalManifest().map((doc) => ({
    id: doc.id,
    slug: doc.slug,
    title: doc.title,
    order: doc.order,
    sourcePdf: doc.sourcePdf,
    markdownPath: doc.markdownPath,
    wordCount: doc.wordCount,
  }));

  const response: CanonicalManifestApiResponse = {
    ok: true,
    count: items.length,
    items,
  };

  return NextResponse.json(response, { status: 200 });
}
