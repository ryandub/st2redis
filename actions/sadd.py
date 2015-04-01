from lib.base import BaseRedisAction

__all__ = [
    'SaddAction'
]


class SaddAction(BaseRedisAction):
    def run(self, key, value):
        return self._client.sadd(key, value)
