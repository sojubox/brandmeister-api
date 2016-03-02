###################################################################################################################
#
# A P I   M O D U L E
#
# THIS IS THE RATE LIMIT MODULE
#
###################################################################################################################

import time
from redis import Redis
from flask import current_app

# Global variable not loaded by default
redis = None


# This is created for testing purposes. No real Redis database will be used for testing.
class FakeRedis(object):
    def __init__(self):
        self.v = {}
        self.last_key = None

    def pipeline(self):
        return self

    def incr(self, key):
        if self.v.get(key, None) is None:
            self.v[key] = 0
        self.v[key] += 1
        self.last_key = key

    def expireat(self, key, time):
        pass

    def execute(self):
        return [self.v[self.last_key]]


# This is the real Redis database that supports Rate Limit functionality
class RateLimit(object):
    expiration_window = 10

    def __init__(self, key_prefix, limit, period):
        # Call to global variable in order to read defaults from config
        global redis
        if redis is None and current_app.config['USE_RATE_LIMITS']:
            if current_app.config['TESTING']:
                redis = FakeRedis()
            else:
                redis = Redis()

        self.reset = (int(time.time()) // period) * period + period
        self.key = key_prefix + str(self.reset)
        self.limit = limit
        self.period = period
        p = redis.pipeline()
        p.incr(self.key)
        p.expireat(self.key, self.reset + self.expiration_window)
        self.current = p.execute()[0]

    @property
    def allowed(self):
        return self.current <= self.limit

    @property
    def remaining(self):
        return self.limit - self.current