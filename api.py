from flask import Flask,jsonify
# from Flask import flask,jsonify # type: ignore

app = Flask(__name__)

@app.route('/success', methods=['GET'])
def success_message():
    return  "First app hosting in AWS and it is successful"

if __name__ == '__main__':
    app.run(debug=True)