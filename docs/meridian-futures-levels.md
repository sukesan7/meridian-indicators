# Meridian — Futures Levels

[← Back to the main README](../README.md) · [View source](../indicators/futures/meridian-futures-levels/meridian-futures-levels.pine)

<p align="center">
  <img src="../screenshots/Meridian_Futures_Levels.png" alt="Meridian Futures Levels" width="100%">
</p>

## Purpose

**Meridian — Futures Levels** is the primary price-overlay indicator for the Meridian futures suite. It organizes futures-session structure, prior references, Opening Range, Initial Balance, VWAP bands, projections and confluence zones into a configurable chart layer.

Its primary question is:

> Where are the important prices, and how is the market behaving when it reaches them?

## Best Use

- Markets: NQ, ES, MNQ, MES and related index futures
- Timeframes: 1, 5 and 15 minutes are recommended
- Chart type: standard candles
- Session timezone: `America/New_York`
- Live contract: preferred for current execution context

## Session Structure

The default session definitions are:

- Full futures session: 18:00–17:00 ET
- Overnight session: 18:00–09:30 ET
- RTH: 09:30–16:00 ET

The script can display:

- full-session open
- RTH open
- overnight high, low and optional midpoint
- subtle session shading
- vertical time markers for premarket, market open, NY killzone end and market close

All sessions are editable.

## Opening Range and Initial Balance

### Opening Range

The Opening Range starts at the configured RTH open and supports 1, 5, 15 or 30-minute durations.

$$
ORH_t = \max(High_1,\ldots,High_t)
$$

$$
ORL_t = \min(Low_1,\ldots,Low_t)
$$

The midpoint is:

$$
ORM = \frac{ORH + ORL}{2}
$$

The shaded region, lines and labels are limited to RTH.

### Initial Balance

The Initial Balance uses a configurable number of minutes from the RTH open, with 60 minutes as the conventional default.

$$
IBH = \max(High\ during\ IB)
$$

$$
IBL = \min(Low\ during\ IB)
$$

$$
IBM = \frac{IBH + IBL}{2}
$$

IB drawings also stop at the RTH close.

## Custom VWAP and Deviation Engine

VWAP can be anchored to:

- RTH
- full futures session
- week

The core calculation is:

$$
VWAP = \frac{\sum P_iV_i}{\sum V_i}
$$

Two deviation methods are available.

### Volume-weighted deviation

$$
\sigma_v = \sqrt{\frac{\sum P_i^2V_i}{\sum V_i} - VWAP^2}
$$

### Unweighted deviation

$$
\sigma_u = \sqrt{\frac{\sum P_i^2}{N} - \left(\frac{\sum P_i}{N}\right)^2}
$$

Up to three configurable upper/lower bands can be displayed:

$$
Upper_k = VWAP + m_k\sigma
$$

$$
Lower_k = VWAP - m_k\sigma
$$

## Previous-Day and Previous-Week References

The indicator supports:

- previous-day high and low
- previous-week high and low

Previous-day values can come from either:

1. the confirmed exchange daily candle; or
2. the custom RTH session tracked by the script.

Higher-timeframe exchange references request the previous completed candle, preventing an unfinished daily or weekly bar from being used as the prior reference.

## Fibonacci and Range Projections

Available anchor ranges:

- Opening Range
- Initial Balance
- Overnight range
- Previous Day
- Previous Week

For a range $R = High-Low$, an internal retracement is:

$$
Level_r = Low + rR
$$

An upper projection is:

$$
Projection_{up} = High + pR
$$

A lower projection is:

$$
Projection_{down} = Low - pR
$$

Default retracements are 0.382, 0.500 and 0.618. Default projection distances are 0.272, 0.618 and 1.000, corresponding to levels such as 1.272 above and −0.272 below the range.

## Confluence Clustering

The clustering engine combines visible levels from selected families:

- day/week references
- OR, IB and overnight structure
- VWAP and bands
- Fibonacci levels

Levels are sorted by price and grouped when they fall within either:

- a fixed tick tolerance; or
- an ATR-normalized tolerance

Each contributor has a predefined weight. A cluster center is calculated as a weighted average:

$$
ClusterCenter = \frac{\sum w_iL_i}{\sum w_i}
$$

The displayed score combines total contributor weight with a small contributor-count bonus. The highest-ranked clusters are rendered as bounded zones. A cluster above price is styled as potential resistance, one below price as potential support, and one surrounding price as neutral confluence.

## Acceptance and Rejection States

The state engine tracks selected levels including PDH/PDL, PWH/PWL, OR, IB, overnight, VWAP, the first VWAP band, first Fib projection and session opens.

### Acceptance

A level is accepted above or below after the configured number of consecutive closes beyond a tick buffer.

For acceptance above:

$$
Close_t > Level + Buffer
$$

for `N` consecutive closes.

### Rejection

A bullish rejection requires:

- price approached from above
- the bar touched or exceeded the level within tolerance
- the bar closed back above the acceptance buffer
- the lower wick met the minimum ATR fraction

A bearish rejection uses the inverse conditions.

When multiple events occur on one bar, the script selects the strongest event using level weight and distance from price. Chart labels are off by default, while the last confirmed state remains available in the HUD and alerts.

## Dashboard

The compact Futures Levels HUD shows:

- active session
- OR range
- IB range
- current VWAP
- most recent level-state event
- timeframe or confirmed-state status

Price-scale values, right-edge labels, state labels and state-aware colors are independently configurable.

## Alerts

The indicator includes static alert conditions and optional dynamic JSON `alert()` events. Structured events include symbol, timeframe, level, state, price, close and bar timestamp.

## Reading the Indicator

A useful sequence is:

1. Identify the nearest objective level or confluence cluster.
2. Check whether price is approaching from above or below.
3. Observe acceptance/rejection behavior.
4. Check participation and regime in Futures Context.
5. Check whether value in Futures Profile is migrating toward or away from the level.

## Important Settings

| Group | Setting | Effect |
|---|---|---|
| Sessions | Session strings | Defines futures, overnight and RTH windows |
| Opening Range | Duration | Selects 1/5/15/30-minute OR |
| Initial Balance | Duration | Sets IB collection period |
| VWAP | Anchor and deviation method | Selects reset period and band model |
| Previous References | Previous-day source | Chooses exchange daily or custom RTH |
| Clustering | Tolerance and contributors | Controls confluence zones |
| Acceptance/Rejection | Close, wick and tolerance rules | Controls state sensitivity |
| HUD | Position and alerts | Controls dashboard and JSON events |

## Limitations

- OR and IB precision depend on chart bars aligning with their boundaries.
- Continuous futures can contain rollover or back-adjustment effects.
- Exchange daily bars and custom RTH bars may produce different previous-day values.
- Clusters show proximity, not guaranteed support or resistance.
- State classifications are rule-based and can produce false positives.

## Suggested Companions

- [Meridian — Futures Context](./meridian-futures-context.md)
- [Meridian — Futures Profile](./meridian-futures-profile.md)

## License

This source file is covered by the repository's [MPL-2.0 license](../LICENSE).
