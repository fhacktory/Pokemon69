from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/search")
def search():
    return jsonify({
        'req': {
            'city': request.args.get('city'),
            'job': request.args.get('job')
        }
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
