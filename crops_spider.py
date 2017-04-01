# -*- coding:utf-8 -*-
# ------------------------------------------------------
#   版本：py2.7
#   日期：2017-03-18
#   作者：今孝
#   目标网址：http://www.cgris.net/query/croplist.php#
# ------------------------------------------------------

'''爬取主要的信息  但是有个别会遗漏，需要再次爬取'''
from selenium import webdriver
import re,sys,time,pymysql
reload(sys)  #解决编码
sys.setdefaultencoding('utf-8')

def connectDB():
    host="localhost"
    dbName="qitazuowu"   ####大类参数修改处----数据库名
    user="root"
    password="root"
    db=pymysql.connect(host,user,password,dbName,charset='utf8')
    return db #一定要返回连接的db
    cursorDB=db.cursor()
    return cursorDB
y=1;create=1
ziduan_list=[]
url='http://www.cgris.net/query/do.php#其它作物,橡胶'    ####修改参数处----小类的地址需要修改
browser = webdriver.Chrome()
browser.get(url)
browser.implicitly_wait(3)
browser.find_element_by_css_selector('div[onclick="query()"]').click()
browser.implicitly_wait(2)

reg=r',(.*?)$'
table_name1=re.findall(reg,url)[0]
print table_name1
html=browser.page_source
reg=r'<td class="cap">(.*?)</td>'
reg=re.compile(reg,re.S)
count=re.findall(reg,html)
ziduan_count=len(count)-4  #字段的个数
yushu=ziduan_count%3

if ziduan_count%3==0:
    ziduan_count=ziduan_count/3
else:
    ziduan_count=ziduan_count/3+1
for i in range(1,ziduan_count+1):
    for j in range(1,6,2):
        if i==ziduan_count:
            if yushu==0:
                a='#r2 > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child('+str(i)+') > td:nth-child('+str(j)+')'
                first_col=browser.find_element_by_css_selector(a).text
                ziduan_list.append(first_col)
            elif yushu==1:
                a='#r2 > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child('+str(i)+') > td:nth-child(1)'
                first_col=browser.find_element_by_css_selector(a).text
                ziduan_list.append(first_col)
                break
            elif yushu==2:
                for k in range(1,4,2):
                    a='#r2 > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child('+str(i)+') > td:nth-child('+str(k)+')'
                    first_col=browser.find_element_by_css_selector(a).text
                    ziduan_list.append(first_col)
                break
        else:
            a='#r2 > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child('+str(i)+') > td:nth-child('+str(j)+')'
            first_col=browser.find_element_by_css_selector(a).text
            ziduan_list.append(first_col)

if create==1:
    '''创建数据表'''
    sql_createTable="CREATE TABLE IF NOT EXISTS "+table_name1+" (id int(11) NOT NULL AUTO_INCREMENT,name varchar(255),"+' varchar(255),'.join(ziduan_list)+" varchar(255),PRIMARY KEY (`id`))ENGINE=MyISAM DEFAULT CHARSET=utf8"
    print sql_createTable
    DB_create=connectDB()
    cur_create=DB_create.cursor()
    cur_create.execute(sql_createTable)
    DB_create.close()
    create=0
browser.find_element_by_id('lasthehe').click()
con_list=[];value_list=[]
while y<5890:       ####修改参数----看一共有多少个就修改这里的参数
    try:
        con_list.append(table_name1)
        value_list.append('%s')
        for i in range(1,ziduan_count+1):
            for j in range(2,7,2):
                if i==ziduan_count:
                    if yushu==0:
                        a='#r2 > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child('+str(i)+') > td:nth-child('+str(j)+')'
                        first_col=browser.find_element_by_css_selector(a).text
                        con_list.append(first_col)
                        value_list.append('%s')
                    elif yushu==1:
                        a='#r2 > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child('+str(i)+') > td:nth-child(2)'
                        first_col=browser.find_element_by_css_selector(a).text
                        con_list.append(first_col)
                        value_list.append('%s')
                        break
                    elif yushu==2:
                        for k in range(2,5,2):
                            a='#r2 > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child('+str(i)+') > td:nth-child('+str(k)+')'
                            first_col=browser.find_element_by_css_selector(a).text
                            con_list.append(first_col)
                            value_list.append('%s')
                        break
                else:
                    a='#r2 > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child('+str(i)+') > td:nth-child('+str(j)+')'
                    first_col=browser.find_element_by_css_selector(a).text
                    con_list.append(first_col)
                    value_list.append('%s')
        index_1=ziduan_list.index('统一编号')
        sql_quchong="select * from "+table_name1+" where 统一编号="+"'"+con_list[index_1+1]+"'"
        sql="insert into "+table_name1+"("+"name,"+','.join(ziduan_list)+")"+"value("+','.join(value_list)+")"
        DB_insert=connectDB()
        cur_insert=DB_insert.cursor()
        if cur_insert.execute(sql_quchong):
            DB_insert.commit()
            DB_insert.close()
            con_list=[]
            value_list=[]
            print '已存在',y
        else:
            cur_insert.execute(sql,con_list)
            DB_insert.commit()
            DB_insert.close()
            con_list=[]
            value_list=[]
        browser.find_element_by_id('prehehe').click()
        time.sleep(5)
    except Exception,e:
        print e
        time.sleep(5)
        continue
    y+=1