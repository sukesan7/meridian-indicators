# Meridian — Futures Levels

[← Indicator documentation](../README.md) · [View source](../../src/futures/meridian-futures-levels.pine)

**Version:** 0.2.0<br>
**Status:** Stable<br>
**Primary markets:** NQ, MNQ, ES and MES

<p align="center"><img src="../../assets/screenshots/futures-levels.png" alt="Meridian Futures Levels" width="100%"></p>

## Purpose

Futures Levels is the objective location layer for index futures. It tracks session structure, VWAP, prior-period references, projections, confluence and confirmed interaction with those references. It does not predict direction.

## v0.2 revamp

- standardized Meridian palette, developing/confirmed/projected line semantics and the clean `Meridian -- Futures Levels` HUD;
- vertical time markers are off by default and cluster contributor text is hidden by default to reduce chart clutter;
- OR/IB lines are dashed while developing and solid once confirmed;
- preserved the v0.1.5 session-identity correction for RTH-only charts, futures maintenance gaps, weekends and holidays;
- retained source-identity resets for moving VWAP and previous-period acceptance/rejection state;
- retained stale/closed-data detection and explicit non-futures warnings;
- aligned telemetry/version metadata with v0.2.0.

## Main references

- full futures session and session open;
- overnight high, low and midpoint;
- RTH open;
- Opening Range and Initial Balance;
- custom RTH/full-session/week VWAP plus configurable deviation bands;
- confirmed previous day and previous week;
- Fibonacci retracements and symmetric range projections;
- confluence clusters.

## Session and VWAP integrity

RTH identity uses the configured local session date rather than assuming an out-of-session chart bar exists. Full-session and overnight identity use `time_tradingday`, so the daily CME maintenance gap still creates a new trading session.

This prevents the former failure where an RTH-only chart could carry Friday's VWAP into the next trading day, or a futures chart could carry a full-session VWAP across the maintenance break.

Dynamic VWAP state is reset with the VWAP anchor. Moving-reference rejection compares the previous close with the previous tracked VWAP/band value rather than the current moved value.

## OR / IB

The default OR is 15 minutes and IB is 60 minutes. Developing geometry uses the developing visual state; confirmed lines become solid after the collection window completes.

## Confluence

Nearby independent references are grouped with tick- or ATR-aware tolerance. The normal label is intentionally short (`CONFLUENCE ×N`). Detailed contributor names are optional.

Clusters summarize calculated proximity. They do not prove resting liquidity.

## Recommended setup

```text
Market: active NQ/MNQ or ES/MES contract
Chart: 1–15 minutes
Extended hours: enabled
Timezone: America/New_York
Full session: 18:00–17:00 ET
Overnight: 18:00–09:30 ET
RTH: 09:30–16:00 ET
VWAP anchor: RTH or Full Futures Session
```

## Dashboard

The fixed top-right HUD shows session, OR, IB, VWAP, last interaction state and data state. It intentionally omits version and configuration noise.

## Alerts

Confirmed alerts cover accepted-above, accepted-below, bullish rejection and bearish rejection. Optional JSON telemetry uses the same confirmed state engine.

## Limitations

The script is designed for futures. RTH references can be inspected on SPY, but futures-session/overnight semantics should not be treated as authoritative there; use Options Levels for SPY options workflows. Continuous-contract adjustments can change historical references, and coarse charts reduce OR/IB timing precision.
