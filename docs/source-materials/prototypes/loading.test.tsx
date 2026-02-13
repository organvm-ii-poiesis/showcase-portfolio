import { render, screen } from "@testing-library/react";

import GlobalLoading from "@/app/loading";

describe("global loading skeleton", () => {
  it("renders with aria-busy for assistive technology", () => {
    render(<GlobalLoading />);

    const section = screen.getByRole("region", { name: /loading content/i });
    expect(section).toHaveAttribute("aria-busy", "true");
  });

  it("renders loading bars", () => {
    const { container } = render(<GlobalLoading />);

    const bars = container.querySelectorAll(".loading-bar");
    expect(bars.length).toBeGreaterThanOrEqual(3);
  });
});
