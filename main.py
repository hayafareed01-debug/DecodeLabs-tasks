import tkinter as tk
from tkinter import messagebox


# Caesar Cipher Function

def caesar_cipher(text, shift):
    result = ""

    for char in text:

        # Uppercase letters
        if char.isupper():
            result += chr(
                (ord(char) - ord("A") + shift) % 26 + ord("A")
            )

        # Lowercase letters
        elif char.islower():
            result += chr(
                (ord(char) - ord("a") + shift) % 26 + ord("a")
            )

        # Keep spaces, numbers and symbols unchanged
        else:
            result += char

    return result


# Encrypt Function

def encrypt_text():

    text = input_text.get("1.0", tk.END).rstrip("\n")

    if not text:
        messagebox.showwarning(
            "No Text",
            "Please enter some text first."
        )
        return

    try:
        shift = int(key_entry.get())
    except ValueError:
        messagebox.showerror(
            "Invalid Key",
            "Please enter a whole number as the encryption key."
        )
        return

    encrypted = caesar_cipher(text, shift)

    encrypted_output.delete("1.0", tk.END)
    encrypted_output.insert(tk.END, encrypted)

    decrypted_output.delete("1.0", tk.END)
    decrypted_output.insert(
        tk.END,
        caesar_cipher(encrypted, -shift)
    )


# Decrypt Function

def decrypt_text():

    text = input_text.get("1.0", tk.END).rstrip("\n")

    if not text:
        messagebox.showwarning(
            "No Text",
            "Please enter the encrypted text first."
        )
        return

    try:
        shift = int(key_entry.get())
    except ValueError:
        messagebox.showerror(
            "Invalid Key",
            "Please enter a whole number as the encryption key."
        )
        return

    decrypted = caesar_cipher(text, -shift)

    decrypted_output.delete("1.0", tk.END)
    decrypted_output.insert(tk.END, decrypted)

    encrypted_output.delete("1.0", tk.END)
    encrypted_output.insert(
        tk.END,
        caesar_cipher(decrypted, shift)
    )


# Clear Function

def clear_all():

    input_text.delete("1.0", tk.END)
    encrypted_output.delete("1.0", tk.END)
    decrypted_output.delete("1.0", tk.END)

    key_entry.delete(0, tk.END)
    key_entry.insert(0, "3")


# Main Window

root = tk.Tk()

root.title("Basic Encryption & Decryption")

root.geometry("760x650")

root.minsize(700, 600)

# Dark blue-gray background
root.configure(bg="#263746")


# Fonts

TITLE_FONT = ("Segoe UI Semibold", 22)
SUBTITLE_FONT = ("Segoe UI", 11)
LABEL_FONT = ("Segoe UI Semibold", 12)
BUTTON_FONT = ("Segoe UI Semibold", 11)
TEXT_FONT = ("Consolas", 11)


# Title

title = tk.Label(
    root,
    text="🔐 Basic Encryption & Decryption",
    font=TITLE_FONT,
    bg="#263746",
    fg="#f2f6f9"
)

title.pack(pady=(25, 4))


# Subtitle

subtitle = tk.Label(
    root,
    text="Caesar Cipher — A Simple Introduction to Encryption",
    font=SUBTITLE_FONT,
    bg="#263746",
    fg="#b8c7d3"
)

subtitle.pack(pady=(0, 15))


# Encryption Key

key_frame = tk.Frame(
    root,
    bg="#263746"
)

key_frame.pack(pady=2)


key_label = tk.Label(
    key_frame,
    text="Encryption Key (Shift):",
    font=("Segoe UI Semibold", 11),
    bg="#263746",
    fg="#e4edf3"
)

key_label.pack(
    side=tk.LEFT,
    padx=5
)


key_entry = tk.Entry(
    key_frame,
    width=8,
    font=("Consolas", 11),
    justify="center",
    relief="solid",
    bd=1,
    bg="#f7fafc",
    fg="#263746"
)

key_entry.pack(
    side=tk.LEFT,
    padx=5
)

key_entry.insert(0, "3")


# Input Section

input_frame = tk.Frame(
    root,
    bg="#263746"
)

input_frame.pack(
    fill="x",
    padx=35,
    pady=(5, 10)
)


input_label = tk.Label(
    input_frame,
    text="Enter Text",
    font=LABEL_FONT,
    bg="#263746",
    fg="#e4edf3"
)

input_label.pack(anchor="w")


input_text = tk.Text(
    input_frame,
    height=5,
    font=TEXT_FONT,
    wrap="word",
    relief="solid",
    bd=1,
    bg="#f7fafc",
    fg="#263746",
    insertbackground="#263746"
)

input_text.pack(
    fill="x",
    pady=5
)


# Buttons

button_frame = tk.Frame(
    root,
    bg="#263746"
)

button_frame.pack(pady=2)


# Encrypt Button
encrypt_button = tk.Button(
    button_frame,
    text="🔒  ENCRYPT",
    command=encrypt_text,
    font=BUTTON_FONT,
    width=15,
    bg="#527da5",
    fg="white",
    activebackground="#426886",
    activeforeground="white",
    relief="flat",
    padx=10,
    pady=10,
    cursor="hand2"
)

encrypt_button.pack(
    side=tk.LEFT,
    padx=10
)


# Decrypt Button
decrypt_button = tk.Button(
    button_frame,
    text="🔓  DECRYPT",
    command=decrypt_text,
    font=BUTTON_FONT,
    width=15,
    bg="#568a69",
    fg="white",
    activebackground="#467255",
    activeforeground="white",
    relief="flat",
    padx=10,
    pady=10,
    cursor="hand2"
)

decrypt_button.pack(
    side=tk.LEFT,
    padx=10
)


# Clear Button
clear_button = tk.Button(
    button_frame,
    text="🗑  CLEAR",
    command=clear_all,
    font=BUTTON_FONT,
    width=15,
    bg="#9d5f5f",
    fg="white",
    activebackground="#7e4d4d",
    activeforeground="white",
    relief="flat",
    padx=10,
    pady=10,
    cursor="hand2"
)

clear_button.pack(
    side=tk.LEFT,
    padx=10
)


# Output Section

output_frame = tk.Frame(
    root,
    bg="#263746"
)

output_frame.pack(
    fill="both",
    expand=True,
    padx=35,
    pady=(12, 10)
)


# Encrypted Output

encrypted_label = tk.Label(
    output_frame,
    text="Encrypted Output",
    font=LABEL_FONT,
    bg="#263746",
    fg="#e4edf3"
)

encrypted_label.pack(
    anchor="w"
)


encrypted_output = tk.Text(
    output_frame,
    height=4,
    font=TEXT_FONT,
    wrap="word",
    relief="solid",
    bd=1,
    bg="#f7fafc",
    fg="#263746",
    insertbackground="#263746"
)

encrypted_output.pack(
    fill="x",
    pady=(5, 10)
)


# Decrypted Output
decrypted_label = tk.Label(
    output_frame,
    text="Decrypted Output",
    font=LABEL_FONT,
    bg="#263746",
    fg="#e4edf3"
)

decrypted_label.pack(
    anchor="w"
)


decrypted_output = tk.Text(
    output_frame,
    height=4,
    font=TEXT_FONT,
    wrap="word",
    relief="solid",
    bd=1,
    bg="#f7fafc",
    fg="#263746",
    insertbackground="#263746"
)

decrypted_output.pack(
    fill="x",
    pady=5
)


# Footer
footer = tk.Label(
    root,
    text="Note: Caesar Cipher is for learning purposes and is not secure for real passwords or sensitive data.",
    font=("Segoe UI", 9),
    bg="#263746",
    fg="#9fb0bd"
)

footer.pack(
    pady=(0, 12)
)

# Start Application
root.mainloop()
