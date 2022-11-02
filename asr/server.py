# -*- coding: utf-8 -*-

import json
import os
from flask import Flask, request
from asr import asr
from tools.nnet_recognizer import recognizer
app = Flask(__name__)



def _declareRec():
    dir="models/"
    final=dir+"final.mdl"
    hclg=dir+"graph/HCLG.fst"
    words=dir+"graph/words.txt"
    try:
        rec = recognizer(final, hclg, words)
        return rec
    except Exception as e:
        print("Napaka pri pripravi razpoznavalnika")

@app.route('/')
@app.route('/', methods=['GET'])
def get_response():
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

@app.route('/', methods=['POST'])
def post_response():
    try:
        if request.method == 'POST':
            wav_file=request.files['file']
            filePath = "temp/"+wav_file.filename
            wav_file.save(filePath)
            asr_result=asr(filePath,rec)
            os.remove(filePath)
            result='{"result":' + '"' + asr_result + '"}'
            return result
    except Exception as e:
        print(e)

if __name__ == '__main__':
    rec=_declareRec()
    app.run(host='0.0.0.0', port='5000')
