# splent_marketplace_app

The SPLENT marketplace web application — built with SPLENT itself.

This product is the visual front of the marketplace: it consumes the same
`index.json` that the `splent` CLI uses (see
[splent_index](https://github.com/splent-io/splent_index)) and helps you
**choose** features, not just list them:

- Catalog with categories, archetypes and real contract data
  (provides / requires / used by), straight from each feature's
  auto-generated `[tool.splent.contract]`.
- Dependency graph per feature: hard requirements, soft (optional)
  integrations, reverse dependencies, and provides collisions.
- UVL-driven configurator: pick an SPL, select features with live
  validity checking against the variability model (mandatory groups,
  alternatives, constraints), and get the exact `splent` commands to
  build your product.

The marketplace stores no package data of its own — the index is a
regenerable cache of the feature contracts, and publishing a feature is
`splent feature:release`. The app's own database only holds what is
genuinely the marketplace's: users, favourites, metrics and curation.

## Status

Product scaffolding in progress (SPLENT product derived from the SPL
workflow: `product:create` → feature selection → `product:derive`).
