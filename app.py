from flask import Flask, render_template, request
import plan_list
import plan
import dbutil
import account
import audiobook
import threadutil
import util  # 自定义
import time  # 系统自带
from concurrent.futures import as_completed  # 系统自带

app = Flask(__name__)  # 原始flask 代码
# app = Flask(__name__, template_folder='.', static_folder='.', static_url_path='')


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/plan.html')
def view_plan():
    dbutil.print_cfg()
    return render_template('plan.html')


@app.route('/add_plan.html')
def view_add_plan():
    return render_template('add_plan.html')


@app.route('/add_plan', methods=('GET', 'POST'))
def add_plan():
    if request.method == 'POST':
        print('前端调用接口，add_plan')
        # 0. 获取请求参数
        sqlvaluedict = {
            "date": request.values.get('date'),
            "planid1": request.values.get('planid1'), "planisfinish1": request.values.get('planisfinish1'),
            "planid2": request.values.get('planid2'), "planisfinish2": request.values.get('planisfinish2'),
            "planid3": request.values.get('planid3'), "planisfinish3": request.values.get('planisfinish3'),
            "planid4": request.values.get('planid4'), "planisfinish4": request.values.get('planisfinish4'),
            "planid5": request.values.get('planid5'), "planisfinish5": request.values.get('planisfinish5'),
            "planid6": request.values.get('planid6'), "planisfinish6": request.values.get('planisfinish6'),
            "planid7": request.values.get('planid7'), "planisfinish7": request.values.get('planisfinish7'),
            "planid8": request.values.get('planid8'), "planisfinish8": request.values.get('planisfinish8'),
            "planid9": request.values.get('planid9'), "planisfinish9": request.values.get('planisfinish9'),
            "planid10": request.values.get('planid10'), "planisfinish10": request.values.get('planisfinish10'),
            "planid11": request.values.get('planid11'), "planisfinish11": request.values.get('planisfinish11'),
            "planid12": request.values.get('planid12'), "planisfinish12": request.values.get('planisfinish12'),
            "planid13": request.values.get('planid13'), "planisfinish13": request.values.get('planisfinish13'),
            "planid14": request.values.get('planid14'), "planisfinish14": request.values.get('planisfinish14'),
            "planid15": request.values.get('planid15'), "planisfinish15": request.values.get('planisfinish15'),
            "planid16": request.values.get('planid16'), "planisfinish16": request.values.get('planisfinish16'),
            "planid17": request.values.get('planid17'), "planisfinish17": request.values.get('planisfinish17'),
            "planid18": request.values.get('planid18'), "planisfinish18": request.values.get('planisfinish18'),
            "planid19": request.values.get('planid19'), "planisfinish19": request.values.get('planisfinish19'),
            "planid20": request.values.get('planid20'), "planisfinish20": request.values.get('planisfinish20'),
        }

        # 0.1 根据用户输入的str,判断plan表里是否有，没有插入
        # 获取数据库plan表所有的plan
        queryallplan_sql = 'select id,name from plan'
        allplan_result = plan.query_plan(queryallplan_sql)  # json
        # print('===================== allplan_result', allplan_result)
        # 所有name的数组
        allplannames_arr = []
        for item in allplan_result['data']:
            # print('item===========', item)
            # print('item["name"]===========', item['name'])
            # print('item.name===========', item.name)  # dict 错误写法
            allplannames_arr.append(item['name'])
        # print('所有name的数组===============', allplannames_arr)

        plandict = {
            "planid1": request.values.get('planid1'),
            "planid2": request.values.get('planid2'),
            "planid3": request.values.get('planid3'),
            "planid4": request.values.get('planid4'),
            "planid5": request.values.get('planid5'),
            "planid6": request.values.get('planid6'),
            "planid7": request.values.get('planid7'),
            "planid8": request.values.get('planid8'),
            "planid9": request.values.get('planid9'),
            "planid10": request.values.get('planid10'),
            "planid11": request.values.get('planid11'),
            "planid12": request.values.get('planid12'),
            "planid13": request.values.get('planid13'),
            "planid14": request.values.get('planid14'),
            "planid15": request.values.get('planid15'),
            "planid16": request.values.get('planid16'),
            "planid17": request.values.get('planid17'),
            "planid18": request.values.get('planid18'),
            "planid19": request.values.get('planid19'),
            "planid20": request.values.get('planid20')
        }
        # 不存在的插入plan数据表里
        for key, value in plandict.items():
            if value is None or value == '':
                pass
            else:
                if value not in allplannames_arr:
                    sql = 'insert into plan(name) values(%(name)s)'  # 插入
                    dbutil.execute(sql, {'name': value})

        # 1. 执行sql
        # 拼接sql 插入列
        cols = "("
        values = "("
        for key, value in sqlvaluedict.items():
            if value is None or value == "":  # 空
                # print(key, '空')
                pass
            else:  # 非空
                cols += key + ','  # 拼接插入列
                values += '%(' + key + ')s,'  # 拼接插入列的value
        cols = cols.strip(",")
        values = values.strip(",")
        cols += ')'
        values += ')'
        print('sql-->cols==', cols)
        print('sql-->values==', values)

        add_plan_sql = 'insert into plan_list' + cols + ' values' + values
        print('插入sql= ', add_plan_sql)
        # 将sqlvaluedict 里涉及str的转成plan表里的id
        # 再次获取数据库plan表所有的plan
        queryallplan_sql = 'select id,name from plan'
        allplan_result = plan.query_plan(queryallplan_sql)  # json
        print('=========== sqlvaluedict=', sqlvaluedict)
        print('=========== sqlvaluedict.items()=', sqlvaluedict.items())
        for key, value in sqlvaluedict.items():
            if 'planid' in key and value != '':
                for item in allplan_result['data']:
                    if value == item['name']:
                        sqlvaluedict[key] = item['id']  # str --> int(id)
        print('转化后的 插入sql value = ', sqlvaluedict)

        plan_list.add_plan(add_plan_sql, sqlvaluedict)
        return ''  # 路由里必须添加return


# @app.route('/planlist', )  # 不写methods,默认是get方法，否则前端报错Method Not Allowed
@app.route('/planlist', methods=('GET', 'POST', 'DELETE'))
def planlist():
    resultjson = {
        "code": 500,
        "msg": "",
        "count": 0,
        "data": []
    }
    # 获取数据
    if request.method == 'GET':
        print('前端调用接口，/plan')
        # 1. 获取请求参数
        page = int(request.values.get('page'))  # str
        # print('=================type', type(page))  # str
        limit = int(request.values.get('limit'))  # str-->int

        # 2. 数据库查询数据
        # eg SELECT customernumber, customername, creditlimit FROM customers LIMIT 0,5
        sql = 'select * from plan_list order by id limit %(index)s, %(limit)s'
        values = dict()
        values.update({
            "index": (page-1) * limit,
            "limit": limit
        })
        result = plan_list.query_plan(sql, values)
        # result = plan_list.query_plan(sql, [int(page), int(limit)])
        print('查询planlist--> result == ', result)  # NoneType
        print('查询planlist--> result.type == ', type(result))

        # 2. 返回值 dict，模拟数据
        # result = {
        #     "code": 0
        #     , "msg": ""
        #     , "count": 10
        #     , "data": [{
        #         "id": "1"
        #         , "date": "2021-12-06"
        #         , "plan1": "打卡"
        #         , "planisfinish1": "1"
        #         , "plan2": "还钱"
        #         , "planisfinish2": "1"
        #         , "plan3": "基金"
        #         , "planisfinish3": "0"
        #         , "plan4": "学习"
        #         , "planisfinish4": "1"
        #         , "plan5": "草榴打卡"
        #         , "planisfinish5": "1"
        #         , "plan6": "发twitter"
        #         , "planisfinish6": "0"
        #         , "plan7": "打扫家"
        #         , "planisfinish7": "1"
        #         , "plan8": "穿短袖"
        #         , "planisfinish8": "0"
        #         , "plan9": "做事情的渴望"
        #         , "planisfinish9": "0"
        #         , "plan10": "修改有道云笔记的邮箱密码"
        #         , "planisfinish10": "1"
        #         , "plan11": "带吃的"
        #         , "planisfinish11": "0"
        #         , "plan12": "换运动裤"
        #         , "planisfinish12": "0"
        #         , "plan13": "地铁"
        #         , "planisfinish13": "0"
        #         , "plan14": "去瘾"
        #         , "planisfinish14": "0"
        #         , "plan15": "循环锻炼意志力去瘾，每天10次"
        #         , "planisfinish15": "0"
        #     }, {
        #         "id": "2"
        #         , "date": "2021-12-07"
        #         , "plan1": "打卡"
        #         , "planisfinish1": "1"
        #         , "plan2": "还钱"
        #         , "planisfinish2": "1"
        #         , "plan3": "基金"
        #         , "planisfinish3": "0"
        #         , "plan4": "学习"
        #         , "planisfinish4": "1"
        #         , "plan5": "草榴打卡"
        #         , "planisfinish5": "1"
        #         , "plan6": "发twitter"
        #         , "planisfinish6": "0"
        #         , "plan7": "打扫家"
        #         , "planisfinish7": "1"
        #         , "plan8": "穿短袖"
        #         , "planisfinish8": "0"
        #         , "plan9": "做事情的渴望"
        #         , "planisfinish9": "0"
        #     }]
        # }
        return result  # 必须加return

    # 修改数据 post接口
    if request.method == 'POST':
        print('前端调用接口 [post]，/plan')
        # 1. 获取选中行的数据
        sqlvaluedict = {
            "id": request.values.get('id'),
            "date": request.values.get('date'),
            "planid1": request.values.get('planid1'), "planisfinish1": request.values.get('planisfinish1'),
            "planid2": request.values.get('planid2'), "planisfinish2": request.values.get('planisfinish2'),
            "planid3": request.values.get('planid3'), "planisfinish3": request.values.get('planisfinish3'),
            "planid4": request.values.get('planid4'), "planisfinish4": request.values.get('planisfinish4'),
            "planid5": request.values.get('planid5'), "planisfinish5": request.values.get('planisfinish5'),
            "planid6": request.values.get('planid6'), "planisfinish6": request.values.get('planisfinish6'),
            "planid7": request.values.get('planid7'), "planisfinish7": request.values.get('planisfinish7'),
            "planid8": request.values.get('planid8'), "planisfinish8": request.values.get('planisfinish8'),
            "planid9": request.values.get('planid9'), "planisfinish9": request.values.get('planisfinish9'),
            "planid10": request.values.get('planid10'), "planisfinish10": request.values.get('planisfinish10'),
            "planid11": request.values.get('planid11'), "planisfinish11": request.values.get('planisfinish11'),
            "planid12": request.values.get('planid12'), "planisfinish12": request.values.get('planisfinish12'),
            "planid13": request.values.get('planid13'), "planisfinish13": request.values.get('planisfinish13'),
            "planid14": request.values.get('planid14'), "planisfinish14": request.values.get('planisfinish14'),
            "planid15": request.values.get('planid15'), "planisfinish15": request.values.get('planisfinish15'),
            "planid16": request.values.get('planid16'), "planisfinish16": request.values.get('planisfinish16'),
            "planid17": request.values.get('planid17'), "planisfinish17": request.values.get('planisfinish17'),
            "planid18": request.values.get('planid18'), "planisfinish18": request.values.get('planisfinish18'),
            "planid19": request.values.get('planid19'), "planisfinish19": request.values.get('planisfinish19'),
            "planid20": request.values.get('planid20'), "planisfinish20": request.values.get('planisfinish20'),
        }
        # 0.1 根据用户输入的str,判断plan表里是否有，没有插入
        # 获取数据库plan表所有的plan
        queryallplan_sql = 'select id,name from plan'
        allplan_result = plan.query_plan(queryallplan_sql)  # json
        # print('===================== allplan_result', allplan_result)
        # 所有name的数组
        allplannames_arr = []
        for item in allplan_result['data']:
            # print('item===========', item)
            # print('item["name"]===========', item['name'])
            # print('item.name===========', item.name)  # dict 错误写法
            allplannames_arr.append(item['name'])
        # print('所有name的数组===============', allplannames_arr)

        plandict = {
            "planid1": request.values.get('planid1'),
            "planid2": request.values.get('planid2'),
            "planid3": request.values.get('planid3'),
            "planid4": request.values.get('planid4'),
            "planid5": request.values.get('planid5'),
            "planid6": request.values.get('planid6'),
            "planid7": request.values.get('planid7'),
            "planid8": request.values.get('planid8'),
            "planid9": request.values.get('planid9'),
            "planid10": request.values.get('planid10'),
            "planid11": request.values.get('planid11'),
            "planid12": request.values.get('planid12'),
            "planid13": request.values.get('planid13'),
            "planid14": request.values.get('planid14'),
            "planid15": request.values.get('planid15'),
            "planid16": request.values.get('planid16'),
            "planid17": request.values.get('planid17'),
            "planid18": request.values.get('planid18'),
            "planid19": request.values.get('planid19'),
            "planid20": request.values.get('planid20')
        }
        # 不存在的插入plan数据表里
        for key, value in plandict.items():
            if value is None or value == '':
                pass
            else:
                if value not in allplannames_arr:
                    sql = 'insert into plan(name) values(%(name)s)'  # 插入
                    dbutil.execute(sql, {'name': value})

        # 2. 执行sql
        # 拼接sql 插入列
        sql_set = ""
        for key, value in sqlvaluedict.items():
            if value is None or value == "":  # 空
                sql_set += key + '=null,'  # 拼接set 语句
                # pass  # 这样写如果是空的不会修改，有bug
            else:  # 非空
                sql_set += key + '=%(' + key + ')s,'  # 拼接set 语句

        sql_set = sql_set.strip(",")
        sql = "update plan_list set " + sql_set + ' where id=%(id)s'
        print('sql-->sql_set==', sql_set)
        print('sql-->==', sql)

        # 执行
        # 将sqlvaluedict 里涉及str的转成plan表里的id
        # 再次获取数据库plan表所有的plan
        queryallplan_sql = 'select id,name from plan'
        allplan_result = plan.query_plan(queryallplan_sql)  # json
        print('=========== sqlvaluedict=', sqlvaluedict)
        print('=========== sqlvaluedict.items()=', sqlvaluedict.items())
        for key, value in sqlvaluedict.items():
            # print('===========key value=', key, value)
            if 'planid' in key and value != '':
                for item in allplan_result['data']:
                    if value == item['name']:
                        sqlvaluedict[key] = item['id']  # str --> int(id)
        print('转化后的 插入sql value = ', sqlvaluedict)
        result = plan_list.update_plan(sql, sqlvaluedict)
        print('修改结果=', result)

        # 3. 返回结果,默认返回plan.py 执行结果，不是json数据，返回默认
        resultjson['code'] = 200
        resultjson['msg'] = '修改成功'
        resultjson['count'] = 1
        if isinstance(result, dict):
            return result  # 判断是否是json格式，是就返回

    # 删除数据 delete接口
    if request.method == 'DELETE':
        print('前端调用接口 [delete]，/plan')
        # 1. 获取请求参数
        sqlvaluedict = {
            "id": request.values.get('id'),
            "date": request.values.get('date'),
            "planid1": request.values.get('planid1'), "planisfinish1": request.values.get('planisfinish1'),
            "planid2": request.values.get('planid2'), "planisfinish2": request.values.get('planisfinish2'),
            "planid3": request.values.get('planid3'), "planisfinish3": request.values.get('planisfinish3'),
            "planid4": request.values.get('planid4'), "planisfinish4": request.values.get('planisfinish4'),
            "planid5": request.values.get('planid5'), "planisfinish5": request.values.get('planisfinish5'),
            "planid6": request.values.get('planid6'), "planisfinish6": request.values.get('planisfinish6'),
            "planid7": request.values.get('planid7'), "planisfinish7": request.values.get('planisfinish7'),
            "planid8": request.values.get('planid8'), "planisfinish8": request.values.get('planisfinish8'),
            "planid9": request.values.get('planid9'), "planisfinish9": request.values.get('planisfinish9'),
            "planid10": request.values.get('planid10'), "planisfinish10": request.values.get('planisfinish10'),
            "planid11": request.values.get('planid11'), "planisfinish11": request.values.get('planisfinish11'),
            "planid12": request.values.get('planid12'), "planisfinish12": request.values.get('planisfinish12'),
            "planid13": request.values.get('planid13'), "planisfinish13": request.values.get('planisfinish13'),
            "planid14": request.values.get('planid14'), "planisfinish14": request.values.get('planisfinish14'),
            "planid15": request.values.get('planid15'), "planisfinish15": request.values.get('planisfinish15'),
            "planid16": request.values.get('planid16'), "planisfinish16": request.values.get('planisfinish16'),
            "planid17": request.values.get('planid17'), "planisfinish17": request.values.get('planisfinish17'),
            "planid18": request.values.get('planid18'), "planisfinish18": request.values.get('planisfinish18'),
            "planid19": request.values.get('planid19'), "planisfinish19": request.values.get('planisfinish19'),
            "planid20": request.values.get('planid20'), "planisfinish20": request.values.get('planisfinish20'),
        }
        # 2. 执行sql
        sql = 'delete from plan_list where id=%(id)s'
        result = plan_list.delete_plan(sql, sqlvaluedict)
        # 3. 返回结果
        resultjson['code'] = 200
        resultjson['msg'] = '删除成功'
        resultjson['count'] = 1
        if isinstance(result, dict):
            return result

    return resultjson


# ############################################################################################ [账号相关]
@app.route('/add_account.html')
def view_add_account():
    return render_template('/account/add_account.html')


@app.route('/account.html')
def view_account():
    return render_template('/account/account.html')


@app.route('/account', methods=('GET', 'POST', 'DELETE'))
def interface_account():
    default_result = {
        "code": 500,
        "msg": "",
        "count": 0,
        "data": []
    }
    # 获取数据
    if request.method == 'GET':
        print('前端调用接口[get]，/account')
        # 1. 获取请求参数
        page = int(request.values.get('page'))  # str
        limit = int(request.values.get('limit'))  # str-->int

        # 2. 数据库查询数据
        sql = 'select * from account order by id limit %(index)s, %(limit)s'
        values = dict()
        values.update({
            "index": (page - 1) * limit,
            "limit": limit
        })
        result = account.query_account(sql, values)

        return result  # 必须加return

    # 修改数据 post接口
    if request.method == 'POST':
        print('前端调用接口 [post]，/account')
        # 1. 获取选中行数据
        sqlvaluedict = {
            "id": int(request.values.get('id')),
            "type": request.values.get('type'),
            "sitename": request.values.get('sitename'),
            "sitetype": request.values.get('sitetype'),
            "url": request.values.get('url'),
            "username": request.values.get('username'),
            "initpw": request.values.get('initpw'),
            "newpw": request.values.get('newpw'),
            "email": request.values.get('email'),
            "phone": request.values.get('phone'),
            "QRcode": request.values.get('QRcode'),
            "key": request.values.get('key'),
            "pwrules": request.values.get('pwrules'),
            "safequestion": request.values.get('safequestion'),
            "safeanswer": request.values.get('safeanswer'),
            "createtime": request.values.get('createtime'),
            "updatetime": request.values.get('updatetime'),
            "isuseful": request.values.get('isuseful'),
            "remark": request.values.get('remark')
        }
        # 格式转换
        if type(sqlvaluedict['type']) == str:
            if sqlvaluedict['type'] == "":
                # sqlvaluedict['type'] = None # 报错
                sqlvaluedict['type'] = 0
            else:
                sqlvaluedict['type'] = int(sqlvaluedict['type'])
        if type(sqlvaluedict['isuseful']) == str:
            if sqlvaluedict['isuseful'] == "":
                sqlvaluedict['isuseful'] = None
            else:
                sqlvaluedict['isuseful'] = int(sqlvaluedict['isuseful'])
        sql = "update account set type=%(type)s,sitename=%(sitename)s,sitetype=%(sitetype)s,url=%(url)s,username=%(username)s," \
              "initpw=%(initpw)s,newpw=%(newpw)s,email=%(email)s,phone=%(phone)s,QRcode=%(QRcode)s,`key`=%(key)s,pwrules=%(pwrules)s," \
              "safequestion=%(safequestion)s,safeanswer=%(safeanswer)s,createtime=%(createtime)s,updatetime=%(updatetime)s, " \
              "isuseful=%(isuseful)s,remark=%(remark)s where id=%(id)s"

        result = account.update_account(sql, sqlvaluedict)
        if isinstance(result, dict):
            result['code'] = 200
            result['msg'] = '修改成功'
            result['count'] = 1
            return result  # 判断是否是json格式，是就返回

    # 删除数据 delete接口
    if request.method == 'DELETE':
        print('前端调用接口 [delete]，/account')
        # 1. 获取选中行数据
        sqlvaluedict = {
            "id": int(request.values.get('id')),
            "type": request.values.get('type'),
            "sitename": request.values.get('sitename'),
            "sitetype": request.values.get('sitetype'),
            "url": request.values.get('url'),
            "username": request.values.get('username'),
            "initpw": request.values.get('initpw'),
            "newpw": request.values.get('newpw'),
            "email": request.values.get('email'),
            "phone": request.values.get('phone'),
            "QRcode": request.values.get('QRcode'),
            "key": request.values.get('key'),
            "pwrules": request.values.get('pwrules'),
            "safequestion": request.values.get('safequestion'),
            "safeanswer": request.values.get('safeanswer'),
            "createtime": request.values.get('createtime'),
            "updatetime": request.values.get('updatetime'),
            "isuseful": request.values.get('isuseful'),
            "remark": request.values.get('remark')
        }
        # 格式转换
        if type(sqlvaluedict['type']) == str:
            if sqlvaluedict['type'] == "":
                sqlvaluedict['type'] = None
            else:
                sqlvaluedict['type'] = int(sqlvaluedict['type'])
        if type(sqlvaluedict['isuseful']) == str:
            if sqlvaluedict['isuseful'] == "":
                sqlvaluedict['isuseful'] = None
            else:
                sqlvaluedict['isuseful'] = int(sqlvaluedict['isuseful'])

        # 2. 执行sql
        sql = 'delete from account where id=%(id)s'
        result = account.delete_account(sql, sqlvaluedict)
        # 3. 返回结果
        if isinstance(result, dict):
            result['code'] = 200
            result['msg'] = '删除成功'
            result['count'] = 1
            return result
    return default_result  # 返回默认数据


@app.route('/add_account', methods=('GET', 'POST'))
def add_account():
    default_result = {
        "code": 500,
        "msg": "",
        "count": 0,
        "data": []
    }
    if request.method == 'POST':
        print('前端调用接口 [post]，add_account')
        # 0. 获取请求参数
        sqlvaluedict = {
            # "id": request.values.get('id'),
            "type": request.values.get('type'),
            "sitename": request.values.get('sitename'),
            "sitetype": request.values.get('sitetype'),
            "url": request.values.get('url'),
            "username": request.values.get('username'),
            "initpw": request.values.get('initpw'),
            "newpw": request.values.get('newpw'),
            "email": request.values.get('email'),
            "phone": request.values.get('phone'),
            "QRcode": request.values.get('QRcode'),
            "key": request.values.get('key'),
            "pwrules": request.values.get('pwrules'),
            "safequestion": request.values.get('safequestion'),
            "safeanswer": request.values.get('safeanswer'),
            "createtime": request.values.get('createtime'),
            "updatetime": request.values.get('updatetime'),
            "isuseful": request.values.get('isuseful'),
            "remark": request.values.get('remark')
        }
        # 格式转换
        if type(sqlvaluedict['type']) == str:
            if sqlvaluedict['type'] == "":
                # sqlvaluedict['type'] = None # 报错
                sqlvaluedict['type'] = 0
            else:
                sqlvaluedict['type'] = int(sqlvaluedict['type'])
        if type(sqlvaluedict['isuseful']) == str:
            if sqlvaluedict['isuseful'] == "":
                sqlvaluedict['isuseful'] = None
            else:
                sqlvaluedict['isuseful'] = int(sqlvaluedict['isuseful'])

        # 1. 执行sql

        add_account_sql = "insert into account(`type`, sitename, sitetype, url, username, initpw, newpw, email, phone, " \
                       "QRcode, `key`, pwrules, safequestion, safeanswer, createtime, updatetime, isuseful, remark) " \
                       "values(%(type)s, %(sitename)s,%(sitetype)s,%(url)s,%(username)s,%(initpw)s,%(newpw)s,%(email)s,%(phone)s," \
                       "%(QRcode)s,%(key)s,%(pwrules)s,%(safequestion)s,%(safeanswer)s,%(createtime)s,%(updatetime)s,%(isuseful)s,%(remark)s)"
        print('插入sql= ', add_account_sql)

        account.add_account(add_account_sql, sqlvaluedict)

    default_result['code'] =     200
    default_result['msg'] = '添加成功'
    default_result['count'] = 1
    return default_result  # 路由里必须添加return


@app.route('/audiobook.html')
def view_audiobook():
    return render_template('/audiobook/index.html')


@app.route('/audiobook', methods=('GET', 'POST', 'DELETE'))
def interface_audiobook():
    """
    接口:
    :return:
    """
    resultjson = {
        "code": 500,
        "msg": "",
        "count": 0,
        "data": []
    }
    # 获取数据
    if request.method == 'GET':
        print('前端调用接口[GET]，/audiobook')
        # 1. 获取请求参数
        typeid = None
        if "typeid" in request.values:
            typeid = int(request.values.get('typeid'))  # str -->int
        page = int(request.values.get('page'))  # str -->int
        limit = int(request.values.get('limit'))  # str-->int

        # 2. 数据库查询数据
        # eg SELECT customernumber, customername, creditlimit FROM customers LIMIT 0,5
        sql = f"select * from audiobook where typeid={typeid} order by id limit {(page-1) * limit}, {limit}"
        result = audiobook.query(sql)

        return result  # 必须加return


@app.route('/audiobook/chapter.html')
def view_audiobook_chapter():
    return render_template('/audiobook/chapter.html')


@app.route('/audiobook/xuanhuan.html')
def view_audiobook_xuanhuan():
    return render_template('/audiobook/xuanhuan.html')


@app.route('/audiobook/xuanhuan')
def interface_audiobook_xuanhuan():
    """
    接口: 玄幻
    :return:
    """
    resultjson = {
        "code": 500,
        "msg": "",
        "count": 0,
        "data": []
    }
    # 获取数据
    if request.method == 'GET':
        print('前端调用接口，/audiobook/xuanhuan')
        # 1. 获取请求参数
        page = int(request.values.get('page'))  # str
        limit = int(request.values.get('limit'))  # str-->int

        # 2. 数据库查询数据
        # eg SELECT customernumber, customername, creditlimit FROM customers LIMIT 0,5
        sql = f"select * from audiobook where typeid=2 order by id limit {(page-1) * limit}, {limit}"
        result = audiobook.query(sql)

        return result  # 必须加return


@app.route('/audiobook/wuxia.html')
def view_audiobook_wuxia():
    return render_template('/audiobook/wuxia.html')


@app.route('/audiobook/wuxia')
def interface_audiobook_wuxia():
    """
    接口: 武侠
    :return:
    """
    resultjson = {
        "code": 500,
        "msg": "",
        "count": 0,
        "data": []
    }
    # 获取数据
    if request.method == 'GET':
        print('前端调用接口，/audiobook/wuxia')
        # 1. 获取请求参数
        page = int(request.values.get('page'))  # str
        limit = int(request.values.get('limit'))  # str-->int

        # 2. 数据库查询数据
        # eg SELECT customernumber, customername, creditlimit FROM customers LIMIT 0,5
        sql = f"select * from audiobook where typeid=3 order by id limit {(page-1) * limit}, {limit}"
        result = audiobook.query(sql)

        return result  # 必须加return


@app.route('/audiobook/dushi.html')
def view_audiobook_dushi():
    return render_template('/audiobook/dushi.html')


@app.route('/audiobook/dushi')
def interface_audiobook_dushi():
    """
    接口: 都市
    :return:
    """
    resultjson = {
        "code": 500,
        "msg": "",
        "count": 0,
        "data": []
    }
    # 获取数据
    if request.method == 'GET':
        print('前端调用接口，/audiobook/dushi')
        # 1. 获取请求参数
        page = int(request.values.get('page'))  # str
        limit = int(request.values.get('limit'))  # str-->int

        # 2. 数据库查询数据
        # eg SELECT customernumber, customername, creditlimit FROM customers LIMIT 0,5
        sql = f"select * from audiobook where typeid=4 order by id limit {(page-1) * limit}, {limit}"
        result = audiobook.query(sql)

        return result  # 必须加return


@app.route('/audiobook/yanqing.html')
def view_audiobook_yanqing():
    return render_template('/audiobook/yanqing.html')


@app.route('/audiobook/yanqing')
def interface_audiobook_yanqing():
    """
    接口: 言情
    :return:
    """
    resultjson = {
        "code": 500,
        "msg": "",
        "count": 0,
        "data": []
    }
    # 获取数据
    if request.method == 'GET':
        print('前端调用接口，/audiobook/yanqing')
        # 1. 获取请求参数
        page = int(request.values.get('page'))  # str
        limit = int(request.values.get('limit'))  # str-->int

        # 2. 数据库查询数据
        # eg SELECT customernumber, customername, creditlimit FROM customers LIMIT 0,5
        sql = f"select * from audiobook where typeid=5 order by id limit {(page-1) * limit}, {limit}"
        result = audiobook.query(sql)

        return result  # 必须加return


@app.route('/audiobook/kehuan.html')
def view_audiobook_kehuan():
    return render_template('/audiobook/kehuan.html')


@app.route('/audiobook/kehuan')
def interface_audiobook_kehuan():
    """
    接口: 科幻
    :return:
    """
    resultjson = {
        "code": 500,
        "msg": "",
        "count": 0,
        "data": []
    }
    # 获取数据
    if request.method == 'GET':
        print('前端调用接口，/audiobook/kehuan')
        # 1. 获取请求参数
        page = int(request.values.get('page'))  # str
        limit = int(request.values.get('limit'))  # str-->int

        # 2. 数据库查询数据
        # eg SELECT customernumber, customername, creditlimit FROM customers LIMIT 0,5
        sql = f"select * from audiobook where typeid=6 order by id limit {(page-1) * limit}, {limit}"
        result = audiobook.query(sql)

        return result  # 必须加return


@app.route('/audiobook/tuili.html')
def view_audiobook_tuili():
    return render_template('/audiobook/tuili.html')


@app.route('/audiobook/tuili')
def interface_audiobook_tuili():
    """
    接口: 推理
    :return:
    """
    resultjson = {
        "code": 500,
        "msg": "",
        "count": 0,
        "data": []
    }
    # 获取数据
    if request.method == 'GET':
        print('前端调用接口，/audiobook/tuili')
        # 1. 获取请求参数
        page = int(request.values.get('page'))  # str
        limit = int(request.values.get('limit'))  # str-->int

        # 2. 数据库查询数据
        # eg SELECT customernumber, customername, creditlimit FROM customers LIMIT 0,5
        sql = f"select * from audiobook where typeid=7 order by id limit {(page-1) * limit}, {limit}"
        result = audiobook.query(sql)

        return result  # 必须加return


@app.route('/audiobook/kongbu.html')
def view_audiobook_kongbu():
    return render_template('/audiobook/kongbu.html')


@app.route('/audiobook/kongbu')
def interface_audiobook_kongbu():
    """
    接口: 恐怖
    :return:
    """
    resultjson = {
        "code": 500,
        "msg": "",
        "count": 0,
        "data": []
    }
    # 获取数据
    if request.method == 'GET':
        print('前端调用接口，/audiobook/kongbu')
        # 1. 获取请求参数
        page = int(request.values.get('page'))  # str
        limit = int(request.values.get('limit'))  # str-->int

        # 2. 数据库查询数据
        # eg SELECT customernumber, customername, creditlimit FROM customers LIMIT 0,5
        sql = f"select * from audiobook where typeid=8 order by id limit {(page-1) * limit}, {limit}"
        result = audiobook.query(sql)

        return result  # 必须加return


@app.route('/audiobook/jingsong.html')
def view_audiobook_jingsong():
    return render_template('/audiobook/jingsong.html')


@app.route('/audiobook/jingsong')
def interface_audiobook_jingsong():
    """
    接口: 惊悚
    :return:
    """
    resultjson = {
        "code": 500,
        "msg": "",
        "count": 0,
        "data": []
    }
    # 获取数据
    if request.method == 'GET':
        print('前端调用接口，/audiobook/jingsong')
        # 1. 获取请求参数
        page = int(request.values.get('page'))  # str
        limit = int(request.values.get('limit'))  # str-->int

        # 2. 数据库查询数据
        # eg SELECT customernumber, customername, creditlimit FROM customers LIMIT 0,5
        sql = f"select * from audiobook where typeid=9 order by id limit {(page-1) * limit}, {limit}"
        result = audiobook.query(sql)

        return result  # 必须加return


@app.route('/audiobook/lishi.html')
def view_audiobook_lishi():
    return render_template('/audiobook/lishi.html')


@app.route('/audiobook/lishi')
def interface_audiobook_lishi():
    """
    接口: 历史
    :return:
    """
    resultjson = {
        "code": 500,
        "msg": "",
        "count": 0,
        "data": []
    }
    # 获取数据
    if request.method == 'GET':
        print('前端调用接口，/audiobook/lishi')
        # 1. 获取请求参数
        page = int(request.values.get('page'))  # str
        limit = int(request.values.get('limit'))  # str-->int

        # 2. 数据库查询数据
        # eg SELECT customernumber, customername, creditlimit FROM customers LIMIT 0,5
        sql = f"select * from audiobook where typeid=10 order by id limit {(page-1) * limit}, {limit}"
        result = audiobook.query(sql)

        return result  # 必须加return


@app.route('/audiobook/junshi.html')
def view_audiobook_junshi():
    return render_template('/audiobook/junshi.html')


@app.route('/audiobook/junshi')
def interface_audiobook_junshi():
    """
    接口: 军事
    :return:
    """
    resultjson = {
        "code": 500,
        "msg": "",
        "count": 0,
        "data": []
    }
    # 获取数据
    if request.method == 'GET':
        print('前端调用接口，/audiobook/junshi')
        # 1. 获取请求参数
        page = int(request.values.get('page'))  # str
        limit = int(request.values.get('limit'))  # str-->int

        # 2. 数据库查询数据
        # eg SELECT customernumber, customername, creditlimit FROM customers LIMIT 0,5
        sql = f"select * from audiobook where typeid=11 order by id limit {(page-1) * limit}, {limit}"
        result = audiobook.query(sql)

        return result  # 必须加return


@app.route('/audiobook/wangyou.html')
def view_audiobook_wangyou():
    return render_template('/audiobook/wangyou.html')


@app.route('/audiobook/wangyou')
def interface_audiobook_wangyou():
    """
    接口: 网游
    :return:
    """
    resultjson = {
        "code": 500,
        "msg": "",
        "count": 0,
        "data": []
    }
    # 获取数据
    if request.method == 'GET':
        print('前端调用接口，/audiobook/wangyou')
        # 1. 获取请求参数
        page = int(request.values.get('page'))  # str
        limit = int(request.values.get('limit'))  # str-->int

        # 2. 数据库查询数据
        # eg SELECT customernumber, customername, creditlimit FROM customers LIMIT 0,5
        sql = f"select * from audiobook where typeid=12 order by id limit {(page-1) * limit}, {limit}"
        result = audiobook.query(sql)

        return result  # 必须加return


@app.route('/audiobook/guanshang.html')
def view_audiobook_guanshang():
    return render_template('/audiobook/guanshang.html')


@app.route('/audiobook/guanshang')
def interface_audiobook_guanshang():
    """
    接口: 官商
    :return:
    """
    resultjson = {
        "code": 500,
        "msg": "",
        "count": 0,
        "data": []
    }
    # 获取数据
    if request.method == 'GET':
        print('前端调用接口，/audiobook/guanshang')
        # 1. 获取请求参数
        page = int(request.values.get('page'))  # str
        limit = int(request.values.get('limit'))  # str-->int

        # 2. 数据库查询数据
        # eg SELECT customernumber, customername, creditlimit FROM customers LIMIT 0,5
        sql = f"select * from audiobook where typeid=13 order by id limit {(page-1) * limit}, {limit}"
        result = audiobook.query(sql)

        return result  # 必须加return


@app.route('/audiobook/pingshu.html')
def view_audiobook_pingshu():
    return render_template('/audiobook/pingshu.html')


@app.route('/audiobook/pingshu')
def interface_audiobook_pingshu():
    """
    接口: 评书
    :return:
    """
    resultjson = {
        "code": 500,
        "msg": "",
        "count": 0,
        "data": []
    }
    # 获取数据
    if request.method == 'GET':
        print('前端调用接口，/audiobook/pingshu')
        # 1. 获取请求参数
        page = int(request.values.get('page'))  # str
        limit = int(request.values.get('limit'))  # str-->int

        # 2. 数据库查询数据
        # eg SELECT customernumber, customername, creditlimit FROM customers LIMIT 0,5
        sql = f"select * from audiobook where typeid=14 order by id limit {(page-1) * limit}, {limit}"
        result = audiobook.query(sql)

        return result  # 必须加return


@app.route('/audiobook/xiangsheng.html')
def view_audiobook_xiangsheng():
    return render_template('/audiobook/xiangsheng.html')


@app.route('/audiobook/xiangsheng')
def interface_audiobook_xiangsheng():
    """
    接口: chuanyue
    :return:
    """
    resultjson = {
        "code": 500,
        "msg": "",
        "count": 0,
        "data": []
    }
    # 获取数据
    if request.method == 'GET':
        print('前端调用接口，/audiobook/xiangsheng')
        # 1. 获取请求参数
        page = int(request.values.get('page'))  # str
        limit = int(request.values.get('limit'))  # str-->int

        # 2. 数据库查询数据
        # eg SELECT customernumber, customername, creditlimit FROM customers LIMIT 0,5
        sql = f"select * from audiobook where typeid=15 order by id limit {(page-1) * limit}, {limit}"
        result = audiobook.query(sql)

        return result  # 必须加return


@app.route('/audiobook/wenxue.html')
def view_audiobook_wenxue():
    return render_template('/audiobook/wenxue.html')


@app.route('/audiobook/wenxue')
def interface_audiobook_wenxue():
    """
    接口: chuanyue
    :return:
    """
    resultjson = {
        "code": 500,
        "msg": "",
        "count": 0,
        "data": []
    }
    # 获取数据
    if request.method == 'GET':
        print('前端调用接口，/audiobook/wenxue')
        # 1. 获取请求参数
        page = int(request.values.get('page'))  # str
        limit = int(request.values.get('limit'))  # str-->int

        # 2. 数据库查询数据
        # eg SELECT customernumber, customername, creditlimit FROM customers LIMIT 0,5
        sql = f"select * from audiobook where typeid=16 order by id limit {(page-1) * limit}, {limit}"
        result = audiobook.query(sql)

        return result  # 必须加return


@app.route('/audiobook/ertong.html')
def view_audiobook_ertong():
    return render_template('/audiobook/ertong.html')


@app.route('/audiobook/ertong')
def interface_audiobook_ertong():
    """
    接口: chuanyue
    :return:
    """
    resultjson = {
        "code": 500,
        "msg": "",
        "count": 0,
        "data": []
    }
    # 获取数据
    if request.method == 'GET':
        print('前端调用接口，/audiobook/ertong')
        # 1. 获取请求参数
        page = int(request.values.get('page'))  # str
        limit = int(request.values.get('limit'))  # str-->int

        # 2. 数据库查询数据
        # eg SELECT customernumber, customername, creditlimit FROM customers LIMIT 0,5
        sql = f"select * from audiobook where typeid=17 order by id limit {(page-1) * limit}, {limit}"
        result = audiobook.query(sql)

        return result  # 必须加return


@app.route('/audiobook/chuanyue.html')
def view_audiobook_chuanyue():
    return render_template('/audiobook/chuanyue.html')


@app.route('/audiobook/chuanyue')
def interface_audiobook_chuanyue():
    """
    接口: chuanyue
    :return:
    """
    resultjson = {
        "code": 500,
        "msg": "",
        "count": 0,
        "data": []
    }
    # 获取数据
    if request.method == 'GET':
        print('前端调用接口，/audiobook/chuanyue')
        # 1. 获取请求参数
        page = int(request.values.get('page'))  # str
        limit = int(request.values.get('limit'))  # str-->int

        # 2. 数据库查询数据
        # eg SELECT customernumber, customername, creditlimit FROM customers LIMIT 0,5
        sql = f"select * from audiobook where typeid=18 order by id limit {(page-1) * limit}, {limit}"
        result = audiobook.query(sql)

        return result  # 必须加return


@app.route('/audiobook/yule.html')
def view_audiobook_yule():
    return render_template('/audiobook/yule.html')


@app.route('/audiobook/yule')
def interface_audiobook_yule():
    """
    接口: 娱乐
    :return:
    """
    resultjson = {
        "code": 500,
        "msg": "",
        "count": 0,
        "data": []
    }
    # 获取数据
    if request.method == 'GET':
        print('前端调用接口，/audiobook/yule')
        # 1. 获取请求参数
        page = int(request.values.get('page'))  # str
        limit = int(request.values.get('limit'))  # str-->int

        # 2. 数据库查询数据
        # eg SELECT customernumber, customername, creditlimit FROM customers LIMIT 0,5
        sql = f"select * from audiobook where typeid=19 order by id limit {(page-1) * limit}, {limit}"
        result = audiobook.query(sql)

        return result  # 必须加return


@app.route('/audiobook/xiaohua.html')
def view_audiobook_xiaohua():
    return render_template('/audiobook/xiaohua.html')


@app.route('/audiobook/xiaohua')
def interface_audiobook_xiaohua():
    """
    接口: 戏曲
    :return:
    """
    resultjson = {
        "code": 500,
        "msg": "",
        "count": 0,
        "data": []
    }
    # 获取数据
    if request.method == 'GET':
        print('前端调用接口，/audiobook/xiaohua')
        # 1. 获取请求参数
        page = int(request.values.get('page'))  # str
        limit = int(request.values.get('limit'))  # str-->int

        # 2. 数据库查询数据
        # eg SELECT customernumber, customername, creditlimit FROM customers LIMIT 0,5
        sql = f"select * from audiobook where typeid=20 order by id limit {(page-1) * limit}, {limit}"
        result = audiobook.query(sql)

        return result  # 必须加return


@app.route('/audiobook/xiqu.html')
def view_audiobook_xiqu():
    return render_template('/audiobook/xiqu.html')


@app.route('/audiobook/xiqu')
def interface_audiobook_xiqu():
    """
    接口: 戏曲
    :return:
    """
    resultjson = {
        "code": 500,
        "msg": "",
        "count": 0,
        "data": []
    }
    # 获取数据
    if request.method == 'GET':
        print('前端调用接口，/audiobook/xiqu')
        # 1. 获取请求参数
        page = int(request.values.get('page'))  # str
        limit = int(request.values.get('limit'))  # str-->int

        # 2. 数据库查询数据
        # eg SELECT customernumber, customername, creditlimit FROM customers LIMIT 0,5
        sql = f"select * from audiobook where typeid=21 order by id limit {(page-1) * limit}, {limit}"

        result = audiobook.query(sql)
        print('查询audiobook --> result == ', result)

        return result  # 必须加return


@app.route('/audiobook/baijiajiangtan.html')
def view_audiobook_baijiajiangtan():
    return render_template('/audiobook/baijiajiangtan.html')


@app.route('/audiobook/baijiajiangtan')
def interface_audiobook_baijiajiangtan():
    resultjson = {
        "code": 500,
        "msg": "",
        "count": 0,
        "data": []
    }
    # 获取数据
    if request.method == 'GET':
        print('前端调用接口，/audiobook/baijiajiangtan')
        # 1. 获取请求参数
        page = int(request.values.get('page'))  # str
        limit = int(request.values.get('limit'))  # str-->int

        # 2. 数据库查询数据
        # eg SELECT customernumber, customername, creditlimit FROM customers LIMIT 0,5
        sql = f"select * from audiobook where typeid=22 order by id limit {(page-1) * limit}, {limit}"

        result = audiobook.query(sql)
        print('查询audiobook --> result == ', result)

        return result  # 必须加return

    # 修改数据 post接口
    if request.method == 'POST':
        print('前端调用接口 [post]，/plan')
        # 1. 获取选中行的数据
        sqlvaluedict = {
            "id": request.values.get('id'),
            "date": request.values.get('date'),
            "planid1": request.values.get('planid1'), "planisfinish1": request.values.get('planisfinish1'),
            "planid2": request.values.get('planid2'), "planisfinish2": request.values.get('planisfinish2'),
            "planid3": request.values.get('planid3'), "planisfinish3": request.values.get('planisfinish3'),
            "planid4": request.values.get('planid4'), "planisfinish4": request.values.get('planisfinish4'),
            "planid5": request.values.get('planid5'), "planisfinish5": request.values.get('planisfinish5'),
            "planid6": request.values.get('planid6'), "planisfinish6": request.values.get('planisfinish6'),
            "planid7": request.values.get('planid7'), "planisfinish7": request.values.get('planisfinish7'),
            "planid8": request.values.get('planid8'), "planisfinish8": request.values.get('planisfinish8'),
            "planid9": request.values.get('planid9'), "planisfinish9": request.values.get('planisfinish9'),
            "planid10": request.values.get('planid10'), "planisfinish10": request.values.get('planisfinish10'),
            "planid11": request.values.get('planid11'), "planisfinish11": request.values.get('planisfinish11'),
            "planid12": request.values.get('planid12'), "planisfinish12": request.values.get('planisfinish12'),
            "planid13": request.values.get('planid13'), "planisfinish13": request.values.get('planisfinish13'),
            "planid14": request.values.get('planid14'), "planisfinish14": request.values.get('planisfinish14'),
            "planid15": request.values.get('planid15'), "planisfinish15": request.values.get('planisfinish15'),
            "planid16": request.values.get('planid16'), "planisfinish16": request.values.get('planisfinish16'),
            "planid17": request.values.get('planid17'), "planisfinish17": request.values.get('planisfinish17'),
            "planid18": request.values.get('planid18'), "planisfinish18": request.values.get('planisfinish18'),
            "planid19": request.values.get('planid19'), "planisfinish19": request.values.get('planisfinish19'),
            "planid20": request.values.get('planid20'), "planisfinish20": request.values.get('planisfinish20'),
        }
        # 0.1 根据用户输入的str,判断plan表里是否有，没有插入
        # 获取数据库plan表所有的plan
        queryallplan_sql = 'select id,name from plan'
        allplan_result = plan.query_plan(queryallplan_sql)  # json
        # print('===================== allplan_result', allplan_result)
        # 所有name的数组
        allplannames_arr = []
        for item in allplan_result['data']:
            # print('item===========', item)
            # print('item["name"]===========', item['name'])
            # print('item.name===========', item.name)  # dict 错误写法
            allplannames_arr.append(item['name'])
        # print('所有name的数组===============', allplannames_arr)

        plandict = {
            "planid1": request.values.get('planid1'),
            "planid2": request.values.get('planid2'),
            "planid3": request.values.get('planid3'),
            "planid4": request.values.get('planid4'),
            "planid5": request.values.get('planid5'),
            "planid6": request.values.get('planid6'),
            "planid7": request.values.get('planid7'),
            "planid8": request.values.get('planid8'),
            "planid9": request.values.get('planid9'),
            "planid10": request.values.get('planid10'),
            "planid11": request.values.get('planid11'),
            "planid12": request.values.get('planid12'),
            "planid13": request.values.get('planid13'),
            "planid14": request.values.get('planid14'),
            "planid15": request.values.get('planid15'),
            "planid16": request.values.get('planid16'),
            "planid17": request.values.get('planid17'),
            "planid18": request.values.get('planid18'),
            "planid19": request.values.get('planid19'),
            "planid20": request.values.get('planid20')
        }
        # 不存在的插入plan数据表里
        for key, value in plandict.items():
            if value is None or value == '':
                pass
            else:
                if value not in allplannames_arr:
                    sql = 'insert into plan(name) values(%(name)s)'  # 插入
                    dbutil.execute(sql, {'name': value})

        # 2. 执行sql
        # 拼接sql 插入列
        sql_set = ""
        for key, value in sqlvaluedict.items():
            if value is None or value == "":  # 空
                sql_set += key + '=null,'  # 拼接set 语句
                # pass  # 这样写如果是空的不会修改，有bug
            else:  # 非空
                sql_set += key + '=%(' + key + ')s,'  # 拼接set 语句

        sql_set = sql_set.strip(",")
        sql = "update plan_list set " + sql_set + ' where id=%(id)s'
        print('sql-->sql_set==', sql_set)
        print('sql-->==', sql)

        # 执行
        # 将sqlvaluedict 里涉及str的转成plan表里的id
        # 再次获取数据库plan表所有的plan
        queryallplan_sql = 'select id,name from plan'
        allplan_result = plan.query_plan(queryallplan_sql)  # json
        print('=========== sqlvaluedict=', sqlvaluedict)
        print('=========== sqlvaluedict.items()=', sqlvaluedict.items())
        for key, value in sqlvaluedict.items():
            # print('===========key value=', key, value)
            if 'planid' in key and value != '':
                for item in allplan_result['data']:
                    if value == item['name']:
                        sqlvaluedict[key] = item['id']  # str --> int(id)
        print('转化后的 插入sql value = ', sqlvaluedict)
        result = plan_list.update_plan(sql, sqlvaluedict)
        print('修改结果=', result)

        # 3. 返回结果,默认返回plan.py 执行结果，不是json数据，返回默认
        resultjson['code'] = 200
        resultjson['msg'] = '修改成功'
        resultjson['count'] = 1
        if isinstance(result, dict):
            return result  # 判断是否是json格式，是就返回

    # 删除数据 delete接口
    if request.method == 'DELETE':
        print('前端调用接口 [delete]，/plan')
        # 1. 获取请求参数
        sqlvaluedict = {
            "id": request.values.get('id'),
            "date": request.values.get('date'),
            "planid1": request.values.get('planid1'), "planisfinish1": request.values.get('planisfinish1'),
            "planid2": request.values.get('planid2'), "planisfinish2": request.values.get('planisfinish2'),
            "planid3": request.values.get('planid3'), "planisfinish3": request.values.get('planisfinish3'),
            "planid4": request.values.get('planid4'), "planisfinish4": request.values.get('planisfinish4'),
            "planid5": request.values.get('planid5'), "planisfinish5": request.values.get('planisfinish5'),
            "planid6": request.values.get('planid6'), "planisfinish6": request.values.get('planisfinish6'),
            "planid7": request.values.get('planid7'), "planisfinish7": request.values.get('planisfinish7'),
            "planid8": request.values.get('planid8'), "planisfinish8": request.values.get('planisfinish8'),
            "planid9": request.values.get('planid9'), "planisfinish9": request.values.get('planisfinish9'),
            "planid10": request.values.get('planid10'), "planisfinish10": request.values.get('planisfinish10'),
            "planid11": request.values.get('planid11'), "planisfinish11": request.values.get('planisfinish11'),
            "planid12": request.values.get('planid12'), "planisfinish12": request.values.get('planisfinish12'),
            "planid13": request.values.get('planid13'), "planisfinish13": request.values.get('planisfinish13'),
            "planid14": request.values.get('planid14'), "planisfinish14": request.values.get('planisfinish14'),
            "planid15": request.values.get('planid15'), "planisfinish15": request.values.get('planisfinish15'),
            "planid16": request.values.get('planid16'), "planisfinish16": request.values.get('planisfinish16'),
            "planid17": request.values.get('planid17'), "planisfinish17": request.values.get('planisfinish17'),
            "planid18": request.values.get('planid18'), "planisfinish18": request.values.get('planisfinish18'),
            "planid19": request.values.get('planid19'), "planisfinish19": request.values.get('planisfinish19'),
            "planid20": request.values.get('planid20'), "planisfinish20": request.values.get('planisfinish20'),
        }
        # 2. 执行sql
        sql = 'delete from plan_list where id=%(id)s'
        result = plan_list.delete_plan(sql, sqlvaluedict)
        # 3. 返回结果
        resultjson['code'] = 200
        resultjson['msg'] = '删除成功'
        resultjson['count'] = 1
        if isinstance(result, dict):
            return result

    return resultjson


@app.route('/audiobook/qita')
def interface_audiobook_qita():
    """
    接口: 其它
    :return:
    """
    resultjson = {
        "code": 500,
        "msg": "",
        "count": 0,
        "data": []
    }
    # 获取数据
    if request.method == 'GET':
        print('前端调用接口，/audiobook/qita')
        # 1. 获取请求参数
        page = int(request.values.get('page'))  # str
        limit = int(request.values.get('limit'))  # str-->int

        # 2. 数据库查询数据
        # eg SELECT customernumber, customername, creditlimit FROM customers LIMIT 0,5
        sql = f"select * from audiobook where typeid=1 order by id limit {(page-1) * limit}, {limit}"
        result = audiobook.query(sql)

        return result  # 必须加return


@app.route('/audiobook/all')
def interface_audiobook_all():
    """
    接口: 所有
    :return:
    """
    resultjson = {
        "code": 500,
        "msg": "",
        "count": 0,
        "data": []
    }
    # 获取数据
    if request.method == 'GET':
        print('前端调用接口，/audiobook/all')
        # 1. 获取请求参数
        page = int(request.values.get('page'))  # str
        limit = int(request.values.get('limit'))  # str-->int

        # 2. 数据库查询数据
        # eg SELECT customernumber, customername, creditlimit FROM customers LIMIT 0,5
        sql = f"select * from audiobook order by id limit {(page-1) * limit}, {limit}"
        result = audiobook.query(sql)

        return result  # 必须加return


@app.route('/spider/audiobook', methods=('GET', 'POST', 'DELETE'))
def spider_audiobook():
    default_result = {
        "code": 500,
        "msg": "",
        "count": 0,
        "data": []
    }

    # 修改数据 post接口
    if request.method == 'POST':
        print('前端调用接口 [post]，/audiobook')
        # 1. 获取选中行数据
        print('启动爬取章节线程。。')
        # 1. 从一个网站的url (各种分类的url,几个分类起几个线程)
        # 玄幻 https://www.tingbook.cc/book/1.html
        # 武侠 https://www.tingbook.cc/book/2.html
        # 都市 https://www.tingbook.cc/book/3.html
        # 言情 https://www.tingbook.cc/book/4.html
        # 科幻 https://www.tingbook.cc/book/5.html
        # 推理 https://www.tingbook.cc/book/6.html
        # 恐怖 https://www.tingbook.cc/book/7.html
        # 惊悚 https://www.tingbook.cc/book/8.html
        # 历史 https://www.tingbook.cc/book/9.html
        # 军事 https://www.tingbook.cc/book/10.html
        # 网游 https://www.tingbook.cc/book/11.html
        # 官商 https://www.tingbook.cc/book/12.html
        # 评书 https://www.tingbook.cc/book/13.html
        # 相声 https://www.tingbook.cc/book/14.html
        # 文学 https://www.tingbook.cc/book/15.html
        # 儿童 https://www.tingbook.cc/book/16.html
        # 穿越 https://www.tingbook.cc/book/28.html
        # 娱乐 https://www.tingbook.cc/book/29.html
        # 笑话 https://www.tingbook.cc/book/30.html
        # 戏曲 https://www.tingbook.cc/book/31.html
        # 其它 https://www.tingbook.cc/book/32.html
        # 百家讲坛 https://www.tingbook.cc/book/33.html
        # 评书专区 https://www.52pingshu.com/
        # app下载 https://tingbook.cc/downapp/
        # util.create_thrads_by_class_threading()
        category_dict = {
            # html_cateoryid : typeid (数据库)
            "1": 2,
            "2": 3,
            "3": 4,
            "4": 5,
            "5": 6,
            "6": 7,
            "7": 8,
            "8": 9,
            "9": 10,
            "10": 11,
            "11": 12,
            "12": 13,
            "13": 14,
            "14": 15,
            "15": 16,
            "16": 17,
            "28": 18,
            "29": 19,
            "30": 20,
            "31": 21,
            "32": 1,
            "33": 22,
            "type1": "玄幻",
            "type2": "武侠",
            "type3": "都市",
            "type4": "言情",
            "type5": "科幻",
            "type6": "推理",
            "type7": "恐怖",
            "type8": "惊悚",
            "type9": "历史",
            "type10": "军事",
            "type11": "网游",
            "type12": "官商",
            "type13": "评书",
            "type14": "相声",
            "type15": "文学",
            "type16": "儿童",
            "type28": "穿越",
            "type29": "娱乐",
            "type30": "笑话",
            "type31": "戏曲",
            "type32": "其它",
            "type33": "百家讲坛",
        }
        # 目前的写法是，顺序执行，如果第一类爬完了，才执行下一类
        audiobook.spider_audiobook('https://www.tingbook.cc/book/1.html', category_dict, 10)  # 玄幻
        audiobook.spider_audiobook('https://www.tingbook.cc/book/2.html', category_dict, 10)  # 武侠
        audiobook.spider_audiobook('https://www.tingbook.cc/book/3.html', category_dict, 10)  # 都市
        audiobook.spider_audiobook('https://www.tingbook.cc/book/4.html', category_dict, 10)  # 言情
        audiobook.spider_audiobook('https://www.tingbook.cc/book/5.html', category_dict, 10)  # 科幻
        audiobook.spider_audiobook('https://www.tingbook.cc/book/6.html', category_dict, 10)  # 推理
        audiobook.spider_audiobook('https://www.tingbook.cc/book/7.html', category_dict, 10)  # 恐怖
        audiobook.spider_audiobook('https://www.tingbook.cc/book/8.html', category_dict, 10)  # 惊悚
        audiobook.spider_audiobook('https://www.tingbook.cc/book/9.html', category_dict, 10)  # 历史
        audiobook.spider_audiobook('https://www.tingbook.cc/book/10.html', category_dict, 10)  # 军事
        audiobook.spider_audiobook('https://www.tingbook.cc/book/11.html', category_dict, 10)  # 网游
        audiobook.spider_audiobook('https://www.tingbook.cc/book/12.html', category_dict, 10)  # 官商
        audiobook.spider_audiobook('https://www.tingbook.cc/book/13.html', category_dict, 10)  # 评书
        audiobook.spider_audiobook('https://www.tingbook.cc/book/14.html', category_dict, 10)  # 相声
        audiobook.spider_audiobook('https://www.tingbook.cc/book/16.html', category_dict, 10)  # 儿童
        audiobook.spider_audiobook('https://www.tingbook.cc/book/28.html', category_dict, 10)  # 穿越
        audiobook.spider_audiobook('https://www.tingbook.cc/book/29.html', category_dict, 10)  # 娱乐
        audiobook.spider_audiobook('https://www.tingbook.cc/book/30.html', category_dict, 10)  # 笑话
        audiobook.spider_audiobook('https://www.tingbook.cc/book/31.html', category_dict, 10)  # 戏曲
        audiobook.spider_audiobook('https://www.tingbook.cc/book/32.html', category_dict, 10)  # 其它
        audiobook.spider_audiobook('https://www.tingbook.cc/book/33.html', category_dict, 10)  # 百家讲坛

    # 删除数据 delete接口
    if request.method == 'DELETE':
        print('前端调用接口 [post]，/audiobook')
        util.close_thrads_by_class_threading()

    return default_result  # 返回默认数据


@app.route('/test.html')
def view_test():
    # audiobook.test()
    util.fun1()
    return "Hello"
    # return render_template('/audiobook/test.html')


@app.route('/audiobook_chapter', methods=('GET', 'POST', 'DELETE'))
def interface_audiobook_chapter():
    # 思路:
    # 循环:
    # 1. 从数据库取10条未爬取的book的url, -->插入线程池 -->过60秒检测-->任务都做完了,就再加10条任务-->任务没做完,过60秒继续检查
    all_task = []
    default_task_num = 40  # 默认添加几个任务
    default_loop_time = 10  # 默认轮询时间,查询是否任务列表空了
    while True:
        if len(all_task) < 5:
            print(f'--------------任务列表 <5,添加{default_task_num}个任务')
            # 1. 从数据库取10条未爬取的book的url
            sql = f'select id, name, url from audiobook where spider_status=0 limit 0,{default_task_num}'
            result_tuple = dbutil.execute_project('audiobook', sql)
            print(f'获取10条书的url= {result_tuple}')

            if len(result_tuple) == 0:
                print('有声书spider_status =0 个数为0,所有有声书爬取完成,主线程应结束!!!')
                break
            # 2. 给线程池添加 10 个任务-爬取书的章节(每个方法,自动更新数据库)
            print('线程池添加任务,爬取书的章节,存入数据库...')
            for i in range(default_task_num):  # 初始化10个
                if i > len(result_tuple):
                    break
                print(f'爬取audiobook, id={result_tuple[i][0]}, name={result_tuple[i][1]}, url={result_tuple[i][2]}')
                task = threadutil.THREADPOOL.submit(audiobook.spider_chapters, "https://www.tingbook.cc", result_tuple[i][0], result_tuple[i][1], result_tuple[i][2])
                all_task.append(task)

        else:
            print(f'--------------任务列表 !!!! >=5, 剩余任务{len(all_task)}个')

        print('等待60秒,查询任务状态==========================')
        for second in range(default_loop_time):
            print(f'主线程休眠 {second} 秒')
        time.sleep(default_loop_time)  # 1分钟检查一次
        print(f'----------------> 当前所有的任务列表{ len(all_task) }个= {all_task}')
        # print(f'----------------> 当前所有的 线程池 列表 {threadutil.THREADPOOL}')

        for task in as_completed(all_task):
            print(f'共有任务 {len(all_task)}, 查询当前任务task = {task}')
            if task.done() is True:
                print(f'任务{task} 完成了, 删除!')
                all_task.remove(task)

        '''  # 能用,但不好
        for index, task in enumerate(all_task):
            if task.done() is False:
                break

            # 判断最后一次,线程执行完毕后,添加新线程
            if index == len(all_task) - 1:
                all_task = []
        '''
    return "hahah"


@app.route('/audiobook_chapter_media', methods=('GET', 'POST', 'DELETE'))
def interface_audiobook_chapter_media():
    # # 1. 从数据库取10条未下载 的 chapter 的url, -->插入线程池 -->过60秒检测-->任务都做完了,就再加10条任务-->任务没做完,过60秒继续检查
    # all_task = []
    # default_task_num = 40  # 默认添加几个任务 20
    # # default_task_num = 1  # 默认添加几个任务 20
    # default_loop_time = 10  # 默认轮询时间,查询是否任务列表空了 10
    # while True:
    #     if len(all_task) < 10:
    #         print(f'--------------任务列表 <5,添加{default_task_num}个任务')
    #         # 1. 从数据库取10条未爬取的book的url
    #         sql = f'select id, name, url from chapter where spider_status=0 limit 0,{default_task_num}'
    #         result_tuple = dbutil.execute_project('audiobook', sql)
    #         print(f'获取10条 chapter 的url= {result_tuple}')
    #
    #         if len(result_tuple) == 0:
    #             print('有声书spider_status =0 个数为0,所有有声书 media 爬取完成,主线程应结束!!!')
    #             break
    #
    #         # 2. 给线程池添加 10 个任务-爬取章节 mp3(每个方法,自动更新数据库)
    #         print('线程池添加任务,爬取书的章节 media,存入数据库...')
    #         for i in range(default_task_num):  # 初始化10个
    #             if i > len(result_tuple):
    #                 break
    #             print(f'爬取 chapter-media, id={result_tuple[i][0]}, name={result_tuple[i][1]}, url={result_tuple[i][2]}')
    #             task = threadutil.THREADPOOL.submit(audiobook.spider_chapters_medias, result_tuple[i][0], result_tuple[i][1],
    #                                                 result_tuple[i][2])
    #             all_task.append(task)
    #     else:
    #         print(f'--------------爬取 chapter - media 任务列表 !!!! >=5, 剩余任务{len(all_task)}个')
    #
    #     print('等待60秒,查询任务状态==========================')
    #     for second in range(default_loop_time):
    #         print(f'主线程休眠 {second} 秒')
    #     time.sleep(default_loop_time)  # 1分钟检查一次
    #     print(f'----------------> 当前所有的任务列表(chapter-media){len(all_task)}个= {all_task}')
    #     # print(f'----------------> 当前所有的 线程池 列表 {threadutil.THREADPOOL}')
    #
    #     for task in as_completed(all_task):
    #         print(f'共有任务(chapter-media) {len(all_task)}, 查询当前任务task = {task}')
    #         if task.done() is True:
    #             print(f'任务{task} 完成了, 删除!')
    #             all_task.remove(task)

    threadutil.THREADPOOL.submit(audiobook.checkis_done_spider_chapters_medias)

    return "完了"


@app.route('/download_audiobook_chapter_media', methods=('GET', 'POST', 'DELETE'))
def download_audiobook_chapter_media():
    """
    下载chapter 媒体文件
    :return:
    """
    threadutil.THREADPOOL.submit(audiobook.checkis_done_download_chapter_media)

    return "下载chapter-meida 线程,处理完了"


@app.route('/audiobook_remove_duplicate', methods=('GET', 'POST', 'DELETE'))
def audiobook_remove_duplicate():
    """
    下载chapter 媒体文件
    :return:
    """
    threadutil.THREADPOOL.submit(audiobook.audiobook_remove_duplicate)

    return "删除重复数据 线程,处理完了"


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
