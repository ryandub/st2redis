import json

from lib.base import BaseRedisAction

__all__ = [
    'SMembersAction'
]


class SMembersAction(BaseRedisAction):
    def run(self, key):
        return json.dumps(list(self._client.smembers(key)))
