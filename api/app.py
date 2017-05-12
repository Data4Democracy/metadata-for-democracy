#!/usr/bin/env python
import os

port = os.getenv('MD4D_API_PORT', '8080')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(port), debug=True)
