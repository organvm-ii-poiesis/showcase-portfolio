import type { MetadataRoute } from "next";

import { getAllEvolutionaryDocs, getCanonicalManifest } from "@/lib/content";

export default async function sitemap(): Promise<MetadataRoute.Sitemap> {
  const baseUrl = "https://met4morfoses.com";
  const lastModified = new Date("2018-03-20");

  const staticRoutes: MetadataRoute.Sitemap = [
    { url: baseUrl, lastModified, changeFrequency: "monthly", priority: 1.0 },
    { url: `${baseUrl}/feed`, lastModified, changeFrequency: "monthly", priority: 0.8 },
    { url: `${baseUrl}/scroll`, lastModified, changeFrequency: "monthly", priority: 0.8 },
    { url: `${baseUrl}/oracle`, lastModified, changeFrequency: "monthly", priority: 0.7 },
    { url: `${baseUrl}/archive`, lastModified, changeFrequency: "monthly", priority: 0.6 },
    { url: `${baseUrl}/about`, lastModified, changeFrequency: "monthly", priority: 0.5 },
  ];

  const canonicalDocs = getCanonicalManifest();
  const readRoutes: MetadataRoute.Sitemap = canonicalDocs.map((doc) => ({
    url: `${baseUrl}/read/${doc.slug}`,
    lastModified,
    changeFrequency: "monthly" as const,
    priority: 0.9,
  }));

  const evolutionaryDocs = await getAllEvolutionaryDocs();
  const evolutionRoutes: MetadataRoute.Sitemap = evolutionaryDocs.map((doc) => ({
    url: `${baseUrl}/evolution/${doc.slug}`,
    lastModified,
    changeFrequency: "monthly" as const,
    priority: 0.6,
  }));

  return [...staticRoutes, ...readRoutes, ...evolutionRoutes];
}
