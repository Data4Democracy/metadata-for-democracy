#!/usr/bin/env python
import os
from flask import Flask

app = Flask(__name__)
port = os.getenv('MD4D_API_PORT', '8080')

@app.route("/")
def home():
  return 'Hello from the metadata-for-democracy API.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(port), debug=True)
