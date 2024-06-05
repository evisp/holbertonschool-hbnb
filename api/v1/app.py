import sys
import os

# Add the current directory to the Python path
current_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(current_dir)

from flask import Flask
from v1.urls import register_routes
from persistence.file_storage import FileStorage

app = Flask(__name__)
storage = FileStorage()

register_routes(app, storage)

if __name__ == '__main__':
    storage.reload()
    app.run(debug=True, port=5001)
