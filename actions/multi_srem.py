import json

from lib.base import BaseRedisAction

__all__ = [
    'MultiSRemAction'
]


class MultiSRemAction(BaseRedisAction):
    def run(self, key, values):
        values = json.loads(values)
        for value in values:
            self._client.srem(key, value)

        return True
