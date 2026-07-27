# Meridian — Futures Levels

[← Indicator documentation](../README.md) · [View source](../../src/futures/meridian-futures-levels.pine)

**Version:** 0.1.0<br>
**Status:** Stable<br>
**Primary markets:** NQ, MNQ, ES and MES

<p align="center"><img src="../../assets/screenshots/futures-levels.png" alt="Meridian Futures Levels" width="100%"></p>

## Purpose

Futures Levels is a session-aware overlay for objective index-futures references, custom VWAP, projected levels and confluence clusters. It describes location; it does not predict direction.

## Main features

- full-session, overnight and RTH structure;
- overnight midpoint and optional session shading;
- configurable Opening Range and Initial Balance;
- custom session VWAP with volume-weighted or unweighted deviation bands;
- confirmed previous-day and previous-week references;
- configurable Fibonacci retracements and range projections;
- clustering across independent level families;
- confirmed acceptance and rejection states;
- compact HUD and optional dynamic JSON alerts.

## Recommended setup

```text
Market: active NQ, MNQ, ES or MES contract
Chart: 1–15 minutes, standard candles
Extended hours: enabled
Timezone: America/New_York
Full session: 18:00–17:00 ET
Overnight: 18:00–09:30 ET
RTH: 09:30–16:00 ET
```

## Opening Range and Initial Balance

The Opening Range and Initial Balance are tracked from their configured starts and durations. Developing levels can be shown while the window is active, then freeze when complete. Finer charts align more precisely with start and end boundaries.

## VWAP engine

The script maintains its own session VWAP. Deviation bands can use volume-weighted variance or an unweighted price variance. Optional carry behavior controls whether completed values remain visible outside the active session.

## Confirmed references

Previous-day and previous-week values come from completed higher-timeframe bars. The script uses the confirmed-source offset required for safe historical requests.

## Confluence clusters

Enabled level families are grouped when their prices fall within the selected tick- or ATR-based tolerance. A cluster requires the configured number of independent contributors. The displayed cluster is a summary of nearby references, not a new market-data source.

## Acceptance and rejection

Tracked levels can progress through touch, acceptance or rejection logic. Acceptance requires price to hold beyond the configured threshold; rejection requires a test and close back away from the level. Cooldowns and label caps limit repeated events.

## Important settings

| Group | Use |
|---|---|
| General | Enable state, label format and right-side extension |
| Sessions | Full, overnight and RTH definitions |
| Opening Range / Initial Balance | Duration, developing lines and fills |
| VWAP | Source, deviation method, bands and display |
| Previous Day / Week | Reference visibility |
| Fibonacci + Projections | Anchor family and projected levels |
| Level Clustering | Tolerance, contributor count and labels |
| Acceptance / Rejection | Touch and confirmation thresholds |
| Theme / HUD | Visual density and dashboard placement |
| Alerts | Static conditions and optional dynamic JSON |

## Alerts

Static conditions cover accepted-above, accepted-below, bullish rejection and bearish rejection events. Dynamic JSON can include the tracked level and state when explicitly enabled.

## Limitations

- Session levels depend on the chart feed and selected contract.
- Continuous-contract adjustments can alter historical references.
- Clusters summarize proximity; they do not prove liquidity or order concentration.
- Coarse charts reduce OR, IB and state timing precision.

## Suggested companions

Use [Futures Context](./futures-context.md) for environment and [Futures Profile](./futures-profile.md) for auction structure.
