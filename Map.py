# -*- coding: utf-8 -*-
# @Project: PythonFile
# @Author: dingjun
# @File name: Any4
# @Create time: 2021/12/26 19:45
import pyecharts.options as opts
from pyecharts.globals import ThemeType
from pyecharts.commons.utils import JsCode
from pyecharts.charts import Timeline, Grid, Bar, Map, Pie
import pandas as pd

# 获取数据函数
df = pd.read_excel("F:\\PythonFile\\BigWork\\other\\da.xlsx")
df1 = df[~(df['from'].isnull())]  # 去除地区为空的行
df1 = df1.rename(columns={'time': 'date'})  # 重命名列名为date
s_day = '2012-01-01'
df1 = df1[df1['date'] >= s_day]
df1['num'] = 1
#
dateDf = df1.groupby([df1['date'].apply(lambda x: x.year), df1['from']])['num'].sum()  # 按照年份和地区分了
date_year = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
area_name = ['上海', '云南', '内蒙古', '北京', '吉林', '四川', '天津', '宁夏',
             '安徽', '山东', '山西', '广东', '广西', '新疆', '江苏', '江西',
             '河北', '河南', '浙江', '海南', '湖北', '湖南', '甘肃', '福建',
             '西藏', '贵州', '辽宁', '重庆', '陕西', '青海', '黑龙江']
#
#
# 获得某一年各省份对应的数据
def get_year_list(year):
    All_area = []
    for area in area_name:
        year_list = []
        print(dateDf.loc[(year, area)], end=" ")
        year_list.append(dateDf[(year, area)])  # 这一年的30多个省份的论文数量
        year_list.append(area)  # 添加地方名称到列表中
        All_area.append(year_list)
    return All_area  # 返回今年所有地区的论文数量
#
#
# 获得近10年的数据
def get_dict():
    All_data = []
    for i in range(2012, 2022):  # 遍历10年
        data_list = []
        area_data = get_year_list(i)  # 今年的数据
        for j, area in enumerate(area_name):
            data_dict = {"name": area, "value": area_data[j]}
            data_list.append(data_dict)
        All_data.append(data_list)
    return All_data
#
#
data1 = []


def get_data():
    All_Data = get_dict()  # 获取所有画地图所需要的数据
    for i, year in enumerate(date_year):
        data_dict = {"time": year, "data": All_Data[i]}
        data1.append(data_dict)




def get_year_chart(year: int):
    map_data = [
        [[x["name"], x["value"]] for x in d["data"]] for d in data1 if d["time"] == year
    ][0]
    min_data, max_data = (
        min([d[1][0] for d in map_data]),
        max([d[1][0] for d in map_data]),
    )
    map_chart = (
        Map()
            .add(
            series_name="",
            data_pair=map_data,
            label_opts=opts.LabelOpts(is_show=False),
            is_map_symbol_show=False,
            itemstyle_opts={
                "normal": {"areaColor": "#323c48", "borderColor": "#404a59"},
                "emphasis": {
                    "label": {"show": Timeline},
                    "areaColor": "rgba(255,255,255, 0.5)",
                },
            },
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="近10年以来全国高校文分布情况",
                subtitle="GDP单位:亿元",
                pos_left="center",
                pos_top="top",
                title_textstyle_opts=opts.TextStyleOpts(
                    font_size=25, color="rgba(255,255,255, 0.9)"
                ),
            ),
            tooltip_opts=opts.TooltipOpts(
                is_show=True,
                formatter=JsCode(
                    """function(params) {
                    if ('value' in params.data) {
                        return params.data.value[2] + ': ' + params.data.value[0];
                    }
                }"""
                ),
            ),
            visualmap_opts=opts.VisualMapOpts(
                is_calculable=True,
                dimension=0,
                pos_left="10",
                pos_top="center",
                range_text=["High", "Low"],
                range_color=["lightskyblue", "yellow", "orangered"],
                textstyle_opts=opts.TextStyleOpts(color="#ddd"),
                min_=min_data,
                max_=max_data,
            ),
        )
    )

    bar_x_data = [x[0] for x in map_data]

    # 这里注释的部分会导致 label 和 value 与 饼图不一致
    # 使用下面的 List[Dict] 就可以解决这个问题了。
    # bar_y_data = [x[1][0] for x in map_data]
    bar_y_data = [{"name": x[0], "value": x[1][0]} for x in map_data]
    bar = (
        Bar()
            .add_xaxis(xaxis_data=bar_x_data)
            .add_yaxis(
            series_name="",
            yaxis_index=1,
            y_axis=bar_y_data,
            label_opts=opts.LabelOpts(
                is_show=True, position="right", formatter="{b}: {c}"
            ),
        )
            .reversal_axis()
            .set_global_opts(
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(is_show=False)),
            yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(is_show=False)),
            tooltip_opts=opts.TooltipOpts(is_show=False),
            visualmap_opts=opts.VisualMapOpts(
                is_calculable=True,
                dimension=0,
                pos_left="10",
                pos_top="center",
                range_text=["High", "Low"],
                range_color=["lightskyblue", "yellow", "orangered"],
                textstyle_opts=opts.TextStyleOpts(color="#ddd"),
                min_=min_data,
                max_=max_data,
            ),
            graphic_opts=[
                opts.GraphicGroup(
                    graphic_item=opts.GraphicItem(
                        rotation=JsCode("Math.PI / 4"),
                        bounding="raw",
                        right=110,
                        bottom=110,
                        z=100,
                    ),
                    children=[
                        opts.GraphicRect(
                            graphic_item=opts.GraphicItem(left="center", top="center", z=100),
                            graphic_shape_opts=opts.GraphicShapeOpts(width=400, height=50),
                            graphic_basicstyle_opts=opts.GraphicBasicStyleOpts(
                                fill="rgba(0,0,0,0.3)"
                            ),
                        ),
                        opts.GraphicText(
                            graphic_item=opts.GraphicItem(left="center", top="center", z=100),
                            graphic_textstyle_opts=opts.GraphicTextStyleOpts(
                                text=f"{str(year)} 年",
                                font="bold 26px Microsoft YaHei",
                                graphic_basicstyle_opts=opts.GraphicBasicStyleOpts(fill="#fff"),
                            ),
                        ),
                    ],
                )
            ],
        )
    )

    grid_chart = (
        Grid()
            .add(
            bar,
            grid_opts=opts.GridOpts(
                pos_left="10", pos_right="45%", pos_top="70%", pos_bottom="5"
            ),
        )
            .add(map_chart, grid_opts=opts.GridOpts())
    )

    return grid_chart


# Draw Timeline
time_list = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
timeline = Timeline(
    init_opts=opts.InitOpts(width="1800px", height="900px", theme=ThemeType.DARK)
)
# get_data()
for y in time_list:
    g = get_year_chart(year=y)
    timeline.add(g, time_point=str(y))

timeline.add_schema(
    orient="vertical",
    is_auto_play=True,
    is_inverse=True,
    play_interval=5000,
    pos_left="null",
    pos_right="5",
    pos_top="20",
    pos_bottom="20",
    width="50",
    label_opts=opts.LabelOpts(is_show=True, color="#fff"),
)

# timeline.render("china_gdp_from_1980.html")
timeline.render("近10年全国论文分布地图.html")
