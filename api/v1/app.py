import sys
import os

# Add the parent directory of the current directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from flask import Flask
from .urls import register_routes
from persistence.data_manager import DataManager

app = Flask(__name__)
data_manager = DataManager()

# Initialize data manager
data_manager.reload()

register_routes(app, data_manager)

if __name__ == '__main__':
    data_manager.reload()
    app.run(debug=True, port=5001)
