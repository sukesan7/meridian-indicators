# Contributing to Meridian Indicators

Thank you for improving the project. Contributions should keep each indicator focused, explainable and reproducible.

## Before opening a pull request

1. Search existing issues for the same problem.
2. Reproduce the behavior on the latest source.
3. Record the exact symbol, contract, timeframe, timezone, visible session and relevant settings.
4. Keep the change limited to one problem or feature.
5. Run `python tools/validate_repo.py`.
6. Compile the changed script in TradingView and test the affected path with Bar Replay.

## Bug reports

A useful bug report includes:

- indicator and version;
- exact chart symbol and data feed when known;
- date/time of the affected bar;
- expected and actual behavior;
- settings that differ from defaults;
- screenshot or short recording;
- whether the issue reproduces after a chart reload.

## Code standards

- Use Pine Script v6.
- Preserve confirmed higher-timeframe data patterns.
- Bound arrays, labels, lines and boxes.
- Avoid duplicate calculations when one series can be reused.
- Do not add credentials, endpoints or private service identifiers.
- Keep source comments limited to the required version directive, SPDX identifier and compact script metadata. Put design explanations in `docs/`.
- Use clear names and explicit state transitions rather than compressed or opaque logic.
- Avoid named-strategy scope creep in the strategy-neutral setup engine.

## Documentation

Calculation changes must update the matching indicator guide and `manifest.json` when the version changes. Public source filenames remain versionless.

## Pull-request evidence

Describe the reason for the change, the calculation path affected, repainting implications, resource impact and validation performed. Screenshots should use standard candles and identify the symbol/timeframe.

## Licensing

By contributing, you agree that your contribution is licensed under the Mozilla Public License 2.0.
