.PHONY: help rules rules-check

help: ## Show available targets
	@grep -E '^[a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-14s %s\n", $$1, $$2}'

rules: ## Validate rules and regenerate docs/rules/REGISTRY.md
	python3 scripts/check_rules.py --write

rules-check: ## Validate rules; fail if the registry is stale (CI)
	python3 scripts/check_rules.py --check
