"""
# 入口文件
"""
from utils import util
from utils import config


if __name__ == '__main__':
    # 1. 实例化类
    myconfig = config.Config()
    print('main获取配置文件, db_host= ', myconfig.get_value('db_host'))
    print('main获取配置文件, db_user= ', myconfig.get_value('db_user'))
    print('main获取配置文件, db_password= ', myconfig.get_value('db_password'))
    print('main获取配置文件, db_name= ', myconfig.get_value('db_name'))

    # 1. 只加载一次配置文件
    db_host = myconfig.get_value('db_host')
    if db_host == '':
        print('db_host配置为空，读取配置文件。。。。。')
        config_dict = util.get_arg_from_cfg('conf/config.ini')

        # 设置全局参数
        myconfig.set_value('db_host', config_dict['db_host'])
        myconfig.set_value('db_user', config_dict['db_user'])
        myconfig.set_value('db_password', config_dict['db_password'])
        myconfig.set_value('db_name', config_dict['db_name'])

    # 2. 获取全局变量
    print('全局变量', myconfig.get_value('db_host'))
    print('全局变量', myconfig.get_value('db_user'))
    print('全局变量', myconfig.get_value('db_password'))
    print('全局变量', myconfig.get_value('db_name'))

