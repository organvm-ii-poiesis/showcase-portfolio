import { normalizeText } from "../content-engine";

/**
 * Quantifiable stylistic metrics for a block of MET4 text.
 */
export interface StyleDNA {
  /** Map of character/concept handles to their frequency. */
  entityRegistry: Record<string, number>;
  /** Unique word count. */
  vocabularySize: number;
  /** Mean word count per sentence. */
  avgSentenceLength: number;
  /** Percentage of symbols/fragmentation markers per word. */
  fragmentationScore: number;
  /** Patterns specifically identifying the "glitch" aesthetic. */
  glitchPatterns: {
    /** Ratio of uppercase characters to total characters. */
    capsLockRatio: number;
    /** Ratio of non-alphanumeric symbols to total characters. */
    symbolDensity: number;
  };
}

/**
 * Scans raw text and extracts its stylistic "DNA".
 * @param rawText The source text to analyze.
 * @returns A StyleDNA object quantifying the text's properties.
 */
export function analyzeText(rawText: string): StyleDNA {
  const text = normalizeText(rawText);
  const words = text.split(/\s+/).filter(w => w.length > 0);
  const sentences = text.split(/[.!?]+/).filter(s => s.trim().length > 0);
  
  // Entity Registry (starts with @)
  const entityRegistry: Record<string, number> = {};
  words.forEach(word => {
    if (word.startsWith("@") && word.length > 1) {
      const entity = word.replace(/[^@a-zA-Z0-9-]/g, "").toUpperCase();
      entityRegistry[entity] = (entityRegistry[entity] || 0) + 1;
    }
  });

  // Glitch Analysis
  const upperCaseCount = text.replace(/[^A-Z]/g, "").length;
  const symbolCount = text.replace(/[a-zA-Z0-9\s]/g, "").length;
  
  // Heuristic for fragmentation: lots of short segments separated by symbols
  const fragmentationScore = words.length > 0 ? (symbolCount / words.length) * 100 : 0;

  return {
    entityRegistry,
    vocabularySize: new Set(words.map(w => w.toLowerCase())).size,
    avgSentenceLength: words.length / (sentences.length || 1),
    fragmentationScore,
    glitchPatterns: {
      capsLockRatio: text.length > 0 ? upperCaseCount / text.length : 0,
      symbolDensity: text.length > 0 ? symbolCount / text.length : 0
    }
  };
}

/**
 * Aggregates multiple StyleDNA reports into a single project-level profile.
 * @param dnas Array of individual document DNAs.
 * @returns An averaged project-level StyleDNA.
 */
export function mergeDNA(dnas: StyleDNA[]): StyleDNA {
  const merged: StyleDNA = {
    entityRegistry: {},
    vocabularySize: 0,
    avgSentenceLength: 0,
    fragmentationScore: 0,
    glitchPatterns: { capsLockRatio: 0, symbolDensity: 0 }
  };

  const total = dnas.length;
  if (total === 0) return merged;

  dnas.forEach(dna => {
    Object.entries(dna.entityRegistry).forEach(([key, count]) => {
      merged.entityRegistry[key] = (merged.entityRegistry[key] || 0) + count;
    });
    merged.vocabularySize += dna.vocabularySize;
    merged.avgSentenceLength += dna.avgSentenceLength;
    merged.fragmentationScore += dna.fragmentationScore;
    merged.glitchPatterns.capsLockRatio += dna.glitchPatterns.capsLockRatio;
    merged.glitchPatterns.symbolDensity += dna.glitchPatterns.symbolDensity;
  });

  // Average out the metrics
  merged.avgSentenceLength /= total;
  merged.fragmentationScore /= total;
  merged.glitchPatterns.capsLockRatio /= total;
  merged.glitchPatterns.symbolDensity /= total;

  return merged;
}
