import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np
from cryptography.fernet import Fernet
import cv2
from sklearn.cluster import KMeans
import os

# Generate encryption key
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Load encryption key
def load_key():
    return open("secret.key", "rb").read()

# Encrypt message
def encrypt_message(message):
    key = load_key()
    cipher = Fernet(key)
    return cipher.encrypt(message.encode())

# Decrypt message
def decrypt_message(encrypted_message):
    key = load_key()
    cipher = Fernet(key)
    return cipher.decrypt(encrypted_message).decode()

# Convert text to binary
def message_to_binary(message):
    return ''.join(format(byte, '08b') for byte in message)

# Convert binary to text
def binary_to_message(binary_data):
    return bytes([int(binary_data[i:i+8], 2) for i in range(0, len(binary_data), 8)])

# Hide encrypted message in image using LSB
def hide_message(image_path, message):
    img = Image.open(image_path)
    img_array = np.array(img)
    encrypted_message = encrypt_message(message)
    binary_message = message_to_binary(encrypted_message) + '1111111111111110'  # End marker

    index = 0
    for row in img_array:
        for pixel in row:
            for channel in range(3):  # RGB channels
                if index < len(binary_message):
                    pixel[channel] = (pixel[channel] & ~1) | int(binary_message[index])
                    index += 1

    encoded_img = Image.fromarray(img_array)
    
    # Ask user for filename to save encrypted image
    save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG Files", "*.png"), ("All Files", "*.*")])
    if save_path:
        encoded_img.save(save_path)
        messagebox.showinfo("Success", f"Message hidden successfully in {save_path}")

# Generate encryption key if not found
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Load encryption key (Generate if missing)
def load_key():
    if not os.path.exists("secret.key"):  # Check if file exists
        generate_key()  # Create a new key if missing
    return open("secret.key", "rb").read()



# Extract message from image
def extract_message(image_path):
    img = Image.open(image_path)
    img_array = np.array(img)
    
    binary_message = ""
    for row in img_array:
        for pixel in row:
            for channel in range(3):
                binary_message += str(pixel[channel] & 1)

    end_marker = "1111111111111110"
    if end_marker in binary_message:
        binary_message = binary_message[:binary_message.index(end_marker)]
    else:
        messagebox.showerror("Error", "No hidden message found!")
        return None

    encrypted_message = binary_to_message(binary_message)
    decrypted_message = decrypt_message(encrypted_message)
    messagebox.showinfo("Extracted Message", decrypted_message)

# AI-Based Noise Detection (Stego Security)
def detect_stego_noise(image_path):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_reshaped = img.reshape((-1, 3))

    kmeans = KMeans(n_clusters=3, random_state=42)
    kmeans.fit(img_reshaped)
    
    labels = kmeans.labels_
    noise_level = np.std(labels)

    if noise_level > 5:  # Arbitrary threshold for noise detection
        messagebox.showwarning("Warning", "Potential Steganographic noise detected!")
    else:
        messagebox.showinfo("Analysis", "No significant noise detected.")

# GUI Functions
def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        img = Image.open(file_path)
        img = img.resize((250, 250))
        img_tk = ImageTk.PhotoImage(img)
        panel.config(image=img_tk)
        panel.image = img_tk
        global selected_image
        selected_image = file_path

def encode_message():
    if selected_image:
        message = text_entry.get()
        if message:
            hide_message(selected_image, message)
        else:
            messagebox.showerror("Error", "Enter a message to hide!")
    else:
        messagebox.showerror("Error", "No image selected!")

def decode_message():
    if selected_image:
        extract_message(selected_image)
    else:
        messagebox.showerror("Error", "No image selected!")

def analyze_image():
    if selected_image:
        detect_stego_noise(selected_image)
    else:
        messagebox.showerror("Error", "No image selected!")

# GUI Setup
root = tk.Tk()
root.title("Secure AI-Powered Steganography")
root.geometry("400x500")

panel = tk.Label(root)
panel.pack()

btn_open = tk.Button(root, text="Open Image", command=open_image)
btn_open.pack()

text_entry = tk.Entry(root, width=40)
text_entry.pack()

btn_encode = tk.Button(root, text="Encode Message", command=encode_message)
btn_encode.pack()

btn_decode = tk.Button(root, text="Decode Message", command=decode_message)
btn_decode.pack()

btn_analyze = tk.Button(root, text="Analyze Image (AI Security)", command=analyze_image)
btn_analyze.pack()

root.mainloop()
