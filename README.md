# Branch Naming Validation Hook

This repository provides a pre-commit hook to enforce branch naming conventions.

## Installation

Add the following to your `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/billy-doyle/branch-naming-hook
    rev: v1.0.0  # Use the latest tag or branch
    hooks:
      - id: branch-naming-hook
        args: ["<project_abbr>"]  # Replace <project_abbr> with your project abbreviation (e.g., "ST")
