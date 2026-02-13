import type { StyleDNA } from "./analyzer";
import ontologyData from "@/data/ontology.json";

interface OntologyMapping {
  mappings: Record<string, string>;
  categories: Record<string, { label: string; color: string }>;
}

const ENTITY_NAME_MAP: Record<string, string> = {
  "@DAFNE": "Daphne",
  "@APOLO": "Apollo",
  "@JOV": "Jove",
  "@NARSISVS": "Narcissus",
  "@EKO": "Echo",
  "@HERMAFRODITVS": "Hermaphroditus",
  "@PERSEVS": "Perseus",
  "@MINERVA": "Minerva",
  "@VENVS": "Venus",
  "@MARS": "Mars",
};

const THEMATIC_FLAVORS: Record<string, string[]> = {
  avian: ["wing-beat", "sky-drift", "feather-logic"],
  floral: ["root-lock", "photosynthesis", "bloom-sequence"],
  mineral: ["stone-code", "geologic-time", "solid-state"],
  divine: ["sky-fire", "immortal-loop", "thunder-syntax"],
  aquatic: ["fluid-dynamics", "wave-form", "depth-pressure"],
  mammalian: ["blood-heat", "fur-pattern", "instinct-mode"],
  stellar: ["orbit-decay", "constellation-map", "light-speed"],
  arboreal: ["bark-skin", "leaf-network", "sap-flow"],
};

/**
 * A sophisticated generator that uses the project's ontology and style DNA
 * to create context-aware metamorphoses.
 */
export class SmartGenerator {
  private dna: StyleDNA;
  private ontology: OntologyMapping;

  constructor(dna: StyleDNA) {
    this.dna = dna;
    this.ontology = ontologyData as unknown as OntologyMapping;
  }

  /**
   * Generates text that respects the semantic category of the input entities.
   * @param input The raw source text to transform.
   * @returns The "MET4-ified" synthetic text.
   */
  public generate(input: string): string {
    let text = input;

    // 1. Semantic Entity Injection
    Object.entries(this.ontology.mappings).forEach(([handle, category]) => {
      const name = ENTITY_NAME_MAP[handle] || handle.replace("@", "");
      const regex = new RegExp(`\\b${name}\\b`, "gi");

      if (regex.test(text)) {
        text = text.replace(regex, handle);
        
        // Stochastic thematic flavor injection
        if (Math.random() > 0.75) {
          const flavors = THEMATIC_FLAVORS[category] || ["metamorphosis"];
          const flavor = flavors[Math.floor(Math.random() * flavors.length)];
          text = text.replace(handle, `${handle} [${flavor}]`);
        }
      }
    });

    return this.applyGlitch(text);
  }

  /**
   * Applies stylistic glitches based on the provided Style DNA.
   * @param text The text to glitch.
   * @returns The glitched text with variable casing and fragmentation.
   */
  private applyGlitch(text: string): string {
    const words = text.split(/\s+/);
    const result: string[] = [];

    words.forEach((word) => {
      result.push(word);

      const roll = Math.random() * 100;
      
      // Handle fragmentation (line breaks)
      if (roll < this.dna.fragmentationScore / 6) {
        result.push("\n\n");
      } 
      // Handle extra spacing
      else if (roll < this.dna.fragmentationScore / 2) {
        result.push("   ");
      }

      // Handle capitalization
      if (Math.random() * 100 < this.dna.glitchPatterns.capsLockRatio * 100) {
        result[result.length - 1] = result[result.length - 1].toUpperCase();
      }
    });

    return result.join(" ").trim();
  }
}
