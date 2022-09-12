# -*- coding: utf-8 -*-
# @Project: PythonFile
# @Author: dingjun
# @File name: data1
# @Create time: 2021/12/24 16:45
# 分析所有论文中每年的论文数量

import pandas as pd
import os, time
import pyecharts.options as opts
from pyecharts.charts import Line

# 将在 v1.1.0 中更改
from pyecharts.commons.utils import JsCode
from pyecharts.charts import Line

frames = []


# 将多个excel文件合并成一个csv文件
def join_file():
    for root, dirs, files in os.walk(r'F:\PythonFile\BigWork\other'):
        for file in files:
            print(os.path.join(root, file))
            df = pd.read_excel(os.path.join(root, file))
            df.drop(columns=['Unnamed: 0'], inplace=True)
            df.rename(columns={'时间': 'date'}, inplace=True)  # 修改时间的列名
            frames.append(df)


# 注意处理文件的时候，文件不能打开
def save_file():
    join_file()
    result = pd.concat(frames)  # 合并所有数据
    result.drop(columns=['播放：', '时长：', '发布时间：', '基金：', '会议名称：', '会议地点：', '报纸日期：', '版名：',
                         '版号：', '副标题：', '第一完成单位：', '中图分类号：', '学科分类号：', '成果简介：',
                         '成果入库时间：', '成果完成人：', '评价形式：', '研究起止时间：', '引题：', '专题活动：',
                         '主办单位：', '成果类别：', '成果水平：'], inplace=True)
    print(result.head())
    print(result.shape)
    result.to_excel('F:\\PythonFile\\BigWork\\other\\all.xlsx', index=False)


# 统计近20年内的论文数量图
def get_year():
    df1 = pd.read_excel(r'F:\PythonFile\BigWork\other\da.xlsx')
    df1.rename(columns={'time': 'date'}, inplace=True)
    df1['date'] = pd.to_datetime(df1['date'])
    s_day = '2000-01-01'  # 起始时间
    e_day = '2021-12-31'  # 结束时间
    con1 = df1['date'] >= s_day
    con2 = df1['date'] <= e_day
    df1 = df1[con1 & con2]  # 删选指定时间范围数据
    df1 = df1.sort_values(by='date', ascending=True, na_position='first')  # 按时间先后顺序排序
    df1 = df1.reset_index(drop=True)  # 重设索引
    # df.to_excel("南开大学-detail.xlsx")
    groupDf = df1
    groupDf.index = groupDf['date']
    groupDf['num'] = 1  # 增加一列num，记录总数量
    gm = groupDf.groupby(groupDf.index.year)
    yearDf = gm.count()
    cnt = yearDf['num']  # 2000~2021年每年的论文数量
    return cnt


# save_file()
cnt = get_year()
print("cnt = ", cnt)

# cnt = [2283, 2720, 3196, 4120, 5665, 7133, 10714, 11840, 11059, 13088, 11673, 12014, 12969, 15765,
#        17349, 12960, 22720, 29317, 30413, 37024, 35938, 20573]


"""
Gallery 使用 pyecharts 1.0.0
参考地址: https://echarts.apache.org/examples/editor.html?c=multiple-x-axis

目前无法实现的功能:

1、暂无
"""
# 画图模板折线图
(
    Line(init_opts=opts.InitOpts(width="1600px", height="800px"))
    .add_xaxis(
        xaxis_data=[
            "2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010"]
    )
    .extend_axis(
        xaxis_data=[
            "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021"],
        xaxis=opts.AxisOpts(
            type_="category",
            axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
            axisline_opts=opts.AxisLineOpts(
                is_on_zero=False, linestyle_opts=opts.LineStyleOpts(color="#6e9ef1",)
            ),
            axispointer_opts=opts.AxisPointerOpts(
                is_show=True
            ),
        ),
    )
    .add_yaxis(
        series_name="2000~2010年",
        is_smooth=False,
        symbol="square",
        is_symbol_show=True,  # 显示点的具体数据
        color="#6e9ef1",
        y_axis=cnt[0:11],  # cnt[0:9]
        label_opts=opts.LabelOpts(is_show=True),
        markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")]),  # 标记平均值 MarkLineItem标记平均线
        linestyle_opts=opts.LineStyleOpts(width=2),
    )
    .add_yaxis(
        series_name="2011~2021年",
        is_smooth=False,  # 直线不平滑
        symbol="square",  # 点的样式
        is_symbol_show=True,  # 显示点的数据
        color="#d14a61",

        y_axis=cnt[11:22],  # cnt[10:22]
        label_opts=opts.LabelOpts(is_show=True),
        markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")]),  # 标记平均值
        linestyle_opts=opts.LineStyleOpts(width=2),
    )
    .set_global_opts(
        legend_opts=opts.LegendOpts(),
        tooltip_opts=opts.TooltipOpts(trigger="none", axis_pointer_type="cross"),
        xaxis_opts=opts.AxisOpts(
            type_="category",
            axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
            axisline_opts=opts.AxisLineOpts(
                is_on_zero=False, linestyle_opts=opts.LineStyleOpts(color="#d14a61")
            ),
            axispointer_opts=opts.AxisPointerOpts(
                is_show=True
            ),
        ),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            splitline_opts=opts.SplitLineOpts(
                is_show=True, linestyle_opts=opts.LineStyleOpts(opacity=1)
            ),
        ),
    )
    .render("论文数量与年份情况.html")
)
