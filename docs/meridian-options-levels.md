# Meridian — Options Levels

[← Back to the main README](../README.md) · [View source](../indicators/options/meridian-options-levels/meridian-options-levels.pine)

<p align="center">
  <img src="../screenshots/Meridian_Options_Levels.png" alt="Meridian Options Levels" width="100%">
</p>

## Purpose

**Meridian — Options Levels** is a chart-overlay indicator for intraday analysis of liquid option underlyings such as SPY and QQQ. It organizes the most frequently referenced session levels into one consistent visual system so traders can evaluate where the underlying is trading before selecting or managing an options position.

The indicator is applied to the **underlying chart**, not to an individual option contract. It does not calculate an option's implied volatility, Greeks or expected value.

## Best Use

- Markets: SPY, QQQ and other liquid U.S. equities or ETFs
- Chart type: standard time-based candles
- Timeframes: typically 1–15 minutes
- Extended hours: required for live premarket high/low tracking
- Primary session timezone: `America/New_York`

## Features

### Previous regular-session levels

- Previous-day high (`PDH`)
- Previous-day low (`PDL`)
- Previous-day close (`PDC`)
- Previous-week high (`PWH`)
- Previous-week low (`PWL`)

The script tracks regular-session bars directly. When a completed day or week rolls into the next period, those values are frozen and published as prior references. The line begins at the bar where the high, low or close occurred.

### Current-session references

- Regular-session open (`RTH OPEN`)
- Premarket high (`PMH`)
- Premarket low (`PML`)
- Opening-range high (`ORH`)
- Opening-range low (`ORL`)

Premarket levels develop only during the configured premarket session, then remain fixed during RTH. The Opening Range develops for the configured number of minutes after the regular-session open and then becomes fixed.

### RTH VWAP and deviation bands

The script uses an RTH-anchored VWAP that resets on the first regular-session bar:

$$
VWAP_t = \frac{\sum_{i=1}^{t} P_iV_i}{\sum_{i=1}^{t}V_i}
$$

where $P_i$ is the selected source, normally `hlc3`, and $V_i$ is volume. Optional first and second deviation bands use the selected multipliers around the anchored VWAP.

### Optional EMA trend filter

A configurable fast and slow EMA can be displayed to provide a simple directional reference. The defaults are 9 and 21 periods.

### Right-edge labels

Labels are distributed across separate right-edge columns to reduce collisions. Prices, offsets, sizes and colors are configurable.

## How the Levels Are Calculated

### Previous day

Only regular-session bars contribute to the current day's high, low and close. At the next premarket or RTH open:

1. The completed RTH values are copied into the previous-day fields.
2. Prior drawing objects are replaced.
3. A new RTH session begins tracking.

Completed prior-day values do not continue changing during the new session.

### Previous week

The script maintains a regular-session high and low for the current calendar week. When the weekly key changes, the completed values become `PWH` and `PWL`.

### Premarket

During the configured premarket session:

$$
PMH_t = \max(PMH_{t-1}, High_t)
$$

$$
PML_t = \min(PML_{t-1}, Low_t)
$$

Extended-hours bars must be visible for this calculation to receive premarket data.

### Opening Range

At the RTH open, the script starts a timer for the configured range length. Until that timer expires:

$$
ORH_t = \max(High_1, \ldots, High_t)
$$

$$
ORL_t = \min(Low_1, \ldots, Low_t)
$$

The shaded box covers only the actual Opening Range time window. For accurate results, the chart timeframe should be no larger than the Opening Range duration.

## Reading the Indicator

A level is not automatically support or resistance. It is a reference at which to observe:

- approach speed and candle expansion
- acceptance through closes beyond the level
- rejection through failed breaks or wick responses
- participation from Options Context RVOL
- location relative to RTH VWAP
- agreement or conflict between the fast and slow EMA

A common workflow is to mark the nearest levels before the open, then use the Context pane to judge whether a move through them has directional and participation support.

## Important Settings

| Group | Setting | Effect |
|---|---|---|
| Sessions | Regular session | Defines RTH tracking and VWAP reset |
| Sessions | Premarket session | Defines PMH/PML collection window |
| Opening Range | Opening-range minutes | Sets the range duration after RTH open |
| VWAP | Band 1 / Band 2 | Shows optional deviation envelopes |
| Trend Filters | Fast / slow EMA | Controls optional EMA references |
| Labels | Price and offset controls | Adjusts label density at the right edge |
| Alerts | Enable alerts | Activates close-confirmed alert conditions |

## Alerts

Available alert conditions include:

- PDH and PDL breaks
- PMH and PML breaks
- PWH and PWL breaks
- Opening Range breakout and breakdown
- VWAP reclaim and loss
- Bullish and bearish VWAP rejection

Alerts are evaluated using close-confirmed conditions to reduce noise from temporary wick-throughs.

## Limitations

- Premarket levels require extended-hours data.
- The script is designed for intraday charts.
- A chart timeframe larger than the Opening Range duration cannot represent the exact intrabar boundary.
- VWAP and volume quality depend on the symbol's TradingView feed.
- The indicator analyzes the underlying, not the option chain.

## Suggested Companion

Use [Meridian — Options Context](./meridian-options-context.md) beneath the chart to compare the level structure with RSI, same-time RVOL, VWAP state, Opening Range state and EMA agreement.

## License

This source file is covered by the repository's [MPL-2.0 license](../LICENSE).
