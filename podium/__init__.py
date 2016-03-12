from flask import Flask, jsonify, request
from flask.ext.cors import CORS

import ranking
import api

def run():
    app = Flask("Podium")
    CORS(app)

    @app.route("/search")
    def search():

        raw = api.get_info(request.args.get('city'), request.args.get('job'))

        res = ranking.rankme(raw)

        return jsonify({
            'req': {
                'city': request.args.get('city'),
                'job': request.args.get('job')
            },
            'res' : res
        })

    app.run(debug=True, host='0.0.0.0', port=8080)
