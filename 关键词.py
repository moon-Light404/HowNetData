# -*- coding: utf-8 -*-
# @Project: PythonFile
# @Author: dingjun
# @File name: Any5
# @Create time: 2021/12/27 18:43
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import WordCloud
from pyecharts.globals import SymbolType

df = pd.read_excel("F:\\PythonFile\\BigWork\\other\\da.xlsx")
keyDf = df['关键词']


def get_key():
    keywords = {}
    for words in keyDf:
        for key in words.split(";"):
            if key:
                if key not in keywords:
                    keywords[key] = 1
                else:
                    keywords[key] += 1
    return keywords


count_data = get_key()
# del_list = []
# for key, value in count_data.items():
#     if value < 100: # 把出现数量小于100的关键词删除
#         del_list.append(key)
#     else:
#         continue
# # 删除对应的key
# for key in list(count_data.keys()):
#     if key in del_list:
#         del count_data[key]
#     else:
#         continue
print("count_data = ", count_data)
data = list(count_data.items()) # 字典转成列表
print("data = ", data)
c = (
    WordCloud()
    .add("论文关键词分析", data, word_size_range=[20, 100], shape=SymbolType.DIAMOND)
    .set_global_opts(title_opts=opts.TitleOpts(title="论文关键词词云分析图"))
    .render("论文关键词词云.html")
)
