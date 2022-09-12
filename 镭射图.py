from pyecharts import options as opts
from pyecharts.charts import Radar

v1 = [[1050, 918,289,104,32,4]]
c = (
    Radar()
    .add_schema(
        schema=[
            opts.RadarIndicatorItem(name="期刊", max_=1500),
            opts.RadarIndicatorItem(name="硕士", max_=1500),
            opts.RadarIndicatorItem(name="中国会议", max_=500),
            opts.RadarIndicatorItem(name="博士", max_=200),
            opts.RadarIndicatorItem(name="国际会议", max_=50),
            opts.RadarIndicatorItem(name="辑刊", max_=10),
        ]
    )
    .add("文章类型", v1)
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        legend_opts=opts.LegendOpts(selected_mode="single"),
        title_opts=opts.TitleOpts(title="南昌大学论文文章类型"),
    )
    .render("ncdx.html")
)