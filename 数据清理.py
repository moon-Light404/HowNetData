import os
import pandas as pd
dir_all=os.path.join(os.path.curdir,'school')
ls_ham=[]
for root,dirs,files in os.walk(dir_all):
    for f in files:
        file_name=f
        ds_file = os.path.join('school',file_name)
        df_data2 = pd.read_excel(ds_file,header=0)
        df_data2['时间']= df_data2['时间'].str.extract('(\d+[-/]\d+[-/]\d{2})', expand=False)
        df_data2['时间']=pd.to_datetime(df_data2['时间'],errors='coerce')
        df_data2['时间'] = pd.to_datetime(df_data2['时间']).dt.date
        df_data2.to_excel(ds_file, index=False)
        li=[]
        li2=[]
        if 'detail' not in ds_file:
            df_data = pd.read_excel(ds_file, header=0)
            df_time = df_data [['时间']]
            li=df_time[df_time.isnull().T.any()].index
            df = df_data[['author']]
            li2=df[df.isnull().T.any()].index
        else:
            df_data = pd.read_excel(ds_file, header=0)
            df_time = df_data [['时间']]
            li=df_time[df_time.isnull().T.any()].index
            df = df_data[['关键词：']]
            li2=df[df.isnull().T.any()].index
            df_data2 = df_data2[['name', '期刊类型', '系别', '关键词：', '专辑：', '专题：']]
        for i in li:
            i=int(i)
            df_data2.drop([i], axis=0, inplace=True)
        for i in li2:
          if i not in li:
            i=int(i)
            df_data2.drop([i], axis=0, inplace=True)
        df_data2.to_excel(ds_file, index=False)

for root, dirs, files in os.walk(dir_all):
    for f in files:
        file_name = f
        ds_file = os.path.join('school', file_name)
        if 'detail' not in ds_file:
            df_data1= pd.read_excel(ds_file, header=0)
            ds_file2=ds_file.rstrip('.xlsx')
            ds_file2=ds_file2+'-detail.xlsx'
            df_data2= pd.read_excel(ds_file2, header=0)
            merge_df=pd.merge(df_data1,df_data2,on=['name'],how='right')
            merge_df.to_excel(ds_file,index=False)
frames = []
for root, dirs, files in os.walk(dir_all):
    for f in files:
        file_name = f
        ds_file = os.path.join('school', file_name)
        if 'detail' not in ds_file:
            df = pd.read_excel(ds_file, header=0)
            frames.append(df)
result = pd.concat(frames)
result.index = result .index + 1
result.columns = ['index', 'name', 'author', 'source', 'time', '文章类型',
                    '链接', '期刊类型', '系别', '关键词', '专辑', '专题', '分类号']
result.to_excel('da.xlsx', index=False)

for root,dirs,files in os.walk(dir_all):
        for f in files:
            file_name = f
            ds_file = os.path.join('school', file_name)
            df_data2 = pd.read_excel(ds_file, header=0)
            df_data2['专辑：'] = df_data2['专辑：'] +';'
            df_data2['专辑：'] = df_data2['专辑：'].str.extract('(\w+;)', expand=False)
            df_data2['专辑：'] = df_data2['专辑'].str.rstrip(';')
            df_data2.to_excel(ds_file, index=False)
for root,dirs,files in os.walk(dir_all):
        for f in files:
            file_name = f
            ds_file = os.path.join('school', file_name)
            li=[]
            df_data = pd.read_excel(ds_file, header=0)
            df_time = df_data [['专辑']]
            li=df_time[df_time.isnull().T.any()].index
            for i in li:
                i=int(i)
                df_data.drop([i], axis=0, inplace=True)
            df_data.to_excel(ds_file, index=False)
for root,dirs,files in os.walk(dir_all):
    for f in files:
        file_name=f
        ds_file = os.path.join('school',file_name)
        if 'detail' in ds_file:
            df_data = pd.read_excel(ds_file, header=0)
            ds_file2=ds_file.rstrip('-detail.xlsx')
            ds_file2=ds_file2.replace('school\\','')
            df_data['系别']=ds_file2
            df_data.to_excel(ds_file, index=False)


        df_data2['时间']= df_data2['时间'].str.extract('(\d+[-/]\d+[-/]\d{2})', expand=False)
        df_data2['时间']=pd.to_datetime(df_data2['时间'],errors='coerce')
        df_data2['时间'] = pd.to_datetime(df_data2['时间']).dt.date
        df_data2.to_excel(ds_file, index=False)
        li=[]
        li2=[]
        if 'detail' not in ds_file:
            df_data = pd.read_excel(ds_file, header=0)
            df_time = df_data [['时间']]
            li=df_time[df_time.isnull().T.any()].index
            df = df_data[['author']]
            li2=df[df.isnull().T.any()].index
        else:
            df_data = pd.read_excel(ds_file, header=0)
            df_time = df_data [['时间']]
            li=df_time[df_time.isnull().T.any()].index
            df = df_data[['关键词：']]
            li2=df[df.isnull().T.any()].index
            df_data2 = df_data2[['name', '期刊类型', '系别', '关键词：', '专辑：', '专题：']]
        for i in li:
            i=int(i)
            df_data2.drop([i], axis=0, inplace=True)
        for i in li2:
          if i not in li:
            i=int(i)
            df_data2.drop([i], axis=0, inplace=True)
        df_data2.to_excel(ds_file, index=False)
for root,dirs,files in os.walk(dir_all):
    for f in files:
        file_name=f
        ds_file = os.path.join('school',file_name)
        if 'detail' in ds_file:
            df_data = pd.read_excel(ds_file, header=0)
            ds_file2=ds_file.rstrip('-detail.xlsx')
            ds_file2=ds_file2.replace('school\\','')
            df_data['系别']=ds_file2
            df_data.to_excel(ds_file, index=False)

for root,dirs,files in os.walk(dir_all):
        for f in files:
            file_name = f
            ds_file = os.path.join('school', file_name)
            df_data2 = pd.read_excel(ds_file, header=0)
            df_data2['专辑'] = df_data2['专辑'] +';'
            df_data2['专辑'] = df_data2['专辑'].str.extract('(\w+;)', expand=False)
            df_data2['专辑'] = df_data2['专辑'].str.rstrip(';')
            df_data2.to_excel(ds_file, index=False)
for root,dirs,files in os.walk(dir_all):
        for f in files:
            file_name = f
            ds_file = os.path.join('school', file_name)
            li=[]
            df_data = pd.read_excel(ds_file, header=0)
            df_time = df_data [['专辑']]
            li=df_time[df_time.isnull().T.any()].index
            for i in li:
                i=int(i)
                df_data.drop([i], axis=0, inplace=True)
            df_data.to_excel(ds_file, index=False)



import pandas

li1=['清华大学', '北京大学', '中国人民大学', '北京工业大学', '北京理工大学', '北京航空航天大学', '北京化工大学', '北京邮电大学','对外经济贸易大学', '中国传媒大学',
               '中央民族大学', '中国矿业大学', '中央财经大学', '中国政法大学', '中国石油大学(北京)', '中央音乐学院', '北京体育大学', '北京外国语大学', '北京交通大学', '北京科技大学',
               '北京林业大学', '中国农业大学', '北京中医药大学', '华北电力大学(北京)', '北京师范大学', '中国地质大学(北京)']
li2=['复旦大学', '华东师范大学', '上海外国语大学', '上海大学','同济大学', '华东理工大学', '东华大学', '上海财经大学', '上海交通大学','第二军医大学']
li3=['武汉大学', '华中科技大学', '中国地质大学(武汉)','华中师范大学', '华中农业大学', '中南财经政法大学', '武汉理工大学',]
li4=['广西大学']
li5=['南开大学', '天津大学', '天津医科大学']
li6=['西藏大学']
li7=['重庆大学', '西南大学']
li8=['东北农业大学', '东北林业大学', '哈尔滨工业大学', '哈尔滨工程大学', ]
li9=[ '青海大学']
li10=['华北电力大学(保定)', '河北工业大学']
li11=['宁夏大学']
li12=['大连理工大学', '东北大学', '辽宁大学', '大连海事大学']
li13=['贵州大学']
li14=['吉林大学', '东北师范大学','延边大学']
li15=['云南大学']
li16=['南京大学', '东南大学', '苏州大学','河海大学', '中国药科大学','中国矿业大学(徐州)', '南京师范大学', '南京理工大学', '南京航空航天大学', '江南大学', '南京农业大学']
li17=['南昌大学']
li18=['安徽大学', '合肥工业大学', '中国科学技术大学']
li19=['浙江大学']
li20=['厦门大学', '福州大学']
li21=['郑州大学']
li22=['山东大学', '中国海洋大学', '中国石油大学(华东)']
li23=['太原理工大学']
li24=['兰州大学']
li25=['湖南大学', '中南大学', '湖南师范大学', '国防科学技术大学']
li26=['海南大学']
li27=['中山大学', '暨南大学', '华南理工大学', '华南师范大学']
li28=['四川大学', '西南交通大学', '电子科技大学', '西南财经大学', '四川农业大学']
li29=['西北大学', '西安交通大学', '西北工业大学', '陕西师范大学', '西北农林科技大学', '西安电子科技大学', '长安大学', '第四军医大学']
li30=['内蒙古大学']
li31=['新疆大学', '石河子大学']
import os
import pandas as pd
dir_all=os.path.join(os.path.curdir,'school')
ls_ham=[]
for root,dirs,files in os.walk(dir_all):
        for f in files:
            file_name = f
            ds_file = os.path.join('school', file_name)
            ds_file2 = ds_file.rstrip('.xlsx')
            ds_file2 = ds_file2.replace('school\\', '')
            if ds_file2 in li1:
                df_data2 = pd.read_excel(ds_file, header=0)
                df_data2['from']='北京'
                df_data2.to_excel(ds_file, index=False)
            elif ds_file2 in li2:
                df_data2 = pd.read_excel(ds_file, header=0)
                df_data2['from']='上海'
                df_data2.to_excel(ds_file, index=False)
            elif ds_file2 in li3:
                df_data2 = pd.read_excel(ds_file, header=0)
                df_data2['from']='湖北'
                df_data2.to_excel(ds_file, index=False)
            elif ds_file2 in li4:
                df_data2 = pd.read_excel(ds_file, header=0)
                df_data2['from']='广西'
                df_data2.to_excel(ds_file, index=False)
            elif ds_file2 in li5:
                df_data2 = pd.read_excel(ds_file, header=0)
                df_data2['from']='天津'
                df_data2.to_excel(ds_file, index=False)
            elif ds_file2 in li6:
                df_data2 = pd.read_excel(ds_file, header=0)
                df_data2['from']='西藏'
                df_data2.to_excel(ds_file, index=False)
            elif ds_file2 in li7:
                df_data2 = pd.read_excel(ds_file, header=0)
                df_data2['from']='重庆'
                df_data2.to_excel(ds_file, index=False)
            elif ds_file2 in li8:
                df_data2 = pd.read_excel(ds_file, header=0)
                df_data2['from']='黑龙江'
                df_data2.to_excel(ds_file, index=False)
            elif ds_file2 in li9:
                df_data2 = pd.read_excel(ds_file, header=0)
                df_data2['from']='青海'
                df_data2.to_excel(ds_file, index=False)
            elif ds_file2 in li10:
                df_data2 = pd.read_excel(ds_file, header=0)
                df_data2['from']='河北'
                df_data2.to_excel(ds_file, index=False)
            elif ds_file2 in li11:
                df_data2 = pd.read_excel(ds_file, header=0)
                df_data2['from']='宁夏'
                df_data2.to_excel(ds_file, index=False)
            elif ds_file2 in li12:
                df_data2 = pd.read_excel(ds_file, header=0)
                df_data2['from']='辽宁'
                df_data2.to_excel(ds_file, index=False)
            elif ds_file2 in li13:
                df_data2 = pd.read_excel(ds_file, header=0)
                df_data2['from']='贵州'
                df_data2.to_excel(ds_file, index=False)
            elif ds_file2 in li14:
                df_data2 = pd.read_excel(ds_file, header=0)
                df_data2['from']='吉林'
                df_data2.to_excel(ds_file, index=False)
            elif ds_file2 in li15:
                df_data2 = pd.read_excel(ds_file, header=0)
                df_data2['from']='云南'
                df_data2.to_excel(ds_file, index=False)
            elif ds_file2 in li16:
                df_data2 = pd.read_excel(ds_file, header=0)
                df_data2['from']='江苏'
                df_data2.to_excel(ds_file, index=False)
            elif ds_file2 in li17:
                df_data2 = pd.read_excel(ds_file, header=0)
                df_data2['from']='江西'
                df_data2.to_excel(ds_file, index=False)
            elif ds_file2 in li18:
                df_data2 = pd.read_excel(ds_file, header=0)
                df_data2['from']='安徽'
                df_data2.to_excel(ds_file, index=False)
            elif ds_file2 in li19:
                df_data2 = pd.read_excel(ds_file, header=0)
                df_data2['from']='浙江'
                df_data2.to_excel(ds_file, index=False)
            elif ds_file2 in li20:
                df_data2 = pd.read_excel(ds_file, header=0)
                df_data2['from']='福建'
                df_data2.to_excel(ds_file, index=False)
            elif ds_file2 in li21:
                df_data2 = pd.read_excel(ds_file, header=0)
                df_data2['from']='河南'
                df_data2.to_excel(ds_file, index=False)
            elif ds_file2 in li22:
                df_data2 = pd.read_excel(ds_file, header=0)
                df_data2['from']='山东'
                df_data2.to_excel(ds_file, index=False)
            elif ds_file2 in li23:
                df_data2 = pd.read_excel(ds_file, header=0)
                df_data2['from']='山西'
                df_data2.to_excel(ds_file, index=False)
            elif ds_file2 in li24:
                df_data2 = pd.read_excel(ds_file, header=0)
                df_data2['from']='甘肃'
                df_data2.to_excel(ds_file, index=False)
            elif ds_file2 in li25:
                df_data2 = pd.read_excel(ds_file, header=0)
                df_data2['from']='湖南'
                df_data2.to_excel(ds_file, index=False)
            elif ds_file2 in li26:
                df_data2 = pd.read_excel(ds_file, header=0)
                df_data2['from']='海南'
                df_data2.to_excel(ds_file, index=False)
            elif ds_file2 in li27:
                df_data2 = pd.read_excel(ds_file, header=0)
                df_data2['from']='广东'
                df_data2.to_excel(ds_file, index=False)
            elif ds_file2 in li28:
                df_data2 = pd.read_excel(ds_file, header=0)
                df_data2['from']='四川'
                df_data2.to_excel(ds_file, index=False)
            elif ds_file2 in li29:
                df_data2 = pd.read_excel(ds_file, header=0)
                df_data2['from']='陕西'
                df_data2.to_excel(ds_file, index=False)
            elif ds_file2 in li30:
                df_data2 = pd.read_excel(ds_file, header=0)
                df_data2['from']='内蒙古'
                df_data2.to_excel(ds_file, index=False)
            elif ds_file2 in li31:
                df_data2 = pd.read_excel(ds_file, header=0)
                df_data2['from']='新疆'
                df_data2.to_excel(ds_file, index=False)







