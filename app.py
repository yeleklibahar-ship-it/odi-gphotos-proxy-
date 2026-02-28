from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "Kodi Google Photos Proxy Calisiyor!"

if __name__ == "__main__":
    # Render'ın portunu otomatik ayarlar
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
