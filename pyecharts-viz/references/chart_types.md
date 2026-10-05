# pyecharts Chart Type Reference

This reference collects minimal pyecharts examples that you can adapt quickly. Use it to pick a chart, copy a starting point, and replace the sample data with real values.

## Usage Notes

1. These are starter examples, not production-ready dashboards.
2. Most examples focus on the smallest useful configuration.
3. Map-based charts may require extra map packages or provider API keys.
4. Newer ECharts 6 chart types are shown through `Custom` series examples.

## Table of Contents

1. [Basic Charts](#basic-charts)
2. [Composite Charts](#composite-charts)
3. [3D Charts](#3d-charts)

---

## Basic Charts

### Bar - Bar Chart

```python
from pyecharts import options as opts
from pyecharts.charts import Bar

bar = (
    Bar()
    .add_xaxis(["Shirts", "Sweaters", "Ties", "Pants", "Coats", "Heels", "Socks"])
    .add_yaxis("Store A", [114, 55, 27, 101, 125, 27, 105])
    .add_yaxis("Store B", [57, 134, 137, 129, 145, 60, 49])
    .set_global_opts(title_opts=opts.TitleOpts(title="Bar Chart Example"))
)
```

### Line - Line Chart

```python
from pyecharts import options as opts
from pyecharts.charts import Line

line = (
    Line()
    .add_xaxis(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
    .add_yaxis("Sales", [120, 200, 150, 80, 70, 110, 130])
    .set_global_opts(title_opts=opts.TitleOpts(title="Line Chart Example"))
)
```

### Pie - Pie Chart

```python
from pyecharts import options as opts
from pyecharts.charts import Pie

pie = (
    Pie()
    .add(
        "Products",
        [
            ("Shirts", 114),
            ("Sweaters", 55),
            ("Ties", 27),
            ("Pants", 101),
            ("Coats", 125),
        ],
        radius=["40%", "75%"],
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="Pie Chart Example"))
)
```

### Scatter - Scatter Chart

```python
from pyecharts import options as opts
from pyecharts.charts import Scatter

scatter = (
    Scatter()
    .add_xaxis(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
    .add_yaxis("Units Sold", [120, 200, 150, 80, 70, 110, 130])
    .set_global_opts(title_opts=opts.TitleOpts(title="Scatter Chart Example"))
)
```

### EffectScatter - Scatter Chart with Ripple Effect

```python
from pyecharts import options as opts
from pyecharts.charts import EffectScatter

es = (
    EffectScatter()
    .add_xaxis(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
    .add_yaxis("Units Sold", [120, 200, 150, 80, 70, 110, 130])
    .set_global_opts(title_opts=opts.TitleOpts(title="Effect Scatter Example"))
)
```

### Map - Map Chart

```python
from pyecharts import options as opts
from pyecharts.charts import Map

map_chart = (
    Map()
    .add(
        "Data",
        [("China", 100), ("United States", 50), ("Canada", 60), ("Brazil", 40)],
        "world",
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="Map Example"))
)
```

### Geo - Geographic Coordinate Chart

```python
from pyecharts import options as opts
from pyecharts.charts import Geo

geo = (
    Geo()
    .add_schema(maptype="world")
    .add(
        "Cities",
        [("New York", 100), ("London", 80), ("Tokyo", 60), ("Sydney", 50)],
        type_="effectScatter",
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="Geo Chart Example"))
)
```

### Graph - Network Graph

```python
from pyecharts import options as opts
from pyecharts.charts import Graph

nodes = [
    {"name": "Node 1"},
    {"name": "Node 2"},
    {"name": "Node 3"},
]
links = [
    {"source": "Node 1", "target": "Node 2"},
    {"source": "Node 2", "target": "Node 3"},
]

graph = (
    Graph()
    .add("", nodes, links, repulsion=8000)
    .set_global_opts(title_opts=opts.TitleOpts(title="Graph Example"))
)
```

### HeatMap - Heat Map

```python
from pyecharts import options as opts
from pyecharts.charts import HeatMap

heatmap = (
    HeatMap()
    .add_xaxis(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
    .add_yaxis(
        "Time",
        ["12a", "1a", "2a", "3a", "4a", "5a", "6a", "7a", "8a", "9a"],
        [[0, 0, 10], [0, 1, 20], [1, 0, 30]],  # [x index, y index, value]
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="Heat Map Example"))
)
```

### Boxplot - Box Plot

```python
from pyecharts import options as opts
from pyecharts.charts import Boxplot

boxplot = (
    Boxplot()
    .add_xaxis(["Category A", "Category B", "Category C"])
    .add_yaxis(
        "Data",
        [[10, 20, 30, 40, 50], [15, 25, 35, 45, 55], [12, 22, 32, 42, 52]],
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="Box Plot Example"))
)
```

### Kline - Candlestick Chart

```python
from pyecharts import options as opts
from pyecharts.charts import Kline

kline = (
    Kline()
    .add_xaxis(["2024-01-01", "2024-01-02", "2024-01-03"])
    .add_yaxis(
        "Kline",
        [[2320.26, 2320.26, 2287.3, 2362.94], [2300, 2291.3, 2288.26, 2308.38]],
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="Candlestick Chart Example"))
)
```

### Gauge - Gauge Chart

```python
from pyecharts import options as opts
from pyecharts.charts import Gauge

gauge = (
    Gauge()
    .add("", [("Completion", 75)])
    .set_global_opts(title_opts=opts.TitleOpts(title="Gauge Example"))
)
```

### Funnel - Funnel Chart

```python
from pyecharts import options as opts
from pyecharts.charts import Funnel

funnel = (
    Funnel()
    .add(
        "Conversion",
        [("Visit", 100), ("Inquiry", 60), ("Order", 40), ("Payment", 20)],
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="Funnel Chart Example"))
)
```

### Radar - Radar Chart

```python
from pyecharts import options as opts
from pyecharts.charts import Radar

radar = (
    Radar()
    .add_schema(
        schema=[
            {"name": "Sales", "max": 100},
            {"name": "Management", "max": 100},
            {"name": "Engineering", "max": 100},
            {"name": "Service", "max": 100},
        ]
    )
    .add("Budget", [[80, 70, 90, 85]])
    .add("Actual", [[70, 80, 85, 90]])
    .set_global_opts(title_opts=opts.TitleOpts(title="Radar Chart Example"))
)
```

### Polar - Polar Chart

```python
from pyecharts import options as opts
from pyecharts.charts import Polar

polar = (
    Polar()
    .add_schema(angleaxis_opts=opts.AngleAxisOpts(data=["Mon", "Tue", "Wed"]))
    .add("Data", [1, 2, 3], type_="bar")
    .set_global_opts(title_opts=opts.TitleOpts(title="Polar Chart Example"))
)
```

### WordCloud - Word Cloud

```python
from pyecharts import options as opts
from pyecharts.charts import WordCloud

wordcloud = (
    WordCloud()
    .add(
        words=[("Python", 100), ("ECharts", 80), ("Visualization", 60)],
        word_size_range=[20, 50],
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="Word Cloud Example"))
)
```

### Liquid - Liquid Fill Chart

```python
from pyecharts import options as opts
from pyecharts.charts import Liquid

liquid = (
    Liquid()
    .add("lq", [0.6, 0.7])
    .set_global_opts(title_opts=opts.TitleOpts(title="Liquid Fill Example"))
)
```

### Sunburst - Sunburst Chart

```python
from pyecharts import options as opts
from pyecharts.charts import Sunburst

sunburst = (
    Sunburst()
    .add(
        "Data",
        [
            {
                "name": "Group A",
                "value": 10,
                "children": [{"name": "Subgroup A1", "value": 5}],
            },
            {"name": "Group B", "value": 8},
        ],
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="Sunburst Example"))
)
```

### Tree - Tree Chart

```python
from pyecharts import options as opts
from pyecharts.charts import Tree

tree = (
    Tree()
    .add(
        "tree",
        [
            {"name": "Root", "children": [{"name": "Child 1"}, {"name": "Child 2"}]},
        ],
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="Tree Chart Example"))
)
```

### TreeMap - Treemap Chart

```python
from pyecharts import options as opts
from pyecharts.charts import TreeMap

treemap = (
    TreeMap()
    .add(
        "Data",
        [
            {"name": "Category A", "value": 100},
            {"name": "Category B", "value": 80},
            {"name": "Category C", "value": 60},
        ],
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="Treemap Example"))
)
```

### ThemeRiver - Theme River Chart

```python
from pyecharts import options as opts
from pyecharts.charts import ThemeRiver

theme_river = (
    ThemeRiver()
    .add(
        ["Theme A", "Theme B", "Theme C"],
        [["2024-01", 10, 20], ["2024-02", 15, 25]],
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="Theme River Example"))
)
```

### Sankey - Sankey Diagram

```python
from pyecharts import options as opts
from pyecharts.charts import Sankey

sankey = (
    Sankey()
    .add(
        "sankey",
        nodes=[{"name": "Source"}, {"name": "Middle"}, {"name": "Target"}],
        links=[
            {"source": "Source", "target": "Middle", "value": 50},
            {"source": "Middle", "target": "Target", "value": 30},
        ],
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="Sankey Example"))
)
```

### Chord - Chord Diagram

```python
from pyecharts import options as opts
from pyecharts.charts import Chord

chord = (
    Chord()
    .add(
        schema=[
            {"name": "A"},
            {"name": "B"},
            {"name": "C"},
        ],
        matrix=[[0, 10, 20], [10, 0, 30], [20, 30, 0]],
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="Chord Diagram Example"))
)
```

### Parallel - Parallel Coordinates

```python
from pyecharts import options as opts
from pyecharts.charts import Parallel

parallel = (
    Parallel()
    .add_schema(
        schema=[
            {"dim": 0, "name": "Dimension 1"},
            {"dim": 1, "name": "Dimension 2"},
            {"dim": 2, "name": "Dimension 3"},
        ]
    )
    .add("Data", [[1, 2, 3], [2, 3, 4]])
    .set_global_opts(title_opts=opts.TitleOpts(title="Parallel Coordinates Example"))
)
```

### PictorialBar - Pictorial Bar Chart

```python
from pyecharts import options as opts
from pyecharts.charts import PictorialBar

pictorial_bar = (
    PictorialBar()
    .add_xaxis(["A", "B", "C"])
    .add_yaxis("Data", [10, 20, 30], symbol="circle")
    .set_global_opts(title_opts=opts.TitleOpts(title="Pictorial Bar Example"))
)
```

### Calendar - Calendar Chart

```python
from pyecharts import options as opts
from pyecharts.charts import Calendar

calendar = (
    Calendar()
    .add(
        "",
        [["2024-01-01", 10], ["2024-01-02", 20]],
        calendar_opts=opts.CalendarOpts(range_="2024"),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="Calendar Chart Example"))
)
```

### Custom - Custom Chart

```python
from pyecharts import options as opts
from pyecharts.charts import Custom

custom = (
    Custom()
    .add_xaxis(["A", "B", "C"])
    .add_yaxis(
        "Data",
        [[10, 20], [20, 30], [30, 40]],
        custom_series_func="function (api) { return {...}; }",
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="Custom Chart Example"))
)
```

### Violin - Violin Chart (New in ECharts 6)

```python
from pyecharts import options as opts
from pyecharts.charts import Custom

# Violin charts are implemented with a custom series.
violin = (
    Custom()
    .add_xaxis(["Category A", "Category B", "Category C"])
    .add_yaxis(
        "Violin",
        [[0, 10, 20, 30, 40, 50], [5, 15, 25, 35, 45, 55]],
        custom_series_type="violin",
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="Violin Chart Example"))
)
```

### Stage - Stage Chart (New in ECharts 6)

```python
from pyecharts import options as opts
from pyecharts.charts import Custom

stage = (
    Custom()
    .add_xaxis(["Stage 1", "Stage 2", "Stage 3"])
    .add_yaxis(
        "Stage",
        [[10, 20], [20, 30], [30, 40]],
        custom_series_type="stage",
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="Stage Chart Example"))
)
```

### SegmentedDoughnut - Segmented Doughnut Chart (New in ECharts 6)

```python
from pyecharts import options as opts
from pyecharts.charts import Custom

doughnut = (
    Custom()
    .add(
        "Doughnut",
        [{"name": "A", "value": 30}, {"name": "B", "value": 40}],
        custom_series_type="segmentedDoughnut",
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="Segmented Doughnut Example"))
)
```

### Contour - Contour Chart (New in ECharts 6)

```python
from pyecharts import options as opts
from pyecharts.charts import Custom

contour = (
    Custom()
    .add_xaxis([i for i in range(10)])
    .add_yaxis(
        "Contour",
        [[x, y, (x**2 + y**2) ** 0.5] for x in range(10) for y in range(10)],
        custom_series_type="contour",
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="Contour Chart Example"))
)
```

### BarRange - Range Bar Chart (New in ECharts 6)

```python
from pyecharts import options as opts
from pyecharts.charts import Custom

bar_range = (
    Custom()
    .add_xaxis(["Category A", "Category B", "Category C"])
    .add_yaxis(
        "Range",
        [[10, 30], [20, 40], [15, 35]],  # [minimum, maximum]
        custom_series_type="barRange",
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="Range Bar Example"))
)
```

### LineRange - Range Line Chart (New in ECharts 6)

```python
from pyecharts import options as opts
from pyecharts.charts import Custom

line_range = (
    Custom()
    .add_xaxis(["Mon", "Tue", "Wed", "Thu", "Fri"])
    .add_yaxis(
        "Range",
        [[10, 30], [15, 35], [20, 40], [18, 38], [12, 32]],
        custom_series_type="lineRange",
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="Range Line Example"))
)
```

### BMap - Baidu Map

```python
from pyecharts import options as opts
from pyecharts.charts import BMap

bmap = (
    BMap()
    .add_schema(baidu_ak="your_baidu_ak", center=[116.40, 39.90], zoom=10)
    .add("Data", [("Tiananmen Square", [116.40, 39.90])])
    .set_global_opts(title_opts=opts.TitleOpts(title="Baidu Map Example"))
)
```

### AMap - AMap

```python
from pyecharts import options as opts
from pyecharts.charts import AMap

amap = (
    AMap()
    .add_schema(amap_ak="your_amap_ak", center=[116.40, 39.90], zoom=10)
    .add("Data", [("Tiananmen Square", [116.40, 39.90])])
    .set_global_opts(title_opts=opts.TitleOpts(title="AMap Example"))
)
```

### GMap - Google Map

```python
from pyecharts import options as opts
from pyecharts.charts import GMap

gmap = (
    GMap()
    .add("Data", [("China", 100), ("USA", 80)], "world")
    .set_global_opts(title_opts=opts.TitleOpts(title="GMap Example"))
)
```

### LMap - Leaflet Map

```python
from pyecharts import options as opts
from pyecharts.charts import LMap

lmap = (
    LMap()
    .add("Data", [("Beijing", [39.90, 116.40])])
    .set_global_opts(title_opts=opts.TitleOpts(title="Leaflet Map Example"))
)
```

---

## Composite Charts

### Grid - Multi-Chart Cartesian Layout

```python
from pyecharts import options as opts
from pyecharts.charts import Grid, Bar, Line

bar = Bar().add_xaxis(["A", "B"]).add_yaxis("bar", [10, 20])
line = Line().add_xaxis(["A", "B"]).add_yaxis("line", [5, 15])

grid = (
    Grid()
    .add(bar, grid_opts=opts.GridOpts(pos_left="5%", pos_right="55%"))
    .add(line, grid_opts=opts.GridOpts(pos_left="50%", pos_right="5%"))
    .set_global_opts(title_opts=opts.TitleOpts(title="Grid Combination Example"))
)
```

### Page - Sequential Multi-Chart Page

```python
from pyecharts import options as opts
from pyecharts.charts import Page, Bar, Line

bar = Bar().add_xaxis(["A"]).add_yaxis("bar", [10])
line = Line().add_xaxis(["A"]).add_yaxis("line", [5])

page = Page(layout=Page.SimplePageLayout).add(bar).add(line)
```

### Tab - Tabbed Multi-Chart View

```python
from pyecharts import options as opts
from pyecharts.charts import Tab, Bar, Line

bar = Bar().add_xaxis(["A"]).add_yaxis("bar", [10])
line = Line().add_xaxis(["A"]).add_yaxis("line", [5])

tab = Tab()
tab.add(bar, "Bar Chart")
tab.add(line, "Line Chart")
```

### Timeline - Timeline Carousel Chart

```python
from pyecharts import options as opts
from pyecharts.charts import Timeline, Bar

timeline = Timeline()
for i in range(2014, 2018):
    bar = Bar().add_xaxis(["A", "B"]).add_yaxis("data", [10, 20])
    timeline.add(bar, f"{i}")
```

---

## 3D Charts

### Bar3D - 3D Bar Chart

```python
from pyecharts import options as opts
from pyecharts.charts import Bar3D

bar3d = (
    Bar3D()
    .add(
        "3D Bars",
        [[x, y, z] for x in range(10) for y in range(10) for z in range(5)],
        xaxis3d_opts=opts.Axis3DOpts(type_="category"),
        yaxis3d_opts=opts.Axis3DOpts(type_="category"),
        grid3d_opts=opts.Grid3DOpts(width=100, height=100, depth=100),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="3D Bar Chart Example"))
)
```

### Line3D - 3D Line Chart

```python
from pyecharts import options as opts
from pyecharts.charts import Line3D
import math

data = [[math.sin(t / 10), math.cos(t / 10), t / 10] for t in range(0, 100)]

line3d = (
    Line3D()
    .add(
        "",
        data,
        line3d_opts=opts.Line3DOpts(magnitude=3),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="3D Line Chart Example"))
)
```

### Scatter3D - 3D Scatter Chart

```python
from pyecharts import options as opts
from pyecharts.charts import Scatter3D
import random

data = [
    [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)]
    for _ in range(80)
]

scatter3d = (
    Scatter3D()
    .add("", data)
    .set_global_opts(title_opts=opts.TitleOpts(title="3D Scatter Chart Example"))
)
```

### Surface3D - 3D Surface Chart

```python
from pyecharts import options as opts
from pyecharts.charts import Surface3D
import math

data = [[x, y, math.sin(x) * math.cos(y)] for x in range(-5, 5) for y in range(-5, 5)]

surface3d = (
    Surface3D()
    .add("", data)
    .set_global_opts(title_opts=opts.TitleOpts(title="3D Surface Chart Example"))
)
```

### Lines3D - 3D Trajectory Lines

```python
from pyecharts import options as opts
from pyecharts.charts import Lines3D

lines3d = (
    Lines3D()
    .add(
        "Trajectory",
        [[[x, x**2, 0] for x in range(-5, 5)]],
        line3d_opts=opts.Lines3DEffectOpts(),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="3D Trajectory Example"))
)
```

### Map3D - 3D Map

```python
from pyecharts import options as opts
from pyecharts.charts import Map3D

map3d = (
    Map3D()
    .add_schema()
    .add(
        "Data",
        [("China", 100), ("United States", 50)],
        type_="bars3D",
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="3D Map Example"))
)
```

### MapGlobe - Globe Chart

```python
from pyecharts import options as opts
from pyecharts.charts import MapGlobe

map_globe = (
    MapGlobe()
    .add_schema()
    .add(
        "Data",
        [("China", 100), ("United States", 80)],
        type_="bars3D",
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="Globe Chart Example"))
)
```

### GraphGL - 3D Graph Chart

```python
from pyecharts import options as opts
from pyecharts.charts import GraphGL

graph_gl = (
    GraphGL()
    .add(
        "",
        nodes=[{"name": "Node 1", "value": 10}],
        links=[{"source": "Node 1", "target": "Node 2"}],
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="3D Graph Example"))
)
```
