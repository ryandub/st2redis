import json

from lib.base import BaseRedisAction

__all__ = [
    'LRangeAction'
]


class LRangeAction(BaseRedisAction):
    def run(self, key, start, end):
        return json.dumps(self._client.lrange(key, start, end))
