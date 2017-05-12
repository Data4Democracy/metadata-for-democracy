#!/usr/bin/env python
import os
from flask import Flask

app = Flask(__name__)
port = os.getenv('MD4D_WEBHOOK_PORT', '8079')

@app.route("/")
def home():
  return 'Hello from the metadata-for-democracy web hook.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(port), debug=True)
