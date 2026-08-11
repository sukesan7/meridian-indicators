# Meridian — Options Context

[← Indicator documentation](../README.md) · [View source](../../src/options/meridian-options-context.pine)

**Version:** 0.2.1<br>
**Status:** Stable<br>
**Dependency:** `TradingView/ta/12`<br>
**Use on:** liquid US-listed options underlyings such as SPY and QQQ

<p align="center"><img src="../../assets/screenshots/options-context.png" alt="Meridian Options Context" width="100%"></p>

## Purpose

Options Context is a lower-pane market-environment model designed to be used beside [Options Levels](./options-levels.md).

The two indicators intentionally have different responsibilities:

- **Options Levels** answers **where price matters** by selecting active support and resistance reaction zones.
- **Options Context** answers **what directional environment exists when price reaches those areas**.

Options Context does not attempt to recreate the support/resistance engine from Options Levels. Instead, it converts intraday trend, structure, momentum, participation, persistence, volatility and confirmed higher-timeframe behavior into an explainable directional score, a separate confidence score and a `Levels Bias`.

The indicator analyzes the underlying security. It does not read option-chain Greeks, implied volatility, dealer positioning, individual option liquidity or exchange order-book data.

## Primary outputs

The v0.2.1 engine separates direction from confidence:

```text
Context Direction     -100 ... +100
Context Confidence       0 ... 100
```

A positive Context Direction favors bullish interpretation, a negative value favors bearish interpretation, and values near zero indicate balanced or conflicting evidence.

Context Confidence is not the absolute value of Context Direction. Two bars can have the same directional score while carrying very different confidence because participation, factor agreement, persistence and volatility conditions differ.

Neither output is a probability, expected return or win rate.

## Context model

When higher-timeframe context is enabled, the intraday model contributes 85% of the available directional weight and the HTF composite contributes 15%.

Within the intraday model, the relative component weights are:

| Component | Intraday weight | Purpose |
|---|---:|---|
| Trend | 26% | EMA structure and slope |
| Structure | 24% | RTH VWAP, Opening Range and RTH-open location |
| Momentum | 21% | Normalized return, RSI and momentum change |
| Participation | 16% | Same-time RVOL with directional bar behavior |
| Persistence | 13% | Consistency of intraday directional evidence |

If HTF context is disabled, the available intraday components are renormalized.

### Trend

Trend is a continuous `-100…+100` score built from:

- ATR-normalized fast/slow EMA spread;
- slow-EMA slope;
- fast-EMA slope.

The default local EMA lengths are 9 and 21. Slope and spread are normalized so the same raw price distance does not mean the same thing in every volatility regime.

### Structure

Structure measures price location relative to three session references:

- regular-session VWAP — 60%;
- finalized Opening Range — 30%;
- regular-session open — 10%.

Price above or below VWAP contributes continuously according to ATR-normalized displacement.

The Opening Range contributes only after its configured collection window is finalized. While price remains inside the range, the score reflects location within the range; confirmed movement beyond the range increases directional magnitude.

Options Context intentionally does not import PDH, PDL, PWH, pivots or the reaction-zone registry from Options Levels. Those belong to the location layer.

### Momentum

Momentum combines:

- ATR-normalized multi-bar log return — 55%;
- centered RSI — 35%;
- change in normalized momentum — 10%.

RSI is therefore a supporting input rather than a fixed bullish/bearish threshold vote.

### Participation

Participation retains TradingView's same-time relative-volume model through `TradingView/ta/12`.

The script calculates both:

- same-time **bar RVOL**;
- same-time **cumulative RVOL**.

Participation intensity combines the two, then applies directional information from:

- the bar's close location inside its high/low range;
- the normalized one-bar return.

High volume without directional displacement therefore does not receive the same directional score as high-volume expansion with a strong close.

The pane can display normalized RVOL columns while the dashboard and research outputs preserve the uncapped RVOL ratios.

### Persistence

Persistence measures whether recent regular-session bars have consistently supported the same side through:

- price versus RTH VWAP;
- fast EMA versus slow EMA;
- bar-to-bar return direction.

The default lookback is 12 RTH bars. Early in the session, the calculation adjusts to the number of available RTH bars rather than treating unavailable history as negative evidence.

### Volatility

Volatility is intentionally non-directional.

The model compares a short ATR with a longer ATR, standardizes that ratio against its rolling history and maps the result to a `0…100` volatility score.

Volatility affects **Context Confidence**, not Context Direction. This prevents an expanding-volatility condition from being interpreted as bullish or bearish by itself.

## Higher-timeframe model

v0.2.1 tracks confirmed regular-session trend state on:

- 1 hour;
- 4 hours;
- 1 day;
- 1 week.

Each timeframe produces two separate values:

```text
HTF Direction     -100 ... +100
HTF Quality           0 ... 100
```

### Per-timeframe direction

Each HTF direction score uses six dimensions:

| HTF component | Weight |
|---|---:|
| EMA20 / EMA50 structure | 28% |
| Fast/slow EMA slope | 22% |
| Recent ATR-normalized path return | 22% |
| Path efficiency | 13% |
| Persistence versus the fast EMA | 10% |
| RSI | 5% |

#### EMA structure

The distance between the HTF fast and slow EMA is normalized by HTF ATR.

#### EMA slope

Both fast and slow EMA slopes are evaluated. The slope is calculated **per bar** before ATR normalization so increasing the slope lookback does not mechanically inflate the score.

The slow EMA contributes 65% of the slope component and the fast EMA contributes 35%.

#### Recent path return

The default HTF path lookback is five completed bars.

The net move over those bars is normalized by ATR and by the square root of the lookback length. This makes the HTF score responsive to recent directional deterioration even when longer moving-average structure remains intact.

#### Path efficiency

Path efficiency compares net movement with the total absolute path traveled over the lookback.

A persistent directional move receives a larger signed value than a volatile sequence that travels widely but finishes near its starting point.

#### Persistence

The HTF persistence component measures how consistently closes remain above or below the HTF fast EMA over the configured persistence window.

#### RSI

RSI remains a minor confirmation input. It is centered around 50 and contributes only 5% of the HTF direction score.

### HTF quality

HTF Quality evaluates how strong and internally coherent the six per-timeframe components are.

A timeframe can therefore display a meaningful directional score without automatically being treated as high quality if its underlying components disagree.

### HTF Composite

The four confirmed timeframe scores are combined as:

| Timeframe | Composite weight |
|---|---:|
| 1H | 35% |
| 4H | 30% |
| 1D | 22% |
| 1W | 13% |

The weighting intentionally favors the horizons most relevant to intraday options trading while preserving daily and weekly macro context.

### HTF Conviction

`HTF Conviction` is a `0…100` quality measure derived from:

- average HTF directional magnitude;
- average per-timeframe HTF Quality;
- cross-timeframe directional coherence.

This replaces the earlier pure alignment percentage. Four weak same-sign timeframes no longer produce an automatic `100%` reading.

### HTF breadth

The dashboard expresses cross-timeframe participation directly:

```text
4/4 BULL
3/4 BULL
3/4 BEAR
MIXED
```

A timeframe counts as directional only after exceeding the configurable HTF directional threshold.

### Tactical and macro HTF views

Research outputs also separate:

```text
HTF Tactical = 55% 1H + 45% 4H
HTF Macro    = 65% 1D + 35% 1W
```

This makes disagreements such as bearish 1H/4H behavior inside a still-bullish daily/weekly trend visible instead of hiding them inside one composite number.

## Confirmed HTF behavior

Higher-timeframe calculations use a regular-session ticker and the previous completed bar from each requested timeframe.

That means:

- the 1H score changes after an hourly bar confirms;
- the 4H score changes after its requested four-hour bar confirms;
- the 1D score changes after the daily regular session completes;
- the 1W score changes after the weekly bar completes.

The HTF matrix therefore favors stable, non-repainting context over immediate developing-candle responsiveness.

Outside regular trading hours, the most recently confirmed regular-session HTF state remains visible.

## Context Confidence

Context Confidence combines:

| Confidence input | Weight |
|---|---:|
| Magnitude-adjusted directional agreement | 45% |
| Participation quality | 30% |
| Volatility relevance | 15% |
| Absolute persistence | 10% |

Directional agreement is magnitude-aware. Weak same-sign inputs do not receive a perfect agreement score simply because their signs match.

Missing evidence is omitted from weighted calculations rather than silently converted into bearish, bullish or zero evidence where the model supports renormalization.

## Regime states

Context Direction is converted into a confirmed regime state with hysteresis.

The directional regions are approximately:

| Context Direction | Regime |
|---:|---|
| `>= +75` | Strong Bull |
| `+45 to +75` | Bull |
| `+20 to +45` | Bull Lean |
| `-20 to +20` | Balanced |
| `-45 to -20` | Bear Lean |
| `-75 to -45` | Bear |
| `<= -75` | Strong Bear |

The state machine uses separate entry and exit behavior so small movements around a threshold do not continuously flip the displayed regime.

## Levels Bias

`Levels Bias` is the companion output for Options Levels.

It does not create a new support or resistance zone. It tells the trader which side of the existing Levels map deserves more attention given current context.

| Condition | Levels Bias |
|---|---|
| Confidence below 35 | `LOW CONVICTION` |
| Direction `>= +45` | `PREFER SUPPORT` |
| Direction `+20…+45` | `SUPPORT LEAN` |
| Direction between `-20…+20` | `TWO-SIDED` |
| Direction `-45…-20` | `RESISTANCE LEAN` |
| Direction `<= -45` | `PREFER RESISTANCE` |

The hidden `Zone Preference` research output uses:

```text
+1 = favor support
 0 = neutral / insufficient confidence
-1 = favor resistance
```

This creates a simple data contract for future optional integration without making Options Context dependent on Options Levels.

## Default display

The pane can show:

- Context Direction;
- Context Confidence;
- normalized RVOL columns;
- subtle regime background;
- optional RSI-momentum score;
- optional HTF Composite;
- optional legacy v0.1 comparison.

The detailed dashboard can show:

- current direction and regime;
- confidence and confidence state;
- Levels Bias;
- Trend;
- Structure;
- Momentum;
- Participation;
- Persistence;
- HTF Composite;
- HTF Conviction and breadth;
- 1H / 4H state;
- 1D / 1W state;
- bar and cumulative RVOL;
- volatility;
- RTH / Opening Range state.

A compact dashboard mode keeps only the primary context, HTF, RVOL and volatility information.

## Recommended setup

```text
Chart: SPY, QQQ or another liquid US-listed underlying
Timeframe: 1–15 minutes
Candles: standard
Regular session: 09:30–16:00 ET
Timezone: America/New_York
Opening Range: 15 minutes
RVOL history: 20 sessions
Local EMA: 9 / 21
RSI: 14
HTF EMA: 20 / 50
HTF path lookback: 5 bars
HTF persistence: 6 bars
Higher-timeframe context: enabled
Dashboard: Detailed
```

The indicator is designed for intraday charts **below 60 minutes**. It raises a runtime error on non-intraday charts or chart timeframes of one hour and above.

## Important settings

| Group | Use |
|---|---|
| Session | Timezone, regular session, weekday filter and Opening Range duration |
| Normalization | Local ATR normalization length |
| Trend | Fast/slow EMA lengths plus spread and slope sensitivity |
| Structure | VWAP source and displacement scales for VWAP, Opening Range and RTH open |
| Momentum | RSI, normalized-return lookback and momentum-change sensitivity |
| Participation | Same-time RVOL history, real-time estimation, thresholds and display cap |
| Persistence | Number of RTH bars used to measure directional consistency |
| Volatility | Short/long ATR regime lengths and volatility z-score calibration |
| Higher Timeframes | HTF EMA/ATR settings, path and persistence lookbacks, score scales and directional threshold |
| Visuals | Context, confidence, RVOL, HTF, RSI and regime-background visibility |
| Dashboard | Detailed/compact mode, position and text size |
| Alerts | Direction/confidence thresholds and strong-regime failure window |
| Colors | Context, regime and dashboard palette |
| Research / Debug | Data Window research series and optional v0.1 comparison |

## Alerts

All alert conditions are evaluated on confirmed chart bars.

Available alerts are:

- `Strong Bull Context`
- `Strong Bear Context`
- `Bullish Context Transition`
- `Bearish Context Transition`
- `High-Confidence Directional Context`
- `Aligned RVOL Surge`
- `Bull Context Failure`
- `Bear Context Failure`

The alert design intentionally focuses on regime and participation transitions. Price-level entry, rejection, acceptance and flip alerts remain the responsibility of Options Levels.

## Research outputs

When `Show research values in Data Window` is enabled, the script exposes:

- Context Score;
- Context Confidence;
- Agreement Score;
- Directional Coherence;
- Trend Score;
- Structure Score;
- Momentum Score;
- Participation Score;
- Persistence Score;
- Volatility Score;
- Bar RVOL;
- Cumulative RVOL;
- HTF Score;
- HTF Conviction;
- HTF Directional Coherence;
- HTF Tactical Score;
- HTF Macro Score;
- 1H / 4H / 1D / 1W Trend Score;
- 1H / 4H / 1D / 1W Trend Quality;
- Zone Preference;
- Legacy Context Score.

The optional legacy comparison plot scales the old v0.1 `-5…+5` binary score by 20 so its behavior can be visually compared with the continuous v0.2 engine during Bar Replay.

## Data behavior

Same-time RVOL uses the TradingView technical-analysis library and requires enough historical regular-session observations to build its baseline.

The current real-time RVOL bar can be estimated before close when `Estimate unclosed real-time bar` is enabled. Context alerts themselves still require confirmed chart bars.

Opening Range precision depends on chart timeframe. If the chart timeframe is coarser than the configured Opening Range duration, the dashboard reports `OR: LOWER TF` rather than implying false boundary precision.

Higher-timeframe context is requested from regular-session data and uses completed HTF bars by design.

## Limitations

- Context Direction, Context Confidence and HTF Conviction are model scores, not probabilities or expected returns.
- `PREFER SUPPORT` and `PREFER RESISTANCE` describe contextual preference; they are not entry instructions.
- The indicator does not read options-chain data, Greeks, implied volatility, dealer positioning or contract-specific liquidity.
- Same-time RVOL quality depends on the underlying's data quality and sufficient historical observations.
- Strong higher-timeframe structure can remain bullish during an intraday selloff, or bearish during an intraday rally. This is intentional; HTF context informs the local model but does not dictate it.
- Confirmed HTF values introduce deliberate latency because developing 1H, 4H, daily and weekly bars are not used as finalized evidence.
- Opening Range precision decreases when chart bars are too coarse for the configured collection window.
- Volatility regimes and component relationships can change across symbols and market environments; default parameters are starting points rather than universal optimization.
- A high-confidence directional reading can still occur after price has become extended. Location, execution and risk remain separate decisions.

## Companion workflow

A practical interpretation sequence is:

1. Use **Options Levels** to identify the active support and resistance reaction zones.
2. Use **Options Context** to determine whether the environment favors support reactions, resistance reactions, both sides or neither side with sufficient conviction.
3. Use the HTF matrix to distinguish tactical 1H/4H behavior from daily/weekly macro structure.
4. Use Context Confidence, participation and persistence to decide how much weight to place on the directional reading.
5. Treat execution, option selection, stop placement and position sizing as separate decisions.

Options Levels answers **where price matters**. Options Context answers **how the surrounding market environment should affect interpretation of those locations**.
