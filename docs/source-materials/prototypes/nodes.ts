import feedItems from "@/data/feed-items.json";
import nodeMap from "@/data/node-map.json";
import type { FeedItem, NarrativeNode } from "@/types/content";

export function getNarrativeNodes(): NarrativeNode[] {
  return nodeMap as NarrativeNode[];
}

export function getFeedItems(): FeedItem[] {
  return (feedItems as FeedItem[]).sort((a, b) => a.timestampOrder - b.timestampOrder);
}

export function nodeLabel(id: string): string {
  return id.replace(/^@/, "");
}
