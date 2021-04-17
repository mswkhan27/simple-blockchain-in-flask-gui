import os
import random
from flask import (
    Flask,
    jsonify,
    g,
    redirect,
    render_template,
    request,
    session,
    json,
    url_for, Response
)
from blockchain import Blockchain
from blockchain import Block

app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
blockchain = Blockchain()
print(blockchain.isChainValid())


@app.route('/')
def main():
    for n in range(1):
        blockchain.add(Block("Block " + str(n + 1)))

    return render_template('index.html', blockchain=blockchain)


@app.route('/addBlock', methods=['POST'])
def addBlock():
    dataVal = request.form['dataName']
    blockchain.add(Block(dataVal))
    hashVal = blockchain.chain[-1].hash
    prevHashVal = blockchain.chain[-1].previous_hash
    timestampVal = blockchain.chain[-1].timestamp
    print(blockchain.isChainValid())
    return jsonify(
        {'status': 'OK', 'hash': hashVal, 'data': dataVal, 'prevhash': prevHashVal, 'timestamp': timestampVal})


@app.route('/checkChain', methods=['POST'])
def checkChain():
    blockVal = request.form['blockId']
    dataVal = request.form['newData']
    blockchain.chain[int(blockVal)].data = dataVal

    status = blockchain.isChainValid()

    return jsonify({'status': status})


@app.route('/getchain', methods=['GET'])
def getchain():
    j = 0
    blockChainJsonList = []
    for c in blockchain.chain:
        obj = {
            'hash': c.hash,
            'data': c.data,
            'prevhash': c.previous_hash,
            'timestamp': c.timestamp
        }



        blockChainJsonList.append(obj)
        j += 1

    obj1 = {
        'hash': "null",
        'data': "null",
        'prevhash': "null",
        'timestamp': "null"
    }
    blockChainJsonList.append(obj1)
    blockchainJson = {'chain': blockChainJsonList}

    return jsonify(blockchainJson)
