# Meridian — Futures Context

[← Back to the main README](../README.md) · [View source](../indicators/futures/meridian-futures-context/meridian-futures-context-v0.1.6.pine)

<p align="center">
  <img src="../screenshots/Meridian_Futures_Context.png" alt="Meridian Futures Context" width="100%">
</p>

## Purpose

**Meridian — Futures Context** is a lower-pane market-state indicator for NQ, ES, MNQ and MES. It measures participation, realized volatility, VWAP location, EMA structure, directional quality and relative strength, then combines those features into an explainable regime classification.

Its primary question is:

> What type of market environment is currently developing?

## Dashboard Cards

The fixed dashboard contains six cards:

- **Regime:** market-state classification, directional bias and agreement confidence
- **Participation:** same-time bar RVOL and cumulative RVOL
- **Trend Structure:** EMA state, ADX and directional efficiency
- **Volatility:** realized-volatility ratio and z-score
- **Relative Strength:** beta-adjusted NQ/ES residual
- **Location / Range:** RTH VWAP state and developing-range ratio

The supporting pane displays RVOL columns, cumulative RVOL, realized-volatility ratio and an optional range ratio around a 1.0 normal baseline.

## Same-Time-of-Day Baseline Engine

The script divides each RTH session into chart-timeframe slots. For example, on a five-minute chart, the 10:05 candle is compared only with historical 10:05 candles.

For every slot, bounded circular arrays retain prior-session observations. The current confirmed bar is written only after its calculations have used the previous-session baseline, preventing the current observation from contaminating its own comparison.

### Bar RVOL

$$
RVOL_{bar}(t) = \frac{Volume_{today,t}}{AverageVolume_{prior\ sessions,t}}
$$

### Cumulative RVOL

$$
RVOL_{cum}(t) = \frac{\sum_{open}^{t}Volume_{today}}{\sum_{open}^{t}ExpectedVolume_{historical}}
$$

### Developing-range ratio

The session high-low range through the current slot is compared with the historical average developing range through that same slot:

$$
RangeRatio(t) = \frac{Range_{today,open\rightarrow t}}{AverageRange_{prior\ sessions,open\rightarrow t}}
$$

The baseline requires the configured minimum number of samples before these metrics become active.

## RTH VWAP Context

The script calculates its own RTH VWAP and volume-weighted deviation:

$$
VWAP = \frac{\sum P_iV_i}{\sum V_i}
$$

$$
\sigma_v = \sqrt{\frac{\sum P_i^2V_i}{\sum V_i}-VWAP^2}
$$

The price-location z-score is:

$$
VWAPZ = \frac{Close - VWAP}{\sigma_v}
$$

VWAP state also considers normalized slope and the number of recent price/VWAP crossings. Repeated crossings near VWAP are classified as rotation rather than directional acceptance.

## EMA Structure

The default EMA stack is 9, 20 and 50. The script calculates:

- ordering of the three EMAs
- maximum-to-minimum spread normalized by ATR
- fast and middle EMA slopes normalized by ATR
- pullback state
- compression or expansion

Possible states include:

- Bull Expansion
- Bear Expansion
- Bull Pullback
- Bear Pullback
- Bull Stack
- Bear Stack
- Compressed
- Tangled

## Trend Quality

### ADX and DI

Directional Movement Index supplies `+DI`, `−DI` and ADX. ADX contributes strength while the DI relationship contributes direction.

### Directional efficiency

The efficiency ratio compares net movement with total path length:

$$
Efficiency_n = \frac{|Close_t-Close_{t-n}|}{\sum_{i=1}^{n}|Close_i-Close_{i-1}|}
$$

Values near 1 indicate direct movement; lower values indicate a more rotational path.

### Trend-quality score

The normalized trend-quality score is:

- 35% ADX strength
- 30% directional efficiency
- 20% EMA separation
- 15% absolute VWAP slope

## Realized Volatility

The script uses log returns:

$$
r_t = \ln\left(\frac{Close_t}{Close_{t-1}}\right)
$$

Rolling realized volatility is the square root of the sum of squared returns over the selected window:

$$
RV_t = \sqrt{\sum_{i=t-n+1}^{t}r_i^2}
$$

It is compared with an EMA baseline:

$$
RVRatio = \frac{RV_t}{EMA(RV)_t}
$$

A rolling z-score is also displayed.

## Relative Strength

Automatic mode compares:

- NQ/MNQ against ES
- ES/MES against NQ

A custom anchor can be selected.

One-bar log returns are used to estimate rolling beta:

$$
\beta = Corr(r_{chart},r_{anchor})\times\frac{\sigma_{chart}}{\sigma_{anchor}}
$$

Over the configured horizon, the residual is:

$$
Residual = Return_{chart} - \beta Return_{anchor}
$$

The residual is converted to a rolling z-score. Values above the positive threshold are `Leading`, values below the negative threshold are `Lagging`, and values between are `In Line`.

## Regime Engine

The engine is deterministic and consists of five major scores.

### Direction score

Direction combines:

- EMA ordering
- price and slope relative to RTH VWAP
- +DI versus −DI
- efficiency direction
- optional relative-strength contribution
- price relative to RTH open

The raw sum is normalized to a range from −1 to +1.

### Expansion score

Expansion uses available features with these target weights:

- 35% realized-volatility expansion
- 30% developing-range expansion
- 20% cumulative RVOL
- 15% bar RVOL

Missing same-time metrics are removed from the denominator rather than forced to zero.

### Compression score

Compression uses:

- 30% EMA compression
- 20% weak ADX
- 20% volatility contraction
- 15% developing-range compression
- 15% low efficiency

### Balance score

Balance uses:

- 30% recent VWAP crossings
- 25% proximity to VWAP
- 25% low directional efficiency
- 20% low absolute direction score

### Resulting regimes

- Bull Expansion
- Bear Expansion
- Bull Trend
- Bear Trend
- Balanced Rotation
- Compression
- Volatility Expansion
- Transition
- Outside RTH

The displayed confidence is a feature-agreement score derived from the winning regime's component scores. It is not a forecast probability.

## Reading the Pane

A useful interpretation sequence is:

1. Read the Regime card.
2. Confirm whether Participation and Volatility agree.
3. Check Trend Structure for expansion, pullback or compression.
4. Check Relative Strength for leadership or lag.
5. Use Location / Range to determine whether price is accepted away from VWAP or rotating near it.
6. Return to Futures Levels and Profile to identify the nearest structural reference.

## Important Settings

| Group | Setting | Effect |
|---|---|---|
| Session + Baselines | Historical sessions | Number of samples retained per time slot |
| Participation | RVOL thresholds | Defines quiet, elevated and extreme states |
| Realized Volatility | Windows and ratios | Controls expansion/contraction sensitivity |
| VWAP Context | Slope and crossing rules | Controls directional versus rotating VWAP states |
| EMA Structure | Lengths and ATR thresholds | Controls stack, expansion and compression states |
| Trend Quality | ADX/efficiency thresholds | Controls trend-strength scoring |
| Relative Strength | Anchor, beta and z-score | Controls cross-futures comparison |
| Regime Engine | Regime thresholds | Controls final classifications |
| Dashboard | Dimensions and position | Controls fixed panel layout |

## Alerts

Close-confirmed alert conditions include:

- regime change
- same-time RVOL spike
- realized-volatility expansion
- relative-strength dislocation

Optional dynamic JSON alerts include the regime, confidence, direction score, RVOL, volatility ratio, relative z-score and timestamp.

## Limitations

- Same-time baselines require historical sessions to warm up.
- The baseline is timeframe-specific; changing timeframe creates different slots.
- The indicator is intended for minute-based intraday charts, normally 1–15 minutes.
- Relative strength depends on both symbols having aligned data.
- Confidence measures feature agreement, not trade expectancy.
- Continuous futures can distort historical returns around rollover.

## Suggested Companions

- [Meridian — Futures Levels](./meridian-futures-levels.md)
- [Meridian — Futures Profile](./meridian-futures-profile.md)

## License

This source file is covered by the repository's [MPL-2.0 license](../LICENSE).
