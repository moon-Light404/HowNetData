# -*- coding:utf-8 -*-
import json
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import time
import os


def GetSchool():
    res = []
    path1 = os.getcwd()
    path2 = "ChinaSchool.json"
    with open(os.path.join(path1, path2), encoding='utf-8') as f:
        d_json = json.load(f)
    print("一共" + str(len(d_json)) + "个省份")
    sum = 0
    li_key = list(d_json.keys())
    for i in li_key[25:31]:  # 改成 0:5 , 5:10 , 10:15, 15:20, 20:25, 25:31就行
        with open("log.txt", 'a') as f:
            f.write("正在爬取" + i + "的大学\n")
        sum += len(d_json[i]['all'])
        res.extend(d_json[i]['all'])
    print("正在爬取其中的" + str(sum) + "所大学")
    return res


def GetTitValue(name):  # 得到机构代码
    headers = {
        'Referer': 'https://kns.cnki.net/kns8/DefaultResult/Index?dbcode=SCDB&kw=%E6%B5%99%E6%B1%9F%E5%A4%A7%E5%AD%A6',
        'Cookie': r'''cnkiUserKey=c5708868-9970-a796-cf75-a171ff9651e7; Ecp_loginuserbk=nj0350; Ecp_ClientIp=222.204.1.5; Ecp_ClientId=3211219151203049572; yeswholedownload=%3Bhlkf202112040; ASP.NET_SessionId=g3i5inkx2vbnvjwwqlvdrfuz; SID_kns8=123121; _pk_ses=*; LID=WEEvREcwSlJHSldSdmVqM1BLVXBGTDd5VzEwZ3p0ajJ5UjhHeVJWTWp3RT0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4IQMovwHtwkF4VYPoHbKxJw!!; Ecp_session=1; Ecp_LoginStuts={"IsAutoLogin":false,"UserName":"nj0350","ShowName":"%E5%8D%97%E6%98%8C%E5%A4%A7%E5%AD%A6","UserType":"bk","BUserName":"","BShowName":"","BUserType":"","r":"AMHKq9"}; c_m_LinID=LinID=WEEvREcwSlJHSldSdmVqM1BLVXBGTDd5VzEwZ3p0ajJ5UjhHeVJWTWp3RT0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4IQMovwHtwkF4VYPoHbKxJw!!&ot=12/23/2021 19:58:25; c_m_expire=2021-12-23%2019%3A58%3A25; CurrSortField=%e5%8f%91%e8%a1%a8%e6%97%b6%e9%97%b4%2f(%e5%8f%91%e8%a1%a8%e6%97%b6%e9%97%b4%2c%27TIME%27); CurrSortFieldType=desc; knsLeftGroupSelectItem=7%3B4%3B5%3B; _pk_id=c21af64c-7b13-4c8c-a2e8-006faf2fa133.1639897405.3.1640175544.1640174298.'''}
    url = 'https://kns.cnki.net/KNS8/Group/Result'
    post_data = {
        'queryJson': r'{"Platform":"","DBCode":"SCDB","KuaKuCode":"CJFQ,CCND,CIPD,CDMD,BDZK,CISD,SNAD,CCJD,GXDB_SECTION,CJFN,CCVD","QNode":{"QGroup":[{"Key":"Subject","Title":"","Logic":1,"Items":[{"Title":"主题","Name":"SU","Value":"' + name + '","Operate":"%=","BlurType":""}],"ChildItems":[]}]}}'}
    r = requests.post(url=url, data=post_data, headers=headers)
    r.encoding = 'utf-8'
    # print(r.)
    soup = BeautifulSoup(r.text, 'html.parser')
    a = soup.find_all('input')
    for i in a:
        if i['text'] == name and re.search('\d+', i['value']):
            print("机构代码:", i['value'])
            return i['value']


def GetSqlVal(url, name):  # 翻页需要有sqlval不然无法翻页
    headers = {'Referer': 'https://kns.cnki.net/kns8/DefaultResult/Index?dbcode=SCDB&kw=%u5357%u660c%u5927%u5b66'}
    post_data = {'IsSearch': 'true',
                 'QueryJson': r'{"Platform":"","DBCode":"SCDB","KuaKuCode":"CJFQ,CCND,CIPD,CDMD,BDZK,CISD,SNAD,CCJD,GXDB_SECTION,CJFN,CCVD","QNode":{"QGroup":[{"Key":"Subject","Title":"","Logic":1,"Items":[{"Title":"主题","Name":"SU","Value":"' + name + r'","Operate":"%=","BlurType":""}],"ChildItems":[]}]}}',
                 'PageName': 'DefaultResult', 'DBCode': 'SCDB',
                 'KuaKuCodes': 'CJFQ,CCND,CIPD,CDMD,BDZK,CISD,SNAD,CCJD,GXDB_SECTION,CJFN,CCVD', 'CurPage': 1,
                 'RecordsCntPerPage': 50, 'CurDisplayMode': 'listmode', 'CurrSortField': r"发表时间/(发表时间,'TIME')",
                 'CurrSortFieldType': 'desc', 'IsSentenceSearch': 'false', 'Subject': ''}
    r = requests.post(url, data=post_data, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    a = soup.find(id='sqlVal')
    # print(r.text)
    return a['value']


def ToHerf(url,schoolname):
    headers = {'Referer': 'https://kns.cnki.net/kns8/DefaultResult/Index?dbcode=SCDB&kw=%u5357%u660c%u5927%u5b66'}
    try:
        href_re = requests.get(url, headers=headers)
    except Exception:
        print("网络连接错误")
        time.sleep(2)
        href_re = requests.get(url, headers=headers)
    href_re.encoding = 'utf-8'
    h_soup = BeautifulSoup(href_re.text, 'html.parser')
    dic_all = {}
    if h_soup.find(class_='top-tip'):
        dic_all['期刊类型'] = h_soup.find(class_='top-tip').text
    if h_soup.find('a', class_='author'):
        dic_all['系别']=''
        for i in h_soup.find_all('a', class_='author'):
            if schoolname in i.text:
                dic_all['系别'] += i.text
    for x in h_soup.find_all(class_='row'):
        li_rowtit = x.find_all(class_='rowtit')
        li_p = x.find_all('p')
        if len(li_rowtit) != len(li_p):
            continue
        dic_tmp = {}
        for y in range(len(li_rowtit)):
            dic_tmp[''.join(li_rowtit[y].text)] = ''.join(li_p[y].text.split())
        dic_all.update(dic_tmp)
    return dic_all


def GetAllData(url, sqlval, schoolname):
    post_data = {'IsSearch': 'false',
                 'QueryJson': r'{"Platform":"","DBCode":"SCDB","KuaKuCode":"CJFQ,CCND,CIPD,CDMD,BDZK,CISD,SNAD,CCJD,GXDB_SECTION,CJFN,CCVD","QNode":{"QGroup":[{"Key":"Subject","Title":"","Logic":1,"Items":[{"Title":"主题","Name":"SU","Value":"南昌大学","Operate":"%=","BlurType":""}],"ChildItems":[]}]}}',
                 'SearchSql': sqlval, 'PageName': 'DefaultResult', 'HandlerId': 8, 'DBCode': 'SCDB',
                 'KuaKuCodes': 'CJFQ,CCND,CIPD,CDMD,BDZK,CISD,SNAD,CCJD,GXDB_SECTION,CJFN,CCVD', 'CurPage': 1,
                 'RecordsCntPerPage': 50, 'CurDisplayMode': 'listmode', 'CurrSortField': "发表时间/(发表时间,'TIME')",
                 'CurrSortFieldType': 'desc', 'IsSortSearch': 'false', 'IsSentenceSearch': 'false', 'Subject': ''}
    titvalue = GetTitValue(schoolname)

    post_data = {'IsSearch': 'true',
                 'QueryJson': r'{"Platform":"","DBCode":"SCDB","KuaKuCode":"CJFQ,CDMD,CIPD,CCND,CISD,SNAD,BDZK,CCJD,CCVD,CJFN","QNode":{"QGroup":[{"Key":"Subject","Title":"","Logic":1,"Items":[{"Title":"主题","Name":"SU","Value":"' + schoolname + '","Operate":"%=","BlurType":""}],"ChildItems":[]},{"Key":"SCDBGroup","Title":"","Logic":1,"Items":[],"ChildItems":[{"Key":"7","Title":"","Logic":1,"Items":[{"Key":"' + titvalue + '","Title":"' + schoolname + '","Logic":2,"Name":"机构代码","Operate":"","Value":"' + titvalue + '","ExtendType":14,"ExtendValue":"","Value2":"","BlurType":""}],"ChildItems":[]}]}]}}',
                 'SearchSql': sqlval, 'PageName': 'DefaultResult', 'HandlerId': 45, 'DBCode': 'SCDB',
                 'KuaKuCodes': 'CJFQ%2CCDMD%2CCIPD%2CCCND%2CCISD%2CSNAD%2CBDZK%2CCCJD%2CCCVD%2CCJFN', 'CurPage': 1,
                 'RecordsCntPerPage': 20, 'CurDisplayMode': 'listmode',
                 'CurrSortField': '%25e5%258f%2591%25e8%25a1%25a8%25e6%2597%25b6%25e9%2597%25b4%252f(%25e5%258f%2591%25e8%25a1%25a8%25e6%2597%25b6%25e9%2597%25b4%252c%2527TIME%2527)',
                 'CurrSortFieldType': 'desc', 'IsSortSearch': 'false', 'IsSentenceSearch': 'false', 'Subject': ''}
    # 这个时候为true,是为了得到sqlval
    headers = {'Referer': 'https://kns.cnki.net/kns8/DefaultResult/Index?dbcode=SCDB&kw=%u5357%u660c%u5927%u5b66'}

    r = requests.post(url, data=post_data, headers=headers)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, "html.parser")
    # print(soup)
    a = soup.find(id='sqlVal')
    sqlval = a['value']  # 重置sqlval
    count = int(re.findall(r'\d+', soup.find(class_='total').text)[0])  # 找到数量
    print(count)
    #count=2
    all_name = []
    all_data = {}
    all_author = []
    all_source = []
    all_date = []
    all_data = []
    all_quote = []
    all_download = []
    all_href = []
    dic_all = []
    for i in range(1, int(count) + 1):
        print("正在爬取第" + str(i) + "页")
        post_data = {'IsSearch': 'false',
                     'QueryJson': r'{"Platform":"","DBCode":"SCDB","KuaKuCode":"CJFQ,CCND,CIPD,CDMD,BDZK,CISD,SNAD,CCJD,GXDB_SECTION,CJFN,CCVD","QNode":{"QGroup":[{"Key":"Subject","Title":"","Logic":1,"Items":[{"Title":"主题","Name":"SU","Value":"南昌大学","Operate":"%=","BlurType":""}],"ChildItems":[]}]}}',
                     'SearchSql': sqlval, 'PageName': 'DefaultResult', 'HandlerId': 8, 'DBCode': 'SCDB',
                     'KuaKuCodes': 'CJFQ,CCND,CIPD,CDMD,BDZK,CISD,SNAD,CCJD,GXDB_SECTION,CJFN,CCVD', 'CurPage': i,
                     'RecordsCntPerPage': 50, 'CurDisplayMode': 'listmode', 'CurrSortField': "发表时间/(发表时间,'TIME')",
                     'CurrSortFieldType': 'desc', 'IsSortSearch': 'false', 'IsSentenceSearch': 'false', 'Subject': ''}
        post_data = {'IsSearch': 'false',
                     'QueryJson': r'{"Platform":"","DBCode":"SCDB","KuaKuCode":"CJFQ,CDMD,CIPD,CCND,CISD,SNAD,BDZK,CCJD,CCVD,CJFN","QNode":{"QGroup":[{"Key":"Subject","Title":"","Logic":1,"Items":[{"Title":"主题","Name":"SU","Value":"' + schoolname + '","Operate":"%=","BlurType":""}],"ChildItems":[]},{"Key":"SCDBGroup","Title":"","Logic":1,"Items":[],"ChildItems":[{"Key":"7","Title":"","Logic":1,"Items":[{"Key":"' + titvalue + '","Title":"' + schoolname + '","Logic":2,"Name":"机构代码","Operate":"","Value":"' + titvalue + '","ExtendType":14,"ExtendValue":"","Value2":"","BlurType":""}],"ChildItems":[]}]}]}}',
                     'SearchSql': sqlval, 'PageName': 'DefaultResult', 'HandlerId': '117', 'DBCode': 'SCDB',
                     'KuaKuCodes': 'CJFQ%2CCCND%2CCIPD%2CCDMD%2CBDZK%2CCISD%2CSNAD%2CCCJD%2CGXDB_SECTION%2CCJFN%2CCCVD',
                     'CurPage': i, 'RecordsCntPerPage': '20', 'CurDisplayMode': 'listmode',
                     'CurrSortField': '%25e5%258f%2591%25e8%25a1%25a8%25e6%2597%25b6%25e9%2597%25b4%252f(%25e5%258f%2591%25e8%25a1%25a8%25e6%2597%25b6%25e9%2597%25b4%252c%2527TIME%2527)',
                     'CurrSortFieldType': 'desc', 'IsSortSearch': 'false', 'IsSentenceSearch': 'false', 'Subject': ''}
        for_re = requests.post(url, data=post_data, headers=headers)
        for_re.encoding = 'utf-8'
        soup_m = BeautifulSoup(for_re.text, "html.parser")
        # count = int(re.findall(r'\d+', soup_m.find(class_='total').text)[0])#count重置
        # print(soup_m)
        for j in soup_m.find(class_='result-table-list').find_all('tr')[1:]:
            # print(''.join(j.find(class_='name').text.split()))
            all_name.append(''.join(j.find(class_='name').text.split()))
            all_author.append(''.join(j.find(class_='author').text.split()))
            all_source.append(''.join(j.find(class_='source').text.split()))
            all_date.append(''.join(j.find(class_='date').text.split()))
            all_data.append(''.join(j.find(class_='data').text.split()))
            all_quote.append(''.join(j.find(class_='quote').text.split()))
            all_download.append(''.join(j.find(class_='download').text.split()))
            all_href.append(j.find(class_='fz14')['href'])
            url_tmp = 'https://kns.cnki.net/' + j.find(class_='fz14')['href']
            dic_all.append(ToHerf(url_tmp,schoolname))

    pd_detail = pd.DataFrame(dic_all)
    all_detail = pd.DataFrame({'name': all_name, 'source': all_source, '时间': all_date, })
    pd_detail = all_detail.join(pd_detail)
    print(pd_detail.columns)
    path1 = os.path.abspath(__file__)
    path1 = os.path.dirname(path1)
    pd_detail.to_excel(os.path.join(path1, schoolname + '-detail.xlsx'))
    all_data = {'name': all_name, 'author': all_author, 'source': all_source, '时间': all_date, '数据库': all_data,
                "链接": all_href}
    return all_data


url = 'https://kns.cnki.net/KNS8/Brief/GetGridTableHtml'
headers = {'Referer': 'https://kns.cnki.net/kns8/DefaultResult/Index?dbcode=SCDB&kw=%u5357%u660c%u5927%u5b66'}

school_list = ['清华大学', '北京大学', '中国人民大学', '北京工业大学', '北京理工大学', '北京航空航天大学', '北京化工大学', '北京邮电大学', '对外经济贸易大学', '中国传媒大学',
               '中央民族大学', '中国矿业大学', '中央财经大学', '中国政法大学', '中国石油大学(北京)', '中央音乐学院', '北京体育大学', '北京外国语大学', '北京交通大学', '北京科技大学',
               '北京林业大学', '中国农业大学', '北京中医药大学', '华北电力大学(北京)', '北京师范大学', '中国地质大学(北京)', '复旦大学', '华东师范大学', '上海外国语大学', '上海大学',
               '同济大学', '华东理工大学', '东华大学', '上海财经大学', '上海交通大学', '广西大学', '南开大学', '天津大学', '天津医科大学', '西藏大学', '重庆大学', '西南大学',
               '青海大学', '华北电力大学(保定)', '河北工业大学', '宁夏大学', '大连理工大学', '东北大学', '辽宁大学', '大连海事大学', '贵州大学', '吉林大学', '东北师范大学',
               '延边大', '云南大学', '东北农业大学', '东北林业大学', '哈尔滨工业大学', '哈尔滨工程大学', '南京大学', '东南大学', '苏州大学', '河海大学', '中国药科大学',
               '中国矿业大学(徐州)', '南京师范大学', '南京理工大学', '南京航空航天大学', '江南大学', '南京农业大学', '南昌大学', '安徽大学', '合肥工业大学', '中国科学技术大学',
               '浙江大学', '厦门大学', '福州大学', '郑州大学', '山东大学', '中国海洋大学', '中国石油大学(华东)', '太原理工大学', '武汉大学', '华中科技大学', '中国地质大学(武汉)',
               '华中师范大学', '华中农业大学', '中南财经政法大学', '武汉理工大学', '兰州大学', '湖南大学', '中南大学', '湖南师范大学', '海南大学', '中山大学', '暨南大学',
               '华南理工大学', '华南师范大学', '四川大学', '西南交通大学', '电子科技大学', '西南财经大学', '四川农业大学', '西北大学', '西安交通大学', '西北工业大学', '陕西师范大学',
               '西北农林科技大学', '西安电子科技大学', '长安大学', '内蒙古大学', '新疆大学', '石河子大学', '第二军医大学', '第四军医大学', '国防科学技术大学']

print(school_list)
school_list = list(dict.fromkeys(school_list))  # 去重
print("一共", len(school_list), "个学校")

# 一共116个
for i in school_list[:116]:  # 在这里改吧[0,36] [36,72] [72,108],[108,112]
    path1 = os.path.abspath(__file__)
    path1 = os.path.dirname(path1)
    if os.path.exists(os.path.join(path1,str(school_list.index(i))+i+".xlsx")):#如果该文件存在就不爬了
        print(os.path.join(path1,str(school_list.index(i))+i+".xlsx"),'已经存在，将跳过该大学')
        continue
    try:
        print("正在爬取" +str(school_list.index(i))+ i + "\n----------")
        with open(os.path.join(path1, 'log.txt'), 'a') as f:
            f.write("\n正在爬取" + str(school_list.index(i)) + i + "\n----------")
        sqlval = GetSqlVal(url, i)
        data = GetAllData(url, sqlval, i)
        data_frame = pd.DataFrame(data)
        data_frame.to_excel(os.path.join(path1, str(school_list.index(i))+i + ".xlsx"))#这个就有序号了
    except Exception:
        t = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print("出现未知错误，请重试")
        with open(os.path.join(path1, 'log.txt'), 'a') as f:
            f.write("\n" + t + "正在爬取" + i + ",出现错误，请及时处理" + "索引位置为" + str(school_list.index(i)) + '下次可以从这里开始\n')
        time.sleep(2)
        continue
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
