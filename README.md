# Gitmodules Commit Hooks (for pre-commit)

## Setup

See [Pre-commit documentation](https://pre-commit.com/#adding-pre-commit-plugins-to-your-project).

## Supported Hooks

### sort-submodules

```yaml
- repo: https://github.com/garthwilliamson/pre-commit-gitmodules.git
  rev: 0.1.0
  hooks:
  - id: sort-submodules
```

Sorts submodules and removes lines with `branch =`.

## Roadmap

* Turn hooks into a python modules, using setup.py to install the binaries
* Add hook to check if a .gitmodules are added a submodule is also added at the
  same path. Only for ones that have been added, not removed.
