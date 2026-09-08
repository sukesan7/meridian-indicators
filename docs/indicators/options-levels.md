# Meridian — Options Levels

[← Indicator documentation](../README.md) · [View source](../../src/options/meridian-options-levels.pine)

**Version:** 0.3.0<br>
**Status:** Stable<br>
**Primary market:** SPY; also usable on other liquid US-listed underlyings

<p align="center"><img src="../../assets/screenshots/options-levels.png" alt="Meridian Options Levels" width="100%"></p>

## Purpose

Options Levels is the location layer for the options-underlying workflow. It reduces a large reference universe to one active support reaction zone and one active resistance reaction zone while keeping the calculations explainable and bounded.

The script analyzes the **underlying**. It does not read the option chain, Greeks, implied volatility, dealer positioning or contract-specific liquidity.

## v0.3 revamp

- standardized Meridian palette, small adjustable text and a simple top-right `Meridian -- Options Levels` HUD;
- added confirmed Equal High / Equal Low candidates with ATR/tick-aware tolerance and age limits;
- added optional research-only `POTENTIAL SUPPORT` / `POTENTIAL RESISTANCE` ghost zones below the normal qualification threshold;
- retained the confirmed zone lifecycle, actionability, anti-flicker switching and BUY/SELL edge areas;
- changed Event AVWAP to **Disabled** by default for SPY-focused use; manual and earnings modes remain available;
- kept confirmed daily ATR normalization and robust RTH/premarket date identity.

## Reaction-zone engine

Candidates can come from:

- prior RTH high, low and close;
- prior week high and low;
- premarket high and low;
- finalized Opening Range;
- RTH open;
- RTH VWAP and optional VWAP deviation bands;
- confirmed swing pivots;
- confirmed equal highs/equal lows;
- current-session gap structure;
- adaptive round numbers;
- optional ATR projections;
- optional Event AVWAP.

Candidates are scored from source authority, historical reaction quality, reaction impulse, touch quality, recency and available participation. Nearby candidates are clustered using ATR-, tick- and percentage-aware tolerances. Cluster width is derived from the weighted distribution of the members rather than a fixed arbitrary box.

Selection adds **actionability** so a strong nearby area can outrank a marginally stronger zone several ATR away. Hysteresis prevents small score changes from constantly replacing the displayed zone.

## Zone states

`DISTANT → APPROACHING → INSIDE → REJECTING / ACCEPTING → BROKEN → FLIPPED`

Breaks require configured confirmation rather than a wick alone. A broken zone only flips after a later retest/hold from the opposite side.

## BUY / SELL edge areas

A qualifying support zone can display a brighter `BUY` band at its lower edge; qualifying resistance can display a `SELL` band at its upper edge. These are location cues gated by actionability, not complete trade signals.

## Display modes

| Mode | Use |
|---|---|
| `Reaction Zones` | Clean default view |
| `Zones + Key References` | Adds important raw references |
| `Legacy / Debug` | Investigation and validation |

Potential ghost zones are separate research controls and are off by default.

## SPY starting configuration

```text
Chart: SPY
Timeframe: 1–15 minutes
Candles: standard
Extended hours: enabled when premarket references are wanted
Timezone: America/New_York
RTH: 09:30–16:00 ET
Premarket: 04:00–09:30 ET
Opening Range: 15 minutes
Display: Reaction Zones
Event AVWAP: Disabled unless intentionally anchored
```

## VWAP and Opening Range

RTH VWAP resets from the detected RTH session identity. ±1σ and ±2σ bands can be displayed in normal modes. Whether a VWAP band also participates as a zone candidate is configured separately.

The Opening Range only becomes a zone source after its window finishes. A transparent box can highlight the actual collection period.

## Dashboard

The normal HUD shows only:

- active resistance range;
- active support range;
- nearest-zone state;
- session/data context.

Internal scoring remains in research outputs and tooltips.

## Alerts

Confirmed transitions include zone entry, support/resistance rejection, acceptance/break, confirmed flip and materially stronger zone selection.

## Data integrity

- daily ATR uses the previous completed daily value for normalization;
- confirmed pivots become eligible after right-side confirmation;
- reaction evidence is not credited before the reference was knowable;
- RTH/premarket session starts use calendar identity as well as session membership;
- internal candidate and reaction histories are bounded.

## Limitations

Scores rank evidence; they are not probabilities or expected returns. Premarket references require an extended-hours feed. Event AVWAP quality depends on the chosen anchor. The script does not select an option contract or model execution.

## Companion

Use [Options Context](./options-context.md) to decide whether the current environment favors support reactions, resistance reactions, both sides or neither side with sufficient conviction.
