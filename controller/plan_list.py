"""
业务逻辑：
sql增删改查
"""

# 导自定义包
import plan
import dbutil


# 初始化
add_sql = 'show databases'
add_plan_sql = 'insert into plan_list values(1, "2021-12-7"' \
               ', "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"' \
               ', "16", "17", "18", "19", "20" , "21", "22", "23", "24", "25" , "26", "27", "28", "29", "30"' \
               ', "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"' \
               ', "16", "17", "18", "19", "20" , "21", "22", "23", "24", "25" , "26", "27", "28", "29", "30")'

delete_plan_sql = 'delete from plan_list where id=1'
update_plan_sql = 'update plan_list set planid1="111"'


# 增
def add_plan(add_sql, add_values=None):
    """
    :param add_sql:
    :param add_values:
    :return:
    """
    result = dbutil.execute(add_sql, add_values)
    return result


# 删
def delete_plan(delete_sql, delete_values=None):
    """
    :param delete_sql:
    :param delete_values:
    :return:
    """
    result = dbutil.execute(delete_sql, delete_values)
    return result


# 改
def update_plan(update_sql, update_values=None):
    """
    :param update_sql:
    :param update_values:
    :return:
    """
    result = dbutil.execute(update_sql, update_values)
    return result


# 查
def query_plan(query_sql, query_values=None):
    """
    :param query_sql:
    :param query_values:
    :return:
    """
    # 1. 定义返回json类型
    result = dict()
    result.update({
        "code": 0,
        "msg": "",
        "count": 0,
        "data": []
    })

    # 2. 整理返回数据
    # 获取数据库plan表所有的plan
    queryallplan_sql = 'select id,name from plan'
    allplan_result = plan.query_plan(queryallplan_sql)['data']  # json
    # print('===================== allplan_result', allplan_result)

    # 查询总数
    total_tuple = dbutil.execute('select count(id) from plan_list')
    result['count'] = total_tuple[0][0]

    result_tuple = dbutil.execute(query_sql, query_values)  # tuple类型
    result['code'] = 200
    if result['code'] == 200:
        result['msg'] = 'success'
    else:
        result['msg'] = 'fail'
    for row in result_tuple:
        # print('每行返回结果type==', type(row), row)  # tuple
        data = dict()
        data['id'] = row[0]
        data['date'] = row[1]
        for index, value in enumerate(row):
            if index == int((len(row)-2)/2):
                # print('读取该行数据完成，跳出循环，index', index, int((len(row)-2)/2))
                break
            # print('index===============', type(index))  # index 从0开始
            planid_str = row[2*(index+1)]
            for item in allplan_result:
                if row[2*(index+1)] == item['id']:
                    planid_str = item['name']
            data['planid' + str(index+1)] = planid_str  # 将id 转成str，显示在ui上
            # data['planid' + str(index+1)] = row[2*(index+1)]  # 将id 转成str，显示在ui上，如果不，使用此方法
            data['planisfinish' + str(index+1)] = row[2*(index+1)+1]
        # print('数据库每行数据= ', data)
        result['data'].append(data)

    return result


# 测试
# add_plan(add_sql)  # 增
# add_plan(add_plan_sql)  # 增
# delete_plan(delete_plan_sql)  # 删
# update_plan(update_plan_sql)  # 改

