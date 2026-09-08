# Changelog

All notable repository and public-script changes are recorded here.

## [0.1.3] — 2026-09-07

### Futures Levels 0.1.5

- Reworked session-boundary detection so RTH resets use the New York session date and full-futures/overnight resets use the instrument trading day rather than depending on an out-of-session chart bar.
- Fixed RTH VWAP, full-session VWAP and their deviation bands carrying prior sessions forward on RTH-only charts or across futures maintenance gaps.
- Fixed RTH open, futures-session open and custom-RTH previous-day high/low rollover so new sessions initialize correctly after weekends, holidays and chart-data gaps.
- Added explicit source identities for previous-day and previous-week references so state history resets when the underlying confirmed source period changes, even when the new price is close to the old one.
- Reset VWAP and ±1σ acceptance/rejection state at every VWAP anchor change so confirmation counts cannot span separate sessions or weeks.
- Corrected moving-level rejection logic to compare the previous close with the previous tracked VWAP/band value instead of the current bar's moved reference.
- Restricted RTH-open state/clustering to active RTH and futures-session-open state/clustering to the active full session so stale opens do not influence unrelated overnight periods.
- Corrected vertical time-marker boundary handling, deduplicated markers at exact timestamps and kept historical marker labels aligned with the developing day high.
- Updated the HUD to distinguish the last bar's session from live data freshness, show `LIVE`, `LAST CONFIRMED` or `STALE / CLOSED`, identify the active VWAP anchor and warn when the script is being tested on a non-futures symbol.
- Separated previous-day/week drawing start bars from futures-session bookkeeping and removed unused session-start state.
- Aligned the source header, HUD and dynamic JSON alert metadata to version 0.1.5.
- Preserved confirmed prior-day/prior-week higher-timeframe requests, bounded drawing/state storage and confirmed-bar state alerts.

## [0.1.2] — 2026-08-11

### Options Context 0.2.1

- Rebuilt Options Context from the v0.1 binary `-5…+5` voting model into separate continuous `Context Direction` (`-100…+100`) and `Context Confidence` (`0…100`) outputs.
- Added independently inspectable Trend, Structure, Momentum, Participation, Persistence and Volatility components so directional context remains explainable rather than collapsing all evidence into opaque signals.
- Reworked Trend around ATR-normalized EMA spread and fast/slow EMA slope instead of a simple bullish/bearish EMA vote.
- Reworked Structure around continuous displacement from RTH VWAP, the finalized Opening Range and the RTH open while leaving objective support/resistance ownership to Options Levels.
- Reworked Momentum around ATR-normalized multi-bar returns, centered RSI and momentum change instead of fixed RSI threshold votes.
- Preserved same-time TradingView RVOL baselines while adding directional participation from close location and normalized one-bar return, with separate bar and cumulative RVOL intensity.
- Added session persistence scoring from VWAP location, EMA alignment and bar direction across a configurable RTH lookback.
- Added a non-directional volatility regime score based on short/long ATR behavior and rolling volatility z-score; volatility influences confidence rather than bullish/bearish direction.
- Added confirmed 1H, 4H, 1D and 1W higher-timeframe trend states using regular-session data and completed higher-timeframe bars.
- Deepened each HTF score with EMA structure, per-bar EMA slope, recent ATR-normalized path return, path efficiency, persistence and RSI rather than relying primarily on a moving-average snapshot.
- Added independent HTF quality measurement, weighted HTF Composite, Tactical (`1H + 4H`) and Macro (`1D + 1W`) research scores.
- Replaced the potentially misleading `100% ALIGN` presentation with magnitude-aware `HTF Conviction` and explicit breadth such as `4/4 BULL`, `3/4 BEAR` or `MIXED`.
- Added magnitude-aware directional agreement so weak same-sign components no longer produce artificially perfect confidence.
- Added `Levels Bias` states (`PREFER SUPPORT`, `SUPPORT LEAN`, `TWO-SIDED`, `RESISTANCE LEAN`, `PREFER RESISTANCE`, `LOW CONVICTION`) as the companion contract with Options Levels.
- Added regime hysteresis to reduce rapid label changes around context thresholds.
- Reoriented alerts toward confirmed context transitions, high-confidence directional states, aligned RVOL surges and recent strong-regime failures instead of duplicating price-level alerts owned by Options Levels.
- Added detailed and compact dashboard modes plus research-only Data Window outputs for component scores, agreement/coherence, HTF quality, HTF tactical/macro state, Zone Preference and the legacy v0.1 comparison score.
- Restricted the indicator to intraday chart timeframes below 60 minutes and preserved confirmed/non-lookahead higher-timeframe behavior.

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
