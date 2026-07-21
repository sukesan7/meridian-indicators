# Meridian — Futures Setups

> **Version: v0.3.0 Beta**  
> **Status: Beta · Work in progress**

[← Documentation index](./README.md) · [Main repository README](../README.md)

**Source:** [Daily build](../indicators/futures/meridian-futures-setups/meridian-futures-setups-v0.3.0-beta.pine) · [Research build](../indicators/futures/meridian-futures-setups/meridian-futures-setups-research-v0.3.0-beta.pine)

<p align="center">
  <a href="../screenshots/Meridian_Futures_Setups.png">
    <img src="../screenshots/Meridian_Futures_Setups.png" alt="Meridian Futures Setups beta preview" width="100%">
  </a>
</p>

## Purpose

Meridian — Futures Setups is a strategy-neutral, multi-timeframe confluence scanner for NQ, MNQ, ES and MES.

It does not contain Silver Bullet, Unicorn Model or other named strategy playbooks. The indicator uses one focused **Meridian Choice** engine:

1. Detect valid market zones.
2. Measure the authority of each zone.
3. Find overlapping confluence across timeframes.
4. Evaluate execution structure, liquidity and context.
5. Apply mandatory lifecycle and risk gates.
6. Select the strongest qualified opportunity.
7. Produce a BUY or SELL hypothesis only after the full model passes.

The indicator does not place broker orders. A signal is a rule-based analytical hypothesis, not a guarantee.

## Two builds

The project includes two Pine Script indicators with the same live qualification rules.

### Daily build

Use the daily build for normal chart operation.

Default behavior:

- no raw zone drawings;
- no rejected-candidate labels;
- no dashboard;
- one active trade;
- live threshold of 80;
- at least four independent categories;
- one trade per structural leg;
- only live-qualified signals receive full trade geometry.

### Research build

Use the research build to inspect how the engine behaves.

It adds:

- active multi-timeframe zone drawings;
- timeframe, zone type and score labels;
- rejected touched candidates;
- rejection reasons;
- score-component breakdowns;
- candidate, signal, winner and stopped totals;
- outcome counts by score bucket.

The research build does **not** lower the live signal threshold. It does not convert a rejected or low-score candidate into a BUY or SELL trade.

## Recommended chart configuration

```text
Market: NQ or ES
Primary timeframe: 1 minute
Accepted working timeframes: 2–5 minutes
Chart type: standard candles
Extended hours: enabled
Session timezone: America/New_York
Futures session: 18:00–17:00 ET
Default signal window: 08:00–16:00 ET
Minimum score: 80
Minimum independent categories: 4
Entry mode: Rejection close
Require first qualified touch: enabled
Maximum active trades: 1
```

The indicator reads the configured full futures session, including overnight and premarket bars. The signal window controls when new trades can qualify. Zone detection and context calculations can continue outside that signal window.

Synthetic candles are not recommended as an execution reference.

## Core architecture

The engine has four main layers:

1. **Zone detection** registers FVG, IFVG, OB and BB structures.
2. **Confluence analysis** measures timeframe authority, nesting and surrounding evidence.
3. **Qualification** applies score, category, structure, displacement, stop and objective gates.
4. **Trade lifecycle** manages entry, risk/reward drawings, terminal outcomes and cleanup.

No single indicator concept can create a trade by itself.

# Zone engine

## Timeframes

The engine can detect zones from:

- chart timeframe;
- 5 minutes;
- 15 minutes;
- 30 minutes;
- 1 hour;
- 4 hours.

Each timeframe can be enabled or disabled independently. Zone lifetime is also configurable by timeframe.

Higher-timeframe zones use completed source candles. The zone is registered when that completed information first becomes available to the chart. The drawing is not moved backward to the original higher-timeframe candle.

## Fair Value Gap

A bullish Fair Value Gap is a three-candle imbalance where the newer candle's low is above the older candle's high.

A bearish Fair Value Gap is the opposite condition.

The engine stores:

- direction;
- top and bottom boundaries;
- midpoint;
- source timeframe;
- source ATR;
- detection time;
- expiry time;
- touch count;
- fill percentage;
- state.

## Inversion FVG

An active FVG can become an IFVG after price closes through its invalidating boundary. The transformed zone is tracked in the opposite direction.

An IFVG is not detected as an unrelated new shape. It is a lifecycle transformation of a previously registered FVG.

## Order Block

The current OB model uses the immediate opposing candle before confirmed displacement and a source-timeframe structure break.

The script does not classify every opposite-colored candle as an Order Block.

## Breaker Block

A BB is created after a registered Order Block fails through its invalidating boundary. The BB is therefore a transformed OB, not an independently selected candle sequence.

## Zone-size limits

The script normalizes zone width by the source-timeframe ATR:

```text
normalized zone width = zone height / source ATR
```

Zones below the minimum size or above the maximum size are rejected. This prevents negligible gaps and unusually large zones from receiving misleading authority.

# Meridian Choice scoring

The score contains six capped categories.

| Category | Maximum | Main evidence |
|---|---:|---|
| Zone authority | 30 | Source timeframe, zone type and ATR-normalized width |
| Multi-timeframe overlap | 25 | Same-direction overlap and full nesting |
| Execution structure | 20 | BOS/MSS and displacement |
| Liquidity and structure | 15 | Sweeps, repeated-wick pools, major references and freshness |
| Context | 10 | VWAP, HTF alignment, z-score, RSI and RVOL |
| Intermarket and session | 5 | NQ/ES SMT, PO3 proxy and Opening Range retest |

The total is capped at 100.

The score is not a probability, win rate or forecast confidence percentage.

## Zone authority

Base authority increases with timeframe:

| Source | Base points |
|---|---:|
| Chart timeframe | 5 |
| 5-minute | 8 |
| 15-minute | 12 |
| 30-minute | 15 |
| 1-hour | 18 |
| 4-hour | 22 |

Type adjustments:

- OB: additional authority;
- IFVG: additional authority;
- BB: highest type adjustment.

ATR-normalized width can add up to four points. The complete category is capped at 30.

## Multi-timeframe overlap

Same-direction zones receive additional points when their price ranges overlap.

Examples:

- chart-timeframe IFVG inside a 30-minute BB;
- 5-minute OB overlapping a 1-hour FVG;
- 15-minute FVG inside a 4-hour FVG.

A fully nested zone receives an additional adjustment. The category is capped at 25 so that many correlated zones cannot inflate the score without limit.

## Execution structure

The chart execution layer evaluates:

- confirmed Break of Structure;
- confirmed Market Structure Shift;
- recent directional displacement;
- displacement body divided by ATR;
- body as a fraction of candle range.

MSS contributes more than a normal BOS. Structure and displacement remain separate mandatory gates when their settings are enabled.

## Liquidity and structural references

The engine can use:

- previous-day high and low;
- previous-week high and low;
- overnight high and low;
- Opening Range high and low;
- confirmed chart pivots;
- recent liquidity events;
- repeated-wick liquidity pools.

### Repeated-wick pools

The script clusters confirmed pivot highs or lows inside a configurable tick tolerance. A cluster must contain the required number of touches before it contributes to a score.

This is an OHLC-derived liquidity proxy. It does not show resting limit orders, queue data or Depth of Market liquidity.

## Context

### VWAP

The indicator calculates:

- full futures-session VWAP;
- RTH VWAP after 09:30 ET;
- rejection, reclaim and proximity behavior near the active VWAP.

### Higher-timeframe alignment

Confirmed 1-hour and 4-hour price/EMA relationships provide a small directional context contribution.

### Rolling z-score

The z-score measures price relative to its rolling mean and standard deviation. An extreme reading contributes only when price starts to move back in the setup direction.

### RSI

RSI is a minor supporting input. RSI cannot qualify a trade independently.

### Same-time RVOL

The engine compares current volume with historical volume from the same futures-session time slot. The feature requires enough prior sessions before it becomes available.

## Intermarket and session context

### NQ/ES SMT

The script compares confirmed NQ and ES pivots. Divergence is valid only when the two pivot confirmations occur within the configured separation window.

SMT is supporting evidence. It cannot create a signal independently.

### Power of Three proxy

The current PO3 component uses a documented session proxy:

- overnight range as accumulation;
- a sweep/reclaim of overnight or major liquidity as manipulation;
- movement away through session VWAP as distribution.

It does not claim to reproduce every discretionary interpretation of Power of Three.

### Opening Range

The Opening Range module detects a confirmed breakout and retest of the configured 09:30 range.

# Independent-category requirement

A score must include evidence from enough independent categories.

The default requirement is four categories. The category count prevents one cluster of correlated observations from creating a trade only because several related points were added together.

# Mandatory live gates

A BUY or SELL signal requires all enabled gates to pass:

1. Supported symbol and timeframe.
2. Active signal window.
3. Valid FVG, IFVG, OB or BB.
4. Confirmed interaction with the zone.
5. Minimum total score.
6. Minimum independent-category count.
7. Recent BOS or MSS, when required.
8. Recent displacement, when required.
9. First qualified touch, when required.
10. Valid stop distance.
11. Sufficient room to the nearest objective.
12. Same-direction cooldown permission.
13. One-trade-per-structural-leg permission.
14. Available active-trade capacity.

A high score cannot bypass these gates.

## Strongest-zone selection

Several zones can qualify on the same confirmed bar. The engine selects only the strongest qualified zone rather than opening a trade for every visible concept.

# Entry and risk

## Entry modes

### First touch

The setup triggers when price first intersects the qualified zone.

### Midpoint reclaim

Price must trade through the zone midpoint and close back on the setup side of that midpoint.

### Rejection close

This is the default. Price must intersect the zone and close with a directional candle back through the zone midpoint.

## Stop placement

The default stop is placed beyond the setup-zone invalidation boundary plus a configurable tick buffer:

- bullish setup: below the zone;
- bearish setup: above the zone.

## Stop-size filters

The stop must be on the correct side of entry and inside both tick and ATR limits.

Automatic maximum tick defaults:

- NQ/MNQ: 32 ticks;
- ES/MES: 12 ticks.

A second ATR-based maximum remains active unless stop-size filtering is disabled.

## Objective-space gate

The engine searches for the nearest valid objective in the trade direction from:

- PDH/PDL;
- PWH/PWL;
- overnight high/low;
- Opening Range high/low.

The setup can be rejected when there is not enough room between entry and that objective relative to the proposed risk.

# Trade visualization

A qualified trade shows:

- compact `BUY • score` or `SELL • score` label;
- setup-zone shading;
- transparent red risk region;
- strongest green tint from entry to 1R;
- lighter green tint from 1R to 1.5R;
- lightest green tint from 1.5R to 2R;
- bright STOP line;
- bright 1R, 1.5R and 2R lines.

There is no separate entry line.

# Trade lifecycle

A trade progresses through:

```text
Triggered
→ Active
→ Partial target
→ Completed, stopped or time expired
→ Retained or removed
```

The default maximum drawing duration is 30 minutes. The trade ends earlier when the stop or 2R target is reached.

Outcome processing begins after the entry candle. If a later historical OHLC candle contains both the stop and a target, the script uses a conservative stop-first assumption.

## Retention

Default behavior:

- terminal drawings fade;
- drawings remain for five minutes;
- the trade is removed.

When **Show past trades** is enabled:

- terminal trades remain in a faded historical state;
- default retention is 22 hours;
- retention is configurable;
- the retained-trade count is bounded.

# Research output

The research build can show an active zone when its score is above the separate research-candidate threshold.

Rejected candidates can include reasons such as:

- score/categories;
- no structure;
- no displacement;
- not first touch;
- invalid stop;
- objective too close;
- outside signal window;
- lifecycle gate.

Research score buckets:

- below 60;
- 60–69;
- 70–79;
- 80–89;
- 90 and above.

These statistics are diagnostic counts, not a complete strategy backtest.

# Confirmed-data and repainting model

The critical path uses confirmed information:

- higher-timeframe zones use completed source candles;
- confirmed HTF values are requested with completed expressions;
- chart pivots are used only after confirmation;
- BOS, MSS, qualification and entries run on confirmed chart bars;
- a pivot-dependent event appears when it becomes knowable, not at the historical pivot origin;
- HTF zone drawings begin when the chart receives the completed zone;
- signals are not moved backward after later bars form;
- stop and target checks begin after the entry bar.

Confirmed pivots have unavoidable delay. This delay is preferable to drawing a historical signal before it could have been known.

# Alerts

Available static alerts:

- Meridian BUY;
- Meridian SELL;
- 2R target reached;
- stop reached.

Optional dynamic JSON alerts use:

```text
meridian.futures_setups.event.v3
```

# Important limitations

- The indicator does not place orders.
- It does not use footprint, DOM or resting-order-book data.
- Repeated-wick pools are OHLC proxies, not measured order-book liquidity.
- Historical OHLC candles do not reveal the exact intrabar sequence of stop and target events.
- Continuous futures symbols can contain rollover and back-adjustment effects.
- Confirmed pivots create unavoidable signal delay.
- OB and BB definitions are systematic Meridian implementations, not universal discretionary definitions.
- Score weights and thresholds are initial research values.
- Research counts are not a substitute for a full strategy backtest.

# Beta validation checklist

Before relying on a new release:

1. Compile both source files in TradingView Pine Editor.
2. Test NQ and ES separately.
3. Use a one-minute chart with extended hours enabled.
4. Confirm that overnight and premarket bars contribute to zone state.
5. Verify one bullish and one bearish signal in Bar Replay.
6. Confirm that an HTF zone first appears only after its source candle completes.
7. Confirm that no pivot-dependent signal is moved to an earlier candle.
8. Confirm that only the strongest qualified zone triggers on one bar.
9. Confirm that rejected research candidates do not receive BUY/SELL trade geometry.
10. Confirm stop, 2R and 30-minute expiry behavior.
11. Confirm five-minute cleanup with past trades disabled.
12. Confirm faded 22-hour retention with past trades enabled.
13. Compare score buckets over multiple sessions before changing weights.

# Development status

Meridian — Futures Setups v0.3 is a **beta and work in progress**.

The former multi-strategy design was archived. The public indicator now focuses only on the strategy-neutral Meridian Choice confluence model. Hypothesis-specific methods will be developed as separate indicators rather than added as playbook modes inside this script.

Planned work includes:

- score and category validation;
- replay and live-session integrity testing;
- a dedicated strategy/research companion;
- improved objective and zone-quality modeling;
- separate mean-reversion and session-specific setup indicators;
- integration with future Meridian Backtester research.

# License

This source is covered by the repository's [Mozilla Public License 2.0](../LICENSE). The license does not grant rights to the Meridian Trading name, logos, branding, premium products or private infrastructure.
