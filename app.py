from settings.conf import KEY_YOUTUBE
from flask import Flask, jsonify
from pyyoutube import Api as api_youtube
app = Flask(__name__)



@app.route('/lista', methods=['GET'])
def youtube():
    print('yoooo')
    print(KEY_YOUTUBE)
    status_code = "200"
    try:
        api = api_youtube(api_key=KEY_YOUTUBE)
        videos = api.search_by_keywords(q="surfing", search_type=["channel", "video", "playlist"], limit=10)

        resp = {
            "mensaje": "salida",
            "videos": videos
        }
    except Exception as e:

        resp = {
            "errror": "Ups hubo un problema"
        }
        status_code = 404

    return jsonify(resp), status_code


if __name__ == '__main__':
    app.run(debug=True)
