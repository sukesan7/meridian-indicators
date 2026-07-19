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

**Meridian Indicators** is the public TradingView indicator suite from **Meridian Trading**. The project separates intraday analysis into focused tools:

- **Levels** identifies important session, historical, volatility and confluence references.
- **Context** describes participation, momentum, volatility, relative strength and market regime.
- **Profile** shows where the futures auction accepts value and how that value changes.
- **Setups** converts confirmed liquidity, structure, zone and strategy conditions into temporary trade hypotheses.

The scripts are written in Pine Script v6 and remain fully inspectable. Each indicator documents its calculations, limits and intended use. Meridian indicators are analytical tools. They do not place broker orders and do not provide guaranteed trade outcomes.

## Indicator Suite

| Indicator | Market | Type | Primary purpose | Status | Documentation | Source |
|---|---|---|---|---|---|---|
| **Meridian — Options Levels** | SPY, QQQ and other liquid option underlyings | Overlay | Prior-session levels, premarket structure, Opening Range, RTH VWAP and optional EMA filters | Stable development release | [Read docs](./docs/meridian-options-levels.md) | [View Pine](./indicators/options/meridian-options-levels/meridian-options-levels.pine) |
| **Meridian — Options Context** | SPY, QQQ and other liquid option underlyings | Lower pane | RSI, same-time RVOL, VWAP/OR/EMA agreement and a transparent context score | Stable development release | [Read docs](./docs/meridian-options-context.md) | [View Pine](./indicators/options/meridian-options-context/meridian-options-context.pine) |
| **Meridian — Futures Levels** | NQ, ES, MNQ, MES and related futures | Overlay | Session structure, OR, IB, custom VWAP bands, references, projections, clusters and level states | Stable development release | [Read docs](./docs/meridian-futures-levels.md) | [View Pine](./indicators/futures/meridian-futures-levels/meridian-futures-levels.pine) |
| **Meridian — Futures Context** | NQ, ES, MNQ and MES | Lower pane | Same-time participation, realized volatility, regime, EMA/ADX structure and relative strength | Stable development release | [Read docs](./docs/meridian-futures-context.md) | [View Pine](./indicators/futures/meridian-futures-context/meridian-futures-context-v0.1.6.pine) |
| **Meridian — Futures Profile** | NQ, ES, MNQ and MES | Overlay | Current/previous TPO profiles, value area, profile structure and Auction Market Theory context | Active development | [Read docs](./docs/meridian-futures-profile.md) | [View Pine](./indicators/futures/meridian-futures-profile/meridian-futures-profile-v0.1.1.pine) |
| **Meridian — Futures Setups** | NQ, ES, MNQ and MES | Overlay | Stateful liquidity, structure, FVG/IFVG/OB/BB, SMT, scoring and risk/reward setup management | **Beta · Work in progress** | [Read docs](./docs/meridian-futures-setups.md) | [View Pine](./indicators/futures/meridian-futures-setups/meridian-futures-setups-v0.2.pine) |

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
      <a href="./docs/meridian-futures-setups.md"><img src="./screenshots/Meridian_Futures_Setups.png" alt="Meridian Futures Setups beta preview"></a>
      <br><b>Futures Setups — Beta</b><br>
      Confirmed setup detection, confluence scoring and temporary risk/reward trade hypotheses.
    </td>
  </tr>
</table>

> **Screenshot note:** `Meridian_Futures_Setups.png` is reserved for the Futures Setups preview. Add the image to `screenshots/` when the beta visual design is finalized.

## Quick Start

### Install an indicator in TradingView

1. Open the indicator's `.pine` file from the **Source** column above.
2. Copy the complete source code.
3. Open a chart in TradingView.
4. Select **Pine Editor**.
5. Create a blank indicator and replace its contents with the Meridian source.
6. Save the script and select **Add to chart**.
7. Open the indicator settings and confirm the session timezone, market session and display options.

### Download the repository

Use GitHub's **Code** menu to clone the repository or download it as a ZIP. Indicator source files are stored under `indicators/`. Documentation and screenshots are stored under `docs/` and `screenshots/`.

Clone with Git:

```bash
git clone https://github.com/YOUR_USERNAME/meridian-indicators.git
cd meridian-indicators
```

Replace `YOUR_USERNAME` with the repository owner before publishing this command.

### Update an installed script

TradingView does not automatically update source code copied from GitHub.

1. Open the latest source file in this repository.
2. Review the commit history and changelog.
3. Copy the updated source.
4. Replace the source in your saved TradingView script.
5. Save the script and refresh or re-add it to the chart.

Git commit history and source diffs make each public change reviewable.

## Recommended Chart Setup

### Options indicators

- Apply the scripts to the underlying chart, such as SPY or QQQ, not to an individual option contract.
- Use standard time-based candles.
- Typical working timeframes are 1, 2, 3, 5 and 15 minutes.
- Enable extended hours when premarket levels are required.

### Futures Levels, Context and Profile

- Designed primarily for NQ, ES, MNQ and MES.
- Use standard candles rather than synthetic chart types.
- Use the active contract for live execution context. Continuous contracts are convenient for research but can be affected by rollover and back-adjustment.
- One-minute, five-minute and fifteen-minute charts provide the best alignment for intraday session calculations.
- Confirm the chart timezone and session configuration when calculations appear offset.

### Futures Setups beta

- Primary timeframe: **1 minute**.
- Supported working timeframes: 1, 3, 5 and 15 minutes.
- Recommended markets: NQ, MNQ, ES and MES.
- Recommended session: extended hours.
- Recommended initial mode: `Meridian Choice` with the `Balanced` scoring profile.
- Use `Minimal` or `Signals` display mode for normal chart use.
- Use `Research` mode only for diagnostics because it intentionally shows more internal state.
- Treat all setup markers as rule-based hypotheses, not broker orders or guaranteed entries.

Futures Setups is a **beta and work in progress**. Its thresholds, named strategy definitions, stop limits and visual lifecycle can change during validation.

## Suggested Workflows

### Options workflow

Use **Options Levels** on the price chart and **Options Context** in a lower pane.

- Levels supplies PDH/PDL, premarket, Opening Range and VWAP references.
- Context shows whether momentum and participation support or conflict with price at those references.

### Futures analysis workflow

Use **Futures Levels**, **Futures Context** and **Futures Profile** together.

- Levels answers: *Where are the objective references and confluence zones?*
- Context answers: *Is the session trending, balancing, expanding or compressing?*
- Profile answers: *Where is value forming, migrating or failing?*

The Profile dashboard includes a layout option intended to stack with the Futures Levels dashboard.

### Futures setup workflow

Add **Futures Setups** when you want the suite to convert confirmed market evidence into temporary setup hypotheses.

- Levels supplies objective liquidity and session references.
- Context supplies participation, volatility and regime information.
- Profile supplies value and auction-location context.
- Setups independently registers the evidence that it requires, applies mandatory gates and confluence scoring, and shows only qualified setup zones or triggered trades according to the selected display mode.

Futures Setups does not directly read the internal object state of the other indicators. It recalculates the required data so that it can operate as a standalone public script.

## Repository Layout

```text
meridian-indicators/
├── README.md
├── LICENSE
├── docs/
│   ├── README.md
│   ├── meridian-options-levels.md
│   ├── meridian-options-context.md
│   ├── meridian-futures-levels.md
│   ├── meridian-futures-context.md
│   ├── meridian-futures-profile.md
│   └── meridian-futures-setups.md
├── indicators/
│   ├── options/
│   │   ├── meridian-options-levels/
│   │   └── meridian-options-context/
│   └── futures/
│       ├── meridian-futures-levels/
│       ├── meridian-futures-context/
│       ├── meridian-futures-profile/
│       └── meridian-futures-setups/
└── screenshots/
    ├── Meridian_Options_Levels.png
    ├── Meridian_Options_Context.png
    ├── Meridian_Futures_Levels.png
    ├── Meridian_Futures_Context.png
    ├── Meridian_Futures_Profile.png
    └── Meridian_Futures_Setups.png
```

## Design Principles

- **Transparent:** source code and calculation logic are public.
- **Explainable:** classifications and setup states use documented rules rather than unexplained labels.
- **Session-aware:** intraday calculations use explicit market-session boundaries.
- **Confirmed where required:** completed higher-timeframe values and confirmed pivots are used on critical setup paths.
- **Stateful:** zones, levels and setup hypotheses progress through explicit lifecycles.
- **Customizable:** sessions, thresholds, visual styles, strategies and display density are configurable.
- **Composable:** each indicator has a focused role and can be used independently or with the Meridian suite.
- **Bounded:** drawing objects and retained history are limited to respect Pine Script resource constraints.

## Documentation

Detailed documentation is available for every current indicator:

- [Meridian — Options Levels](./docs/meridian-options-levels.md)
- [Meridian — Options Context](./docs/meridian-options-context.md)
- [Meridian — Futures Levels](./docs/meridian-futures-levels.md)
- [Meridian — Futures Context](./docs/meridian-futures-context.md)
- [Meridian — Futures Profile](./docs/meridian-futures-profile.md)
- [Meridian — Futures Setups — Beta](./docs/meridian-futures-setups.md)

The [documentation index](./docs/README.md) provides a compact list of all indicator guides.

## Development Status

The repository is under active development. Public scripts can receive calculation fixes, usability improvements, new alerts, documentation changes and visual refinements.

**Meridian — Futures Setups is currently a beta and work in progress.** It is being validated through Pine compiler checks, TradingView Replay, live-session observation and later research-harness testing. Its current named strategies are Meridian's explicit implementations of their documented rules. Public descriptions of those strategies can differ.

Review the commit history before updating a script so that you understand what changed. Reproducible chart examples and bug reports are welcome through GitHub Issues once issue tracking is enabled.

## Planned Work

Current research and development areas include:

- Futures Setups beta validation and strategy hardening
- A separate Futures Setups research strategy
- Futures Auction and footprint research
- Constituent and intermarket pressure models
- Additional public strategy templates after formal specification and validation
- Secure Meridian Intelligence integrations

## Disclaimer

These indicators are research and market-analysis tools. They do not provide financial advice, guarantee a result, place broker orders or replace independent risk management. Historical references, statistical classifications, setup scores and alerts can fail or become less useful when market structure changes.

Futures Setups uses OHLC bars. Historical bars do not reveal the exact intrabar sequence when a stop and target occur in the same candle. Named strategies and scoring thresholds remain subject to continued research.

<a id="license"></a>
## License

The source code in this repository is licensed under the [Mozilla Public License 2.0](./LICENSE).

The MPL-2.0 permits use, study, modification and redistribution under its terms. The license applies to covered source code. It does not grant rights to the **Meridian Trading** name, logos, branding, premium products or private infrastructure.

---

<p align="center">
  Developed by <b>Meridian Trading</b>.
</p>
