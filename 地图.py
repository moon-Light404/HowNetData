import pyecharts.options as opts
from pyecharts.globals import ThemeType
from pyecharts.commons.utils import JsCode
from pyecharts.charts import Timeline, Grid, Bar, Map, Pie
data = [{'time': 2012,
         'data': [{'name': '上海', 'value': [2264, '上海']},
                  {'name': '云南', 'value': [67, '云南']},
                  {'name': '内蒙古', 'value': [75, '内蒙古']},
                  {'name': '北京', 'value': [2327, '北京']},
                  {'name': '吉林', 'value': [488, '吉林']},
                  {'name': '四川', 'value': [207, '四川']},
                  {'name': '天津', 'value': [465, '天津']},
                  {'name': '宁夏', 'value': [68, '宁夏']},
                  {'name': '安徽', 'value': [215, '安徽']},
                  {'name': '山东', 'value': [90, '山东']},
                  {'name': '山西', 'value': [428, '山西']},
                  {'name': '广东', 'value': [619, '广东']}, {'name': '广西', 'value': [114, '广西']}, {'name': '新疆', 'value': [132, '新疆']}, {'name': '江苏', 'value': [700, '江苏']}, {'name': '江西', 'value': [136, '江西']}, {'name': '河北', 'value': [58, '河北']}, {'name': '河南', 'value': [181, '河南']}, {'name': '浙江', 'value': [80, '浙江']}, {'name': '海南', 'value': [111, '海南']}, {'name': '湖北', 'value': [482, '湖北']}, {'name': '湖南', 'value': [1056, '湖南']}, {'name': '甘肃', 'value': [109, '甘肃']}, {'name': '福建', 'value': [192, '福建']}, {'name': '西藏', 'value': [30, '西藏']}, {'name': '贵州', 'value': [61, '贵州']}, {'name': '辽宁', 'value': [1087, '辽宁']}, {'name': '重庆', 'value': [349, '重庆']}, {'name': '陕西', 'value': [348, '陕西']}, {'name': '青海', 'value': [64, '青海']}, {'name': '黑龙江', 'value': [147, '黑龙江']}]}, {'time': 2013, 'data': [{'name': '上海', 'value': [3140, '上海']}, {'name': '云南', 'value': [55, '云南']}, {'name': '内蒙古', 'value': [92, '内蒙古']}, {'name': '北京', 'value': [2110, '北京']}, {'name': '吉林', 'value': [634, '吉林']}, {'name': '四川', 'value': [467, '四川']}, {'name': '天津', 'value': [497, '天津']}, {'name': '宁夏', 'value': [195, '宁夏']}, {'name': '安徽', 'value': [263, '安徽']}, {'name': '山东', 'value': [82, '山东']}, {'name': '山西', 'value': [453, '山西']}, {'name': '广东', 'value': [489, '广东']}, {'name': '广西', 'value': [125, '广西']}, {'name': '新疆', 'value': [469, '新疆']}, {'name': '江苏', 'value': [1013, '江苏']}, {'name': '江西', 'value': [107, '江西']}, {'name': '河北', 'value': [122, '河北']}, {'name': '河南', 'value': [198, '河南']}, {'name': '浙江', 'value': [84, '浙江']}, {'name': '海南', 'value': [62, '海南']}, {'name': '湖北', 'value': [473, '湖北']}, {'name': '湖南', 'value': [2027, '湖南']}, {'name': '甘肃', 'value': [104, '甘肃']}, {'name': '福建', 'value': [159, '福建']}, {'name': '西藏', 'value': [33, '西藏']}, {'name': '贵州', 'value': [73, '贵州']}, {'name': '辽宁', 'value': [804, '辽宁']}, {'name': '重庆', 'value': [312, '重庆']}, {'name': '陕西', 'value': [425, '陕西']}, {'name': '青海', 'value': [137, '青海']}, {'name': '黑龙江', 'value': [307, '黑龙江']}]}, {'time': 2014, 'data': [{'name': '上海', 'value': [3048, '上海']}, {'name': '云南', 'value': [50, '云南']}, {'name': '内蒙古', 'value': [74, '内蒙古']}, {'name': '北京', 'value': [1779, '北京']}, {'name': '吉林', 'value': [1040, '吉林']}, {'name': '四川', 'value': [201, '四川']}, {'name': '天津', 'value': [549, '天津']}, {'name': '宁夏', 'value': [960, '宁夏']}, {'name': '安徽', 'value': [284, '安徽']}, {'name': '山东', 'value': [75, '山东']}, {'name': '山西', 'value': [440, '山西']}, {'name': '广东', 'value': [688, '广东']}, {'name': '广西', 'value': [115, '广西']}, {'name': '新疆', 'value': [369, '新疆']}, {'name': '江苏', 'value': [994, '江苏']}, {'name': '江西', 'value': [131, '江西']}, {'name': '河北', 'value': [94, '河北']}, {'name': '河南', 'value': [236, '河南']}, {'name': '浙江', 'value': [94, '浙江']}, {'name': '海南', 'value': [368, '海南']}, {'name': '湖北', 'value': [321, '湖北']}, {'name': '湖南', 'value': [2062, '湖南']}, {'name': '甘肃', 'value': [123, '甘肃']}, {'name': '福建', 'value': [560, '福建']}, {'name': '西藏', 'value': [50, '西藏']}, {'name': '贵州', 'value': [91, '贵州']}, {'name': '辽宁', 'value': [1017, '辽宁']}, {'name': '重庆', 'value': [289, '重庆']}, {'name': '陕西', 'value': [473, '陕西']}, {'name': '青海', 'value': [183, '青海']}, {'name': '黑龙江', 'value': [332, '黑龙江']}]}, {'time': 2015, 'data': [{'name': '上海', 'value': [1602, '上海']}, {'name': '云南', 'value': [139, '云南']}, {'name': '内蒙古', 'value': [64, '内蒙古']}, {'name': '北京', 'value': [1813, '北京']}, {'name': '吉林', 'value': [381, '吉林']}, {'name': '四川', 'value': [270, '四川']}, {'name': '天津', 'value': [399, '天津']}, {'name': '宁夏', 'value': [227, '宁夏']}, {'name': '安徽', 'value': [97, '安徽']}, {'name': '山东', 'value': [86, '山东']}, {'name': '山西', 'value': [425, '山西']}, {'name': '广东', 'value': [380, '广东']}, {'name': '广西', 'value': [111, '广西']}, {'name': '新疆', 'value': [339, '新疆']}, {'name': '江苏', 'value': [886, '江苏']}, {'name': '江西', 'value': [170, '江西']}, {'name': '河北', 'value': [81, '河北']}, {'name': '河南', 'value': [160, '河南']}, {'name': '浙江', 'value': [92, '浙江']}, {'name': '海南', 'value': [591, '海南']}, {'name': '湖北', 'value': [343, '湖北']}, {'name': '湖南', 'value': [1130, '湖南']}, {'name': '甘肃', 'value': [170, '甘肃']}, {'name': '福建', 'value': [884, '福建']}, {'name': '西藏', 'value': [36, '西藏']}, {'name': '贵州', 'value': [388, '贵州']}, {'name': '辽宁', 'value': [759, '辽宁']}, {'name': '重庆', 'value': [262, '重庆']}, {'name': '陕西', 'value': [295, '陕西']}, {'name': '青海', 'value': [63, '青海']}, {'name': '黑龙江', 'value': [247, '黑龙江']}]}, {'time': 2016, 'data': [{'name': '上海', 'value': [4135, '上海']}, {'name': '云南', 'value': [225, '云南']}, {'name': '内蒙古', 'value': [109, '内蒙古']}, {'name': '北京', 'value': [2948, '北京']}, {'name': '吉林', 'value': [1102, '吉林']}, {'name': '四川', 'value': [238, '四川']}, {'name': '天津', 'value': [382, '天津']}, {'name': '宁夏', 'value': [1132, '宁夏']}, {'name': '安徽', 'value': [549, '安徽']}, {'name': '山东', 'value': [70, '山东']}, {'name': '山西', 'value': [421, '山西']}, {'name': '广东', 'value': [633, '广东']}, {'name': '广西', 'value': [112, '广西']}, {'name': '新疆', 'value': [285, '新疆']}, {'name': '江苏', 'value': [1478, '江苏']}, {'name': '江西', 'value': [129, '江西']}, {'name': '河北', 'value': [9, '河北']}, {'name': '河南', 'value': [439, '河南']}, {'name': '浙江', 'value': [123, '浙江']}, {'name': '海南', 'value': [1069, '海南']}, {'name': '湖北', 'value': [336, '湖北']}, {'name': '湖南', 'value': [925, '湖南']}, {'name': '甘肃', 'value': [240, '甘肃']}, {'name': '福建', 'value': [1504, '福建']}, {'name': '西藏', 'value': [46, '西藏']}, {'name': '贵州', 'value': [767, '贵州']}, {'name': '辽宁', 'value': [1184, '辽宁']}, {'name': '重庆', 'value': [654, '重庆']}, {'name': '陕西', 'value': [521, '陕西']}, {'name': '青海', 'value': [149, '青海']}, {'name': '黑龙江', 'value': [525, '黑龙江']}]}, {'time': 2017, 'data': [{'name': '上海', 'value': [3934, '上海']}, {'name': '云南', 'value': [1342, '云南']}, {'name': '内蒙古', 'value': [459, '内蒙古']}, {'name': '北京', 'value': [2529, '北京']}, {'name': '吉林', 'value': [1251, '吉林']}, {'name': '四川', 'value': [371, '四川']}, {'name': '天津', 'value': [487, '天津']}, {'name': '宁夏', 'value': [1362, '宁夏']}, {'name': '安徽', 'value': [540, '安徽']}, {'name': '山东', 'value': [116, '山东']}, {'name': '山西', 'value': [488, '山西']}, {'name': '广东', 'value': [695, '广东']}, {'name': '广西', 'value': [140, '广西']}, {'name': '新疆', 'value': [379, '新疆']}, {'name': '江苏', 'value': [1581, '江苏']}, {'name': '江西', 'value': [197, '江西']}, {'name': '河北', 'value': [76, '河北']}, {'name': '河南', 'value': [399, '河南']}, {'name': '浙江', 'value': [95, '浙江']}, {'name': '海南', 'value': [1515, '海南']}, {'name': '湖北', 'value': [532, '湖北']}, {'name': '湖南', 'value': [934, '湖南']}, {'name': '甘肃', 'value': [401, '甘肃']}, {'name': '福建', 'value': [3045, '福建']}, {'name': '西藏', 'value': [44, '西藏']}, {'name': '贵州', 'value': [1281, '贵州']}, {'name': '辽宁', 'value': [1620, '辽宁']}, {'name': '重庆', 'value': [722, '重庆']}, {'name': '陕西', 'value': [574, '陕西']}, {'name': '青海', 'value': [228, '青海']}, {'name': '黑龙江', 'value': [1559, '黑龙江']}]}, {'time': 2018, 'data': [{'name': '上海', 'value': [2438, '上海']}, {'name': '云南', 'value': [1847, '云南']}, {'name': '内蒙古', 'value': [1066, '内蒙古']}, {'name': '北京', 'value': [2917, '北京']}, {'name': '吉林', 'value': [1267, '吉林']}, {'name': '四川', 'value': [408, '四川']}, {'name': '天津', 'value': [484, '天津']}, {'name': '宁夏', 'value': [1237, '宁夏']}, {'name': '安徽', 'value': [546, '安徽']}, {'name': '山东', 'value': [133, '山东']}, {'name': '山西', 'value': [485, '山西']}, {'name': '广东', 'value': [544, '广东']}, {'name': '广西', 'value': [128, '广西']}, {'name': '新疆', 'value': [320, '新疆']}, {'name': '江苏', 'value': [3325, '江苏']}, {'name': '江西', 'value': [199, '江西']}, {'name': '河北', 'value': [99, '河北']}, {'name': '河南', 'value': [483, '河南']}, {'name': '浙江', 'value': [92, '浙江']}, {'name': '海南', 'value': [1754, '海南']}, {'name': '湖北', 'value': [509, '湖北']}, {'name': '湖南', 'value': [869, '湖南']}, {'name': '甘肃', 'value': [449, '甘肃']}, {'name': '福建', 'value': [2501, '福建']}, {'name': '西藏', 'value': [62, '西藏']}, {'name': '贵州', 'value': [1500, '贵州']}, {'name': '辽宁', 'value': [1376, '辽宁']}, {'name': '重庆', 'value': [746, '重庆']}, {'name': '陕西', 'value': [617, '陕西']}, {'name': '青海', 'value': [192, '青海']}, {'name': '黑龙江', 'value': [1503, '黑龙江']}]}, {'time': 2019, 'data': [{'name': '上海', 'value': [2400, '上海']}, {'name': '云南', 'value': [1320, '云南']}, {'name': '内蒙古', 'value': [1254, '内蒙古']}, {'name': '北京', 'value': [1781, '北京']}, {'name': '吉林', 'value': [1155, '吉林']}, {'name': '四川', 'value': [509, '四川']}, {'name': '天津', 'value': [1200, '天津']}, {'name': '宁夏', 'value': [1284, '宁夏']}, {'name': '安徽', 'value': [647, '安徽']}, {'name': '山东', 'value': [604, '山东']}, {'name': '山西', 'value': [477, '山西']}, {'name': '广东', 'value': [408, '广东']}, {'name': '广西', 'value': [740, '广西']}, {'name': '新疆', 'value': [2087, '新疆']}, {'name': '江苏', 'value': [4759, '江苏']}, {'name': '江西', 'value': [167, '江西']}, {'name': '河北', 'value': [25, '河北']}, {'name': '河南', 'value': [604, '河南']}, {'name': '浙江', 'value': [120, '浙江']}, {'name': '海南', 'value': [1490, '海南']}, {'name': '湖北', 'value': [1369, '湖北']}, {'name': '湖南', 'value': [652, '湖南']}, {'name': '甘肃', 'value': [474, '甘肃']}, {'name': '福建', 'value': [857, '福建']}, {'name': '西藏', 'value': [67, '西藏']}, {'name': '贵州', 'value': [1360, '贵州']}, {'name': '辽宁', 'value': [628, '辽宁']}, {'name': '重庆', 'value': [2605, '重庆']}, {'name': '陕西', 'value': [3804, '陕西']}, {'name': '青海', 'value': [289, '青海']}, {'name': '黑龙江', 'value': [1615, '黑龙江']}]}, {'time': 2020, 'data': [{'name': '上海', 'value': [2129, '上海']}, {'name': '云南', 'value': [456, '云南']}, {'name': '内蒙古', 'value': [934, '内蒙古']}, {'name': '北京', 'value': [2503, '北京']}, {'name': '吉林', 'value': [1550, '吉林']}, {'name': '四川', 'value': [532, '四川']}, {'name': '天津', 'value': [2059, '天津']}, {'name': '宁夏', 'value': [587, '宁夏']}, {'name': '安徽', 'value': [1361, '安徽']}, {'name': '山东', 'value': [1049, '山东']}, {'name': '山西', 'value': [17, '山西']}, {'name': '广东', 'value': [335, '广东']}, {'name': '广西', 'value': [2421, '广西']}, {'name': '新疆', 'value': [2236, '新疆']}, {'name': '江苏', 'value': [5661, '江苏']}, {'name': '江西', 'value': [97, '江西']}, {'name': '河北', 'value': [16, '河北']}, {'name': '河南', 'value': [470, '河南']}, {'name': '浙江', 'value': [140, '浙江']}, {'name': '海南', 'value': [482, '海南']}, {'name': '湖北', 'value': [1099, '湖北']}, {'name': '湖南', 'value': [326, '湖南']}, {'name': '甘肃', 'value': [453, '甘肃']}, {'name': '福建', 'value': [130, '福建']}, {'name': '西藏', 'value': [70, '西藏']}, {'name': '贵州', 'value': [410, '贵州']}, {'name': '辽宁', 'value': [427, '辽宁']}, {'name': '重庆', 'value': [2600, '重庆']}, {'name': '陕西', 'value': [4013, '陕西']}, {'name': '青海', 'value': [254, '青海']}, {'name': '黑龙江', 'value': [843, '黑龙江']}]}, {'time': 2021, 'data': [{'name': '上海', 'value': [455, '上海']}, {'name': '云南', 'value': [36, '云南']}, {'name': '内蒙古', 'value': [1160, '内蒙古']}, {'name': '北京', 'value': [942, '北京']}, {'name': '吉林', 'value': [2290, '吉林']}, {'name': '四川', 'value': [231, '四川']}, {'name': '天津', 'value': [205, '天津']}, {'name': '宁夏', 'value': [72, '宁夏']}, {'name': '安徽', 'value': [57, '安徽']}, {'name': '山东', 'value': [2295, '山东']}, {'name': '山西', 'value': [9, '山西']}, {'name': '广东', 'value': [117, '广东']}, {'name': '广西', 'value': [828, '广西']}, {'name': '新疆', 'value': [1795, '新疆']}, {'name': '江苏', 'value': [1719, '江苏']}, {'name': '江西', 'value': [61, '江西']}, {'name': '河北', 'value': [10, '河北']}, {'name': '河南', 'value': [71, '河南']}, {'name': '浙江', 'value': [2190, '浙江']}, {'name': '海南', 'value': [157, '海南']}, {'name': '湖北', 'value': [270, '湖北']}, {'name': '湖南', 'value': [190, '湖南']}, {'name': '甘肃', 'value': [2019, '甘肃']}, {'name': '福建', 'value': [76, '福建']}, {'name': '西藏', 'value': [44, '西藏']}, {'name': '贵州', 'value': [96, '贵州']}, {'name': '辽宁', 'value': [227, '辽宁']}, {'name': '重庆', 'value': [1162, '重庆']}, {'name': '陕西', 'value': [1204, '陕西']}, {'name': '青海', 'value': [302, '青海']}, {'name': '黑龙江', 'value': [67, '黑龙江']}]}]


def get_year_chart(year: int):
    map_data = [
        [[x["name"], x["value"]] for x in d["data"]] for d in data if d["time"] == year
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
                title="近5年论文数量排行前12的省份",
                subtitle="单位:篇数",
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

    bar_y_data = [{"name": x[0], "value": x[1][0]} for x in map_data]
    bar = (
        Bar()
        .add_xaxis(xaxis_data=bar_x_data)
        .add_yaxis(
            series_name="",
            yaxis_index=1,
            y_axis=bar_y_data,
            label_opts=opts.LabelOpts(
                is_show=True, position="right", formatter="{b}: {c}",
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
    init_opts=opts.InitOpts(width="1200px", height="800px", theme=ThemeType.DARK)
)
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
timeline.render("paper.html")
pie = (
    Pie()
        .add(
        series_name="",
        data_pair=pie_data,
        radius=["12%", "20%"],
        center=["75%", "85%"],
        itemstyle_opts=opts.ItemStyleOpts(
            border_width=1, border_color="rgba(0,0,0,0.3)"
        ),
    )
        .set_global_opts(
        tooltip_opts=opts.TooltipOpts(is_show=True, formatter="{b} {d}%"),
        legend_opts=opts.LegendOpts(is_show=False),
    )
)