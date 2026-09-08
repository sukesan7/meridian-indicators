# Architecture and design boundaries

[← Documentation index](./README.md)

## Suite model

Meridian is organized as a set of independent indicators rather than a single monolith. Each script recalculates the data it needs because Pine scripts cannot directly read another indicator's internal objects or variables.

| Layer | Primary responsibility |
|---|---|
| Levels | Objective price references, reaction zones and session structure |
| Context | Participation, momentum, volatility, trend quality, regime and compact intermarket context |
| Profile | TPO value, distribution shape, Initial Balance quality and auction-state descriptions |
| Setups | Multi-timeframe zone qualification, causal event evidence and trade-hypothesis lifecycle |

This separation keeps chart roles understandable and prevents one experimental engine from destabilizing otherwise mature scripts. The catalog-wide visual contract is documented in [the Meridian design system](./design-system.md).

## Source layout

Public source paths are versionless. Version numbers belong in the source metadata and `manifest.json`, not in filenames. This avoids broken documentation links and makes updating a copied script predictable.

The deprecated multi-strategy Futures Setups v0.2 implementation is intentionally not shipped. Git history, tags or release archives are the correct place for superseded code; the primary source tree contains only supported public builds.

## Session engines

The scripts define explicit sessions and timezones instead of assuming the chart's visual session is sufficient. Session-derived values reset using explicit session or trading-day identities rather than assuming an out-of-session chart bar will always exist between sessions. This is important on RTH-only ETF charts and overnight futures feeds with maintenance gaps.

Session precision depends on chart bars intersecting the configured boundaries. A 1-minute chart provides more precise Opening Range and Initial Balance boundaries than a coarse chart.

## Higher-timeframe data

Critical completed daily, weekly and multi-timeframe values use confirmed source bars. Where `barmerge.lookahead_on` appears, the requested expression is offset by one completed source bar or is produced by a payload that reads completed values. This is a deliberate confirmed-data pattern, not future leakage.

Live values that are intended to develop—such as current-session highs, lows, VWAP, TPO rows or a forming Opening Range—can change until their source window completes.

## Stateful objects

Futures Levels, Profile and Setups retain state across bars. Examples include:

- current session extrema;
- level acceptance and rejection states;
- profile rows and completed-profile references;
- zone state, transformation, expiry and fill percentage;
- linked setup evidence such as liquidity, structure and displacement timing;
- trade-hypothesis targets, stops and terminal outcomes.

Arrays and drawing objects are capped. Cleanup routines delete expired or superseded drawings to prevent uncontrolled object growth.

## Daily and research setup builds

The Futures Setups files intentionally share one engine. The only build-level differences are the indicator identity, the `RESEARCH_BUILD` constant and research-visibility defaults. The repository validator checks that the two files do not silently drift in live qualification logic.

## External dependencies

Only Options Context imports an external Pine library:

```text
TradingView/ta/12
```

It is TradingView's published technical-analysis library and is used for relative-volume calculations. The other scripts are self-contained apart from normal TradingView symbol requests.

## Alerts and data boundaries

The scripts can create alert conditions and, when explicitly enabled, dynamic JSON messages. Pine scripts do not hold API keys, open sockets or directly call Discord, brokers or external servers. Data leaves TradingView only through an alert delivery method configured by the user.

## Scope rules

A contribution should preserve the primary purpose of the target script. Examples of scope creep include embedding execution automation in a levels indicator, adding unrelated named strategies to Futures Setups, or turning a context pane into a full charting framework.

When a proposed feature answers a new analytical question, it should usually become a separate script or remain in research until its role is clear.
