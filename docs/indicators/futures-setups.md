# Meridian — Futures Setups

[← Indicator documentation](../README.md) · [Daily source](../../src/futures/meridian-futures-setups.pine) · [Research source](../../src/futures/meridian-futures-setups-research.pine)

**Version:** 0.3.6-beta<br>
**Status:** Beta<br>
**Primary markets:** NQ, MNQ, ES and MES

<p align="center"><img src="../../assets/screenshots/futures-setups.png" alt="Meridian Futures Setups" width="100%"></p>

## Purpose

Futures Setups is a strategy-neutral, multi-timeframe confluence scanner. One **Meridian Choice** engine detects zones, measures independent evidence, applies lifecycle and risk gates, selects the strongest qualified candidate and creates a temporary BUY or SELL trade hypothesis.

It does not contain named playbooks, place broker orders or guarantee an outcome.

## Choose a build

| Build | Use |
|---|---|
| Daily | Normal chart operation with restrained visuals |
| Research | Zone drawings, candidate labels, rejection reasons, score detail and outcome counters |

The two builds share the same live qualification logic. Research visibility does not lower the score threshold or convert rejected candidates into live signals.

## Recommended configuration

```text
Market: NQ or ES
Primary chart: 1 minute, standard candles
Accepted working charts: 2–5 minutes when explicitly allowed
Extended hours: enabled
Timezone: America/New_York
Futures session: 18:00–17:00 ET
Signal window: 08:00–16:00 ET
Minimum score: 80
Minimum independent categories: 4
Entry mode: Rejection close
Require first qualified touch: enabled
Maximum active trades: 1
```

Zone detection can continue across the configured full futures session. The signal window only controls when a new trade hypothesis can qualify.

## Engine layers

1. **Zone detection:** FVG, IFVG, OB and BB registration.
2. **Confluence analysis:** authority, overlap, structure, liquidity and context.
3. **Qualification:** score, category, timing, stop and objective gates.
4. **Lifecycle:** entry geometry, target/stop state, expiry and cleanup.

No single concept can create a trade by itself.

## Zone engine

### Timeframes

The engine can register chart, 5-minute, 15-minute, 30-minute, 1-hour and 4-hour zones. Higher-timeframe payloads use completed source bars. The zone becomes actionable when the completed information first reaches the chart.

### Fair Value Gap

A bullish FVG is a three-candle imbalance where the newer candle's low is above the older candle's high. A bearish FVG is the inverse. The engine records direction, boundaries, midpoint, source timeframe, ATR, detection time, expiry, touches, fill and state.

### Inversion FVG

An FVG can transform into an IFVG after a confirmed close through its invalidating boundary. The transformation reverses direction and resets expiry to a configurable fraction of the transformed zone's normal lifetime.

### Order Block and Breaker Block

The OB model uses the immediate opposing candle before confirmed displacement and a source-timeframe structure break. A BB is created when a registered OB fails through its invalidating boundary. Neither concept is assigned to every opposite-colored candle.

### Size and lifetime

Zone width is normalized by source-timeframe ATR. Zones outside the configured tick or ATR limits are rejected. Lifetime can be fixed by timeframe or scaled by authority. Four-hour zones can optionally persist to the futures-session close.

## Meridian Choice score

The total score is capped at 100 and is not a probability.

| Category | Maximum | Evidence |
|---|---:|---|
| Zone authority | 30 | Source timeframe, type and ATR-normalized width |
| Multi-timeframe overlap | 25 | Same-direction overlap and nesting |
| Execution structure | 20 | BOS/MSS and displacement |
| Liquidity and structure | 15 | Sweeps, repeated-wick pools, major references and freshness |
| Context | 10 | VWAP, higher-timeframe regime, z-score, RSI and RVOL |
| Intermarket and session | 5 | NQ/ES SMT, PO3 proxy and Opening Range behavior |

### Authority

Base authority rises with timeframe: chart 5, 5-minute 8, 15-minute 12, 30-minute 15, 1-hour 18 and 4-hour 22. OB, IFVG and BB types receive additional authority, and normalized width can add a small capped contribution.

### Overlap

Same-direction zones receive points when price ranges overlap. Full nesting can add further weight. The category cap prevents a large collection of correlated zones from overwhelming other evidence.

### Structure and displacement

The chart execution layer evaluates confirmed Break of Structure, Market Structure Shift and recent directional displacement. MSS has greater authority than ordinary BOS. Structure and displacement can remain mandatory gates even when their points are already included in the score.

### Liquidity

Evidence can include previous-day/week levels, overnight structure, Opening Range, confirmed pivots, recent sweeps and repeated-wick pools. Repeated-wick pools are OHLC-derived clustering proxies, not resting-order or Depth of Market data.

### Context

The engine evaluates full-session and RTH VWAP behavior, confirmed multi-timeframe regime values, rolling z-score, RSI and same-time RVOL. Context contributions are intentionally capped so they cannot replace zone and structure quality.

### Intermarket and session

NQ/ES SMT compares confirmed pivot behavior between the chart and paired symbol. The PO3 component is a session-state proxy. Opening Range behavior can add a small contribution. These are supporting inputs, not standalone triggers.

## Independent-category requirement

A candidate must pass both the total score threshold and the minimum number of independent evidence categories. This reduces the chance that many correlated points from one concept qualify a trade.

## Mandatory live gates

Depending on settings, a live candidate can require:

- supported market and chart timeframe;
- confirmed chart bar inside the signal window;
- active, unexpired and correctly directed zone;
- touch-count and first-qualified-touch compliance;
- recent structure and displacement;
- minimum score and category count;
- valid stop distance in ticks and ATR;
- sufficient objective space;
- active-trade and structural-leg availability.

The strongest candidate on the confirmed bar is selected. Lower-ranked candidates do not create simultaneous duplicate hypotheses.

## Entry and risk

Entry modes include first touch, midpoint reclaim and rejection close. Stop placement uses the selected zone and configured buffer rules, then applies minimum/maximum tick and ATR filters. Targets are displayed at 1R, 1.5R and 2R. Objective-space checks can reject a candidate when a major opposing reference leaves insufficient room.

## Trade lifecycle

A created hypothesis stores its source zone, score, category count, entry, stop, targets, start and expiry. The engine updates target and stop state on confirmed bars, retains completed drawings for a bounded period, and deletes old objects when retention caps are reached.

This is chart analytics, not order management. Intrabar path and slippage are not modeled as broker fills.

## Research output

The research build can show:

- active zones and their timeframe/type labels;
- score tooltips and breakdowns;
- relevant liquidity-pool lines;
- rejected touched candidates and reasons;
- candidate, signal, target and stop totals;
- outcome counts by score bucket.

Use it to diagnose one rule at a time. Research counters are descriptive and are not a substitute for a dedicated backtester.

## Alerts

Static conditions cover BUY, SELL, 2R target and stop events. Optional dynamic JSON includes version, build, direction, source zone, score and trade geometry. Data is only delivered after the user creates a TradingView alert.

## Confirmed-data model

Signals occur on confirmed chart bars. Daily, weekly and higher-timeframe zone inputs use completed source data. Confirmed pivots appear after their right-side confirmation window. Developing session values can still change until their source window closes.

## Limitations

- Beta rules, weights and lifecycle behavior can change.
- The script is not a broker strategy and does not model commissions, slippage or fill priority.
- OHLC-derived liquidity is not order-book liquidity.
- Continuous-contract adjustments can alter historical zones.
- Research results require Bar Replay and live observation before any inference about performance.
- A score is structured evidence, not a forecast probability.

## Validation checklist

Before changing status from beta, validate:

1. chart and higher-timeframe zone registration timing;
2. FVG-to-IFVG and OB-to-BB transformation lifetime;
3. first-touch and structural-leg locks;
4. stop/objective gates across NQ, MNQ, ES and MES;
5. daily/research build parity;
6. Bar Replay behavior around session boundaries;
7. live alerts and terminal trade-state cleanup;
8. score-bucket outcomes in a separate research process.
