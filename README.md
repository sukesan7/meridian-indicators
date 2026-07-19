<p align="center">
  <img src="./screenshots/Meridian%20Trading%20Banner.png" alt="Meridian Trading" width="100%">
</p>

<h1 align="center">Meridian Indicators</h1>

<p align="center">
  Open-source TradingView indicators for structured intraday analysis across options underlyings and index futures.
</p>

<p align="center">
  <img alt="Pine Script v6" src="https://img.shields.io/badge/Pine%20Script-v6-8B5CF6?style=flat-square">
  <img alt="TradingView" src="https://img.shields.io/badge/Platform-TradingView-131722?style=flat-square&logo=tradingview">
  <img alt="License MPL 2.0" src="https://img.shields.io/badge/License-MPL--2.0-7C3AED?style=flat-square">
  <img alt="Open Source" src="https://img.shields.io/badge/Source-Open-22C55E?style=flat-square">
  <img alt="Active Development" src="https://img.shields.io/badge/Status-Active%20Development-F472B6?style=flat-square">
</p>

## Overview

**Meridian Indicators** is the public TradingView indicator suite from **Meridian Trading**. The project is designed around a simple separation of responsibilities:

- **Levels** identifies where price is interacting with important session and historical references.
- **Context** describes the current market environment, participation, momentum, and trend quality.
- **Profile** describes where the futures auction is accepting value and how that value is changing.

The scripts are written in Pine Script v6, remain fully inspectable, and are intended to be useful without requiring hidden calculations or unexplained signal labels. They are analytical tools, not automated trade recommendations.

## Indicator Suite

| Indicator | Market | Type | Primary purpose | Documentation | Source |
|---|---|---|---|---|---|
| **Meridian — Options Levels** | SPY, QQQ and other liquid option underlyings | Overlay | Prior-session levels, premarket structure, opening range, RTH VWAP and optional EMA filters | [Read docs](./docs/meridian-options-levels.md) | [View Pine](./indicators/options/meridian-options-levels/meridian-options-levels.pine) |
| **Meridian — Options Context** | SPY, QQQ and other liquid option underlyings | Lower pane | RSI, same-time RVOL, VWAP/OR/EMA agreement and a transparent context score | [Read docs](./docs/meridian-options-context.md) | [View Pine](./indicators/options/meridian-options-context/meridian-options-context.pine) |
| **Meridian — Futures Levels** | NQ, ES, MNQ, MES and related futures | Overlay | Session structure, OR, IB, custom VWAP bands, references, projections, clusters and level states | [Read docs](./docs/meridian-futures-levels.md) | [View Pine](./indicators/futures/meridian-futures-levels/meridian-futures-levels.pine) |
| **Meridian — Futures Context** | NQ, ES, MNQ and MES | Lower pane | Same-time participation, realized volatility, regime, EMA/ADX structure and relative strength | [Read docs](./docs/meridian-futures-context.md) | [View Pine](./indicators/futures/meridian-futures-context/meridian-futures-context-v0.1.6.pine) |
| **Meridian — Futures Profile** | NQ, ES, MNQ and MES | Overlay | Current/previous TPO profiles, value area, profile structure and Auction Market Theory context | [Read docs](./docs/meridian-futures-profile.md) | [View Pine](./indicators/futures/meridian-futures-profile/meridian-futures-profile-v0.1.1.pine) |

## Screenshots

<table>
  <tr>
    <td width="50%" valign="top">
      <a href="./docs/meridian-options-levels.md"><img src="./screenshots/Meridian_Options_Levels.png" alt="Meridian Options Levels"></a>
      <br><b>Options Levels</b><br>
      Session-aware references for liquid option underlyings.
    </td>
    <td width="50%" valign="top">
      <a href="./docs/meridian-options-context.md"><img src="./screenshots/Meridian_Options_Context.png" alt="Meridian Options Context"></a>
      <br><b>Options Context</b><br>
      Momentum, participation and directional agreement in one pane.
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <a href="./docs/meridian-futures-levels.md"><img src="./screenshots/Meridian_Futures_Levels.png" alt="Meridian Futures Levels"></a>
      <br><b>Futures Levels</b><br>
      RTH/overnight structure, VWAP, OR, IB and confluence zones.
    </td>
    <td width="50%" valign="top">
      <a href="./docs/meridian-futures-context.md"><img src="./screenshots/Meridian_Futures_Context.png" alt="Meridian Futures Context"></a>
      <br><b>Futures Context</b><br>
      Participation, volatility, relative strength and regime classification.
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <a href="./docs/meridian-futures-profile.md"><img src="./screenshots/Meridian_Futures_Profile.png" alt="Meridian Futures Profile"></a>
      <br><b>Futures Profile</b><br>
      TPO value, structure, migration and auction-state interpretation.
    </td>
    <td width="50%" valign="top">
      <b>More Meridian research is in development.</b><br><br>
      Planned work includes Futures Auction, constituent pressure, additional profile research, validation tooling and secure Meridian Intelligence integrations.
    </td>
  </tr>
</table>

## Quick Start

### Install an indicator in TradingView

1. Open the indicator's `.pine` file from the **Source** column above.
2. Select the file contents and copy them.
3. In TradingView, open a chart and select **Pine Editor**.
4. Create a new blank indicator, replace its contents with the Meridian script, and save it.
5. Select **Add to chart**.
6. Open the indicator settings and confirm the session timezone, regular trading hours and preferred display options.

### Download the repository

Use GitHub's **Code** menu to clone the repository or download it as a ZIP. Each indicator is stored in its own folder under `indicators/`, while documentation and screenshots live in `docs/` and `screenshots/`.

### Update an installed script

TradingView does not automatically update code copied from GitHub. To update:

1. Open the latest source file in this repository.
2. Copy the new code.
3. Replace the code in your saved TradingView script.
4. Save and re-add or refresh the indicator.

Git commit history and source diffs make every public change reviewable.

## Recommended Chart Setup

### Options indicators

- Apply the scripts to the **underlying chart**—for example SPY or QQQ—not to an individual option contract.
- Use standard time-based candles.
- Typical working timeframes are 1, 2, 3, 5 and 15 minutes.
- Enable extended hours when premarket levels are required.

### Futures indicators

- Designed primarily for NQ, ES, MNQ and MES.
- Use standard candles rather than synthetic chart types.
- Use the active contract for live execution context; continuous contracts are convenient for research but can be affected by rollover and back-adjustment.
- One-minute, five-minute and fifteen-minute charts provide the best alignment for intraday session calculations.
- Confirm the chart timezone/session configuration when results appear offset.

## Suggested Workflows

### Options workflow

Use **Options Levels** on the price chart and **Options Context** in a lower pane.

- Levels supplies PDH/PDL, premarket, opening-range and VWAP references.
- Context shows whether momentum and participation support or conflict with price at those references.

### Futures workflow

Use **Futures Levels**, **Futures Context** and **Futures Profile** together.

- Levels answers: *Where are the objective references and confluence zones?*
- Context answers: *Is the session trending, balancing, expanding or compressing?*
- Profile answers: *Where is value forming, migrating or failing?*

The Profile dashboard includes a layout option intended to stack above the Futures Levels dashboard when both are enabled.

## Repository Layout

```text
meridian-indicators/
├── README.md
├── LICENSE
├── docs/
│   ├── meridian-options-levels.md
│   ├── meridian-options-context.md
│   ├── meridian-futures-levels.md
│   ├── meridian-futures-context.md
│   └── meridian-futures-profile.md
├── indicators/
│   ├── options/
│   │   ├── meridian-options-levels/
│   │   └── meridian-options-context/
│   └── futures/
│       ├── meridian-futures-levels/
│       ├── meridian-futures-context/
│       └── meridian-futures-profile/
└── screenshots/
```

## Design Principles

- **Transparent:** source code and calculation logic are public.
- **Explainable:** classifications use documented rules rather than unexplained black-box labels.
- **Session-aware:** intraday calculations use explicit market-session boundaries.
- **Non-repainting where appropriate:** completed prior-day, prior-week and completed-profile references do not use future data.
- **Customizable:** sessions, thresholds, visual styles and display density are configurable.
- **Composable:** each indicator has a focused role and can be used independently or as part of the Meridian suite.

## Documentation

Detailed documentation is available for every current indicator:

- [Meridian — Options Levels](./docs/meridian-options-levels.md)
- [Meridian — Options Context](./docs/meridian-options-context.md)
- [Meridian — Futures Levels](./docs/meridian-futures-levels.md)
- [Meridian — Futures Context](./docs/meridian-futures-context.md)
- [Meridian — Futures Profile](./docs/meridian-futures-profile.md)

## Development Status

The repository is under active development. Public scripts may receive calculation fixes, usability improvements, new alerts, documentation changes and visual refinements. Review the commit history before updating a script so you understand what changed.

Bug reports and reproducible chart examples are welcome through GitHub Issues once issue tracking is enabled.

## Disclaimer

These indicators are research and market-analysis tools. They do not provide financial advice, guarantee a result, or replace independent risk management. Historical references, statistical classifications and alerts can fail or become less useful when market structure changes.

<a id="license"></a>
## License

The source code in this repository is licensed under the [Mozilla Public License 2.0](./LICENSE).

The MPL-2.0 permits use, study, modification and redistribution under its terms. The license applies to covered source code; it does not grant rights to the **Meridian Trading** name, logos, branding, premium products or private infrastructure.

---

<p align="center">
  Developed by <b>Meridian Trading</b>.
</p>
