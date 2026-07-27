# Meridian — Options Levels

[← Indicator documentation](../README.md) · [View source](../../src/options/meridian-options-levels.pine)

**Version:** 0.1.7<br>
**Status:** Stable<br>
**Use on:** liquid options underlyings such as SPY and QQQ

<p align="center"><img src="../../assets/screenshots/options-levels.png" alt="Meridian Options Levels" width="100%"></p>

## Purpose

Options Levels is a price-chart overlay for objective intraday references. It is designed for traders who want session levels without turning the chart into a signal generator.

## What it displays

- previous regular-session high, low and close;
- previous-week high and low;
- current regular-session open;
- developing premarket high and low;
- configurable Opening Range high, low and box;
- regular-session VWAP with optional ±1σ and ±2σ bands;
- optional fast and slow EMAs;
- right-edge labels and confirmed break/rejection alerts.

## Recommended setup

```text
Chart: SPY, QQQ or another liquid US-listed underlying
Timeframe: 1–15 minutes
Candles: standard
Extended hours: enabled when premarket levels are needed
Timezone: America/New_York
Regular session: 09:30–16:00 ET
Premarket: 04:00–09:30 ET
Opening Range: 15 minutes
```

## Calculation behavior

Previous-day and previous-week values are rolled from completed sessions. Premarket and Opening Range values develop until their configured windows end. VWAP resets at the detected regular-session open and uses the chart symbol's volume and selected source.

The script is intraday-only and raises a runtime error on non-intraday charts.

## Important settings

| Group | Use |
|---|---|
| Sessions | Timezone, regular session, premarket session and weekdays-only filter |
| Levels | Toggle previous-day, previous-week, close, session open and premarket references |
| Opening Range | Duration, box visibility and shading |
| VWAP | Source, deviation bands and transparency |
| Trend Filters | Optional fast and slow EMAs |
| Colors & Style | Line colors, widths and line styles |
| Labels | Price text, right offset and stagger behavior |
| Alerts | Enable or suppress individual state events |

## Alerts

Available alert conditions include breaks of PDH, PDL, PMH, PML, PWH, PWL, ORH and ORL; VWAP reclaim and loss; and bullish or bearish VWAP rejection. Events are confirmed on chart bars.

## Limitations

- The indicator analyzes the underlying, not option-chain Greeks, implied volatility or contract liquidity.
- Premarket data requires extended-hours bars from the chart feed.
- Opening Range precision depends on chart timeframe and session alignment.
- VWAP and bands are chart-feed calculations and can differ slightly across data providers.

## Companion

Use [Options Context](./options-context.md) below the chart to evaluate momentum and participation at these levels.
