from app import app
from flask import render_template, redirect, url_for

import urlparse
from settings import *
from redis import StrictRedis
from rq import Queue

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
    print redis_conn
    q = Queue('high', connection=redis_conn)
    result = q.enqueue('pi.receive_ping')
    print result
    return redirect(url_for('index'))

if __name__=="__main__":
    ping()
