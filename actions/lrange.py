from lib.base import BaseRedisAction

__all__ = [
    'LRangeAction'
]


class LRangeAction(BaseRedisAction):
    def run(self, key, start, end):
        return self._client.lrange(key, start, end)
