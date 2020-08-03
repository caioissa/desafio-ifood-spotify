from flask import Flask, request
from routers.playlist_router import playlist_router

app = Flask(__name__)

app.register_blueprint(playlist_router)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
