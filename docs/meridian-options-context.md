# Meridian — Options Context

[← Back to the main README](../README.md) · [View source](../indicators/options/meridian-options-context/meridian-options-context.pine)

<p align="center">
  <img src="../screenshots/Meridian_Options_Context.png" alt="Meridian Options Context" width="100%">
</p>

## Purpose

**Meridian — Options Context** is a lower-pane dashboard for intraday analysis of liquid option underlyings. It combines momentum, participation and directional structure into a transparent context score.

The script is designed to answer five questions:

1. Is momentum bullish, bearish or neutral?
2. Is participation elevated for this exact time of day?
3. Is price above or below RTH VWAP?
4. Is price above, inside or below the completed Opening Range?
5. Do the short-term EMAs agree with direction?

It is a context tool rather than a standalone entry signal.

## Best Use

- Apply to SPY, QQQ or another liquid underlying
- Use standard intraday candles
- Pair with Meridian — Options Levels
- Keep the regular-session definition aligned across both indicators

## Pane Components

### RSI

The script calculates standard Relative Strength Index over the selected source and length. The default directional thresholds are:

- Bullish: RSI at or above 55
- Bearish: RSI at or below 45
- Neutral: between the thresholds

The pane can show 40, 50 and 60 guides, an optional 40–60 neutral zone and optional traditional 70/30 guides.

### Same-time Relative Volume

Options Context imports TradingView's official `ta` library and requests relative volume on a regular-session ticker. This prevents extended-hours volume from contaminating RTH comparisons.

Two values are calculated:

- **Bar RVOL:** current bar volume divided by the average volume at the equivalent daily offset.
- **Cumulative RVOL:** cumulative volume since RTH open divided by the historical average cumulative volume through the same offset.

Conceptually:

$$
RVOL_{bar}(t) = \frac{V_{today,t}}{Average(V_{prior\ days,t})}
$$

$$
RVOL_{cum}(t) = \frac{\sum_{open}^{t}V_{today}}{Average\left(\sum_{open}^{t}V_{prior\ days}\right)}
$$

The histogram is normalized to a 0–100 pane for visual compatibility with RSI:

$$
Displayed\ RVOL = \min\left(\frac{RVOL}{DisplayCap},1\right)\times100
$$

The dashboard continues to display the uncapped ratio.

### Daily RTH VWAP

VWAP is anchored at the detected RTH open. The dashboard reports whether price is above, below or at VWAP.

### Opening Range state

The Opening Range develops for the selected number of minutes after RTH open. Once finalized, the dashboard reports whether price is above, below or inside the range.

### EMA structure

The default 9 EMA and 21 EMA create a simple directional component:

- `9 > 21`: bullish contribution
- `9 < 21`: bearish contribution
- equal: neutral

## Context Score

The total score ranges from **−5 to +5**. Each enabled component contributes one point:

| Component | Bullish contribution | Bearish contribution |
|---|---|---|
| VWAP | Close above RTH VWAP | Close below RTH VWAP |
| RSI | RSI at/above bullish threshold | RSI at/below bearish threshold |
| EMA | Fast EMA above slow EMA | Fast EMA below slow EMA |
| Opening Range | Close above finalized ORH | Close below finalized ORL |
| Participation | High-RVOL bullish candle | High-RVOL bearish candle |

The regime mapping is:

| Score | Regime |
|---:|---|
| +4 to +5 | Strong Bull |
| +2 to +3 | Bullish |
| −1 to +1 | Mixed |
| −2 to −3 | Bearish |
| −4 to −5 | Strong Bear |

The score is a measure of feature agreement. It is not a historical probability of a profitable trade.

## Dashboard

The fixed dashboard summarizes:

- Regime and score
- RSI value and state
- Bar and cumulative RVOL
- RTH VWAP state
- Opening Range state
- EMA ordering
- Optional raw volume values

Because it is a Pine table, it remains fixed when the chart is scrolled or zoomed.

## Reading the Indicator

### Stronger alignment

A strong bullish context may include:

- RSI above its bullish threshold
- price above RTH VWAP
- fast EMA above slow EMA
- price above the completed Opening Range
- elevated RVOL on an advancing candle

The bearish equivalent uses the opposite conditions.

### Mixed context

A mixed score is useful information. It can indicate:

- price above VWAP but weak RSI
- an Opening Range break without participation
- elevated volume on a candle opposing the EMA direction
- rotational trade around VWAP

The dashboard is most useful when read against a nearby Options Levels reference rather than in isolation.

## Important Settings

| Group | Setting | Effect |
|---|---|---|
| Session | RTH and timezone | Controls VWAP and Opening Range boundaries |
| RSI | Thresholds | Defines bullish/neutral/bearish momentum |
| Relative Volume | Historical days | Controls the same-time comparison sample |
| Relative Volume | Real-time adjustment | Estimates an unfinished live bar |
| Context Engine | Include OR / participation | Enables or removes score components |
| Dashboard | Position and size | Controls fixed table presentation |

## Alerts

Available close-confirmed alerts include:

- strong bullish or bearish regime
- high RVOL threshold crossing
- VWAP reclaim or loss
- Opening Range break with high RVOL

## Limitations

- The score intentionally uses simple, interpretable components.
- Relative volume needs sufficient historical RTH data.
- An unfinished live candle may change before close.
- The script does not inspect option-chain data, implied volatility or Greeks.
- The Opening Range should be used on a timeframe no larger than its configured duration.

## Suggested Companion

Use [Meridian — Options Levels](./meridian-options-levels.md) on the main chart so the context score can be evaluated around objective session references.

## License

This source file is covered by the repository's [MPL-2.0 license](../LICENSE).
