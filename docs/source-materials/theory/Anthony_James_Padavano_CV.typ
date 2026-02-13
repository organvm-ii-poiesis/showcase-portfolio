// Import the rendercv function and all the refactored components
#import "@preview/rendercv:0.1.0": *

// Apply the rendercv template with custom configuration
#show: rendercv.with(
  name: "Anthony James Padavano",
  footer: context { [#emph[Anthony James Padavano -- #str(here().page())\/#str(counter(page).final().first())]] },
  top-note: [ #emph[Last updated in Feb 2026] ],
  locale-catalog-language: "en",
  page-size: "us-letter",
  page-top-margin: 0.7in,
  page-bottom-margin: 0.7in,
  page-left-margin: 0.7in,
  page-right-margin: 0.7in,
  page-show-footer: true,
  page-show-top-note: true,
  colors-body: rgb(0, 0, 0),
  colors-name: rgb(0, 79, 144),
  colors-headline: rgb(0, 79, 144),
  colors-connections: rgb(0, 79, 144),
  colors-section-titles: rgb(0, 79, 144),
  colors-links: rgb(0, 79, 144),
  colors-footer: rgb(128, 128, 128),
  colors-top-note: rgb(128, 128, 128),
  typography-line-spacing: 0.6em,
  typography-alignment: "justified",
  typography-date-and-location-column-alignment: right,
  typography-font-family-body: "Source Sans 3",
  typography-font-family-name: "Source Sans 3",
  typography-font-family-headline: "Source Sans 3",
  typography-font-family-connections: "Source Sans 3",
  typography-font-family-section-titles: "Source Sans 3",
  typography-font-size-body: 10pt,
  typography-font-size-name: 30pt,
  typography-font-size-headline: 10pt,
  typography-font-size-connections: 10pt,
  typography-font-size-section-titles: 1.4em,
  typography-small-caps-name: false,
  typography-small-caps-headline: false,
  typography-small-caps-connections: false,
  typography-small-caps-section-titles: false,
  typography-bold-name: true,
  typography-bold-headline: false,
  typography-bold-connections: false,
  typography-bold-section-titles: true,
  links-underline: false,
  links-show-external-link-icon: false,
  header-alignment: center,
  header-photo-width: 3.5cm,
  header-space-below-name: 0.7cm,
  header-space-below-headline: 0.7cm,
  header-space-below-connections: 0.7cm,
  header-connections-hyperlink: true,
  header-connections-show-icons: true,
  header-connections-display-urls-instead-of-usernames: false,
  header-connections-separator: "",
  header-connections-space-between-connections: 0.5cm,
  section-titles-type: "with_partial_line",
  section-titles-line-thickness: 0.5pt,
  section-titles-space-above: 0.5cm,
  section-titles-space-below: 0.3cm,
  sections-allow-page-break: true,
  sections-space-between-text-based-entries: 0.3em,
  sections-space-between-regular-entries: 1.2em,
  entries-date-and-location-width: 4.15cm,
  entries-side-space: 0.2cm,
  entries-space-between-columns: 0.1cm,
  entries-allow-page-break: false,
  entries-short-second-row: true,
  entries-summary-space-left: 0cm,
  entries-summary-space-above: 0cm,
  entries-highlights-bullet:  "•" ,
  entries-highlights-nested-bullet:  "•" ,
  entries-highlights-space-left: 0.15cm,
  entries-highlights-space-above: 0cm,
  entries-highlights-space-between-items: 0cm,
  entries-highlights-space-between-bullet-and-text: 0.5em,
  date: datetime(
    year: 2026,
    month: 2,
    day: 12,
  ),
)


= Anthony James Padavano

  #headline([Creative Technologist])

#connections(
  [#connection-with-icon("location-dot")[New York City]],
  [#link("mailto:padavano.anthony@gmail.com", icon: false, if-underline: false, if-color: false)[#connection-with-icon("envelope")[padavano.anthony\@gmail.com]]],
  [#link("https://4444j99.github.io/portfolio/", icon: false, if-underline: false, if-color: false)[#connection-with-icon("link")[4444j99.github.io\/portfolio]]],
  [#link("https://github.com/4444j99", icon: false, if-underline: false, if-color: false)[#connection-with-icon("github")[4444j99]]],
)


== Summary

Creative technologist and artist-engineer with 10+ years across multimedia production, digital marketing, and systems design. Builds autonomous creative systems and treats their governance as artistic medium — most recently shipping an eight-organ orchestration system coordinating 81 repositories across 8 GitHub organizations with \~320K words of public documentation. MFA in Creative Writing; Google-certified in UX Design, Digital Marketing, and Project Management; Meta Full-Stack Developer.

== Skills

#strong[Languages:] Python, TypeScript, JavaScript, Go, Rust, Bash, SQL

#strong[Frameworks:] Node.js, Astro, React, Next.js, FastAPI, Express

#strong[AI \/ ML:] LLM orchestration, multi-agent systems, prompt engineering, RAG pipelines

#strong[Infrastructure:] GitHub Actions, CI\/CD, Docker, PostgreSQL, Git

#strong[Creative:] p5.js, generative art, audio synthesis, interactive installations

#strong[Governance:] Registry design, dependency validation, state machines, documentation systems

== selected projects

#regular-entry(
  [
    #strong[The Eight-Organ System]

    - Designed orchestration architecture coordinating theory, art, commerce, community, and marketing as a single governed system

    - Built machine-readable registry, automated dependency validation (31 edges, zero back-edge violations), and promotion state machine

    - Authored \~320K words of public documentation; 5 GitHub Actions workflows for autonomous governance

  ],
  [
    2024 — Present

  ],
)

#regular-entry(
  [
    #strong[Recursive Engine (RE:GE)]

    - Implemented 21 organ handlers translating epistemological frameworks into executable code with a ritual syntax DSL

    - 1,254 tests, 85\% coverage; myths, identities, and recursive structures as first-class computational objects

  ],
  [
    2024 — Present

  ],
)

#regular-entry(
  [
    #strong[Agentic Titan]

    - Polymorphic agent swarm architecture across 6 self-organizing topologies with 22 agent archetypes

    - 1,095+ tests across 18 implementation phases

  ],
  [
    2024 — Present

  ],
)

#regular-entry(
  [
    #strong[AI-Conductor Model]

    - Developed the workflow producing \~320K words: AI generates volume, human directs and refines

    - Includes quality gates, template compliance validation, and automated link checking across 81 repos

  ],
  [
    2024 — Present

  ],
)

#regular-entry(
  [
    #strong[Generative Music System]

    - Translates symbolic narrative events into live generative music — recursion as counterpoint, identity transformations as harmonic movement

  ],
  [
    2024 — Present

  ],
)

== Experience

#regular-entry(
  [
    #strong[Independent], Creative Technologist

    - Designed and launched the eight-organ orchestration system coordinating 81 repositories across 8 GitHub organizations with automated dependency validation and \~320K words of documentation

    - Built recursive-engine (1,254 tests, 85\% coverage) — a symbolic operating system translating epistemological frameworks into executable Python

    - Developed generative art and music systems, interactive installations, and AI-conductor workflow for human-AI co-creation

  ],
  [
    New York City

    2021 – present

    5 years

  ],
)

#regular-entry(
  [
    #strong[Miami Dade College Foundation], Digital Marketing Manager

    - Designed and executed digital campaigns increasing donor engagement by 32\% and surpassing fundraising goals

    - Rebuilt foundation website — 38\% traffic growth, 22\% improvement in donation conversions

    - Produced multimedia storytelling content driving 28\% increase in click-through rates

  ],
  [
    Miami, FL

    2023 – 2024

    1 year

  ],
)

#regular-entry(
  [
    #strong[AJP Media Arts], Multimedia Specialist

    - Produced video, audio, and visual campaigns achieving 17.5M+ views and driving \$2M in client fundraising and revenue

    - Integrated SEO and paid media strategies achieving 290\% ROI for key campaigns

    - Launched and managed client websites with 42\% engagement increase and 30\% speed improvement

  ],
  [
    New York City

    2011 – present

    15 years

  ],
)

#regular-entry(
  [
    #strong[Miami Dade College, FAU, Nova Southeastern, Keiser, and others], Instructor

    - Designed and delivered 100+ composition courses to 2,000+ students with 85\% above-average grade achievement

    - Applied UX principles to create accessible course materials — 92\% student approval rating

  ],
  [
    South Florida

    2015 – present

    11 years

  ],
)

#regular-entry(
  [
    #strong[Majestic Design], Project Manager

    - Led 50 commercial and residential construction projects from concept to completion — 90\% on-time and within budget

    - Collaborated with marketing teams on 3D renderings and video walkthroughs, securing 25\% increase in repeat business

  ],
  [
    New York City

    2007 – 2018

    11 years

  ],
)

== Education

#education-entry(
  [
    #strong[Florida Atlantic University], Creative Writing

  ],
  [
    2015 – 2018

  ],
  degree-column: [
    #strong[M.F.A.]
  ],
)

#education-entry(
  [
    #strong[CUNY College of Staten Island], English Literature

  ],
  [
    2010 – 2014

  ],
  degree-column: [
    #strong[B.A.]
  ],
)

== Certifications

#strong[Full-Stack Developer — Meta:] 2023 — 2024

#strong[UX Design — Google:] 2022 — 2023

#strong[Digital Marketing & E-commerce — Google:] 2022 — 2023

#strong[Project Management — Google:] 2022 — 2023
