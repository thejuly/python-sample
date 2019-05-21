import os
#from flask import Flask


from flask import Flask, request

import requests
#import psycopg2

import re
import random
from bs4 import BeautifulSoup
from collections import defaultdict
from flask import Flask, request, abort



app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
