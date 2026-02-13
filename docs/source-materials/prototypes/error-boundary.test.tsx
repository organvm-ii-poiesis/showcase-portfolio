import { fireEvent, render, screen } from "@testing-library/react";
import { vi } from "vitest";

import GlobalError from "@/app/error";

describe("global error boundary", () => {
  it("renders the themed fallback UI", () => {
    const error = new Error("test failure");
    const reset = vi.fn();

    render(<GlobalError error={error} reset={reset} />);

    expect(screen.getByText("System Fault")).toBeInTheDocument();
    expect(screen.getByRole("heading", { name: /something fractured/i })).toBeInTheDocument();
    expect(screen.getByRole("link", { name: /return to node map/i })).toHaveAttribute("href", "/");
  });

  it("calls reset when retry button is clicked", () => {
    const error = new Error("test failure");
    const reset = vi.fn();

    render(<GlobalError error={error} reset={reset} />);

    fireEvent.click(screen.getByRole("button", { name: /retry/i }));
    expect(reset).toHaveBeenCalledTimes(1);
  });
});
