from flask import Blueprint,request,jsonify
from .utils import (encrypt_symmetric,decrypt_symmetric,encrypt_asymmetric,decrypt_asymmetric,sign_data,verify_signature)

main=Blueprint('main',__name__)

#Define endpoints
#Define route handlers for our API

@main.route('/encrypt-symmetric', methods=['POST'])
def encrypt_symmetric_route():
    data=request.json.get('data')
    key=request.json.get('key')
    encrypted_data = encrypt_symmetric(data, key)
    return jsonify({'encrypted_data': encrypted_data})

@main.route('/decrypt-symmetric', methods=['POST'])
def decrypt_symmetric_route():
    data=request.json.get('data')
    key=request.json.get('key')
    decrypted_data = decrypt_symmetric(data, key)
    return jsonify({'decrypted_data': decrypted_data})

@main.route('/encrypt-asymmetric', methods=['POST'])
def encrypt_asymmetric_route():
    data=request.json.get('data')
    key=request.json.get('key')
    encrypted_data = encrypt_asymmetric(data, key)
    return jsonify({'encrypted_data': encrypted_data})

@main.route('/decrypt-asymmetric', methods=['POST'])
def decrypt_asymmetric_route():
    data=request.json.get('data')
    key=request.json.get('key')
    decrypted_data = decrypt_asymmetric(data, key)
    return jsonify({'decrypted_data': decrypted_data})

@main.route('/hash', methods=['POST'])
def hash_route():
    data=request.json.get('data')
    if not data:
        return jsonify({'error':'Missing data parameter'}),400
    if not isinstance(data,str):
        return jsonify({'error':'Only string argument can be hashed'}),400
    hash_data = hash(data)
    return jsonify({'hash_data': hash_data})

@main.route('/sign', methods=['POST'])
def sign_route():
    data=request.json.get('data')
    key=request.json.get('key')
    signature = sign_data(data, key)
    return jsonify({'signature': signature})

@main.route('/verify', methods=['POST'])
def verify_signature_route():
    data=request.json.get('data')
    signature=request.json.get('signature')
    key=request.json.get('key')
    verified = verify_signature(data, signature, key)
    if verified:
        return jsonify('Signature verified'),200
    else:
        return jsonify({'error':'Signature and key do not match'}),400