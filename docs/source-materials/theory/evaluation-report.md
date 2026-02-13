# MET4MORFOSES — Evaluation-to-Growth Report

Project: **MET4MORFOSES Web Edition**
Framework: **Evaluation-to-Growth**
Date: 2026-02-12

---

## 1. Critique

### 1.1 Strengths

| Area | Evidence | Location |
|------|----------|----------|
| **Accessibility** | Skip-to-content links, `aria-label`, `aria-live="polite"`, `role="listbox"`/`role="option"` pattern | `layout.tsx:39-43`, `node-map-experience.tsx:57,66` |
| **Analytics resilience** | Zod `.strict()` validation, token-bucket rate limiting, `sendBeacon` with fetch fallback, silent catch on failure | `api/analytics/route.ts:17-29,40-54`, `lib/analytics.ts:54-69` |
| **Content pipeline** | 5-stage sequential build with QA gate (8% fidelity threshold), SHA-256 checksums, Unicode word counting | `scripts/qa-canonical-fidelity.ts`, `scripts/verify-mirror-integrity.ts` |
| **Type safety** | Well-structured union types, typed API responses, `satisfies` keyword usage | `types/content.ts`, `types/api.ts`, `api/analytics/route.ts:15` |
| **Server/client split** | Server components load data and pass immutable props to `"use client"` components | All `page.tsx` files, `node-map-experience.tsx:29-31` |
| **CI/CD** | Two-tier pipeline: always-on (lint+typecheck+test+build) + opt-in E2E with artifact upload | `.github/workflows/ci.yml`, `e2e.yml` |
| **404 handling** | Custom not-found page, `notFound()` calls in dynamic routes | `not-found.tsx`, `read/[docSlug]/page.tsx:56` |

### 1.2 Weaknesses Identified and Addressed

| # | Issue | Severity | Resolution |
|---|-------|----------|------------|
| W1 | Zero error boundaries — no `error.tsx`, no loading states | HIGH | Added `error.tsx` for global, oracle, and reader routes + `loading.tsx` |
| W2 | Missing page metadata on 6 of 7 routes | HIGH | Added `metadata` or `generateMetadata` to all routes |
| W3 | `useMVSAgent` re-registers listeners on every mood change | MEDIUM | Refactored to use refs for stable listener registration |
| W4 | Eager 3D import loads Three.js bundle for all users | MEDIUM | Converted to `next/dynamic` with `ssr: false` |
| W5 | No runtime validation of JSON data files | MEDIUM | Added Zod schemas for `processed-content.json` and `style-dna.json` |
| W6 | Manifest API routes have no rate limiting | LOW | Noted; analytics route already rate-limited |
| W7 | No Open Graph / social sharing metadata | MEDIUM | Added OG and Twitter card fields to root layout |
| W8 | No PDF extraction timeout in build script | LOW | Added `timeout: 30_000` to `spawnSync` |

---

## 2. Logic Check

### Contradiction: useMVSAgent Effect Dependencies

**Before**: The `useEffect` in `use-mvs-agent.ts` had `[mood]` as a dependency. Every mood state change (Observant -> Bored -> Observant) tore down and re-added all event listeners and the idle-check interval. The intent was to track idle-to-bored transitions, but the implementation recreated everything on each transition.

**After**: Refactored to use a `moodRef` that stays in sync via a separate, lightweight effect. The listener registration effect now runs once with stable dependencies (`useCallback` with empty deps), while mood-dependent logic reads from the ref.

### Gap: Mode Navigation Active State

`mode-nav.tsx:47` checks `pathname === mode.href` for active state. This means subroutes (e.g., `/read/intro`) won't highlight any mode chip. This is a known limitation but acceptable since the reader is accessed from within modes rather than being a mode itself.

### Copy Improvement: Default State Message

`node-map-experience.tsx:161` previously showed "No nodes found yet." when no node is selected. This message suggested missing data rather than an unselected state. Changed to "Select a node to explore." to accurately describe the expected interaction.

---

## 3. Logos Review (Rational/Structural Appeal)

### Architecture

The five-mode architecture (Node Map, Feed, Scroll, Reader, Oracle) is conceptually strong. Each mode reframes the same canonical text through a different spatial and temporal logic:

- **Node Map**: spatial/relational (constellation metaphor)
- **Feed**: temporal/sequential (social media metaphor)
- **Scroll**: linear/continuous (traditional reading metaphor)
- **Reader**: structured/navigable (academic edition metaphor)
- **Oracle**: generative/analytical (AI interpretation metaphor)

### Evidence Quality

The content pipeline produces verifiable artifacts with quality reports. The QA script's suspicious-pattern detection (OCR artifacts, encoding issues) adds credibility to the digital provenance claims.

### Structural Improvement: Data Validation

Previously, all JSON data files were loaded with bare `as Type` casts. If pipeline-generated files drifted from expected schemas (e.g., a missing field after a script update), the error would surface as a cryptic runtime crash deep in a component. Now, Zod validation on `processed-content.json` and `style-dna.json` catches schema drift at the data loading boundary with clear error messages, while gracefully falling back to keep the site functional.

---

## 4. Pathos Review (Emotional Resonance)

### Current Tone

The dark atmospheric palette (`#081218` background), animated gradient background (`bg-atmosphere` with 22s drift animation), and generative audio via `GlitchSynth` create an immersive, slightly eerie digital-mythic atmosphere. Trending motifs with fire emoji add a sense of cultural velocity.

### Typography System

The three-font system bridges technical and literary registers effectively:
- **Barlow Condensed** (headlines): industrial, compressed, signal-like
- **Space Grotesk** (body): clean, technical, readable
- **Cormorant Garamond** (literary): classical, serif, thesis-appropriate

### Improvement: Loading States

Previously, mode transitions showed nothing — a blank flash before content appeared. The new `loading.tsx` provides a shimmer skeleton animation using the site's accent colors, maintaining atmospheric continuity during navigation. The shimmer animation respects `prefers-reduced-motion`.

### Improvement: Error States

Previously, any component crash resulted in a white screen (React's default unmount behavior). The new error boundaries maintain the site's visual language — dark backgrounds, themed typography, contextual copy ("Something fractured," "The Oracle has gone silent") — keeping the user within the experience even during failures.

---

## 5. Ethos Review (Credibility)

### Expertise Markers

- Strict TypeScript with `noEmit` type checking
- Comprehensive CI with four required status checks
- Unicode-aware text processing (`\p{L}\p{N}` regex)
- SHA-256 checksums for provenance tracking
- Zod validation at API boundaries (analytics) and now at data boundaries

### Trust Signals

- Public archive with complete source artifacts
- Provenance-tracking mirror manifest with file hashes
- `generateStaticParams` for SEO on dynamic routes
- **New**: Open Graph and Twitter card metadata for social sharing
- **New**: Per-page metadata describing each mode's purpose

### Remaining Gaps

- No structured data (JSON-LD) for academic/thesis content
- No Open Graph images (would require generating or placing a static OG image)
- No `robots.txt` or `sitemap.xml` (could use Next.js metadata-based generation)

---

## 6. Risk Analysis

### Blind Spots Addressed

| # | Blind Spot | Mitigation |
|---|-----------|------------|
| B1 | No WebGL capability detection — R3F Canvas could silently fail | Added `webgl-probe.ts` utility; node map defaults to 2D on incapable devices |
| B2 | Memory leak in rate-limiter `buckets` Map | Added hourly stale bucket eviction in analytics route |
| B3 | `commentary.json` loaded without error surfacing | Existing try/catch returns `[]` — acceptable for optional data |

### Shatter Points Addressed

| # | Vulnerability | Impact | Prevention |
|---|--------------|--------|------------|
| S1 | 3D Canvas crash with no error boundary | White screen | Error boundaries catch React tree failures; WebGL probe prevents loading 3D on incapable devices |
| S2 | Corrupted PDF hangs build indefinitely | CI stuck | 30s timeout on `spawnSync` |
| S3 | `processed-content.json` schema drift | Runtime crash on all reading routes | Zod validation with graceful fallback |
| S4 | PostHog outage blocks analytics | Server-side 500 errors | Already mitigated: try/catch returns 500 gracefully |

---

## 7. Implementation Summary

### Files Created (6)

| File | Purpose |
|------|---------|
| `src/app/error.tsx` | Global error boundary |
| `src/app/oracle/error.tsx` | Oracle-specific error boundary |
| `src/app/read/[docSlug]/error.tsx` | Reader-specific error boundary |
| `src/app/loading.tsx` | Global loading skeleton |
| `src/lib/webgl-probe.ts` | WebGL capability detection utility |
| `docs/evaluation-report.md` | This report |

### Files Modified (14)

| File | Changes |
|------|---------|
| `src/app/layout.tsx` | Template-based title, OG metadata, Twitter cards |
| `src/app/page.tsx` | Added static metadata |
| `src/app/feed/page.tsx` | Added static metadata |
| `src/app/scroll/page.tsx` | Added static metadata |
| `src/app/oracle/page.tsx` | Added metadata + Zod validation for style-dna.json |
| `src/app/archive/page.tsx` | Added static metadata |
| `src/app/about/page.tsx` | Added static metadata |
| `src/app/evolution/[slug]/page.tsx` | Added `generateMetadata` with doc title |
| `src/hooks/use-mvs-agent.ts` | Refactored to stable listener registration via refs |
| `src/components/node-map-experience.tsx` | Dynamic 3D import, WebGL probe, copy fix |
| `src/lib/content.ts` | Zod validation for processed-content.json |
| `src/app/api/analytics/route.ts` | Rate limiter bucket eviction |
| `scripts/ingest-canonical.ts` | 30s timeout on PDF extraction |
| `src/app/globals.css` | Loading skeleton + error boundary styles |
