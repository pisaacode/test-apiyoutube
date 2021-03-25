from settings.conf import KEY_YOUTUBE
from flask import Flask, jsonify, request
from pyyoutube import Api as api_youtube
app = Flask(__name__)


@app.route('/lista', methods=['GET'])
def youtube():
    search = request.args.get("search", None)
    status_code = "200"
    try:
        api = api_youtube(api_key=KEY_YOUTUBE)
        videos = api.search_by_keywords(q=search, search_type=["channel", "video", "playlist"], limit=10)

        resp = {
            "search": search,
            "videos": videos
        }
    except Exception as e:
        resp = {
            "error": "Ups hubo un problema"
        }
        status_code = 404

    return jsonify(resp), status_code


if __name__ == '__main__':
    app.run(debug=True)
