import os

from app import create_app

config_var = os.getenv("FLASK_CONFIG")
app = create_app(config_var)

if __name__ == "__main__":
    app.run()
