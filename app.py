from flask import jsonify

from flask import Flask, request

from sentiment_analysis import sentiment_analysis, emotion_analysis

app = Flask(__name__)


@app.route('/sentiment', methods=['GET'])
def sentiment():
    return jsonify(sentiment_analysis(request.args.get("query"))[0])


@app.route('/emotion', methods=['GET'])
def emotion():
    return jsonify(emotion_analysis(request.args.get("query"))[0])


if __name__ == '__main__':
    app.run()
