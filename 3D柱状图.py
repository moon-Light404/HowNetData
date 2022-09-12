import random

from pyecharts import options as opts
from pyecharts.charts import Bar3D
from pyecharts.faker import Faker

time=[2017,2015,2018,2017,2019,2012,2020,2021,2021]
type1=['医药卫生科技','','工程科技Ⅰ辑','','社会科学Ⅱ辑','','基础科学','','信息科技','','工程科技Ⅱ辑','哲学与人文科学','农业科技','经济与管理科学','社会科学Ⅰ辑']
data =[[0,0, 70], [0, 2, 33],[0, 8, 27],[0, 4, 23],[0, 6, 21],[0, 10, 9],[0, 12, 5],
       [2,0, 78], [2, 2, 41],[2, 8, 11],[2, 4, 27],[2, 6, 15],[2, 10, 14],[2, 14, 6],[2, 12, 2],
       [4,0, 115], [4, 2, 20],[4, 6, 11],[4, 4,11],[4, 8, 6],[4, 10, 2],[4, 12, 1],
       [6,0, 30], [6, 2, 19],[6, 6, 11],[6, 10,10],[6, 4, 9],[6, 8, 5],
       [8,0, 34], [8, 2, 17],[8, 6, 7],[8, 8,1],[8, 10, 1],[8, 4, 1]
       ]
c = (
    Bar3D()
    .add(
        "",
        [[d[1], d[0], d[2]] for d in data],
        xaxis3d_opts=opts.Axis3DOpts(type1, type_="category"),
        yaxis3d_opts=opts.Axis3DOpts(time,type_="category"),
        zaxis3d_opts=opts.Axis3DOpts(type_="value"),
    )
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(max_=20),
        title_opts=opts.TitleOpts(title="Bar3D-基本示例"),
    )
    .render("bar3d_base.html")
)