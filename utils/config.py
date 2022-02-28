"""
全局参数工具类

"""
import configparser


class Config:
    def __init__(self):
        # self.db_host = 'localhost'
        # 配置文件默认数据
        global config_dict
        config_dict = {
            'db_host': '',
            'db_user': '',
            'db_password': '',
            'db_name': ''
        }

    def set_value(self, key, value):
        config_dict[key] = value

    def get_value(self, key):
        """
        获取一个全局变量，不存在则返回默认值
        """
        try:
            return config_dict[key]
        except KeyError:
            return ''  # 返回空

    # 读取配置文件
    def get_arg_from_cfg(self, filepath):
        """
        # fun：相对路径读取配置文件中参数
        # arg1: filepath  # 文件路径）
        # return：json
        """
        print('------------------------------')
        print('相对路径读取配置文件中参数')

        # 1. 实例化configparser对象
        config = configparser.ConfigParser()

        # 2. 读取配置文件
        config.read(filepath, encoding='utf-8')
        print('配置config sections== ', config.sections())
        print('配置config db_host== ', config.get('db', 'db_host'))
        print('配置config db_user== ', config.get('db', 'db_user'))
        print('配置config db_password== ', config.get('db', 'db_password'))
        print('配置config db_name== ', config.get('db', 'db_name'))
        print('------------------------------')

        # 3. 返回字典
        config_dict = {
            'db_host': config.get('db', 'db_host'),
            'db_user': config.get('db', 'db_user'),
            'db_password': config.get('db', 'db_password'),
            'db_name': config.get('db', 'db_name')
        }
        return config_dict


myconfig = Config()