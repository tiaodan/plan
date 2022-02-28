"""
业务逻辑：
sql增删改查
"""

# 导自定义包
import dbutil


# 增
def add_account(add_sql, add_values=None):
    """
    :param add_sql:
    :param add_values:
    :return:
    """
    result = dbutil.execute_project('account', add_sql, add_values)
    return result


# 删
def delete_account(delete_sql, delete_values=None):
    """
    :param delete_sql:
    :param delete_values:
    :return:
    """
    result = dbutil.execute_project('account', delete_sql, delete_values)
    return result


# 改
def update_account(update_sql, update_values=None):
    """
    :param update_sql:
    :param update_values:
    :return:
    """
    result = dbutil.execute_project('account', update_sql, update_values)
    return result


# 查
def query_account(query_sql, query_values=None):
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
    total_tuple = dbutil.execute_project('account', 'select count(id) from account')
    result['count'] = total_tuple[0][0]

    result_tuple = dbutil.execute_project('account', query_sql, query_values)  # tuple类型
    result['code'] = 200
    if result['code'] == 200:
        result['msg'] = 'success'
    else:
        result['msg'] = 'fail'
    for row in result_tuple:
        data = dict()
        data['id'] = row[0]
        data['type'] = row[1]
        data['sitename'] = row[2]
        data['sitetype'] = row[3]
        data['url'] = row[4]
        data['username'] = row[5]
        data['initpw'] = row[6]
        data['newpw'] = row[7]
        data['email'] = row[8]
        data['phone'] = row[9]
        data['QRcode'] = row[10]
        data['key'] = row[11]
        data['pwrules'] = row[12]
        data['safequestion'] = row[13]
        data['safeanswer'] = row[14]
        data['createtime'] = row[15]
        data['updatetime'] = row[16]
        data['isuseful'] = row[17]
        data['remark'] = row[18]
        result['data'].append(data)

    return result