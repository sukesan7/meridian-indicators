<p align="center">
  <img src="./assets/meridian-banner.png" alt="Meridian Trading" width="100%">
</p>

<h1 align="center">Meridian Indicators</h1>

<p align="center">
  Open-source TradingView indicators for structured intraday analysis of liquid options underlyings and US index futures.
</p>

<p align="center">
  <img alt="Pine Script v6" src="https://img.shields.io/badge/Pine%20Script-v6-8B5CF6?style=flat-square">
  <img alt="TradingView" src="https://img.shields.io/badge/Platform-TradingView-131722?style=flat-square&logo=tradingview">
  <img alt="Release 0.2.0" src="https://img.shields.io/badge/Release-v0.2.0-8B5CF6?style=flat-square">
  <img alt="MPL 2.0" src="https://img.shields.io/badge/License-MPL--2.0-22C55E?style=flat-square">
</p>

<p align="center">
  <a href="https://discord.gg/greFd258NP"><img alt="Join Meridian Desk" src="https://img.shields.io/badge/Join%20the%20Community-Meridian%20Desk-5865F2?style=for-the-badge&logo=discord&logoColor=white"></a>
</p>

## Start here

Meridian separates market analysis into focused tools instead of combining every concept into one chart script.

1. Choose an indicator from the catalog below.
2. Open its source file and copy the complete Pine Script.
3. In TradingView, open **Pine Editor**, paste the source into a blank indicator, save it, and select **Add to chart**.

New to TradingView scripts? Read [Getting started](./docs/getting-started.md). Technical users can start with the [architecture](./docs/architecture.md), [design standard](./docs/design-system.md) and [data-integrity model](./docs/data-integrity.md).

## Indicator catalog

| Indicator | Status | Source | Documentation |
|---|---|---|---|
| **Options Levels** | Stable | [script](./src/options/meridian-options-levels.pine) | [docs](./docs/indicators/options-levels.md) |
| **Options Context** | Stable | [script](./src/options/meridian-options-context.pine) | [docs](./docs/indicators/options-context.md) |
| **Futures Levels** | Stable | [script](./src/futures/meridian-futures-levels.pine) | [docs](./docs/indicators/futures-levels.md) |
| **Futures Context** | Stable | [script](./src/futures/meridian-futures-context.pine) | [docs](./docs/indicators/futures-context.md) |
| **Futures Profile** | Preview | [script](./src/futures/meridian-futures-profile.pine) | [docs](./docs/indicators/futures-profile.md) |
| **Futures Setups** | Beta | [daily script](./src/futures/meridian-futures-setups.pine) · [research script](./src/futures/meridian-futures-setups-research.pine) | [docs](./docs/indicators/futures-setups.md) |

**Status meanings:** Stable scripts are the recommended public builds. Preview scripts are usable but still undergoing calculation/interface refinement. Beta scripts require active validation and can change materially between versions.

The machine-readable [manifest](./manifest.json) records current versions, source paths and status.

## Screenshots

<table>
  <tr>
    <td width="50%" valign="top"><a href="./docs/indicators/options-levels.md"><img src="./assets/screenshots/options-levels.png" alt="Meridian Options Levels"></a><br><b>Options Levels</b><br>SPY-focused reaction zones and session references.</td>
    <td width="50%" valign="top"><a href="./docs/indicators/options-context.md"><img src="./assets/screenshots/options-context.png" alt="Meridian Options Context"></a><br><b>Options Context</b><br>Directional context, confidence, participation and confirmed HTF state.</td>
  </tr>
  <tr>
    <td width="50%" valign="top"><a href="./docs/indicators/futures-levels.md"><img src="./assets/screenshots/futures-levels.png" alt="Meridian Futures Levels"></a><br><b>Futures Levels</b><br>Session structure, VWAP, OR, IB and confluence.</td>
    <td width="50%" valign="top"><a href="./docs/indicators/futures-context.md"><img src="./assets/screenshots/futures-context.png" alt="Meridian Futures Context"></a><br><b>Futures Context</b><br>Participation, volatility, trend quality and intermarket regime.</td>
  </tr>
  <tr>
    <td width="50%" valign="top"><a href="./docs/indicators/futures-profile.md"><img src="./assets/screenshots/futures-profile.png" alt="Meridian Futures Profile"></a><br><b>Futures Profile</b><br>TPO value, IB quality and auction-state interpretation.</td>
    <td width="50%" valign="top"><a href="./docs/indicators/futures-setups.md"><img src="./assets/screenshots/futures-setups.png" alt="Meridian Futures Setups"></a><br><b>Futures Setups</b><br>Beta multi-timeframe qualification and trade-hypothesis geometry.</td>
  </tr>
</table>

## Repository layout

```text
meridian-indicators/
├── src/
│   ├── options/
│   └── futures/
├── docs/
│   ├── indicators/
│   ├── getting-started.md
│   ├── architecture.md
│   ├── design-system.md
│   ├── data-integrity.md
│   └── troubleshooting.md
├── assets/
├── tools/
├── manifest.json
├── CHANGELOG.md
├── CONTRIBUTING.md
├── SECURITY.md
├── DISCLAIMER.md
├── LICENSE
└── README.md
```

## Design principles

- **Focused:** every script has one primary analytical responsibility.
- **Consistent:** the catalog uses one semantic palette, line grammar, text scale and HUD design.
- **Explainable:** scores and labels are based on documented rules.
- **Session-aware:** intraday calculations use explicit session identities rather than assuming missing bars exist.
- **Confirmed where required:** persistent higher-timeframe evidence uses completed source data.
- **Bounded:** drawings and historical state are capped to respect Pine limits.
- **Composable:** scripts work independently while using compatible concepts and terminology.
- **Private by default:** scripts contain no credentials and only send alert data after the user explicitly creates a TradingView alert.

## Validation

Before opening a pull request run:

```bash
python -m unittest discover -s tools -p "test_*.py"
python tools/format_repo.py --check
python tools/validate_repo.py
```

Static validation checks metadata, links, source hygiene, balanced delimiters and daily/research Setups parity. It does **not** replace compiling each script in TradingView or validating market behavior with Bar Replay and live data.

## Contributing

Read [CONTRIBUTING.md](./CONTRIBUTING.md) before submitting a change. Calculation changes should include a reproducible symbol, timeframe, session configuration, affected timestamp and expected behavior.

## Community

Meridian Desk is the public place for indicator usage, chart discussion, setup feedback and community support.

<p align="center">
  <a href="https://discord.gg/greFd258NP"><img alt="Meridian Desk Discord" src="https://img.shields.io/badge/Open-Meridian%20Desk-5865F2?style=for-the-badge&logo=discord&logoColor=white"></a>
</p>

Use [GitHub Issues](https://github.com/sukesan7/meridian-indicators/issues) for reproducible bugs and focused feature requests.

## License and risk notice

Source code is licensed under the [Mozilla Public License 2.0](./LICENSE). See [DISCLAIMER.md](./DISCLAIMER.md) for the trading and market-data notice. Meridian Indicators is independent and is not affiliated with or endorsed by TradingView.
