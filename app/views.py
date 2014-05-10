from app import app
from flask import render_template, redirect, url_for

import urlparse
from settings import *
from redis import StrictRedis
from rq import Queue

import time

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/ping')
def ping():
    redis_url = urlparse.urlparse(REDISTOGO_URL)
    redis_conn = StrictRedis(
        host=redis_url.hostname,
        port=redis_url.port,
        password=redis_url.password
    )
    q = Queue('high', connection=redis_conn)
    job = q.enqueue('pi.receive_ping')
    finished = False
    while not finished:
      if job.result is not None:
        finished = True
      else:
        time.sleep(0.5)
    return "success"

if __name__=="__main__":
    ping()
