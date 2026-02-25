import json,os
from pathlib import Path
from flask import Flask,request,jsonify
#用path写一遍；pathlib写一遍
'''
print(os.getcwd())
print(__file__)
print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.abspath(__file__))
print(os.path.basename(__file__))
print(os.path.basename(os.path.abspath(__file__)))
'''
BASE_DIR = Path(__file__).resolve().parent
file_path = Path(BASE_DIR / "data"/"stock_data.json")
#嗯。。为了打牢基础还是先用传统的叭
key_answer=[]
keyword = "tesla"
with open(file_path,"r",encoding = "utf-8") as f:
    data = json.load(f)
    for details in data:
        if details["stock"].lower() == keyword.lower():
            key_answer.append(details["comment"])

print(key_answer)
