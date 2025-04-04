# Import the Flask library
from flask import Flask

# Create a new Flask app
app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
def home():
    # Return a simple "Hello, World!" message
    return 'Hello, World!'

# Run the app if this script is executed directly
if __name__ == '__main__':
    app.run()
