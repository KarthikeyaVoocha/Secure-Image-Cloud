# Secure Image Cloud

## Overview
Secure Image Cloud is a web application that allows users to securely upload, encrypt, and manage images in the cloud. By using strong encryption techniques, the application ensures that even if the database is compromised, unauthorized users cannot access the encrypted images. User IDs are generated based on a password, and images can only be retrieved with the correct user ID and password.

## Features
- **Secure Image Upload**: Users can upload images securely, with encryption applied to ensure data privacy.
- **Password-Based Encryption**: Images are encrypted using a password provided by the user. The password is never stored, adding an extra layer of security.
- **User ID Generation**: User IDs are generated based on the user's password, making it impossible to guess or retrieve the original password.
- **Image Retrieval**: Users can retrieve their images by providing their generated user ID and password, which are checked against the stored encrypted data.

## Technologies Used
- **Backend**: Flask, Python
- **Database**: MongoDB
- **Encryption**: AES, hashlib, base64
- **Frontend**: HTML, CSS, JavaScript

## Installation
To set up the project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/Secure_Image_Cloud.git
   cd Secure_Image_Cloud

2. ** Install dependencies**:
   pip install -r requirements.txt

3. ** Run the code**:
   python app.py

