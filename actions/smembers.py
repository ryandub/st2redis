from lib.base import BaseRedisAction

__all__ = [
    'SMembersAction'
]


class SMembersAction(BaseRedisAction):
    def run(self, key):
        return list(self._client.smembers(key))
