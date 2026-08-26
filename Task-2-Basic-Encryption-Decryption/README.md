#  Basic Encryption & Decryption Application

A simple desktop application built with **Python** and **Tkinter** that demonstrates the **Caesar Cipher** encryption technique. Users can encrypt and decrypt text using a custom shift key through an easy-to-use graphical interface.

## Features

* Encrypt text using Caesar Cipher
* Decrypt text using the same key
* Custom shift key support
* Simple and user-friendly GUI
* Input validation and error handling
* Clear button to reset all fields
* Preserves spaces, numbers, and symbols

## Technologies Used

* Python
* Tkinter
* PyInstaller (for EXE creation)

## Screenshots

### Main Interface

![Main Interface](screenshot1.png)

### Example Output

![Example Output](screenshot2.png)

## Project Structure

```text
Basic Encryption Decryption/
│
├── main.py
├── CaesarCipherApp.exe
├── README.md
├── screenshot1.png
├── screenshot2.png
├── .gitignore
└── .gitattributes
```

## How to Run

### Option 1: Run the EXE

Simply double-click:

```text
CaesarCipherApp.exe
```

No Python installation is required.

### Option 2: Run the Source Code

```bash
python main.py
```

## How It Works

The Caesar Cipher encrypts text by shifting each letter by a fixed number of positions in the alphabet.

Example:

```text
Original Text : HELLO
Shift Key    : 3
Encrypted    : KHOOR
```

To decrypt, the same shift value is applied in the opposite direction.

## Author

**Haya Ali**
Computer Science Student

## Note

This project was created for learning and educational purposes. The Caesar Cipher is a basic encryption method and is not suitable for securing sensitive information.
