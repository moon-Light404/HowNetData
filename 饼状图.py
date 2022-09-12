# -*- coding: utf-8 -*-
# @Project: PythonFile
# @Author: dingjun
# @File name: data3
# @Create time: 2021/12/25 20:56
# -*- coding: utf-8 -*-
# @Project: PythonFile
# @Author: dingjun
# @File name: data3
# @Create time: 2021/12/24 21:54

import pyecharts.options as opts
from pyecharts.charts import Pie, Page
import pandas as pd

df = pd.read_excel("F:\\PythonFile\\BigWork\\other\\da.xlsx")
df.rename(columns={'文章类型': 'type'}, inplace=True)  # 列重命名
innerDf = df['专辑']  # 内部数据统计专辑类型


def get_inner_data():
    df['num'] = 1
    df1 = df.groupby(['type'])['num'].sum()
    print("out_data-----", df1)
    return df1


def get_out_data():
    sub_list = {}
    for sub_name in innerDf:
        if sub_name not in sub_list:
            sub_list[sub_name] = 1
        else:
            sub_list[sub_name] += 1
    print("sub_list:----", sub_list)
    return sub_list


def get_value():
    value = []
    out_data = get_out_data()
    for dict_value in out_data.values():
        value.append(dict_value)
    return value


inner_x_data = ["中国会议", "博士", "国际会议", "报纸", "期刊", "硕士", "科技成果", "视频", "辑刊"]
inner_y_data = get_inner_data()
inner_data_pair = [list(z) for z in zip(inner_x_data, inner_y_data)]

outer_x_data = ["社会科学", "哲学与人文科学", "信息科技", "工程科技", "经济与管理科学", "医药卫生科技", "基础科学", "农业科技"]
outer_y_data = get_value()
outer_data_pair = [list(z) for z in zip(outer_x_data, outer_y_data)]


def first_pie():
    c = (
        Pie(init_opts=opts.InitOpts(width="1600px", height="800px"))
            .add(
            series_name="研究领域",
            radius=["40%", "55%"],
            data_pair=outer_data_pair,
            label_opts=opts.LabelOpts(
                position="outside",
                formatter="{a|{a}}{abg|}\n{hr|}\n {b|{b}: }{c}  {per|{d}%}  ",
                background_color="#eee",
                border_color="#aaa",
                border_width=1,
                border_radius=4,
                rich={
                    "a": {"color": "#999", "lineHeight": 22, "align": "center"},
                    "abg": {
                        "backgroundColor": "#e3e3e3",
                        "width": "100%",
                        "align": "right",
                        "height": 22,
                        "borderRadius": [4, 4, 0, 0],
                    },
                    "hr": {
                        "borderColor": "#aaa",
                        "width": "100%",
                        "borderWidth": 0.5,
                        "height": 0,
                    },
                    "b": {"fontSize": 16, "lineHeight": 33},
                    "per": {
                        "color": "#eee",
                        "backgroundColor": "#334455",
                        "padding": [2, 4],
                        "borderRadius": 2,
                    },
                },
            ),
        )
            .set_global_opts(legend_opts=opts.LegendOpts(pos_left="left", orient="vertical"))
            .set_series_opts(
            tooltip_opts=opts.TooltipOpts(
                trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
            )
        )
    )
    return c


def second_pie():
    d = (
        Pie(init_opts=opts.InitOpts(width="1600px", height="800px"))
            .add(
            series_name="论文类型",
            radius=["40%", "55%"],
            data_pair=inner_data_pair,
            label_opts=opts.LabelOpts(
                position="outside",
                formatter="{a|{a}}{abg|}\n{hr|}\n {b|{b}: }{c}  {per|{d}%}  ",
                background_color="#eee",
                border_color="#aaa",
                border_width=1,
                border_radius=4,
                rich={
                    "a": {"color": "#999", "lineHeight": 22, "align": "center"},
                    "abg": {
                        "backgroundColor": "#e3e3e3",
                        "width": "100%",
                        "align": "right",
                        "height": 22,
                        "borderRadius": [4, 4, 0, 0],
                    },
                    "hr": {
                        "borderColor": "#aaa",
                        "width": "100%",
                        "borderWidth": 0.5,
                        "height": 0,
                    },
                    "b": {"fontSize": 16, "lineHeight": 33},
                    "per": {
                        "color": "#eee",
                        "backgroundColor": "#334455",
                        "padding": [2, 4],
                        "borderRadius": 2,
                    },
                },
            ),
        )
            .set_global_opts(legend_opts=opts.LegendOpts(pos_left="left", orient="vertical"))
            .set_series_opts(
            tooltip_opts=opts.TooltipOpts(
                trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
            )
        )
    )
    return d


page = Page(layout=Page.SimplePageLayout)
page.add(
    first_pie(),
    second_pie(),
)
page.render("全国不同文章类型饼状图.html")
