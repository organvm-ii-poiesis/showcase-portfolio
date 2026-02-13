import { vi } from "vitest";

describe("canUseWebGL", () => {
  it("returns false when document is undefined (SSR)", async () => {
    const originalDocument = globalThis.document;
    // @ts-expect-error — simulating SSR environment
    delete globalThis.document;

    // Dynamic import to get fresh module evaluation
    vi.resetModules();
    const { canUseWebGL } = await import("@/lib/webgl-probe");
    expect(canUseWebGL()).toBe(false);

    globalThis.document = originalDocument;
  });

  it("returns false when canvas context creation fails", async () => {
    vi.resetModules();

    const originalCreateElement = document.createElement.bind(document);
    vi.spyOn(document, "createElement").mockImplementation((tag: string) => {
      if (tag === "canvas") {
        const canvas = originalCreateElement("canvas");
        canvas.getContext = () => null;
        return canvas;
      }
      return originalCreateElement(tag);
    });

    const { canUseWebGL } = await import("@/lib/webgl-probe");
    expect(canUseWebGL()).toBe(false);

    vi.restoreAllMocks();
  });
});
