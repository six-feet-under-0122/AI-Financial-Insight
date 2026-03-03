from flask import Flask, request, jsonify
import json
from pathlib import Path
from flask_cors import CORS
app = Flask(__name__)#创建一个Flask应用
CORS(app)
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
                        'comment':0,
                        'positive':0,
                        'negative':0,
                        'neutral':0,
                        'total':0
                        }),200
    else :
        #这里处理函数
        sentiment =[]
        for d in key_answers:
            sentiment.append(simple_sentiment(d))
        positive = sentiment.count(1)
        negative = sentiment.count(-1)
        neutral = sentiment.count(0)
        total = len(key_answers)


        return jsonify({'comment':key_answers,
                        'positive':positive
                        ,'negative':negative,
                        'neutral':neutral
                        ,'total':total
                        }),200

def simple_sentiment(text):
    positive = ["好","不错","积极","棒"]
    negative = ["不好","不行","消极","差"]
    for item in negative:
        if item in text:
            return -1
    for item in positive:
        if item in text:
            return 1
    return 0
#先用本地json文件
if __name__ == "__main__":
    app.run(debug=True)