"use client";

import Link from "next/link";
import { useEffect } from "react";

export default function GlobalError({
  error,
  reset,
}: {
  error: Error & { digest?: string };
  reset: () => void;
}) {
  useEffect(() => {
    console.error("[MET4] Unhandled error:", error);
  }, [error]);

  return (
    <section className="error-boundary">
      <p className="eyebrow">System Fault</p>
      <h1>Something fractured.</h1>
      <p>An unexpected error disrupted the signal. You can try again or return to the map.</p>
      <div className="error-actions">
        <button onClick={reset}>Retry</button>
        <Link href="/">Return to Node Map</Link>
      </div>
    </section>
  );
}
