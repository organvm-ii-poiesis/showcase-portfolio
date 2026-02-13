"use client";

import posthog from "posthog-js";

import type { AnalyticsEvent, AnalyticsPayload } from "@/types/content";

let initialized = false;

export function initPostHog() {
  if (initialized) {
    return;
  }

  const key = process.env.NEXT_PUBLIC_POSTHOG_KEY;
  const host = process.env.NEXT_PUBLIC_POSTHOG_HOST ?? "https://us.i.posthog.com";

  if (!key) {
    return;
  }

  posthog.init(key, {
    api_host: host,
    capture_pageview: false,
    capture_pageleave: false,
    persistence: "localStorage+cookie",
  });

  initialized = true;
}

export async function trackEvent(event: AnalyticsPayload) {
  const payload: AnalyticsEvent = {
    ...event,
    ts: event.ts ?? new Date().toISOString(),
    sessionId: event.sessionId ?? posthog.get_distinct_id(),
  };

  if (initialized) {
    posthog.capture(payload.eventName, {
      mode: payload.mode,
      docSlug: payload.docSlug,
      sectionId: payload.sectionId,
      nodeId: payload.nodeId,
      value: payload.value,
      metadata: payload.metadata,
      ts: payload.ts,
    });
  }

  if (typeof window !== "undefined") {
    const body = JSON.stringify(payload);
    const endpoint = new URL("/api/analytics", window.location.origin).toString();

    try {
      if (navigator.sendBeacon) {
        const blob = new Blob([body], { type: "application/json" });
        navigator.sendBeacon(endpoint, blob);
        return;
      }

      await fetch(endpoint, {
        method: "POST",
        headers: { "content-type": "application/json" },
        body,
        keepalive: true,
      });
    } catch {
      // Analytics should never break user flows.
    }
  }
}
