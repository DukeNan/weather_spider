from redis import ConnectionPool, Redis

from settings import RedisConfigs


class Client:

    @property
    def redis_client(self):
        pool = ConnectionPool(
            host=RedisConfigs.HOST.value,
            port=RedisConfigs.PORT.value,
            db=RedisConfigs.DB.value,
            password=RedisConfigs.PASSWORD.value,
            decode_responses=True
        )
        return Redis(connection_pool=pool)


client = Client()

if __name__ == '__main__':
    client.redis_client.set('name', '中国')
