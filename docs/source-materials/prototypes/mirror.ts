import mirrorManifest from "@/data/mirror-manifest.json";
import type { MirrorAsset } from "@/types/content";

const allAssets = mirrorManifest as MirrorAsset[];

export type MirrorFilter = {
  query?: string;
  ext?: string;
};

export function getAllMirrorAssets(): MirrorAsset[] {
  return allAssets;
}

export function getMirrorExtensionCounts(): Record<string, number> {
  return allAssets.reduce<Record<string, number>>((accumulator, asset) => {
    const ext = asset.ext || "unknown";
    accumulator[ext] = (accumulator[ext] ?? 0) + 1;
    return accumulator;
  }, {});
}

export function filterMirrorAssets(filter: MirrorFilter): MirrorAsset[] {
  const query = filter.query?.trim().toLowerCase() ?? "";
  const ext = filter.ext?.trim().toLowerCase() ?? "";

  return allAssets.filter((asset) => {
    if (ext && asset.ext !== ext) {
      return false;
    }

    if (!query) {
      return true;
    }

    return [asset.fileName, asset.relativePath, asset.sourceFolder].some((value) =>
      value.toLowerCase().includes(query),
    );
  });
}

export function formatBytes(sizeBytes: number): string {
  if (sizeBytes < 1024) {
    return `${sizeBytes} B`;
  }

  const units = ["KB", "MB", "GB"];
  let value = sizeBytes / 1024;
  let unitIndex = 0;

  while (value >= 1024 && unitIndex < units.length - 1) {
    value /= 1024;
    unitIndex += 1;
  }

  return `${value.toFixed(1)} ${units[unitIndex]}`;
}
