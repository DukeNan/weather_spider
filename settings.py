from enum import Enum


# Email Config
MAIL_HOST = "smtp.163.com"  # 设置服务器
MAIL_USER = "*********"  # 用户名
MAIL_PORT = 465
MAIL_PASS = "**********"  # 口令

# api code
APP_CODE = '**********************'


# api host
class ApiHost(Enum):
    Weather = 'https://jisutqybmf.market.alicloudapi.com'
    StarLucky = 'https://ali-star-lucky.showapi.com'


class RedisKey(Enum):
    Weather = '{}_Weather'  # 天气
    StarLucky = '{}_StarLucky'  # 星座运势


# 星座分类
class Star(Enum):
    Baiyang = 'baiyang'
    Jinniu = 'jinniu'
    Shuangzi = 'shuangzi'
    Juxie = 'juxie'
    Shizi = 'shizi'
    Chunv = 'chunv'
    Tiancheng = 'tiancheng'
    Tianxie = 'tianxie'
    Sheshou = 'sheshou'
    Mojie = 'mojie'
    Shuiping = 'shuiping'
    Shuangyu = 'shuangyu'


# redis configs
class RedisConfigs(Enum):
    HOST = '127.0.0.1'
    PORT = 6379
    PASSWORD = 'admin123'
    DB = 15


SEND_LIST = [
    {'star': '天蝎', 'star_en': 'tianxie', 'city': '北京', 'email': '***********@qq.com'}
]


if __name__ == '__main__':
    print(RedisKey['Weather'])
    print(RedisKey('{date}_weather'))
