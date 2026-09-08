# Meridian — Futures Context

[← Indicator documentation](../README.md) · [View source](../../src/futures/meridian-futures-context.pine)

**Version:** 0.2.0<br>
**Status:** Stable<br>
**Primary markets:** NQ, MNQ, ES and MES

<p align="center"><img src="../../assets/screenshots/futures-context.png" alt="Meridian Futures Context" width="100%"></p>

## Purpose

Futures Context classifies the current futures environment from same-time participation, realized volatility, range development, RTH VWAP location, trend quality and intermarket behavior.

The regime confidence value measures agreement within the model. It is not a win probability.

## v0.2 revamp

- standardized lower-pane colors and the compact `Meridian -- Futures Context` HUD;
- corrected EMA and VWAP slope normalization to measure slope per lookback bar before ATR normalization;
- expanded the former single NQ/ES relative-strength anchor into a multi-peer intermarket engine;
- added beta-adjusted residual z-scores, rolling correlation quality, market breadth and explicit divergence/decoupling states;
- kept the same-time baseline engine isolated from the current session until bars confirm;
- reduced optional plot clutter in the default view.

## Same-time baselines

For each RTH chart-time slot the script stores bounded historical samples. Current bar volume, cumulative volume and developing range are compared with prior sessions at the equivalent stage of the day. The active observation is read against the prior baseline before it is committed after confirmation.

## Trend and volatility

Trend quality combines EMA structure/separation, ADX/DI, directional efficiency and VWAP slope. Realized volatility is compared with its own history and developing range is compared with same-time session history.

## Intermarket engine

Automatic peers are selected from NQ, ES, YM and RTY according to the chart market. For each available peer the engine calculates:

- one-bar return;
- rolling beta and correlation;
- horizon return;
- beta-adjusted residual;
- residual z-score.

Peer residuals are combined with correlation-quality weighting. The model also measures the sign breadth of the chart and available peers.

Possible states include:

- `Broad Risk-On` / `Broad Risk-Off`;
- `Leading` / `Lagging`;
- `Leading / Diverging` / `Lagging / Diverging`;
- `In Line`;
- `Warming Up`.

A large residual is treated as more meaningful when peer correlation remains sufficiently high. This is statistical context, not a guaranteed lead/lag relationship.

## Regime model

The deterministic engine separates direction, trend quality, expansion, compression and balance. Outputs include bullish/bearish trend, directional expansion, balanced rotation, compression, volatility expansion, transition and optional outside-RTH state.

## Recommended setup

```text
Market: NQ/MNQ, ES/MES, YM/MYM or RTY/M2K
Chart: 1–15 minutes
RTH: 09:30–16:00 ET
Same-time baseline: enough loaded sessions for minimum samples
Intermarket: Automatic
```

## Dashboard and alerts

The top-right HUD summarizes regime, participation, trend, volatility, intermarket state, location and data freshness. Confirmed alerts cover regime changes, RVOL spikes, volatility expansion and intermarket dislocation.

## Limitations

Same-time baselines need comparable history. Early closes and missing bars can reduce sample quality. Continuous futures and peer feeds can differ. Intermarket residuals describe abnormal relative movement; they do not prove causality.
