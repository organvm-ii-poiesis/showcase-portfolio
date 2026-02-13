"use client";

import { useEffect, useState, useRef, useCallback } from "react";
import { globalSynth } from "@/lib/audio/synth";

type MVSMood = "Observant" | "Glitchy" | "Bored" | "Helpful";

/**
 * Autonomous background agent representing @MVS.
 * Monitors user activity and reacts to provide presence.
 */
export function useMVSAgent() {
  const [mood, setMood] = useState<MVSMood>("Observant");
  const lastActivity = useRef<number>(0);
  const moodRef = useRef<MVSMood>(mood);

  // Keep refs in sync with state without triggering listener effect re-runs
  useEffect(() => {
    moodRef.current = mood;
  }, [mood]);

  // Initialize timestamp on mount
  useEffect(() => {
    lastActivity.current = Date.now();
  }, []);

  const handleActivity = useCallback(() => {
    lastActivity.current = Date.now();
    if (moodRef.current === "Bored") {
      setMood("Observant");
      globalSynth?.triggerGlitch(20);
    }
  }, []);

  useEffect(() => {
    window.addEventListener("mousemove", handleActivity);
    window.addEventListener("keydown", handleActivity);

    const checkIdle = setInterval(() => {
      const diff = Date.now() - lastActivity.current;

      if (diff > 30000 && moodRef.current !== "Bored") {
        setMood("Bored");
        globalSynth?.setMode("mineral");
      }
    }, 5000);

    return () => {
      window.removeEventListener("mousemove", handleActivity);
      window.removeEventListener("keydown", handleActivity);
      clearInterval(checkIdle);
    };
  }, [handleActivity]);

  return { mood };
}
