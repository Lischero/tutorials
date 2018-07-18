from flask import Flask
app = Flask(__name__)

@app.route('/service1')
def init():
    return "This is service1!"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)