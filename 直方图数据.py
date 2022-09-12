# -*- coding: utf-8 -*-
# @Project: PythonFile
# @Author: dingjun
# @File name: Any3
# @Create time: 2021/12/25 16:27
import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import Bar, Line

AllList = [] # 记录四组文章类型的不同数据
typeList = ['博士', '期刊', '硕士', '中国会议']
timeList = [2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016,
            2017, 2018, 2019, 2020, 2021]


def getList(actype, multiIndex=None):  # 参数是typeList中的值
    num_list = []
    for tm in timeList:
        if (tm, actype) in multiIndex:
            num_list.append(neDf.loc[(tm, actype)])  # 加上对应的数量
        else:
            num_list.append(0)  # 不存在这种文章类型当年的数量为0
    return num_list


BigDf = pd.read_excel("F:\\PythonFile\\BigWork\\other\\da.xlsx")
BigDf.rename(columns={'文章类型': 'type', 'time': 'date'}, inplace=True)  # 列名重命名
# 转换为日期格式
BigDf['date'] = pd.to_datetime(BigDf['date'], errors='coerce')
start_day = '2001-01-01'  # 起始时间
end_day = '2021-12-31'  # 结束时间
con1 = BigDf['date'] >= start_day
con2 = BigDf['date'] <= end_day
BigDf = BigDf[con1 & con2]  # 删选指定时间范围数据
BigDf = BigDf.sort_values(by='date', ascending=True, na_position='first')  # 按时间先后顺序排序
BigDf = BigDf.reset_index(drop=True)  # 重设索引
BigDf['num'] = 1

BigDf['year'] = BigDf['date'].dt.year  # 增加一列年，把年份单独分出来
# 把日期和文章类型单独处理出来，新的dataframe
neDf = BigDf[['year', 'type', 'num']]
neDf = neDf.groupby(['year', 'type']).count()  # 统计每一年不同文章类型的数量，多级索引
neDf = neDf['num'] # 记录数量这一列，到时聚类选择行列只是一个数字
multiIndex = tuple(neDf.index)  # 把二级索引转化成元组
for ty in typeList:
    list1 = getList(ty, multiIndex)
    AllList.append(list1) # 加入到总列表里面
    print(ty)
    print('----------------')
    print(list1)


