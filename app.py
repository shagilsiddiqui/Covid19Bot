from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>This is heruko gandu</h1>'
@app.route("/bot", methods=["POST"])
def response():
    query = dict(request.form)['query']
    res=query
    return jsonify({"response" : res})

if __name__ == '__main__':
    app.run(debug=True)