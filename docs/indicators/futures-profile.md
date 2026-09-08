# Meridian — Futures Profile

[← Indicator documentation](../README.md) · [View source](../../src/futures/meridian-futures-profile.pine)

**Version:** 0.2.0<br>
**Status:** Preview<br>
**Primary markets:** NQ, MNQ, ES and MES

<p align="center"><img src="../../assets/screenshots/futures-profile.png" alt="Meridian Futures Profile" width="100%"></p>

## Purpose

Futures Profile is the auction layer. It builds current and previous RTH Time Price Opportunity profiles, estimates value and profile structure, and classifies how the current auction relates to the completed prior session.

## v0.2 revamp

- standardized profile colors, small adjustable text and the fixed top-right `Meridian -- Futures Profile` HUD;
- added historical Initial Balance quality using bounded IB-range and IB-volume percentile baselines;
- added IB efficiency from net RTH-open displacement relative to the completed IB range;
- fixed a session-roll defect where a profile already finalized at RTH end could have its true RTH close/end bar overwritten by the last premarket bar when the next RTH opened;
- retained bounded maps and drawing limits for profile safety;
- aligned dynamic telemetry with v0.2.0.

## TPO construction

The RTH session is divided into configured time blocks. Each completed block contributes one TPO to every price row traversed by that block. The active block can be included for display while completed-block accounting remains separate.

Row size can be automatic or manual. Automatic sizing uses the previous session range and a target row count, bounded by the instrument tick size.

## Core outputs

- TPO POC, VAH and VAL;
- profile high/low/midpoint;
- Initial Balance and extensions;
- TPO counts above/below POC;
- rotation factor;
- single-print rows;
- poor high / poor low;
- profile shape and auction state;
- current-vs-previous value and POC migration.

## Initial Balance quality

After the configured IB completes, its range and confirmed IB volume are compared with a bounded history of prior completed IBs. The dashboard classifies the current IB as `NARROW`, `NORMAL`, `WIDE` or `EXTREME` and can show its range and volume percentiles.

The statistic is descriptive. It is intended to help study range-consumption/day-type behavior rather than assert that a particular IB percentile guarantees expansion or rotation.

## Estimated volume profile

Optional estimated volume distributes each confirmed chart bar's volume uniformly across every price row the bar traversed. Estimated VPOC/VAH/VAL are useful approximations but are **not** exchange-native volume-at-price, bid/ask delta or footprint data.

## Recommended setup

```text
Market: active NQ/MNQ or ES/MES contract
Chart: 1–15 minutes, standard candles
RTH: 09:30–16:00 ET
TPO block: 30 minutes
Row size: Auto initially
Estimated volume: optional
```

## Dashboard

The simple HUD shows auction state, value migration, profile shape, IB quality, location and data/warning state. Detailed calculation values remain on the chart or in alerts rather than becoming dashboard cards.

## Alerts

Confirmed conditions cover previous POC/VAH/VAL tests, previous single-print interaction, poor-extreme repair and auction-state changes. Optional JSON telemetry mirrors the same confirmed events.

## Limitations

TPO precision depends on chart timeframe, session alignment and row size. Rendering is bounded. Automatic row sizing is a usability heuristic. IB percentiles require enough completed sessions to warm up. Estimated volume is not native footprint data.
