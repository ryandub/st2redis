import redis

from st2actions.runners.pythonrunner import Action

__all__ = [
    'BaseRedisAction'
]


class BaseRedisAction(Action):
    def __init__(self, config):
        super(BaseRedisAction, self).__init__(config=config)
        host = config.get('host', 'localhost')
        db = config.get('db', 0)
        port = config.get('port', 6379)
        password = config.get('password', None)

        self._client = redis.StrictRedis(host=host, port=port, db=db,
                                         password=password)
