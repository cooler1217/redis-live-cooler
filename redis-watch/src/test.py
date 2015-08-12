'''
Created on 2014-04-24

@author: cooler
'''
import redis, logging

def getDB(db):
    pool = redis.ConnectionPool(host="127.0.0.1", port=6379, db=db, password="I2Tou3Zi4")  
    r = RedisWrapper(connection_pool=pool)
    r.set_bredis("127.0.0.1",6379, db ,password="I2Tou3Zi4")
    return r

class RedisWrapper(redis.Redis):

    def set_bredis(self, host,port, db,password):
        pool = redis.ConnectionPool(host=host, port=port, db=db,password=password)  
        self.bredis  = redis.Redis(connection_pool=pool)

    def exists(self, key):
        try:
            return super(RedisWrapper, self).exists(key)
        except Exception, e:
            return self.bredis.exists(key)     

    def expire(self, key, CACHE_TIMEOUT):
        try:
            return super(RedisWrapper, self).expire(key , CACHE_TIMEOUT)
        except Exception, e:
            return self.bredis.expire(key , CACHE_TIMEOUT)

    def delete(self, key):
        try:
            return super(RedisWrapper, self).delete(key)
        except Exception, e:
            return self.bredis.delete(key)

    def get(self, key):
          try:
                return super(RedisWrapper, self).get(key)
          except Exception, e:
                return self.bredis.get(key)

    def set(self, key, value):
        try: 
            super(RedisWrapper, self).set(key, value)
        except Exception, e:
            self.bredis.set(key, value)

    def keys(self, pattern='*'):
          try:
                return super(RedisWrapper, self).keys(pattern='*')
          except Exception, e:
                return self.bredis.keys(pattern='*')

    def lpop(self, name):
          try:
                return super(RedisWrapper, self).lpop(name)
          except Exception, e:
                return self.bredis.lpop(name)

    def lpush(self, name, *values):
          try:
                return super(RedisWrapper, self).lpush(name, *values)
          except Exception, e:
                return self.bredis.lpush(name, *values)

    def lrange(self, name,  start, end):
          try:
                return super(RedisWrapper, self).lrange(name, start, end)
          except Exception, e:
                return self.bredis.lrange(name, start, end)

    def rpop(self, name):
          try:
                return super(RedisWrapper, self).rpop(name)
          except Exception, e:
                return self.bredis.rpop(name)

    def rpush(self, name, *values):
          try:
                return super(RedisWrapper, self).rpush(name, *values)
          except Exception, e:
                return self.bredis.rpush(name, *values)

    def flushdb(self):
        try: 
            super(RedisWrapper, self).flushdb()
        except Exception, e:
            self.bredis.flushdb()

    def pipeline(self):
        try:
            pipe = super(RedisWrapper, self).pipeline()
            pipe.watch("test")
            pipe.execute()
            return pipe
        except Exception, e:
            return self.bredis.pipeline()


'''

'''
if __name__ == '__main__':
    rdb = getDB(1)
    print rdb
    for x in xrange(30,40):
        rdb.set("d"+str(x),"dd"+str(x))