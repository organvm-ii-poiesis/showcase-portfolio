/**
 * MET4 Glitch Synth Engine
 * Uses Web Audio API to create a generative soundscape based on Style DNA.
 */

export type SynthMode = "ambient" | "active" | "glitch";

export class GlitchSynth {
  private ctx: AudioContext | null = null;
  private masterBus: GainNode | null = null;
  private droneOsc: OscillatorNode | null = null;
  private filter: BiquadFilterNode | null = null;
  private isInitialized = false;

  constructor() {}

  public init() {
    if (this.isInitialized) return;
    
    // Safely check for AudioContext across browsers
    const AudioContextClass = (window.AudioContext || 
      (window as unknown as { webkitAudioContext: typeof AudioContext }).webkitAudioContext);
    
    if (!AudioContextClass) {
      console.warn("Web Audio API not supported in this environment.");
      return;
    }

    this.ctx = new AudioContextClass();
    this.masterBus = this.ctx.createGain();
    this.masterBus.gain.value = 0.15; // Low master volume
    this.masterBus.connect(this.ctx.destination);

    this.filter = this.ctx.createBiquadFilter();
    this.filter.type = "lowpass";
    this.filter.frequency.value = 800;
    this.filter.connect(this.masterBus);

    this.startDrone();
    this.isInitialized = true;
  }

  private startDrone() {
    if (!this.ctx || !this.filter) return;

    this.droneOsc = this.ctx.createOscillator();
    this.droneOsc.type = "sine";
    this.droneOsc.frequency.value = 55; // A1
    
    const droneGain = this.ctx.createGain();
    droneGain.gain.value = 0.5;
    
    // Slow LFO for frequency modulation
    const lfo = this.ctx.createOscillator();
    lfo.type = "sine";
    lfo.frequency.value = 0.1;
    const lfoGain = this.ctx.createGain();
    lfoGain.gain.value = 2;
    
    lfo.connect(lfoGain);
    lfoGain.connect(this.droneOsc.frequency);
    
    this.droneOsc.connect(droneGain);
    droneGain.connect(this.filter);
    
    lfo.start();
    this.droneOsc.start();
  }

  public triggerGlitch(intensity: number = 50) {
    if (!this.ctx || !this.filter) return;

    const now = this.ctx.currentTime;
    const duration = 0.05 + Math.random() * 0.1;
    
    const osc = this.ctx.createOscillator();
    osc.type = Math.random() > 0.5 ? "square" : "sawtooth";
    osc.frequency.setValueAtTime(Math.random() * 2000 + 400, now);
    osc.frequency.exponentialRampToValueAtTime(Math.random() * 100 + 40, now + duration);

    const noiseGain = this.ctx.createGain();
    noiseGain.gain.setValueAtTime(0, now);
    noiseGain.gain.linearRampToValueAtTime(intensity / 1000, now + 0.01);
    noiseGain.gain.linearRampToValueAtTime(0, now + duration);

    osc.connect(noiseGain);
    noiseGain.connect(this.filter);

    osc.start(now);
    osc.stop(now + duration);
  }

  public setMode(theme: string) {
    if (!this.filter || !this.ctx) return;
    
    const freq = theme === "divine" ? 2000 : theme === "mineral" ? 400 : 800;
    this.filter.frequency.setTargetAtTime(freq, this.ctx.currentTime, 0.5);
  }

  public stop() {
    if (this.ctx) {
      this.ctx.close().catch(() => {});
      this.isInitialized = false;
    }
  }
}

export const globalSynth = typeof window !== "undefined" ? new GlitchSynth() : null;
