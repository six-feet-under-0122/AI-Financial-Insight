from flask import Flask, request, jsonify
import json
from pathlib import Path
app = Flask(__name__)#创建一个Flask应用

@app.route('/api/search', methods=['GET'])
def search():
    keyword = request.args.get('keywords',' ')#默认值
    if not keyword or not keyword.strip():
        return jsonify({'error': "keywords cannot be empty"}),400
    BASE_DIR = Path(__file__).resolve().parent
    file_path = BASE_DIR/"data"/"stock_data.json"
    key_answers = []
    with open(file_path,'r',encoding='utf-8') as f:
        data = json.load(f)
    for d in data:
        if d["stock"].lower() == keyword.lower():
            key_answers.append(d["comment"])
    if not key_answers:
        return jsonify({'message': "no stock found",
                        'comment':[]}),200
    return jsonify({'comment':key_answers}),200
#先用本地json文件
