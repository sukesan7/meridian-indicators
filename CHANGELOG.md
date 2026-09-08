# Changelog

All notable repository and public-script changes are recorded here.

## [0.2.0] — 2026-09-07

### Catalog design system

- Standardized the public catalog on the Meridian semantic palette: purple brand/header, teal bullish/support, coral bearish/resistance, cyan information, slate neutral, gray pending/developing and amber warnings.
- Standardized drawing semantics: solid confirmed references, dashed developing references, dotted projections, translucent gray potential states and faded/frozen invalidated states.
- Standardized normal text to Small with user-adjustable sizing.
- Rebuilt all normal dashboards as restrained top-right HUDs with `Meridian -- NAME` headers and no version number.
- Added `docs/design-system.md` and removed unused helper functions exposed by the visual cleanup.

### Options Levels 0.3.0

- Retained the reaction-zone architecture while standardizing the chart/HUD presentation for SPY options-underlying use.
- Added confirmed Equal High / Equal Low zone candidates with adaptive tolerance and bounded age.
- Added optional research-only potential support/resistance ghost zones below the normal qualification threshold.
- Changed Event AVWAP to disabled by default for the SPY-focused workflow while retaining manual and earnings modes.
- Preserved confirmed daily ATR, RTH/premarket session identity, actionability, hysteresis, BUY/SELL edge areas and confirmed zone lifecycle behavior.

### Options Context 0.3.0

- Standardized the lower-pane palette and compact dashboard.
- Corrected local EMA slope normalization to a per-bar slope before ATR normalization, preventing the slope-lookback setting from mechanically changing scale.
- Preserved the continuous Direction/Confidence model, same-time RVOL, magnitude-aware agreement and confirmed quality-aware 1H/4H/1D/1W context.
- Added clear live/confirmed/stale data-state presentation.

### Futures Levels 0.2.0

- Standardized chart/HUD visuals and reduced default marker/cluster-label clutter.
- Made OR/IB references dashed while developing and solid after confirmation.
- Preserved and re-audited trading-day/RTH session identities, VWAP reset/state behavior, moving-reference rejection timing and stale-data handling introduced in 0.1.5.
- Updated telemetry metadata to 0.2.0.

### Futures Context 0.2.0

- Standardized lower-pane visuals and corrected EMA/VWAP slopes to per-bar ATR-normalized values.
- Expanded the NQ/ES comparison into a multi-peer NQ/ES/YM/RTY intermarket engine with rolling beta, correlation, residual z-score, breadth and divergence/decoupling states.
- Kept the current session out of its own same-time baseline until observations confirm.

### Futures Profile 0.2.0

- Standardized profile/HUD presentation and added bounded Initial Balance range/volume percentile statistics plus IB efficiency.
- Added narrow/normal/wide/extreme IB classification for auction research.
- Fixed a session-roll defect that could overwrite an already finalized RTH close/end bar with the last premarket bar at the next RTH open.
- Updated telemetry metadata to 0.2.0.

### Futures Setups 0.4.0-beta

- Standardized Daily and Research build visuals while preserving live-qualification parity.
- Added Automatic/Manual multi-timeframe source selection.
- Added bounded zone-width percentile quality on top of ATR normalization.
- Added explicit causal-chain authority for ordered liquidity sweep → structure/MSS → displacement evidence.
- Enhanced overlap authority for breaker/OB + FVG/IFVG combinations without allowing overlap to bypass mandatory gates.
- Added nearest structural objective information to hypothesis evidence after objective-space qualification.
- Reworked research zones around BUILDING / CONFIRMED / INVALIDATED visual states inspired by the useful lifecycle patterns in the legacy research scripts.
- Updated repository parity validation for the 0.4.0-beta Daily/Research headers.

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
