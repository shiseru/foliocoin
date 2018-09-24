import datetime
import hashlib
import json
from flask import Flask, jsonify

class Blockchain:
    def __init__(self):
        """
        Initialize the blockchain object
        """
        self.chain = []
        self.create_block(proof = 1, previous_hash = '0')

    def create_block(self, proof, previous_hash):
        """
        create new block for blockchain
        :param proof: str
        :param previous_hash: str
        :return: dict
        """
        block = {'index' : len(self.chain) + 1,
                 'timestamp' : str(datetime.datetime.now()),
                 'proof' : proof,
                 'previous_hash' : previous_hash}
        self.chain.append(block)
        return block

    def get_previous_block(self):
        """
        return previous block
        :return: dict
        """
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        """
        proof of work algorithm returning new proof
        :param previous_proof: str
        :return: str
        """
        new_proof = 1
        check_proof = False

        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof
