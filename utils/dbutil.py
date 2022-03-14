"""
数据库工具类
"""
import util
import pymysql


# 基础参数
try:
    plan_db_config = util.get_arg_from_ini_cfg('config.ini', 'plan')  # 加载 account 项目 - acount 数据库配置
    account_db_config = util.get_arg_from_ini_cfg('config.ini', 'account')  # 加载 account 项目 - acount 数据库配置
    audiobook_db_config = util.get_arg_from_ini_cfg('config.ini', 'audiobook')  # 加载 audiobook 项目 - audiobook 数据库配置
except Exception:
    print('error..........')
    # raise ValueError  # ? 自动引发异常

plan_db_host = plan_db_config['db_host']
plan_db_user = plan_db_config['db_user']
plan_db_password = plan_db_config['db_password']
plan_db_name = plan_db_config['db_name']
plan_db_port = int(plan_db_config['db_port'])
plan_db_charset = plan_db_config['db_charset']

# 账号项目account 数据库配置
account_db_host = account_db_config['db_host']
account_db_user = account_db_config['db_user']
account_db_password = account_db_config['db_password']
account_db_name = account_db_config['db_name']
account_db_port = int(account_db_config['db_port'])
account_db_charset = account_db_config['db_charset']

# 账号项目 audiobook 数据库配置
audiobook_db_host = audiobook_db_config['db_host']
audiobook_db_user = audiobook_db_config['db_user']
audiobook_db_password = audiobook_db_config['db_password']
audiobook_db_name = audiobook_db_config['db_name']
audiobook_db_port = int(audiobook_db_config['db_port'])
audiobook_db_charset = audiobook_db_config['db_charset']
audiobook_url_prefix = audiobook_db_config['url_prefix']    # audiobook 项目号码前缀


# 查看配置
def print_cfg():
    print('dbutil查看配置==', plan_db_config)
    print('dbutil查看配置(项目account)==', account_db_config)


# 执行一条mysql, 执行默认的数据库配置
def execute(sql, values=None):
    """
    :param sql:
    :param values:
    :return: json
    """
    pass

    # 1. 连接数据库
    db = pymysql.connect(host=plan_db_host, user=plan_db_user, password=plan_db_password, database=plan_db_name, port=plan_db_port, charset=plan_db_charset)

    # 2. 创建cursor
    cursor = db.cursor()

    # 3  执行sql
    try:
        print('dbutils sql ===  ', sql)
        print('dbutils values ===  ', values)
        cursor.execute(sql, values)  # 执行
        db.commit()  # 提交数据库执行
        sql_result = cursor.fetchall()  # 执行语句结果
        # print('执行单条语句结果result == ', sql_result)
        # print('执行单条语句结果result.type == ', type(sql_result))  # tuple
    except Exception as ex:
        print('执行单条语句失败，数据回滚')
        print('异常=', ex)
        db.rollback()
    finally:
        # 4. 关闭连接
        cursor.close()
        db.close()

    # 4. 返回json
    return sql_result


# 执行一条mysql, 使用某项目的的数据库配置
def execute_project(project_name, sql, values=None):
    """
    :param project_name: 项目名称
    :param sql:
    :param values:
    :return: json
    """
    # sql_result = {
    #     "code": 500,
    #     "msg": "",
    #     "count": 0,
    #     "data": []
    # }
    sql_result = ()

    # 1. 连接数据库
    if project_name == 'account':
        # print('account项目')
        db = pymysql.connect(host=account_db_host, user=account_db_user, password=account_db_password, database=account_db_name, port=account_db_port, charset=account_db_charset)
    elif project_name == 'audiobook':
        # print('audiobook 项目')
        db = pymysql.connect(host=audiobook_db_host, user=audiobook_db_user, password=audiobook_db_password, database=audiobook_db_name, port=audiobook_db_port, charset=audiobook_db_charset)
    elif project_name == 'plan':
        db = pymysql.connect(host=plan_db_host, user=plan_db_user, password=plan_db_password, database=plan_db_name, port=plan_db_port, charset=plan_db_charset)

    # 2. 创建cursor
    cursor = db.cursor()

    # 3  执行sql
    try:
        # print('dbutils sql ===  ', sql)
        # print('dbutils values ===  ', values)
        cursor.execute(sql, values)  # 执行
        db.commit()  # 提交数据库执行
        sql_result = cursor.fetchall()  # 执行语句结果
        # print('执行单条语句结果result == ', sql_result)
        # print('执行单条语句结果result.type == ', type(sql_result))  # tuple
    except Exception as ex:
        print('执行单条语句失败，数据回滚')
        print('异常=', ex)
        db.rollback()
    finally:
        # 4. 关闭连接
        cursor.close()
        db.close()

    # 4. 返回json
    return sql_result
