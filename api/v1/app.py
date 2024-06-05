import sys
import os

# Add the parent directory of the current directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from flask import Flask
from urls import register_routes
from persistence.file_storage import FileStorage

app = Flask(__name__)
storage = FileStorage()

register_routes(app, storage)

if __name__ == '__main__':
    storage.reload()
    app.run(debug=True, port=5001)
