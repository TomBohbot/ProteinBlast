import redis
import logging
from blast import blast
from verify_sequences import clean_sequence, valid_dna
from flask import Flask, request, jsonify, render_template
from constants import KEY, OUTPUT_SUCCESS, OUTPUT_ERROR, OUTPUT_EMPTY

r = redis.StrictRedis('localhost', 6379, charset="utf-8", decode_responses=True)
app = Flask(__name__)


@app.route('/')
async def index():
    ip_address = request.remote_addr
    logging.info(f'{ip_address} has visited site home page')
    data = r.lrange(f"{ip_address}::{KEY}", 0, -1 )  
    return render_template('index.html', data=data)


@app.route('/',methods=['POST'])
async def dna_request():
    ip_address = request.remote_addr
    input_dna = request.form['dna_seq']
    logging.info(f'Received DNA input: {input_dna} from user: {ip_address}')
    dna = clean_sequence(input_dna)    
    if not valid_dna(dna):
        logging.info(f'Sending user: {ip_address} inputted invalid DNA: {input_dna}')
        return jsonify(OUTPUT_ERROR)
    sequenced_dna = await blast(dna) 
    if sequenced_dna == None:
        logging.info(f'Sending user: {ip_address} had no match on DNA: {dna}')
        return OUTPUT_EMPTY
    response = OUTPUT_SUCCESS.format(
        sequenced_dna.dna, 
        sequenced_dna.genome,
        sequenced_dna.protein,
        sequenced_dna.match
    )
    r.lpush(f"{ip_address}::{KEY}", response)
    logging.info(f'Sending user: {ip_address} had a match on DNA: {response}')
    return response


if __name__ == '__main__':
    app.run(debug=True)