import json

from settings import RedisKey
from utils.client import client
from utils.tools import now_time


def update_weather(city: str, data: dict):
    """
    key: 20200320_Weather
    """
    now_str = now_time()
    key = RedisKey.Weather.value.format(now_str)
    client.redis_client.hset(name=key, key=city, value=json.dumps(data, ensure_ascii=False))
    if client.redis_client.ttl(key) < 0:
        client.redis_client.expire(key, 3 * 3600)  # 保存3小时
    return True


def get_weather(city: str):
    """
    key: 20200320_Weather
    """
    now_str = now_time()
    key = RedisKey.Weather.value.format(now_str)
    data = client.redis_client.hget(key, city)
    if data:
        return json.loads(data)
    return


def update_star_lucky(star: str, data: dict):
    """
    key: 20200320_StarLucky
    """
    now_str = now_time()
    key = RedisKey.StarLucky.value.format(now_str)
    client.redis_client.hset(name=key, key=star, value=json.dumps(data, ensure_ascii=False))
    if client.redis_client.ttl(key) < 0:
        client.redis_client.expire(key, 7 * 86400)  # 保存七天
    return True


def get_star_lucky(star: str):
    """
    key: 20200320_StarLucky
    """
    now_str = now_time()
    key = RedisKey.StarLucky.value.format(now_str)
    data = client.redis_client.hget(name=key, key=star)
    if data:
        return json.loads(data)
    return


if __name__ == '__main__':
    pass