#!/usr/bin/env python3
"""
Minimal pyecharts chart generator for creating sample charts.

The generated examples are intended as quick starting points. Some chart types,
especially map-based charts, require optional dependencies, map assets, or API keys.

Usage:
    python generate_chart.py [chart_type] [output_file]

Examples:
    python generate_chart.py bar output.html
    python generate_chart.py line line_chart.html

If `output_file` is omitted, the script writes to `<chart_type>_chart.html`.
"""

import math
import random
import sys

from pyecharts import options as opts
from pyecharts.charts import (
    AMap,
    Bar,
    Bar3D,
    BMap,
    Boxplot,
    Calendar,
    Chord,
    Custom,
    EffectScatter,
    Funnel,
    Gauge,
    Geo,
    GMap,
    Graph,
    GraphGL,
    Grid,
    HeatMap,
    Kline,
    Line,
    Line3D,
    Lines3D,
    Liquid,
    LMap,
    Map,
    Map3D,
    MapGlobe,
    Page,
    Parallel,
    PictorialBar,
    Pie,
    Polar,
    Radar,
    Sankey,
    Scatter,
    Scatter3D,
    Sunburst,
    Surface3D,
    Tab,
    ThemeRiver,
    Timeline,
    Tree,
    TreeMap,
    WordCloud,
)

PRODUCTS = ["Shirts", "Sweaters", "Ties", "Pants", "Coats", "Heels", "Socks"]
WEEKDAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
HOURS = ["12a", "1a", "2a", "3a", "4a", "5a", "6a", "7a", "8a", "9a"]
SERIES_A = [114, 55, 27, 101, 125, 27, 105]
SERIES_B = [57, 134, 137, 129, 145, 60, 49]


# ==================== Basic Charts ====================


def create_bar(output="bar_chart.html"):
    """Create a bar chart."""
    bar = (
        Bar()
        .add_xaxis(PRODUCTS)
        .add_yaxis("Store A", SERIES_A)
        .add_yaxis("Store B", SERIES_B)
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar Chart Example"))
    )
    bar.render(output)
    print(f"Bar chart generated: {output}")


def create_line(output="line_chart.html"):
    """Create a line chart."""
    line = (
        Line()
        .add_xaxis(WEEKDAYS)
        .add_yaxis("Sales", [120, 200, 150, 80, 70, 110, 130])
        .set_global_opts(title_opts=opts.TitleOpts(title="Line Chart Example"))
    )
    line.render(output)
    print(f"Line chart generated: {output}")


def create_pie(output="pie_chart.html"):
    """Create a pie chart."""
    pie = (
        Pie()
        .add("Products", list(zip(PRODUCTS, SERIES_A)), radius=["40%", "75%"])
        .set_global_opts(title_opts=opts.TitleOpts(title="Pie Chart Example"))
    )
    pie.render(output)
    print(f"Pie chart generated: {output}")


def create_scatter(output="scatter_chart.html"):
    """Create a scatter chart."""
    scatter = (
        Scatter()
        .add_xaxis(WEEKDAYS)
        .add_yaxis("Units Sold", [120, 200, 150, 80, 70, 110, 130])
        .set_global_opts(title_opts=opts.TitleOpts(title="Scatter Chart Example"))
    )
    scatter.render(output)
    print(f"Scatter chart generated: {output}")


def create_effectscatter(output="effectscatter_chart.html"):
    """Create an effect scatter chart."""
    effect_scatter = (
        EffectScatter()
        .add_xaxis(WEEKDAYS)
        .add_yaxis("Units Sold", [120, 200, 150, 80, 70, 110, 130])
        .set_global_opts(title_opts=opts.TitleOpts(title="Effect Scatter Example"))
    )
    effect_scatter.render(output)
    print(f"Effect scatter chart generated: {output}")


def create_map(output="map_chart.html"):
    """Create a map chart."""
    map_chart = (
        Map()
        .add(
            "Data",
            [("China", 100), ("United States", 50), ("Canada", 60), ("Brazil", 40)],
            "world",
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="Map Example"))
    )
    map_chart.render(output)
    print(f"Map chart generated: {output}")


def create_geo(output="geo_chart.html"):
    """Create a geo chart."""
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
    geo.render(output)
    print(f"Geo chart generated: {output}")


def create_graph(output="graph_chart.html"):
    """Create a graph chart."""
    nodes = [{"name": "Node 1"}, {"name": "Node 2"}, {"name": "Node 3"}]
    links = [
        {"source": "Node 1", "target": "Node 2"},
        {"source": "Node 2", "target": "Node 3"},
    ]
    graph = Graph().add("", nodes, links, repulsion=8000)
    graph.set_global_opts(title_opts=opts.TitleOpts(title="Graph Example"))
    graph.render(output)
    print(f"Graph chart generated: {output}")


def create_heatmap(output="heatmap_chart.html"):
    """Create a heat map."""
    data = [[i, j, random.randint(0, 100)] for i in range(7) for j in range(10)]
    heatmap = (
        HeatMap()
        .add_xaxis(WEEKDAYS)
        .add_yaxis("Time", HOURS, data)
        .set_global_opts(title_opts=opts.TitleOpts(title="Heat Map Example"))
    )
    heatmap.render(output)
    print(f"Heat map generated: {output}")


def create_boxplot(output="boxplot_chart.html"):
    """Create a box plot."""
    data = [[random.randint(1, 100) for _ in range(6)] for _ in range(3)]
    boxplot = (
        Boxplot()
        .add_xaxis(["Category A", "Category B", "Category C"])
        .add_yaxis("Data", data)
        .set_global_opts(title_opts=opts.TitleOpts(title="Box Plot Example"))
    )
    boxplot.render(output)
    print(f"Box plot generated: {output}")


def create_kline(output="kline_chart.html"):
    """Create a candlestick chart."""
    data = [
        [2320.26, 2320.26, 2287.3, 2362.94],
        [2300, 2291.3, 2288.26, 2308.38],
        [2320.26, 2320.26, 2287.3, 2362.94],
    ]
    kline = (
        Kline()
        .add_xaxis(["2024-01-01", "2024-01-02", "2024-01-03"])
        .add_yaxis("Kline", data)
        .set_global_opts(title_opts=opts.TitleOpts(title="Candlestick Chart Example"))
    )
    kline.render(output)
    print(f"Candlestick chart generated: {output}")


def create_gauge(output="gauge_chart.html"):
    """Create a gauge chart."""
    gauge = (
        Gauge()
        .add("Completion", [("Completion", 75)])
        .set_global_opts(title_opts=opts.TitleOpts(title="Gauge Example"))
    )
    gauge.render(output)
    print(f"Gauge chart generated: {output}")


def create_funnel(output="funnel_chart.html"):
    """Create a funnel chart."""
    funnel = (
        Funnel()
        .add(
            "Conversion",
            [("Visit", 100), ("Inquiry", 60), ("Order", 40), ("Payment", 20)],
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="Funnel Chart Example"))
    )
    funnel.render(output)
    print(f"Funnel chart generated: {output}")


def create_radar(output="radar_chart.html"):
    """Create a radar chart."""
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
    radar.render(output)
    print(f"Radar chart generated: {output}")


def create_polar(output="polar_chart.html"):
    """Create a polar chart."""
    polar = (
        Polar()
        .add_schema(angleaxis_opts=opts.AngleAxisOpts(data=["Mon", "Tue", "Wed"]))
        .add("Data", [1, 2, 3], type_="bar")
        .set_global_opts(title_opts=opts.TitleOpts(title="Polar Chart Example"))
    )
    polar.render(output)
    print(f"Polar chart generated: {output}")


def create_wordcloud(output="wordcloud_chart.html"):
    """Create a word cloud."""
    wordcloud = (
        WordCloud()
        .add(
            words=[("Python", 100), ("ECharts", 80), ("Visualization", 60)],
            word_size_range=[20, 50],
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="Word Cloud Example"))
    )
    wordcloud.render(output)
    print(f"Word cloud generated: {output}")


def create_liquid(output="liquid_chart.html"):
    """Create a liquid fill chart."""
    liquid = (
        Liquid()
        .add("lq", [0.6, 0.7])
        .set_global_opts(title_opts=opts.TitleOpts(title="Liquid Fill Example"))
    )
    liquid.render(output)
    print(f"Liquid fill chart generated: {output}")


def create_sunburst(output="sunburst_chart.html"):
    """Create a sunburst chart."""
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
    sunburst.render(output)
    print(f"Sunburst chart generated: {output}")


def create_tree(output="tree_chart.html"):
    """Create a tree chart."""
    tree = (
        Tree()
        .add(
            "tree",
            [{"name": "Root", "children": [{"name": "Child 1"}, {"name": "Child 2"}]}],
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="Tree Chart Example"))
    )
    tree.render(output)
    print(f"Tree chart generated: {output}")


def create_treemap(output="treemap_chart.html"):
    """Create a treemap chart."""
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
    treemap.render(output)
    print(f"Treemap chart generated: {output}")


def create_themeriver(output="themeriver_chart.html"):
    """Create a theme river chart."""
    theme_river = (
        ThemeRiver()
        .add(
            ["Theme A", "Theme B", "Theme C"],
            [["2024-01", 10, 20], ["2024-02", 15, 25]],
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="Theme River Example"))
    )
    theme_river.render(output)
    print(f"Theme river chart generated: {output}")


def create_sankey(output="sankey_chart.html"):
    """Create a sankey diagram."""
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
    sankey.render(output)
    print(f"Sankey chart generated: {output}")


def create_chord(output="chord_chart.html"):
    """Create a chord diagram."""
    chord = (
        Chord()
        .add(
            schema=[{"name": "A"}, {"name": "B"}, {"name": "C"}],
            matrix=[[0, 10, 20], [10, 0, 30], [20, 30, 0]],
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="Chord Diagram Example"))
    )
    chord.render(output)
    print(f"Chord chart generated: {output}")


def create_parallel(output="parallel_chart.html"):
    """Create a parallel coordinates chart."""
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
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Parallel Coordinates Example")
        )
    )
    parallel.render(output)
    print(f"Parallel coordinates chart generated: {output}")


def create_pictorialbar(output="pictorialbar_chart.html"):
    """Create a pictorial bar chart."""
    pictorial_bar = (
        PictorialBar()
        .add_xaxis(["A", "B", "C"])
        .add_yaxis("Data", [10, 20, 30], symbol="circle")
        .set_global_opts(title_opts=opts.TitleOpts(title="Pictorial Bar Example"))
    )
    pictorial_bar.render(output)
    print(f"Pictorial bar chart generated: {output}")


def create_calendar(output="calendar_chart.html"):
    """Create a calendar chart."""
    calendar = (
        Calendar()
        .add(
            "",
            [["2024-01-01", 10], ["2024-01-02", 20]],
            calendar_opts=opts.CalendarOpts(range_="2024"),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="Calendar Chart Example"))
    )
    calendar.render(output)
    print(f"Calendar chart generated: {output}")


# ==================== Composite Charts ====================


def create_grid(output="grid_chart.html"):
    """Create a grid chart."""
    bar = Bar().add_xaxis(PRODUCTS).add_yaxis("Bar", SERIES_A)
    line = Line().add_xaxis(PRODUCTS).add_yaxis("Line", SERIES_B)

    grid = Grid()
    grid.add(bar, grid_opts=opts.GridOpts(pos_left="5%", pos_right="55%"))
    grid.add(line, grid_opts=opts.GridOpts(pos_left="50%", pos_right="5%"))
    grid.render(output)
    print(f"Grid chart generated: {output}")


def create_page(output="page_chart.html"):
    """Create a sequential multi-chart page."""
    bar = Bar().add_xaxis(PRODUCTS).add_yaxis("Bar", SERIES_A)
    line = Line().add_xaxis(PRODUCTS).add_yaxis("Line", SERIES_B)

    page = Page(layout=Page.SimplePageLayout)
    page.add(bar)
    page.add(line)
    page.render(output)
    print(f"Page chart generated: {output}")


def create_tab(output="tab_chart.html"):
    """Create a tabbed multi-chart view."""
    bar = Bar().add_xaxis(PRODUCTS).add_yaxis("Bar", SERIES_A)
    line = Line().add_xaxis(PRODUCTS).add_yaxis("Line", SERIES_B)

    tab = Tab()
    tab.add(bar, "Bar Chart")
    tab.add(line, "Line Chart")
    tab.render(output)
    print(f"Tab chart generated: {output}")


def create_timeline(output="timeline_chart.html"):
    """Create a timeline carousel chart."""
    timeline = Timeline()
    for year in range(2020, 2024):
        bar = (
            Bar()
            .add_xaxis(PRODUCTS)
            .add_yaxis("Store A", SERIES_A)
            .set_global_opts(title_opts=opts.TitleOpts(title=f"{year} Sales Data"))
        )
        timeline.add(bar, f"{year}")
    timeline.render(output)
    print(f"Timeline chart generated: {output}")


# ==================== 3D Charts ====================


def create_bar3d(output="bar3d_chart.html"):
    """Create a 3D bar chart."""
    data = [[i, j, random.randint(0, 10)] for i in range(10) for j in range(10)]

    bar3d = (
        Bar3D()
        .add(
            "3D Bars",
            data,
            xaxis3d_opts=opts.Axis3DOpts(type_="category"),
            yaxis3d_opts=opts.Axis3DOpts(type_="category"),
            grid3d_opts=opts.Grid3DOpts(width=100, height=100, depth=100),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="3D Bar Chart Example"))
    )
    bar3d.render(output)
    print(f"3D bar chart generated: {output}")


def create_line3d(output="line3d_chart.html"):
    """Create a 3D line chart."""
    data = [[math.sin(t / 10), math.cos(t / 10), t / 10] for t in range(0, 100)]

    line3d = (
        Line3D()
        .add("", data, line3d_opts=opts.Line3DOpts(magnitude=3))
        .set_global_opts(title_opts=opts.TitleOpts(title="3D Line Chart Example"))
    )
    line3d.render(output)
    print(f"3D line chart generated: {output}")


def create_scatter3d(output="scatter3d_chart.html"):
    """Create a 3D scatter chart."""
    data = [
        [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)]
        for _ in range(80)
    ]

    scatter3d = (
        Scatter3D()
        .add("", data)
        .set_global_opts(title_opts=opts.TitleOpts(title="3D Scatter Chart Example"))
    )
    scatter3d.render(output)
    print(f"3D scatter chart generated: {output}")


def create_surface3d(output="surface3d_chart.html"):
    """Create a 3D surface chart."""
    data = [
        [x, y, math.sin(x) * math.cos(y)] for x in range(-5, 5) for y in range(-5, 5)
    ]

    surface3d = (
        Surface3D()
        .add("", data)
        .set_global_opts(title_opts=opts.TitleOpts(title="3D Surface Chart Example"))
    )
    surface3d.render(output)
    print(f"3D surface chart generated: {output}")


def create_lines3d(output="lines3d_chart.html"):
    """Create 3D trajectory lines."""
    lines3d = (
        Lines3D()
        .add(
            "Trajectory",
            [[[x, x**2, 0] for x in range(-5, 5)]],
            line3d_opts=opts.Lines3DEffectOpts(),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="3D Trajectory Example"))
    )
    lines3d.render(output)
    print(f"3D trajectory chart generated: {output}")


def create_map3d(output="map3d_chart.html"):
    """Create a 3D map."""
    map3d = (
        Map3D()
        .add_schema()
        .add("Data", [("China", 100), ("United States", 50)], type_="bars3D")
        .set_global_opts(title_opts=opts.TitleOpts(title="3D Map Example"))
    )
    map3d.render(output)
    print(f"3D map generated: {output}")


def create_mapglobe(output="mapglobe_chart.html"):
    """Create a globe chart."""
    map_globe = (
        MapGlobe()
        .add_schema()
        .add("Data", [("China", 100), ("United States", 80)], type_="bars3D")
        .set_global_opts(title_opts=opts.TitleOpts(title="Globe Chart Example"))
    )
    map_globe.render(output)
    print(f"Globe chart generated: {output}")


def create_graphgl(output="graphgl_chart.html"):
    """Create a 3D graph chart."""
    graph_gl = (
        GraphGL()
        .add(
            "",
            nodes=[{"name": "Node 1", "value": 10}, {"name": "Node 2", "value": 6}],
            links=[{"source": "Node 1", "target": "Node 2"}],
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="3D Graph Example"))
    )
    graph_gl.render(output)
    print(f"3D graph chart generated: {output}")


# ==================== Map Series ====================


def create_bmap(output="bmap_chart.html"):
    """Create a Baidu Map chart."""
    bmap = (
        BMap()
        .add_schema(baidu_ak="YOUR_BAIDU_AK", center=[116.40, 39.90], zoom=10)
        .add("Data", [("Tiananmen Square", [116.40, 39.90])])
        .set_global_opts(title_opts=opts.TitleOpts(title="Baidu Map Example"))
    )
    bmap.render(output)
    print(f"Baidu Map chart generated: {output}")


def create_amap(output="amap_chart.html"):
    """Create an AMap chart."""
    amap = (
        AMap()
        .add_schema(amap_ak="YOUR_AMAP_AK", center=[116.40, 39.90], zoom=10)
        .add("Data", [("Tiananmen Square", [116.40, 39.90])])
        .set_global_opts(title_opts=opts.TitleOpts(title="AMap Example"))
    )
    amap.render(output)
    print(f"AMap chart generated: {output}")


def create_gmap(output="gmap_chart.html"):
    """Create a Google Map chart."""
    gmap = (
        GMap()
        .add("Data", [("China", 100), ("USA", 80)], "world")
        .set_global_opts(title_opts=opts.TitleOpts(title="GMap Example"))
    )
    gmap.render(output)
    print(f"GMap chart generated: {output}")


def create_lmap(output="lmap_chart.html"):
    """Create a Leaflet map chart."""
    lmap = (
        LMap()
        .add("Data", [("Beijing", [39.90, 116.40])])
        .set_global_opts(title_opts=opts.TitleOpts(title="Leaflet Map Example"))
    )
    lmap.render(output)
    print(f"Leaflet map chart generated: {output}")


# ==================== Custom Charts (ECharts 6) ====================


def create_custom(output="custom_chart.html"):
    """Create a custom chart."""
    custom = (
        Custom()
        .add_xaxis(["A", "B", "C"])
        .add_yaxis("Data", [[10, 20], [20, 30], [30, 40]])
        .set_global_opts(title_opts=opts.TitleOpts(title="Custom Chart Example"))
    )
    custom.render(output)
    print(f"Custom chart generated: {output}")


def main():
    chart_funcs = {
        # Basic charts
        "bar": create_bar,
        "line": create_line,
        "pie": create_pie,
        "scatter": create_scatter,
        "effectscatter": create_effectscatter,
        "map": create_map,
        "geo": create_geo,
        "graph": create_graph,
        "heatmap": create_heatmap,
        "boxplot": create_boxplot,
        "kline": create_kline,
        "gauge": create_gauge,
        "funnel": create_funnel,
        "radar": create_radar,
        "polar": create_polar,
        "wordcloud": create_wordcloud,
        "liquid": create_liquid,
        "sunburst": create_sunburst,
        "tree": create_tree,
        "treemap": create_treemap,
        "themeriver": create_themeriver,
        "sankey": create_sankey,
        "chord": create_chord,
        "parallel": create_parallel,
        "pictorialbar": create_pictorialbar,
        "calendar": create_calendar,
        "custom": create_custom,
        # Composite charts
        "grid": create_grid,
        "page": create_page,
        "tab": create_tab,
        "timeline": create_timeline,
        # 3D charts
        "bar3d": create_bar3d,
        "line3d": create_line3d,
        "scatter3d": create_scatter3d,
        "surface3d": create_surface3d,
        "lines3d": create_lines3d,
        "map3d": create_map3d,
        "mapglobe": create_mapglobe,
        "graphgl": create_graphgl,
        # Map series
        "bmap": create_bmap,
        "amap": create_amap,
        "gmap": create_gmap,
        "lmap": create_lmap,
    }

    if len(sys.argv) < 2:
        print(__doc__)
        print("\nSupported chart types:")
        for name in sorted(chart_funcs.keys()):
            print(f"  - {name}")
        return

    chart_type = sys.argv[1].lower()
    output = sys.argv[2] if len(sys.argv) > 2 else f"{chart_type}_chart.html"

    if chart_type in chart_funcs:
        chart_funcs[chart_type](output)
    else:
        print(f"Unsupported chart type: {chart_type}")
        print("\nSupported chart types:")
        for name in sorted(chart_funcs.keys()):
            print(f"  - {name}")
        sys.exit(1)


if __name__ == "__main__":
    main()
