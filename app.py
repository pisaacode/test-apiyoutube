from settings.conf import KEY_YOUTUBE
from flask import Flask, jsonify, request
from flask_cors import CORS
from pyyoutube import Api as api_youtube
app = Flask(__name__)
CORS(app)


@app.route('/lista', methods=['GET'])
def youtube():
    search = request.args.get("search", None)
    status_code = "200"
    try:
        api = api_youtube(api_key=KEY_YOUTUBE)
        videos = api.search_by_keywords(q=search, search_type=["channel", "video", "playlist"], count=5, limit=5)

        resp = {
            "search": search,
            "videos": videos
        }
    except Exception as e:
        print(e)
        resp = {
            "error": "Ups hubo un problema"
        }
        status_code = 404

    return jsonify(resp), status_code


if __name__ == '__main__':
    app.run(debug=True)
