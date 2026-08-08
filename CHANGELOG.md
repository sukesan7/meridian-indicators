# Changelog

All notable repository and public-script changes are recorded here.

## [0.1.1] — 2026-08-08

### Options Levels 0.2.1

- Rebuilt Options Levels around a dynamic reaction-zone engine instead of a reference-first chart layout.
- Added scored candidate construction from previous-day, previous-week, premarket, Opening Range, RTH open, confirmed swing pivots, gap structure, adaptive round numbers, RTH VWAP, optional VWAP bands, event AVWAP and optional ATR projections.
- Added explainable candidate scoring using source authority, historical reaction quality, impulse, touch quality, recency and available participation evidence.
- Added adaptive clustering with ATR-, tick- and percentage-aware tolerances, weighted zone centers, dispersion-based widths and diminishing returns for redundant evidence.
- Added actionability scoring so nearby high-quality zones are preferred over distant references, plus hysteresis to reduce zone flicker and unnecessary replacements.
- Changed the default presentation to the strongest active support and resistance reaction zones, with `Zones + Key References` and `Legacy / Debug` modes available for additional detail.
- Added zone lifecycle states for `DISTANT`, `APPROACHING`, `INSIDE`, `REJECTING`, `ACCEPTING`, `BROKEN` and `FLIPPED`.
- Added confirmed break and flip handling so wick-only movement does not immediately redefine a zone.
- Added brighter actionability-gated `BUY` and `SELL` edge areas at the outer edges of qualifying support and resistance zones.
- Simplified zone labels to show the zone role and current state without exposing internal scores, price ranges or confluence strings on the chart.
- Enlarged the compact top-right dashboard and kept range, nearest-state and confirmed daily-ATR information visible.
- Added a transparent Opening Range window box for the configured opening-range period.
- Made ±1σ and ±2σ VWAP bands independently available in normal display modes instead of limiting them to debug mode.
- Added research-only Data Window outputs for support/resistance bounds, strength, actionability and nearest-zone state.
- Replaced legacy level-break alerts with transition-focused alerts for zone entry, rejection, acceptance/break, confirmed flips and materially stronger zone selection.
- Preserved intraday-only operation, confirmed higher-timeframe values and bounded internal state.

## [0.1.0] — 2026-07-25

### Repository

- Rebuilt the public layout around durable `src/`, `docs/`, `assets/` and `tools/` directories.
- Replaced versioned source filenames with stable paths and added a machine-readable manifest.
- Removed the deprecated Futures Setups v0.2 source from the supported public tree.
- Rewrote the README for beginner installation, indicator selection and technical navigation.
- Added practical indicator guides, architecture, data-integrity and troubleshooting documentation.
- Added contribution, security, conduct and trading-risk policies.
- Added GitHub issue templates, pull-request guidance and dependency-free static CI validation.
- Renamed and optimized image assets.

### Source cleanup

- Standardized public indicator naming and US-English UI labels.
- Removed statically verified unused declarations and helper functions.
- Preserved bounded state and confirmed higher-timeframe request patterns.

### Futures Setups 0.3.6-beta

- Corrected the default signal window to 08:00–16:00 ET so code and documentation agree.
- Kept full-session zone/context processing at 18:00–17:00 ET.
- Preserved daily/research live-logic parity and documented the build differences.

### Individual script versions

- Options Levels 0.1.7
- Options Context 0.1.1
- Futures Levels 0.1.0
- Futures Context 0.1.7
- Futures Profile 0.1.2
- Futures Setups 0.3.6-beta
