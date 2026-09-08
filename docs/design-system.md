# Meridian visual and interaction standard

[← Documentation index](./README.md)

The public catalog uses one visual language so a user can move between indicators without relearning colors, object states or dashboard conventions.

## Semantic palette

| Meaning | Default |
|---|---|
| Brand / dashboard header | `#8B5CF6` |
| Bullish / support | `#2DD4BF` |
| Bearish / resistance | `#F87171` |
| Information / POC | `#38BDF8` |
| Neutral | `#94A3B8` |
| Pending / developing | `#A1A1AA` |
| Warning | `#FBBF24` |
| Panel background | `#090E17` |
| Panel border | `#334155` |
| Primary text | `#F8FAFC` |
| Secondary accent | `#C4B5FD` |

Colors remain configurable where the script exposes theme inputs, but these defaults carry the same meaning across the catalog.

## Drawing states

- **Confirmed:** solid line or confirmed semantic color.
- **Developing:** dashed line and/or muted fill.
- **Projected:** dotted line.
- **Potential / building:** neutral gray, typically about 90–94% transparent.
- **Confirmed zone:** semantic support/bull or resistance/bear color, typically about 82–88% transparent.
- **Invalidated / expired:** muted gray, typically about 92–96% transparent, with geometry frozen at resolution.
- **Resolved:** drawings stop extending when the event completes whenever the model has an objective terminal bar.

## Text and dashboards

Normal text defaults to **Small** and can be changed in each indicator's settings. Dashboards are fixed to the top-right corner, use a restrained two-column layout where practical, and do not display the script version.

Every dashboard header follows:

```text
Meridian -- NAME
```

Normal dashboards expose the primary answer, not implementation details. Scores, component breakdowns and rejected candidates belong in tooltips, the Data Window or research-only views.

## Live and confirmed data

Where relevant, Meridian distinguishes:

- `LIVE` — an open realtime bar is still developing;
- `CONFIRMED` — the displayed state comes from confirmed data;
- `STALE / CLOSED` — the chart's last available bar is old relative to wall-clock time.

Higher-timeframe values used as persistent historical evidence use completed source bars unless a feature explicitly documents a developing preview.
