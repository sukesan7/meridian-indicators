# Meridian — Options Context

[← Indicator documentation](../README.md) · [View source](../../src/options/meridian-options-context.pine)

**Version:** 0.3.0<br>
**Status:** Stable<br>
**Dependency:** `TradingView/ta/12`<br>
**Primary market:** SPY; also usable on other liquid US-listed underlyings

<p align="center"><img src="../../assets/screenshots/options-context.png" alt="Meridian Options Context" width="100%"></p>

## Purpose

Options Context is the environment layer used beside Options Levels. Levels answers **where**; Context answers **what directional environment exists when price gets there**.

Primary outputs are:

```text
Context Direction    -100 ... +100
Context Confidence      0 ... 100
Levels Bias           support / resistance / two-sided / low conviction
```

They are model scores, not probabilities.

## v0.3 revamp

- standardized the Meridian lower-pane palette and compact top-right `Meridian -- Options Context` HUD;
- fixed local EMA slope normalization so changing the slope lookback no longer mechanically changes score scale;
- retained the confirmed 1H / 4H / 1D / 1W quality-aware HTF model;
- retained magnitude-aware agreement and HTF conviction rather than the earlier misleading pure sign-alignment percentage;
- added explicit `LIVE`, `CONFIRMED` and `STALE / CLOSED` data-state presentation;
- removed unnecessary dashboard detail from the normal view while keeping research series available.

## Intraday model

The directional model combines:

| Component | Relative role |
|---|---|
| Trend | EMA spread and per-bar EMA slope |
| Structure | RTH VWAP, finalized Opening Range and RTH open |
| Momentum | ATR-normalized return, RSI and momentum change |
| Participation | Same-time bar/cumulative RVOL plus directional bar behavior |
| Persistence | consistency of VWAP, EMA and return direction |

Volatility is non-directional and contributes to confidence rather than bullish/bearish direction.

Same-time RVOL comes from the TradingView technical-analysis library and compares the current stage of the session with prior sessions at the same relative time.

## Higher-timeframe model

Confirmed regular-session 1H, 4H, 1D and 1W states each combine:

- EMA20/EMA50 structure;
- fast and slow EMA slope **per source bar**;
- recent ATR-normalized path return;
- path efficiency;
- persistence versus the fast EMA;
- RSI as a small confirmation input.

Each timeframe produces direction and quality. The composite weights 1H/4H more heavily for intraday options while preserving daily/weekly macro context.

`HTF Conviction` combines magnitude, per-timeframe quality and cross-timeframe coherence. Breadth is presented directly as values such as `4/4 BULL`, `3/4 BEAR` or `MIXED`.

Higher-timeframe requests use completed regular-session source bars so historical states remain stable after reload.

## Levels Bias

| Context | Output |
|---|---|
| low confidence | `LOW CONVICTION` |
| strong positive direction | `PREFER SUPPORT` |
| moderate positive | `SUPPORT LEAN` |
| balanced | `TWO-SIDED` |
| moderate negative | `RESISTANCE LEAN` |
| strong negative | `PREFER RESISTANCE` |

The hidden `Zone Preference` output uses +1 / 0 / -1 for research integration.

## Recommended SPY setup

```text
Chart: SPY
Timeframe: 1–15 minutes
RTH: 09:30–16:00 ET
Opening Range: 15 minutes
RVOL history: 20 sessions
Local EMA: 9 / 21
HTF EMA: 20 / 50
HTF context: enabled
Dashboard: Detailed or Compact
```

The script intentionally rejects chart timeframes of one hour and above.

## Alerts

Confirmed events cover strong bull/bear transitions, ordinary directional transitions, high-confidence directional context, aligned RVOL surges and recent strong-regime failures.

## Research outputs

The Data Window can expose Context Direction, Confidence, agreement/coherence, component scores, RVOL, volatility, HTF composite/conviction, tactical and macro HTF values, per-timeframe direction/quality and the legacy v0.1 comparison score.

## Limitations

Strong HTF trend can coexist with opposite intraday movement. Confirmed HTF evidence is deliberately slower than a developing HTF candle. Context does not know option-chain conditions and should not replace location, execution or risk management.

## Companion

Use [Options Levels](./options-levels.md) for the reaction zones to which the Context reading is applied.
