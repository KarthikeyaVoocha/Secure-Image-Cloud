from flask import Flask
from routes import main  # Import Blueprint from routes.py

app = Flask(__name__)

# Register the main blueprint
app.register_blueprint(main)

if __name__ == '__main__':
    app.run(debug=True)
