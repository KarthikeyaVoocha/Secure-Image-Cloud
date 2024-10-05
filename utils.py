import hashlib
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from database import mongo
import os

# Generate a random salt
def generate_salt():
    return os.urandom(16)

# Encrypt the image and generate a user ID
def encrypt_images(image_data, password):
    salt = generate_salt()
    key = hashlib.sha256(password.encode() + salt).digest()

    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(image_data, AES.block_size))

    iv = cipher.iv
    encrypted_data = base64.b64encode(iv + ct_bytes).decode('utf-8')
    user_id = base64.b64encode(hashlib.sha256(password.encode()).digest()).decode('utf-8')

    return {'salt': base64.b64encode(salt).decode('utf-8'), 'encrypted_data': encrypted_data}, user_id

# Decrypt the image
def decrypt_image(encrypted_data, password, salt):
    encrypted_data = base64.b64decode(encrypted_data)
    salt = base64.b64decode(salt)

    key = hashlib.sha256(password.encode() + salt).digest()

    iv = encrypted_data[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ct = encrypted_data[16:]

    decrypted_data = unpad(cipher.decrypt(ct), AES.block_size)
    return decrypted_data

# Store image data in the database
def store_image_data(user_id, encrypted_data):
    mongo.db.images.insert_one({
        'user_id': user_id,
        'encrypted_data': encrypted_data['encrypted_data'],
        'salt': encrypted_data['salt']
    })

# Retrieve the encrypted data and salt from the database
def get_encrypted_data_and_salt(user_id):
    record = mongo.db.images.find_one({'user_id': user_id})
    if record:
        return record['encrypted_data'], record['salt']
    else:
        raise Exception("User ID not found")

import hashlib
import base64

# Generate user ID from password
def generate_user_id_from_password(password):
    # Use SHA-256 hashing to generate a unique ID based on the password
    return base64.b64encode(hashlib.sha256(password.encode()).digest()).decode('utf-8')
