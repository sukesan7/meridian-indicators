# Troubleshooting

[← Documentation index](./README.md)

## The script will not compile

- Confirm the entire file was copied, including `//@version=6`.
- Paste into a new blank indicator, not into an existing strategy.
- For Options Context, confirm TradingView can resolve `TradingView/ta/12`.
- Recopy the raw source when GitHub line numbers or page chrome were accidentally included.
- Check the current source rather than an old saved local copy.

## Levels are shifted or missing

- Use an intraday chart.
- Confirm the session timezone is `America/New_York` unless you intentionally changed it.
- Confirm extended hours are visible when premarket or overnight values are required.
- Confirm the chart's data session includes the bars needed by the indicator.
- Use a finer timeframe when OR or IB boundaries do not align cleanly.

## Options indicators behave strangely

Apply them to the underlying chart—such as SPY or QQQ—not to an individual option contract. Option contracts can have sparse volume, irregular pricing and different sessions that make underlying-market context misleading.

## Futures relative strength is unavailable

Check the paired symbol input and data entitlement. The default pairing is NQ with ES. A broker or exchange feed can use a different ticker namespace. Select a valid symbol manually when automatic pairing is not available.

## Same-time RVOL says “warming up”

The indicator needs completed historical samples for the same intraday slot. Increase loaded chart history, reduce the required baseline samples where available, or wait for more sessions. Holidays and shortened sessions can reduce usable observations.

## Futures Profile is incomplete or crowded

- Use a supported intraday timeframe.
- Reduce profile width, row labels or anomaly drawings.
- Increase row size when the profile exceeds rendering limits.
- Treat the estimated volume profile as optional; disable it when only TPO structure is needed.

## Futures Setups produces no signals

No signal is often the expected result. Check:

- chart symbol and timeframe support;
- the 08:00–16:00 ET default signal window;
- minimum score and independent-category requirements;
- structure and displacement gates;
- first-touch and maximum-touch rules;
- stop-size and objective-space filters;
- maximum active trades and one-trade-per-leg settings.

Use the research build to inspect candidate scores and rejection reasons. Do not lower every gate at once; change one variable and record the result.

## Too many setup drawings

Use the daily build for normal chart use. In the research build, reduce visible research zones, filter to relevant zones, shorten retention and hide liquidity-pool lines or rejected candidates.

## Alerts do not fire

- Create a TradingView alert after adding the indicator.
- Select the correct Meridian condition.
- Prefer **Once Per Bar Close** for confirmed behavior.
- Recreate an alert after replacing a script with a materially changed version.
- Confirm the indicator's alert toggles and session window are enabled.

## A dynamic JSON alert contains unexpected fields

Review the source and the guide for the selected indicator. The JSON is generated locally in Pine. Delivery format can also be affected by the text entered in TradingView's alert dialog. Do not include credentials in the payload.

## Reporting a reproducible bug

Include the script version, exact symbol, chart timeframe, timezone, visible session, relevant settings, date/time of the bar and a screenshot. State what happened and what you expected instead.
