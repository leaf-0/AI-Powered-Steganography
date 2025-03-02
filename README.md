# AI-Powered-Steganography
AI-powered steganography tool for secure message hiding using AES encryption and LSB technique. Includes noise detection for steganalysis.

🛡️ Secure Data Hiding in Image Using AI-Powered Steganography
🔐 Hide confidential messages inside images using AES encryption and AI-based noise detection!


(Replace with an actual GIF or image showcasing the project in action)





🔍 Overview
This project enables secure data hiding within images using AES encryption and Least Significant Bit (LSB) steganography. It also includes AI-based noise detection to identify potential steganography artifacts in images.

✨ Features
✔️ AES Encryption to secure the hidden message
✔️ AI-Based Noise Detection using KMeans Clustering
✔️ LSB Steganography for undetectable message hiding
✔️ Graphical User Interface (GUI) for easy usage
✔️ Automatic Key Generation for encryption
✔️ Custom Save Option for encrypted images
✔️ Future-Ready – Quantum Cryptography & Blockchain Integration

📸 Screenshots
Encoding Message	Decoding Message	AI Noise Detection
(Replace placeholder images with actual screenshots)

⚙️ Installation
🔹 Prerequisites
📌 Python 3.8+ is required. Install it from here.

🔹 Clone the Repository
bash
Copy
Edit
git clone https://github.com/yourusername/secure-stego.git
cd secure-stego
🔹 Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
If you encounter errors, manually install compatible versions:

bash
Copy
Edit
pip install pillow cryptography numpy==1.24.4 opencv-python==4.5.5.64 scikit-learn==1.0.2
🚀 Usage
🔹 Run the Application
bash
Copy
Edit
python stego.py
🔹 How It Works?
Select an Image – Choose a PNG/JPEG file.
Enter Secret Message – Type your hidden text.
Encrypt & Hide – Click "Encode Message" to encrypt and save the image.
Extract Hidden Data – Click "Decode Message" to reveal the secret.
Analyze for Security – Check if an image has hidden data using AI detection.
📂 Project Structure
bash
Copy
Edit
📦 Secure-Stego
 ┣ 📜 stego.py              # Main script
 ┣ 📜 requirements.txt       # Required dependencies
 ┣ 📜 secret.key             # Encryption key (auto-generated)
 ┣ 📜 LICENSE                # License file
 ┗ 📜 README.md              # This README file
🌍 Future Scope
🚀 What’s Next?

 Quantum Cryptography Support
 Blockchain-Based Authentication
 Steganography in Video & Audio Files
 Real-time Secure Messaging
💡 Contributing
💙 We welcome contributions!

Fork the repository
Create a new branch: git checkout -b feature-name
Commit your changes: git commit -m "Added new feature"
Push and open a Pull Request
📜 License
This project is licensed under the MIT License – see the LICENSE file for details.

📬 Contact
📧 Email: [your.email@example.com]
💼 LinkedIn: Your LinkedIn Profile
🌎 GitHub: yourusername

⭐ Star This Repo!
If you found this project useful, don’t forget to give it a star ⭐! It helps others discover it.
