from app import app
from flask import render_template, redirect, url_for

from helper import create_job

import time

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/ping')
def ping():
    job = create_job()
    finished = False
    while not finished:
      if job.result is not None:
        finished = True
      else:
        time.sleep(0.5)
    return "success"

if __name__=="__main__":
    ping()
