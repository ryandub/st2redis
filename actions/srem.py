
from lib.base import BaseRedisAction

__all__ = [
    'SRemAction'
]


class SRemAction(BaseRedisAction):
    def run(self, key, value):
        result = self._client.srem(key, value)
        if result == 1:
            return True
        else:
            return False
