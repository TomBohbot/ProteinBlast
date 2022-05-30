from flask import Flask, request, jsonify, render_template
from util import clean_sequence, valid_dna
from blast import blast
import asyncio
import redis


r = redis.StrictRedis('localhost', 6379, charset="utf-8", decode_responses=True)
app = Flask(__name__)


@app.route('/')
async def index():
    ip_address = request.remote_addr    
    data = r.lrange(f"{ip_address}::prev_query", 0, -1 )  
    return render_template('index.html', data=data)


@app.route('/',methods=['POST'])
async def dna_request():
    ip_address = request.remote_addr
    dna = clean_sequence(request.form["dna_seq"])
    print(f"Inputted DNA Sequence: {dna}")    
    if not valid_dna(dna):   
        return jsonify("Improper DNA Sequence Inputted.")
    # sequenced_dna = await blast(dna)
    r.rpush(f"{ip_address}::prev_query", dna)    
    return jsonify(f"The DNA you entered is {dna}.")


if __name__ == '__main__':
    app.run(port=5000, debug=True)