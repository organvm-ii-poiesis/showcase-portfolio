import { render, screen } from "@testing-library/react";
import { usePathname } from "next/navigation";
import { vi } from "vitest";

import { ModeNav } from "@/components/mode-nav";

vi.mock("@/lib/analytics", () => ({
  trackEvent: vi.fn(),
}));

// Override the global usePathname mock with a vi.fn() so we can change it per test
vi.mock("next/navigation", () => ({
  usePathname: vi.fn().mockReturnValue("/"),
  notFound: () => {
    throw new Error("NEXT_NOT_FOUND");
  },
}));

describe("ModeNav", () => {
  it("highlights Feed chip when pathname is /feed", () => {
    vi.mocked(usePathname).mockReturnValue("/feed");

    render(<ModeNav />);

    const feedLink = screen.getByRole("link", { name: "Feed" });
    expect(feedLink).toHaveClass("active");

    const nodeMapLink = screen.getByRole("link", { name: "Node Map" });
    expect(nodeMapLink).not.toHaveClass("active");
  });

  it("highlights Node Map chip for subroute /read/intro", () => {
    vi.mocked(usePathname).mockReturnValue("/read/intro");

    render(<ModeNav />);

    const nodeMapLink = screen.getByRole("link", { name: "Node Map" });
    expect(nodeMapLink).toHaveClass("active");
  });

  it("highlights Oracle chip when pathname is /oracle", () => {
    vi.mocked(usePathname).mockReturnValue("/oracle");

    render(<ModeNav />);

    const oracleLink = screen.getByRole("link", { name: "The Oracle" });
    expect(oracleLink).toHaveClass("active");
  });

  it("renders with accessible aria-label when id is provided", () => {
    render(<ModeNav id="mode-navigation" />);

    const nav = screen.getByRole("navigation", { name: "Experience mode" });
    expect(nav).toHaveAttribute("id", "mode-navigation");
  });
});
