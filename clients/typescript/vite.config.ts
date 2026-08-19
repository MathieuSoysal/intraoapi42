import { defineConfig } from 'vitest/config';

export default defineConfig({
  test: {
    // Don't fail if no test files are found
    passWithNoTests: true,
  },
});