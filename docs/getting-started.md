# Getting started

[← Documentation index](./README.md)

## 1. Choose the right script

Use the simplest script that answers your current question.

| Need | Start with |
|---|---|
| Session and historical levels on SPY or QQQ | Options Levels |
| Momentum and participation context for SPY or QQQ | Options Context |
| Session structure and confluence on NQ or ES | Futures Levels |
| Regime, participation and relative strength on NQ or ES | Futures Context |
| TPO value and auction structure | Futures Profile |
| A strict beta setup-qualification engine | Futures Setups daily build |
| Setup diagnostics and research counters | Futures Setups research build |

## 2. Install a script in TradingView

1. Open the source file from the [indicator catalog](../README.md#indicator-catalog).
2. Select **Raw** in GitHub, then copy the entire file.
3. Open a TradingView chart.
4. Open **Pine Editor** at the bottom of the chart.
5. Create a new blank indicator and replace its contents with the copied source.
6. Save the script with the Meridian indicator name.
7. Select **Add to chart**.

TradingView does not automatically update a script copied from GitHub. To update, copy the latest source into the saved Pine Editor script and save again.

## 3. Use the correct chart

### Options indicators

- Apply the script to the underlying chart, such as SPY or QQQ.
- Use a standard time-based intraday chart.
- Enable extended hours when premarket levels are required.
- Start with a 1-, 2-, 3-, 5- or 15-minute chart.

### Futures indicators

- Start with the active NQ, MNQ, ES or MES contract.
- Use standard candles; synthetic bars can alter session highs, lows and confirmation timing.
- Enable the session data needed by the indicator.
- One-, five- and fifteen-minute charts provide the clearest intraday alignment.
- Continuous contracts are convenient for research but can differ around rollover because of back-adjustment.

## 4. Confirm session settings

The default session timezone is `America/New_York`. The futures scripts use CME-style index-futures sessions and the options scripts use US equity regular hours.

When levels appear shifted:

1. confirm the chart symbol and exchange;
2. confirm the chart is intraday;
3. confirm extended-hours visibility;
4. compare the indicator session inputs with the chart session;
5. reload the chart after changing session settings.

## 5. Start with restrained settings

Avoid enabling every visual element at once. Begin with defaults, learn the core output, then add optional bands, labels, clusters or research drawings as needed.

For Futures Setups, begin with:

```text
Market: NQ or ES
Chart: 1 minute, standard candles
Extended hours: enabled
Signal window: 08:00–16:00 ET
Minimum score: 80
Independent categories: 4
Entry mode: Rejection close
First qualified touch: enabled
Maximum active trades: 1
```

## 6. Create alerts deliberately

A Pine script cannot send data by itself. An alert is delivered only after you create it in TradingView. Review the alert condition and any webhook destination before enabling it. Dynamic JSON alerts are intended for users who understand TradingView alert configuration and webhook security.

## Next steps

Read the guide for the selected indicator, then review [data integrity](./data-integrity.md) before relying on historical signals or higher-timeframe values.
