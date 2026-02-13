import { expect, test } from "@playwright/test";

test.describe("accessibility", () => {
  test("skip-link is focusable and targets #main-content", async ({ page }) => {
    await page.goto("/");

    const skipLink = page.locator('a.skip-link[href="#main-content"]');
    await skipLink.focus();
    await expect(skipLink).toBeFocused();
    await expect(skipLink).toHaveAttribute("href", "#main-content");
  });

  test("mode-nav has aria-label 'Experience mode'", async ({ page }) => {
    await page.goto("/");

    const nav = page.getByRole("navigation", { name: "Experience mode" });
    await expect(nav).toBeVisible();
  });

  test("main content landmark exists", async ({ page }) => {
    await page.goto("/");

    const main = page.locator("#main-content");
    await expect(main).toBeVisible();
  });
});
