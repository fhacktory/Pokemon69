import numpy as np
import scipy as sp
import matplotlib as plt
import scipy as stats

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/search")
def search():
    return jsonify({
        'req': {
            'city': request.args.get('city'),
            'job': request.args.get('job')
        },
        'res' : {

        }
    })

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
