# Data integrity, confirmation and repainting

[← Documentation index](./README.md)

## What “confirmed” means

A confirmed value is based on a completed source bar or a completed session window. Confirmation prevents a historical chart from displaying information earlier than it was available in live trading.

Meridian uses confirmed values for critical previous-day, previous-week and higher-timeframe setup inputs. Confirmed pivots also appear only after the required right-side bars exist.

## Values that develop by design

Some outputs must change while a market window is still forming:

- current premarket high and low;
- current Opening Range and Initial Balance;
- current-session VWAP and deviation bands;
- the current TPO profile;
- current participation and volatility estimates;
- an active setup zone's fill, touch and lifecycle state.

These are not historical future leaks. They are live developing values. Their final state is known only after the relevant bar or session completes.

## Higher-timeframe requests

The confirmed request pattern used in the suite combines a completed-source offset with `lookahead_on`, or calls a higher-timeframe payload whose internals use completed bars. The offset is essential: `lookahead_on` without the completed-bar expression can leak future higher-timeframe information into historical bars.

The static validator flags common packaging mistakes, but TradingView compilation and Bar Replay remain required before release.

## Pivot timing

Pivot highs and lows require bars to the right of the pivot. A pivot marker therefore appears after confirmation, not at the moment the turning bar first prints. Documentation and alerts should distinguish the pivot's price location from the later bar where it became knowable.

## Current-bar alerts

Most critical state changes are evaluated on confirmed chart bars. TradingView alert frequency and the user's selected alert mode still matter. For consistent behavior, use **Once Per Bar Close** unless an indicator guide explicitly states otherwise.

## Same-time relative volume

Same-time RVOL compares current activity with equivalent intraday slots from prior sessions. Baselines require enough completed historical samples. Early output can show a warm-up state, and missing or irregular sessions can reduce sample quality.

Options Context uses TradingView's published `ta` library. Futures Context uses bounded circular arrays and does not insert the current session into its own baseline until bars are confirmed.

## External symbols and relative strength

Futures Context and Futures Setups can request a paired futures symbol, normally NQ versus ES. Results depend on the selected data feed, symbol continuity and session alignment. A missing or invalid comparison symbol can disable or degrade the relative-strength component without invalidating unrelated calculations.

## Standard versus synthetic candles

Heikin Ashi, Renko, Range and other synthetic chart types can alter OHLC values and bar timing. Meridian calculations that depend on actual highs, lows, closes, sessions or volume should be evaluated on standard time-based candles.

## Continuous futures contracts

Continuous contracts are useful for historical research, but rollover stitching and back-adjustment can change old prices and gaps. Use the active contract for execution context, and record the exact symbol when reporting a reproducibility issue.

## Estimated volume profile

Futures Profile's optional volume-by-price display distributes each chart bar's volume across the rows traversed by that bar. It is explicitly an estimate. It is not exchange-native volume at price, bid/ask aggressor volume, queue data or Depth of Market.

## Privacy and alert delivery

The repository contains no credentials or telemetry endpoint. Dynamic JSON is constructed inside the chart. It is not transmitted unless the user creates a TradingView alert and selects a notification or webhook destination. Never place secrets directly in public Pine source or alert messages.
