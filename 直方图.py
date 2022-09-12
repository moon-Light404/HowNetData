# -*- coding: utf-8 -*-
# @Project: PythonFile
# @Author: dingjun
# @File name: Any32
# @Create time: 2021/12/25 19:10
import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import Bar, Line, Grid
# -----------------------------------------------
from pyecharts.globals import ThemeType

x_data = ["2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016",
          "2017", "2018", "2019", "2020", "2021"]

bar = (
    Bar(init_opts=opts.InitOpts(width="1600px", height="800px"))
        .add_xaxis(xaxis_data=x_data)
        .add_yaxis(
        series_name="博士",
        y_axis=[
            446, 512, 794, 1230, 2031, 2744, 2197, 2075, 2116, 1860, 2034, 2193, 2959, 2777, 2072, 4015, 4964, 4907,
            5206, 4538, 3190],
        label_opts=opts.LabelOpts(is_show=False, rotate=75),
    )
        .add_yaxis(
        series_name="期刊",
        y_axis=[1623, 1583, 2133, 2598, 2266, 4185, 5024, 4448, 5206, 5747, 6116, 5616, 5814, 6005, 6053, 5590, 5722,
                6415, 7454, 6878, 5339],
        label_opts=opts.LabelOpts(is_show=False, rotate=75),
    )
        .add_yaxis(
        series_name="硕士",
        y_axis=[650, 1070, 1180, 1779, 2760, 3718, 4548, 4533, 5726, 3892, 3712, 5102, 6778, 8092, 4641, 12887,
                18091, 18427, 23430, 24095, 11888],
        label_opts=opts.LabelOpts(is_show=False, rotate=75),
    )
        .extend_axis(
            yaxis=opts.AxisOpts(
                name="会议数量",
                type_="value",
                min_=0,
                max_=900,
                interval=200,
                axislabel_opts=opts.LabelOpts(formatter="{value} "),
            )
        )
        .set_global_opts(
        tooltip_opts=opts.TooltipOpts(
            is_show=True, trigger="axis", axis_pointer_type="cross"
        ),
        xaxis_opts=opts.AxisOpts(
            type_="category",
            axispointer_opts=opts.AxisPointerOpts(is_show=True, type_="shadow"),
        ),
        yaxis_opts=opts.AxisOpts(
            name="数量",
            type_="value",
            min_=0,
            max_=25000,
            interval=2000,
            axislabel_opts=opts.LabelOpts(formatter="{value} "),
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
    )
)
#
line = (
    Line()
    .add_xaxis(xaxis_data=x_data)
    .add_yaxis(
        series_name="中国会议",
        yaxis_index=1,
        is_smooth=True,  # 平滑曲线
        color="#d14a61",
        y_axis=[2, 31, 4, 52, 74, 60, 80, 54, 128, 271, 199, 210, 347, 623, 321, 342, 599, 859, 886, 469, 239],
        label_opts=opts.LabelOpts(is_show=False),
    )
    # .render("line_yaxis_log.html")
)
# [2, 31, 4, 52, 74, 60, 80, 54, 128, 271, 199, 210, 347, 623, 321, 342, 599, 859, 886, 469, 239]
bar.overlap(line).render("近20年来四种文章类型的数量.html")
# line.render("中国会议数量.html")



