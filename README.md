# Showcase Portfolio

[![CI](https://github.com/organvm-ii-poiesis/showcase-portfolio/actions/workflows/ci.yml/badge.svg)](https://github.com/organvm-ii-poiesis/showcase-portfolio/actions/workflows/ci.yml)
[![Coverage](https://img.shields.io/badge/coverage-pending-lightgrey)](https://github.com/organvm-ii-poiesis/showcase-portfolio)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/organvm-ii-poiesis/showcase-portfolio/blob/main/LICENSE)
[![Organ II](https://img.shields.io/badge/Organ-II%20Poiesis-EC4899)](https://github.com/organvm-ii-poiesis)
[![Status](https://img.shields.io/badge/status-active-brightgreen)](https://github.com/organvm-ii-poiesis/showcase-portfolio)
[![Markdown](https://img.shields.io/badge/lang-Markdown-informational)](https://github.com/organvm-ii-poiesis/showcase-portfolio)


[![ORGAN-II: Poiesis](https://img.shields.io/badge/ORGAN--II-Poiesis-6a1b9a?style=flat-square)](https://github.com/organvm-ii-poiesis)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue?style=flat-square)](LICENSE)
[![Status](https://img.shields.io/badge/status-active--development-yellow?style=flat-square)]()

> A living portfolio and exhibition-ready presentation layer for generative art, interactive installations, performance documentation, and AI-human collaborations produced across the ORGAN-II ecosystem.

[Artistic Purpose](#artistic-purpose) | [Conceptual Approach](#conceptual-approach) | [Technical Overview](#technical-overview) | [Installation](#installation) | [Quick Start](#quick-start) | [Working Examples](#working-examples) | [Theory Implemented](#theory-implemented) | [Portfolio & Exhibition](#portfolio--exhibition) | [Related Work](#related-work) | [Contributing](#contributing) | [License](#license) | [Author & Contact](#author--contact)

---

## Artistic Purpose

Every artwork exists in at least two states: the state of making and the state of being seen. The studio and the gallery are not the same space, and the work that moves between them requires translation. A generative algorithm running in a terminal is not the same object as that algorithm's output framed on a wall, projected in a darkened room, or documented in a grant application. The gap between creation and exhibition is not incidental — it is a compositional problem in its own right, and this repository exists to address it.

Showcase Portfolio is the aggregation, curation, and exhibition infrastructure for the entire ORGAN-II ecosystem. It gathers work produced across more than a dozen repositories — real-time performance systems, generative visual engines, AI-assisted composition tools, interactive theatre frameworks, motion-capture experiments, audience-participatory installations — and presents them as a coherent body of artistic practice. The goal is not merely to list projects. The goal is to construct a navigable, visually compelling, exhibition-ready portfolio that communicates the intellectual seriousness, aesthetic range, and technical ambition of this creative practice to the people who decide whether it deserves support: grant reviewers, residency selection committees, gallery curators, academic collaborators, and institutional funders.

This distinction matters because the creative technology field has a persistent presentation problem. The work is often extraordinary — algorithmically sophisticated, aesthetically arresting, conceptually rigorous — but the presentation layer defaults to GitHub repository lists, personal websites that look like developer portfolios, or PDF attachments that strip away the interactivity that makes the work compelling. A generative artwork cannot be adequately represented by a screenshot and a paragraph of description any more than a symphony can be represented by its score. Showcase Portfolio provides the infrastructure for presenting computational art as art: with context, with process documentation, with exhibition history, with the kind of structured metadata that institutional evaluators need to assess the work's significance.

The system is designed to serve two audiences simultaneously. For human viewers — curators, reviewers, collaborators — it provides a visual gallery with thematic groupings, chronological navigation, medium-based filtering, and rich contextual material (artist statements, process documentation, exhibition photographs, press coverage). For institutional systems — grant databases, academic repositories, digital humanities indices — it provides structured metadata in formats that these systems can ingest: Dublin Core fields, ORCID integration points, exhibition history formatted for CV generation, and machine-readable provenance chains that trace each work from concept through exhibition to any subsequent acquisitions or citations.

---

## Conceptual Approach

### The Portfolio as Artwork

The most important design decision in this system is the refusal to treat the portfolio as a neutral container. A portfolio is itself a creative artifact. The choices about what to include, how to sequence works, which relationships to make visible, and how to frame each piece's significance — these are curatorial decisions, and curatorial decisions are aesthetic decisions. Showcase Portfolio treats the act of presenting work with the same rigor applied to making it.

This means the system supports multiple curatorial views of the same body of work. A chronological view reveals the evolution of technique and concern over time. A thematic view groups works by their conceptual preoccupations — recursion, collective agency, spatial awareness, temporal perception — regardless of when they were made. A medium view separates performance works from installation works from purely generative works. A technical view organizes by the computational methods employed: consensus algorithms, shader pipelines, machine learning models, real-time audio synthesis. Each view constructs a different narrative about the practice, and each narrative is useful in a different context: chronological for retrospective exhibitions, thematic for grant applications that emphasize intellectual coherence, medium-based for venue-specific proposals, technical for academic collaborations.

### Structured Metadata for Institutional Contexts

Grant applications, residency applications, and academic CVs require specific information in specific formats. A typical arts council application asks for: title, medium, dimensions or duration, year, venue, whether the work was commissioned or self-initiated, funding sources, collaboration credits, and a brief description. An academic CV requires the same information reorganized into categories: solo exhibitions, group exhibitions, screenings, performances, publications, invited talks. A digital humanities repository requires Dublin Core metadata: creator, title, date, format, description, subject keywords, rights statement.

Showcase Portfolio maintains a single metadata record per work and generates all of these output formats from it. The metadata schema is intentionally comprehensive — it captures more than any single output format requires, so that new formats can be generated without returning to the source material. Each work record includes fields that most portfolio systems omit: the computational method used, the source repository, the relationship to other works in the system (predecessor, variant, component, derivative), the theoretical framework it engages, and a structured process narrative that documents the journey from concept to completion.

### Integration with the ORGAN-II Ecosystem

Showcase Portfolio does not exist in isolation. It is the presentation layer for a system of repositories that each handle a different aspect of creative production. The metasystem-master repository (Omni-Dromenon Engine) produces real-time performance data that Showcase Portfolio can document: audience participation metrics, performer override patterns, consensus dynamics over time. The archive-past-works repository maintains the long-term archival records that Showcase Portfolio draws from for historical exhibitions. The case-studies-methodology repository provides the deep process documentation that Showcase Portfolio can reference when a grant application requires evidence of artistic methodology.

This integration is not decorative. When a work is created in one ORGAN-II repository, its metadata propagates through the system: the archive records its completion, the case study documents its process, and the portfolio presents it to the world. The goal is a unified creative practice where documentation, archiving, and presentation are not afterthoughts but integral parts of the work's lifecycle.

---

## Technical Overview

### Architecture

The portfolio system is built as a static site generator with dynamic data sources. The core architecture separates content (artwork metadata, images, documentation) from presentation (templates, layouts, navigation logic) and from data (structured JSON records that drive both the site and API endpoints).

```
showcase-portfolio/
├── content/
│   ├── works/                  # Per-work directories
│   │   ├── omni-dromenon-v1/
│   │   │   ├── metadata.json   # Structured record
│   │   │   ├── statement.md    # Artist statement
│   │   │   ├── process.md      # Process documentation
│   │   │   └── media/          # Images, video stills, audio
│   │   └── ...
│   ├── exhibitions/            # Exhibition records
│   └── press/                  # Press coverage links
├── src/
│   ├── generators/             # Site generation pipeline
│   │   ├── gallery.ts          # Visual gallery builder
│   │   ├── chronology.ts       # Timeline view
│   │   ├── thematic.ts         # Thematic grouping engine
│   │   └── cv-export.ts        # CV/grant format exporters
│   ├── components/             # UI components
│   │   ├── WorkCard.tsx        # Individual work display
│   │   ├── FilterBar.tsx       # Medium/theme/year filters
│   │   ├── GalleryGrid.tsx     # Responsive grid layout
│   │   └── ExhibitionTimeline.tsx
│   ├── metadata/
│   │   ├── schema.ts           # Zod schema for work records
│   │   ├── dublin-core.ts      # Dublin Core export
│   │   └── cv-formatter.ts     # Academic CV generator
│   └── integrations/
│       ├── registry-sync.ts    # Sync with registry-v2.json
│       └── organ-bridge.ts     # Cross-repo metadata pull
├── templates/
│   ├── grant-application.md    # Grant-ready project list
│   ├── exhibition-proposal.md  # Venue proposal template
│   └── academic-cv.md          # Academic CV format
├── public/                     # Static assets
├── tests/
└── package.json
```

### Metadata Schema

Each work record follows a structured schema validated with Zod:

```typescript
import { z } from "zod";

const WorkRecord = z.object({
  id: z.string().uuid(),
  title: z.string().min(1),
  subtitle: z.string().optional(),
  year: z.number().int().min(2018).max(2030),
  medium: z.enum([
    "generative-visual",
    "interactive-installation",
    "real-time-performance",
    "ai-collaboration",
    "audio-synthesis",
    "motion-capture",
    "mixed-media",
    "net-art",
    "data-sculpture",
  ]),
  dimensions: z.string().optional(),
  duration: z.string().optional(),
  description: z.string().min(50),
  artistStatement: z.string().min(200),
  technicalMethod: z.string(),
  sourceRepo: z.string().url(),
  organ: z.literal("II"),
  relationships: z.array(
    z.object({
      targetId: z.string().uuid(),
      type: z.enum(["predecessor", "variant", "component", "derivative", "response"]),
    })
  ),
  exhibitions: z.array(
    z.object({
      venue: z.string(),
      city: z.string(),
      country: z.string(),
      date: z.string(),
      type: z.enum(["solo", "group", "screening", "performance", "online"]),
      commissioned: z.boolean(),
      fundingSources: z.array(z.string()).optional(),
    })
  ),
  keywords: z.array(z.string()).min(3),
  theoreticalFramework: z.string().optional(),
  rights: z.string().default("MIT"),
  dublinCore: z.object({
    creator: z.string(),
    format: z.string(),
    language: z.string().default("en"),
    subject: z.array(z.string()),
  }),
});
```

### Gallery Generation

The gallery generator produces multiple views from the same dataset:

```typescript
import { WorkRecord } from "./metadata/schema";

interface GalleryView {
  name: string;
  description: string;
  groupBy: keyof WorkRecord | ((work: WorkRecord) => string);
  sortWithin: "chronological" | "alphabetical" | "relevance";
  filter?: (work: WorkRecord) => boolean;
}

const GALLERY_VIEWS: GalleryView[] = [
  {
    name: "chronological",
    description: "All works ordered by year of completion",
    groupBy: "year",
    sortWithin: "chronological",
  },
  {
    name: "by-medium",
    description: "Works grouped by primary medium",
    groupBy: "medium",
    sortWithin: "chronological",
  },
  {
    name: "thematic",
    description: "Works grouped by conceptual concern",
    groupBy: (work) => work.theoreticalFramework ?? "uncategorized",
    sortWithin: "relevance",
  },
  {
    name: "performance",
    description: "Live performance works only",
    groupBy: "year",
    sortWithin: "chronological",
    filter: (work) =>
      work.medium === "real-time-performance" ||
      work.medium === "interactive-installation",
  },
];
```

### CV and Grant Export

The system generates formatted outputs for institutional contexts:

```typescript
function generateGrantProjectList(
  works: WorkRecord[],
  options: { maxWorks: number; focusMedium?: string; since?: number }
): string {
  const filtered = works
    .filter((w) => !options.focusMedium || w.medium === options.focusMedium)
    .filter((w) => !options.since || w.year >= options.since)
    .sort((a, b) => b.year - a.year)
    .slice(0, options.maxWorks);

  return filtered
    .map(
      (w) =>
        `**${w.title}** (${w.year})\n` +
        `${w.medium} | ${w.dimensions ?? w.duration ?? "variable"}\n` +
        `${w.description}\n` +
        `Exhibited: ${w.exhibitions.map((e) => `${e.venue}, ${e.city}`).join("; ")}\n`
    )
    .join("\n---\n");
}
```

---

## Installation

### Prerequisites

- Node.js >= 18.0.0
- pnpm >= 9.0.0
- Git

### Setup

```bash
git clone https://github.com/organvm-ii-poiesis/showcase-portfolio.git
cd showcase-portfolio
pnpm install
```

### Environment Configuration

```bash
cp .env.example .env
```

Required environment variables:

```
PORTFOLIO_TITLE="ORGAN-II Poiesis — Artistic Portfolio"
REGISTRY_URL="https://raw.githubusercontent.com/organvm-iv-taxis/orchestration-start-here/main/registry.json"
OUTPUT_DIR="./dist"
BASE_URL="/showcase-portfolio"
```

---

## Quick Start

### Generate the Portfolio Site

```bash
# Build the static gallery site
pnpm build

# Preview locally
pnpm preview
# Open http://localhost:4173

# Generate grant-ready project list
pnpm run export:grant --max-works 10 --since 2022

# Generate academic CV section
pnpm run export:cv --format markdown

# Generate Dublin Core metadata for all works
pnpm run export:dublin-core --output metadata/
```

### Add a New Work

```bash
# Scaffold a new work record
pnpm run new-work --title "Consensus Landscape" --medium generative-visual --year 2025

# This creates:
# content/works/consensus-landscape/
#   metadata.json  (pre-populated with schema defaults)
#   statement.md   (template for artist statement)
#   process.md     (template for process documentation)
#   media/         (empty directory for images/video)

# Edit the metadata and documentation, then rebuild
pnpm build
```

### Sync from Registry

```bash
# Pull latest metadata from the ORGAN system registry
pnpm run sync:registry

# Pull work documentation from other ORGAN-II repos
pnpm run sync:organs
```

---

## Working Examples

### Example: Generating an Exhibition Proposal

```bash
# Generate a formatted proposal for a gallery submission
pnpm run export:proposal \
  --venue "New Museum" \
  --works omni-dromenon-v1,consensus-landscape,recursive-choir \
  --format pdf

# Output: templates/proposals/new-museum-2025.pdf
# Includes: selected work images, artist statements, technical riders,
#           exhibition history, and a cover letter template
```

### Example: Filtering the Gallery

```typescript
// In a custom view configuration:
const aiCollaborations: GalleryView = {
  name: "ai-collaborations",
  description: "Works involving AI-human creative partnerships",
  groupBy: "year",
  sortWithin: "chronological",
  filter: (work) =>
    work.medium === "ai-collaboration" ||
    work.keywords.includes("machine-learning") ||
    work.keywords.includes("neural-network"),
};
```

### Example: Dublin Core Export

```json
{
  "dc:creator": "Anthony Padavano",
  "dc:title": "Omni-Dromenon v1 — Collective Instrument",
  "dc:date": "2024",
  "dc:format": "interactive installation; real-time performance system",
  "dc:description": "Audience-participatory performance engine using weighted consensus algorithms...",
  "dc:subject": ["interactive art", "real-time systems", "collective authorship", "consensus algorithms"],
  "dc:rights": "MIT License",
  "dc:language": "en",
  "dc:type": "InteractiveResource"
}
```

---

## Theory Implemented

### Curatorial Practice as Computation

Traditional curatorial practice involves subjective judgment: a curator selects works, sequences them, creates dialogues between pieces, and constructs a narrative for the viewer. Showcase Portfolio does not replace this judgment — it augments it with computational tools. The thematic grouping engine uses keyword co-occurrence and relationship graphs to suggest groupings that a human curator might not notice. The chronological view reveals patterns of technical evolution that are invisible when works are encountered individually. The medium-based filtering reveals which areas of practice have been deeply explored and which remain nascent.

This approach draws on digital humanities methods for computational analysis of cultural collections, particularly the work of Lev Manovich on cultural analytics and the concept of "distant reading" as applied to visual culture. The difference is that this system operates on the creator's own corpus rather than on external datasets — it is a tool for self-reflection as much as for presentation.

### Metadata as Practice

The decision to maintain comprehensive structured metadata for every work is itself an artistic and intellectual commitment. It asserts that the context of a work — when it was made, what preceded it, what technical methods it employed, what theoretical framework it engaged — is as significant as the work itself. This position aligns with conceptual art traditions where documentation is constitutive rather than supplementary, and with digital preservation standards that recognize metadata as essential to the long-term intelligibility of computational artifacts.

### The Living Archive

Unlike a static portfolio website that is updated periodically, Showcase Portfolio is designed as a living system. New works propagate into the portfolio automatically when their metadata is committed to their source repositories. Exhibition records accumulate over time. The relationship graph between works grows denser as new works reference, extend, or respond to earlier ones. The portfolio is not a snapshot but a process — it is always becoming, in the same way that an artistic practice is always becoming.

---

## Portfolio & Exhibition

### Current Exhibition Context

Showcase Portfolio is itself a component of the ORGAN-II presentation infrastructure. It has been deployed as part of the organvm system launch (February 2025) and serves as the public-facing gallery for all ORGAN-II creative output.

### Institutional Integration Points

| Context | Output Format | Use Case |
|---------|--------------|----------|
| Arts Council Applications | Markdown/PDF project list | Funding proposals |
| Academic CV | Structured exhibition list | Tenure/promotion files |
| Gallery Proposals | PDF with images | Exhibition submissions |
| Digital Repositories | Dublin Core XML/JSON | Institutional archives |
| Personal Website | Static HTML gallery | Public portfolio |
| ORGAN System Registry | JSON metadata | Cross-organ coordination |

### Grant Application Support

The system is designed with the specific requirements of arts funding applications in mind. Every work record captures the information that major arts councils require: project title, medium, year, duration or dimensions, exhibition history, commissioning context, collaboration credits, and a structured description that addresses both artistic intent and technical innovation. The CV export formats are tested against the submission requirements of organizations including the NEA, Creative Capital, Rhizome, and Ars Electronica.

---

## Related Work

### Cross-Organ Dependencies

| Repository | Organ | Relationship |
|-----------|-------|-------------|
| [metasystem-master](https://github.com/organvm-ii-poiesis/metasystem-master) | II | Primary source of performance documentation and real-time work data |
| [archive-past-works](https://github.com/organvm-ii-poiesis/archive-past-works) | II | Historical records that feed into retrospective portfolio views |
| [case-studies-methodology](https://github.com/organvm-ii-poiesis/case-studies-methodology) | II | Deep process documentation referenced in grant applications |
| [orchestration-start-here](https://github.com/organvm-iv-taxis/orchestration-start-here) | IV | System registry providing cross-organ metadata |
| [public-process](https://github.com/organvm-v-logos/public-process) | V | Building-in-public essays that contextualize the portfolio |

### External References

- Lev Manovich, *Cultural Analytics* (MIT Press, 2020) — computational analysis of visual culture
- Christiane Paul, *Digital Art* (Thames & Hudson, 2023) — survey of digital art practices and exhibition strategies
- Dublin Core Metadata Initiative (https://dublincore.org) — metadata standards for cultural heritage
- International Council of Museums (ICOM) documentation standards
- Rhizome's ArtBase (https://artbase.rhizome.org) — born-digital art preservation

---

## Contributing

### Portfolio Contributions

To add a work to the portfolio, create a new work directory under `content/works/` following the established schema. Every work record must include:

1. A validated `metadata.json` file conforming to the WorkRecord schema
2. An artist statement of at least 200 words explaining the work's intent
3. Process documentation describing the journey from concept to completion
4. At least one high-resolution image or video still

### Technical Contributions

```bash
# Fork and clone
git clone https://github.com/<your-fork>/showcase-portfolio.git
cd showcase-portfolio
pnpm install

# Create a feature branch
git checkout -b feature/your-feature-name

# Make changes, run tests
pnpm test
pnpm build

# Commit (conventional commits)
git commit -m "feat(gallery): add responsive masonry layout"

# Push and open a PR against main
git push origin feature/your-feature-name
```

### Curatorial Contributions

The system welcomes contributions to its curatorial logic: new gallery view configurations, improved thematic grouping algorithms, alternative CV export formats for specific institutional contexts, and accessibility improvements to the gallery interface.

---

## License

[MIT](LICENSE)

---

## Author & Contact

**Author:** Anthony Padavano ([@4444J99](https://github.com/4444J99))

**Organization:** [organvm-ii-poiesis](https://github.com/organvm-ii-poiesis) (ORGAN-II: Poiesis)

**System:** [meta-organvm](https://github.com/meta-organvm) — the eight-organ creative-institutional system coordinating ~80 repositories across theory, art, commerce, orchestration, public process, community, and marketing.

---

<sub>This README is a Gap-Fill Sprint portfolio document for the organvm system. It is written for grant reviewers, hiring managers, and collaborators who want to understand what Showcase Portfolio does, why it exists, and how it fits within a larger creative-institutional architecture.</sub>
