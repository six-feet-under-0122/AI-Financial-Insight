from flask import Flask, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.route('/api/code_name')
def index():
    return jsonify({"code_name":"evan_code_name"})#新版自动jsonify
if __name__ == '__main__':
    app.run(debug=True)