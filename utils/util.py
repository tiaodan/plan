"""
工具类
包含以下方法：
1. get_arg_from_cfg(filepath)  # 读取配置文件
2. get_arg_from_ini_cfg(filepath, section)  # 读取ini配置文件
3. get_html(url, headers=None, device='pc', wait_seconds=1)  # 通过网页地址，获取html,返回str html
4.

"""
import configparser  # 第三方
import requests  # 第三方
from zhconv import convert  # 第三方 简繁体转换
import time  # python 自带
import re  # python 自带
from threading import Thread as thread  # python 自带
import threading  # python 自带
import audiobook  # 自定义


# 基础参数

# 读取配置文件
def get_arg_from_cfg(filepath):
    """
    # fun：相对路径读取配置文件中参数
    # arg1: filepath  # 文件路径）
    # return：json
    """
    print('------------------------------')

    # 1. 实例化configparser对象
    config =configparser.ConfigParser()

    # 2. 读取配置文件
    print('util读取配置文件路径==', filepath)
    config.read(filepath, encoding='utf-8')
    print('配置config sections== ', config.sections())
    print('配置config items = ', config.items('plan'))
    # print('配置config db_host== ', config.get('db', 'db_host'))
    # print('配置config db_user== ', config.get('db', 'db_user'))
    # print('配置config db_password== ', config.get('db', 'db_password'))
    # print('配置config db_name== ', config.get('db', 'db_name'))
    # print('配置config db_port== ', config.get('db', 'db_port'))
    # print('配置config db_charset== ', config.get('db', 'db_charset'))
    print('------------------------------')

    # 3. 返回字典
    config_dict = {
        'db_host': config.get('plan', 'db_host'),
        'db_user': config.get('plan', 'db_user'),
        'db_password': config.get('plan', 'db_password'),
        'db_name': config.get('plan', 'db_name'),
        'db_port': config.get('plan', 'db_port'),
        'db_charset': config.get('plan', 'db_charset')
    }
    return config_dict


# 读取ini配置文件
def get_arg_from_ini_cfg(filepath, section):
    """
    # fun：相对路径读取ini配置文件中参数
    # arg1: filepath  # 文件路径）
    # arg2: section  # ini 配置文件【section】中的内容）
    # return：json
    """
    # 0. 初始化
    config_dict = {
        'db_host': "",
        'db_user': "",
        'db_password': "",
        'db_name': "",
        'db_port': "",
        'db_charset': ""
    }
    # 1. 实例化configparser对象
    config =configparser.ConfigParser()

    # 2. 读取配置文件
    print('------------------------------')
    print('util读取配置文件路径==', filepath)
    config.read(filepath, encoding='utf-8')
    print('配置config sections== ', config.sections())
    print('配置config items = ', config.items(section))
    # print('配置config db_host== ', config.get(section, 'db_host'))
    # print('配置config db_user== ', config.get(section, 'db_user'))
    # print('配置config db_password== ', config.get(section, 'db_password'))
    # print('配置config db_name== ', config.get(section, 'db_name'))
    # print('配置config db_port== ', config.get(section, 'db_port'))
    # print('配置config db_charset== ', config.get(section, 'db_charset'))
    print('------------------------------')

    if section == 'plan':
        # 3. 返回字典
        config_dict = {
            'db_host': config.get(section, 'db_host'),
            'db_user': config.get(section, 'db_user'),
            'db_password': config.get(section, 'db_password'),
            'db_name': config.get(section, 'db_name'),
            'db_port': config.get(section, 'db_port'),
            'db_charset': config.get(section, 'db_charset')
        }
    elif section == 'account':
        # 3. 返回字典
        config_dict = {
            'db_host': config.get(section, 'db_host'),
            'db_user': config.get(section, 'db_user'),
            'db_password': config.get(section, 'db_password'),
            'db_name': config.get(section, 'db_name'),
            'db_port': config.get(section, 'db_port'),
            'db_charset': config.get(section, 'db_charset')
        }
    elif section == 'audiobook':
        # 3. 返回字典
        config_dict = {
            'db_host': config.get(section, 'db_host'),
            'db_user': config.get(section, 'db_user'),
            'db_password': config.get(section, 'db_password'),
            'db_name': config.get(section, 'db_name'),
            'db_port': config.get(section, 'db_port'),
            'db_charset': config.get(section, 'db_charset'),
            'url_prefix': config.get(section, 'url_prefix')
        }

    return config_dict


# --------------------------------------------------------------------------- #
# 通过网页地址，获取html
# Parameter1: url  # 网站链接
# Parameter2: headers=None  # 请求头
# Parameter3: device='pc'  # 设备类型，默认pc , mobie -->手机
# Parameter4: wait_seconds=0  # 循环延时，默认0秒
# output: None
# return: str
# --------------------------------------------------------------------------- #
def get_html(url, headers=None, device='pc', wait_seconds=0):
    result = ""
    try:
        timeout_seconds = 15  # 请求超时时间
        # 模拟电脑请求头
        request_headers_pc = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'
        }

        # 模拟手机请求头
        request_headers_mobie = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36'
        }
        if headers:
            response = requests.get(url, headers=headers, timeout=timeout_seconds)
        else:  # 用户输入请求头 -- 空
            if device == 'mobie':  # 模拟手机请求
                response = requests.get(url, headers=request_headers_mobie)
            else:  # 默认走pc请求
                response = requests.get(url, headers=request_headers_pc)

        # html_text = response.content  # 2进制类型
        html_context = response.text  # str类型
        response.close()  # 关闭，防止报错“远程主机强迫关闭了一个现有的连接”
        # print('每个请求后加个延时 = %s秒' % wait_seconds)
        time.sleep(wait_seconds)  # 每个请求后加个延时，防止报错“远程主机强迫关闭了一个现有的连接”
        if type(html_context) == str:
            return html_context
        else:
            return None

        # print(type(response))    # class类型
        # print(type(html_text), '\n')
        # print(type(html_context))
    except Exception as ex:
        print(ex)
    return result


# --------------------------------------------------------------------------- #
# 根据正则表达式，截取str内容
# Parameter1: regexp  正则表达式
# Parameter1: str 文本
# output: None
# return: list
# --------------------------------------------------------------------------- #
def get_list_from_str_by_regexp(regexp, str):
    strlist = re.findall(regexp, str, re.VERBOSE)  # VERBOSE 表示可用多行书写
    return strlist


def haha():
    print("strstr")


# ---------------------------------------------------create_thrads_by_class_threading------------------------ #
# 启动线程,通过threading 类来创建
# Parameter1: ?
# Parameter1: ?
# output: None
# return: list
# --------------------------------------------------------------------------- #
def create_thrads_by_class_threading():
    print('创建一个线程。。。')
    thread1 = thread(target=audiobook.test())  # 是否就是自启动了？ 使用class 继承的方式会有此问题吗？
    print('当前线程list', threading.enumerate())
    # thread1.start()


# --------------------------------------------------------------------------- #
# 关闭线程,
# Parameter1: ?
# Parameter1: ?
# output: None
# return: list
# --------------------------------------------------------------------------- #
def close_thrads_by_class_threading():
    print('关闭一个线程。。。')
    print('当前线程', threading.current_thread())
    print('当前线程list', threading.enumerate())
    # threading._Thread__stop(threading.enumerate()[1])
    print('关闭线程')


# --------------------------------------------------------------------------- #
# 功能：繁体转简体,
# Parameter1: traditional_str 繁体字符串
# Parameter1: None
# output: None
# return: simple_str 简体字符串
# zh-cn 大陆简体
# zh-tw 台灣正體
# zh-hk 香港繁體
# zh-sg 马新简体
# zh-hans 简体
# zh-hant 繁體
# --------------------------------------------------------------------------- #
def traditional2simple(traditional_str):
    simple_str = convert(traditional_str, 'zh-hans')
    return simple_str


# --------------------------------------------------------------------------- #
# 功能：简体转繁体,
# Parameter1: simple_str 简体字符串
# output: None
# return: traditional_str 繁体字符串
# zh-cn 大陆简体
# zh-tw 台灣正體
# zh-hk 香港繁體
# zh-sg 马新简体
# zh-hans 简体
# zh-hant 繁體
# --------------------------------------------------------------------------- #
def simple2traditional(simple_str):
    traditional_str = convert(simple_str, 'zh-hant')
    return traditional_str