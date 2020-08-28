from flask import Flask, request
from routers.playlist_router import playlist_router

app = Flask(__name__)

app.register_blueprint(playlist_router)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='80')
