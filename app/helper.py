import urlparse
from settings import *
from redis import StrictRedis
from rq import Queue

def create_job():
  print "Queueing job."
  redis_url = urlparse.urlparse(REDISTOGO_URL)
  redis_conn = StrictRedis(
      host=redis_url.hostname,
      port=redis_url.port,
      password=redis_url.password
  )
  q = Queue('high', connection=redis_conn)
  job = q.enqueue('pi.receive_ping')
  return job
