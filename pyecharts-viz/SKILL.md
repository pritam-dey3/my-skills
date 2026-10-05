---
name: pyecharts-viz
license: MIT
description: Generate pyecharts visualization examples and starter code. Use this skill when a user needs to create a pyecharts chart, compare chart options, learn how a chart works, or turn data into a visualization. It covers 49 chart types, 31 basic charts such as Bar, Line, Pie, Scatter, and Map; 4 composite charts such as Grid, Page, Tab, and Timeline; 8 3D charts such as Bar3D, Line3D, and Scatter3D; and 6 newer ECharts 6 chart types such as Violin and Stage.
---

# pyecharts Visualization Examples

## Attribution

Adapted from the Chinese-language [pyecharts/skills](https://github.com/pyecharts/skills)
by pyecharts, with modifications by Pritam Dey.

The upstream MIT license and copyright notice are preserved in [LICENSE](LICENSE).

## Quick Start

Use this workflow when generating a pyecharts chart example:

1. **Choose a chart type** - Select the most suitable chart based on the user's request.
2. **Find a reference example** - Look up the matching example in `references/chart_types.md`.
3. **Replace the sample data** - Swap the placeholder values with the user's real data.
4. **Render the output** - Call `.render()` to generate an HTML file, or `.render_notebook()` for notebook usage.

## When to Use This Skill

Use this skill when the user wants to:

1. Generate a pyecharts example from scratch.
2. Translate data into a chart quickly.
3. Compare multiple pyecharts chart types.
4. Build a dashboard-style layout with Grid, Page, Tab, or Timeline.
5. Work with 3D charts or map-based charts.

Do not use this skill when the user needs a different plotting library, such as matplotlib, seaborn, plotly, or altair.

## Chart Type Overview

See `references/chart_types.md` for the full chart catalog and minimal example code.

| Category | Count | Main Types |
|------|---------|---------|
| Basic charts | 31 | Bar, Line, Pie, Scatter, Map, Geo, Graph, HeatMap, and more |
| Composite charts | 4 | Grid, Page, Tab, Timeline |
| 3D charts | 8 | Bar3D, Line3D, Scatter3D, Surface3D, Map3D, MapGlobe, and more |
| New ECharts 6 charts | 6 | Violin, Stage, SegmentedDoughnut, Contour, BarRange, LineRange |

**49 chart types are covered in total**

## Core Capabilities

1. **Generate example code** - Provide a complete runnable example for any supported chart type.
2. **Use sample data** - Quickly create data for validation and experimentation.
3. **Combine charts** - Use Grid, Page, Tab, and Timeline to build multi-chart layouts.
4. **Map integration** - Support China maps, world maps, and Baidu, AMap, Google Maps, and Leaflet integrations.
5. **Output options** - Render to HTML, images with `snapshot_selenium`, or notebooks.

## Chart Selection Guide

Use these rules of thumb when the user does not specify a chart type:

| Goal | Recommended charts |
|------|--------------------|
| Compare categories | Bar, Line, PictorialBar |
| Show parts of a whole | Pie, Funnel, Sunburst, TreeMap |
| Show relationships | Scatter, EffectScatter, Graph, Sankey, Chord |
| Show change over time | Line, Bar, Timeline, ThemeRiver, Calendar |
| Show geographic data | Map, Geo, BMap, AMap, GMap, LMap, Map3D |
| Show multivariate or high-dimensional data | Radar, Parallel, HeatMap, Scatter3D |

## Practical Notes

1. **Map providers need keys** - BMap and AMap require real API keys before they will render correctly.
2. **Map assets may be required** - Some region maps require additional pyecharts map packages.
3. **Image export is optional** - Rendering to PNG requires `snapshot_selenium` and a compatible browser driver.
4. **3D charts need the right frontend assets** - Use them only when the environment supports the required ECharts components.
5. **Notebook output is different from file output** - Prefer `.render_notebook()` inside notebooks and `.render()` for standalone HTML.

## Standard Chart Structure

```python
from pyecharts import options as opts
from pyecharts.charts import Bar

chart = (
    Bar()
    .add_xaxis(["A", "B", "C"])
    .add_yaxis("Series", [10, 20, 30])
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Chart Title"),
        xaxis_opts=opts.AxisOpts(),
        yaxis_opts=opts.AxisOpts(),
    )
)
chart.render("output.html")
```

## Common Configuration Reference

### Global options (`set_global_opts`)
- `title_opts` - Title configuration
- `legend_opts` - Legend configuration
- `tooltip_opts` - Tooltip configuration
- `xaxis_opts` / `yaxis_opts` - Axis configuration
- `visualmap_opts` - Visual mapping configuration
- `datazoom_opts` - Zoom region configuration

### Series options
- `label_opts` - Label styling
- `itemstyle_opts` - Item styling
- `linestyle_opts` - Line styling
- `markpoint_opts` / `markline_opts` - Mark points and mark lines

## Output Options

### Render to an HTML file
```python
chart.render("chart.html")
```

### Render to an image (requires extra dependencies)
```python
from snapshot_selenium import snapshot as driver
from pyecharts.render import make_snapshot

make_snapshot(driver, chart.render(), "chart.png")
```

### Notebook environment
```python
chart.render_notebook()
```

## References

- **Detailed chart types and examples**: `references/chart_types.md`
- **Official pyecharts documentation**: https://pyecharts.org
- **Example gallery**: https://gallery.pyecharts.org
