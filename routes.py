from flask import Blueprint, render_template, request, jsonify
from utils import encrypt_images, decrypt_image, store_image_data, get_encrypted_data_and_salt, generate_user_id_from_password

main = Blueprint('main', __name__)

# Home Page
@main.route('/')
def home():
    return render_template('home.html')

# Upload Page
@main.route('/upload', methods=['GET', 'POST'])
def upload_page():
    if request.method == 'POST':
        image = request.files['image']
        password = request.form['password']

        # Encrypt the image and generate a user ID
        encrypted_data, user_id = encrypt_images(image.read(), password)

        # Store the encrypted image data
        store_image_data(user_id, encrypted_data)

        return jsonify({"message": "Image uploaded and encrypted successfully", "user_id": user_id})

    return render_template('upload.html')

# Retrieve Image Page (GET method to display the form)
@main.route('/retrieve', methods=['GET', 'POST'])
def retrieve_image():
    if request.method == 'GET':
        return render_template('retrive.html')

    # POST method to retrieve the image
    if request.method == 'POST':
        user_id = request.form['user_id']
        password = request.form['password']

        try:
            # Retrieve encrypted image data and salt from database
            encrypted_data, salt = get_encrypted_data_and_salt(user_id)

            # Decrypt the image using password and salt
            decrypted_image = decrypt_image(encrypted_data, password, salt)
            import io
            from flask import send_file
            # Convert decrypted image (bytes) to a file-like object
            image_io = io.BytesIO(decrypted_image)

            # Create a response that serves the image directly
            return send_file(image_io, mimetype='image/png')

        except Exception as e:
            return jsonify({"error": str(e)}), 400
