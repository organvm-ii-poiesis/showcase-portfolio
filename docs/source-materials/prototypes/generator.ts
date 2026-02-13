import type { StyleDNA } from "./analyzer";
import { SmartGenerator } from "./ai-engine";

/**
 * Applies MET4 stylistic transformations to a raw text based on Style DNA.
 * Uses the Semantic AI Engine for context-aware generation.
 */
export function transformText(rawText: string, dna: StyleDNA): string {
  const engine = new SmartGenerator(dna);
  return engine.generate(rawText);
}
