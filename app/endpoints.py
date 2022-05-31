import redis
from blast import blast
from verify_sequences import clean_sequence, valid_dna
from flask import Flask, request, jsonify, render_template
from constants import KEY, OUTPUT_SUCCESS, OUTPUT_ERROR, OUTPUT_EMPTY

r = redis.StrictRedis('localhost', 6379, charset="utf-8", decode_responses=True)
app = Flask(__name__)


@app.route('/')
async def index():
    ip_address = request.remote_addr    
    data = r.lrange(f"{ip_address}::{KEY}", 0, -1 )  
    return render_template('index.html', data=data)


@app.route('/',methods=['POST'])
async def dna_request():
    ip_address = request.remote_addr
    dna = clean_sequence(request.form['dna_seq'])    
    if not valid_dna(dna):   
        return jsonify(OUTPUT_ERROR)
    sequenced_dna = await blast(dna) 
    if sequenced_dna == None:
        return OUTPUT_EMPTY
    response = OUTPUT_SUCCESS.format(
        sequenced_dna.dna, 
        sequenced_dna.genome,
        sequenced_dna.protein,
        sequenced_dna.match
    )
    r.rpush(f"{ip_address}::{KEY}", response)
    return response


if __name__ == '__main__':
    app.run(port=5000, debug=True)