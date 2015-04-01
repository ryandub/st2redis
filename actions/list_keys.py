from lib.base import BaseRedisAction

__all__ = [
    'ListKeysAction'
]


class ListKeysAction(BaseRedisAction):
    def run(self):
        return self._client.keys()
