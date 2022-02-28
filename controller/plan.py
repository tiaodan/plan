"""
业务逻辑：
sql增删改查
"""

# 导自定义包
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

    # 查询总数
    total_tuple = dbutil.execute('select count(id) from plan')
    print('=============', total_tuple)
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
        data['name'] = row[1]
        result['data'].append(data)

    return result


# 测试
# add_plan(add_sql)  # 增
# add_plan(add_plan_sql)  # 增
# delete_plan(delete_plan_sql)  # 删
# update_plan(update_plan_sql)  # 改

