# Meridian — Futures Context

[← Indicator documentation](../README.md) · [View source](../../src/futures/meridian-futures-context.pine)

**Version:** 0.1.7<br>
**Status:** Stable<br>
**Primary markets:** NQ, MNQ, ES and MES

<p align="center"><img src="../../assets/screenshots/futures-context.png" alt="Meridian Futures Context" width="100%"></p>

## Purpose

Futures Context is a lower-pane market-environment classifier. It combines same-time participation, realized volatility, developing range, RTH VWAP location, EMA structure, ADX, directional efficiency and beta-adjusted relative strength.

The dashboard's confidence value is feature agreement, not empirical win probability.

## Same-time baseline engine

The script stores bounded historical samples for each RTH chart-time slot. Current bar volume and developing session range are compared with prior sessions at the equivalent time. The active session is not added to its own baseline until bars confirm.

Outputs include:

- bar RVOL;
- cumulative RVOL;
- developing-range ratio;
- warm-up and sample-readiness state.

## Trend and volatility

EMA stacking and separation describe directional structure. ADX and DI measure trend strength and direction. Directional efficiency compares net movement with total path length. Rolling realized volatility is compared with its own baseline and z-score.

## Relative strength

The default anchor automatically pairs Nasdaq futures with S&P futures and vice versa. Rolling beta, return correlation and a relative residual z-score describe dislocation between the chart symbol and the anchor.

This is a statistical comparison, not a guaranteed lead-lag signal.

## Regime engine

The deterministic engine scores direction, expansion, compression and balance. The resulting labels include bullish or bearish trend/expansion, balanced rotation, compression, volatility expansion, transition and outside-RTH states.

## Recommended setup

```text
Market: NQ/ES or micro equivalent
Chart: 1–15 minutes
RTH: 09:30–16:00 ET
Baseline history: enough loaded sessions for same-time samples
Relative anchor: automatic NQ/ES pairing
Alerts: once per bar close
```

## Important settings

| Group | Use |
|---|---|
| General | Enable state and outside-RTH classification |
| Session + Baselines | RTH definition, history and minimum samples |
| Participation / RVOL | Participation thresholds and display |
| Realized Volatility | Windows, expansion and contraction thresholds |
| VWAP Context | Source, slopes and rotation behavior |
| EMA Structure | Lengths, compression and expansion thresholds |
| Trend Quality | ADX, DI and efficiency |
| Relative Strength | Anchor, beta window and residual thresholds |
| Regime Engine | Direction and state thresholds |
| Supporting Plots | Pane visibility and caps |
| Dashboard + Alerts | Layout and static/dynamic alerts |

## Alerts

Conditions cover regime changes, same-time RVOL spikes, realized-volatility expansion and relative-strength dislocation. Optional dynamic JSON includes regime and component values.

## Limitations

- Baselines need sufficient loaded history and comparable sessions.
- Early closes, holidays and missing bars can reduce same-time sample quality.
- Relative strength depends on the comparison symbol and data feed.
- Regime labels describe current evidence; they are not forecasts.

## Suggested companions

Use [Futures Levels](./futures-levels.md) for location and [Futures Profile](./futures-profile.md) for auction context.
