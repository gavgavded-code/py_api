from fastapi import FastAPI
from my_module import json_to_list_dict
import os
from typing import Optional
#поиск директории
script_dir= os.path.dirname(os.path.abspath(__file__))
up_dir=os.path.dirname(script_dir)
path_to_json=os.path.join(up_dir, 'BD.json')

app=FastAPI()
@app.get("/")
async def home():
    return "home"

@app.get("/students")
async def get_students():
    return json_to_list_dict(path_to_json)