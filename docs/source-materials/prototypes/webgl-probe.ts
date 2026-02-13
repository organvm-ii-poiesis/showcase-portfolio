/**
 * Probes for WebGL2 (preferred) or WebGL1 support.
 * Returns false on devices/browsers without GPU compositing.
 */
export function canUseWebGL(): boolean {
  if (typeof document === "undefined") return false;

  try {
    const canvas = document.createElement("canvas");
    const gl =
      canvas.getContext("webgl2") ??
      canvas.getContext("webgl") ??
      canvas.getContext("experimental-webgl");
    return gl !== null;
  } catch {
    return false;
  }
}
