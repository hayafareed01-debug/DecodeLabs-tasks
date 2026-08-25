import tkinter as tk
import string


BACKGROUND = "#FCE4EC"
CARD = "#FFF5F8"
PINK = "#F8BBD0"
DARK_PINK = "#AD4A72"
TEXT = "#4A3A40"
GREY = "#777777"
BUTTON = "#E8DDE1"
BUTTON_TEXT = "#5F555A"
GREEN = "#2E8B57"
RED = "#D9534F"
ORANGE = "#E69A00"


def update_requirements(event=None):
    password = password_entry.get()

    if len(password) >= 8:
        length_label.config(
            text="✓  At least 8 characters",
            fg=GREEN
        )
    else:
        length_label.config(
            text="✗  At least 8 characters",
            fg=RED
        )

    if any(char.isupper() for char in password):
        uppercase_label.config(
            text="✓  Contains uppercase letter",
            fg=GREEN
        )
    else:
        uppercase_label.config(
            text="✗  Contains uppercase letter",
            fg=RED
        )

    if any(char.islower() for char in password):
        lowercase_label.config(
            text="✓  Contains lowercase letter",
            fg=GREEN
        )
    else:
        lowercase_label.config(
            text="✗  Contains lowercase letter",
            fg=RED
        )

    if any(char.isdigit() for char in password):
        number_label.config(
            text="✓  Contains a number",
            fg=GREEN
        )
    else:
        number_label.config(
            text="✗  Contains a number",
            fg=RED
        )

    if any(char in string.punctuation for char in password):
        symbol_label.config(
            text="✓  Contains a symbol",
            fg=GREEN
        )
    else:
        symbol_label.config(
            text="✗  Contains a symbol",
            fg=RED
        )

    if password and " " not in password:
        space_label.config(
            text="✓  No spaces",
            fg=GREEN
        )
    else:
        space_label.config(
            text="✗  No spaces",
            fg=RED
        )


def check_password():

    password = password_entry.get()

    if password == "":
        result_label.config(
            text="Please enter a password.",
            fg=RED
        )
        return

    length_ok = len(password) >= 8
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_number = any(char.isdigit() for char in password)
    has_symbol = any(char in string.punctuation for char in password)
    no_spaces = " " not in password

    score = sum([
        length_ok,
        has_uppercase,
        has_lowercase,
        has_number,
        has_symbol,
        no_spaces
    ])

    if score <= 2:
        strength = "WEAK"
        result_color = RED

    elif score <= 4:
        strength = "MEDIUM"
        result_color = ORANGE

    else:
        strength = "STRONG"
        result_color = GREEN

    result_label.config(
        text=f"Password Strength: {strength}",
        fg=result_color
    )


def toggle_password():

    if password_entry.cget("show") == "*":
        password_entry.config(show="")
    else:
        password_entry.config(show="*")



def clear_password():

    password_entry.delete(0, tk.END)

    length_label.config(
        text="✗  At least 8 characters",
        fg=RED
    )

    uppercase_label.config(
        text="✗  Contains uppercase letter",
        fg=RED
    )

    lowercase_label.config(
        text="✗  Contains lowercase letter",
        fg=RED
    )

    number_label.config(
        text="✗  Contains a number",
        fg=RED
    )

    symbol_label.config(
        text="✗  Contains a symbol",
        fg=RED
    )

    space_label.config(
        text="✗  No spaces",
        fg=RED
    )

    result_label.config(text="")

    password_entry.focus()


window = tk.Tk()

window.title("Password Strength Checker")
window.geometry("550x650")
window.resizable(False, False)

window.configure(bg=BACKGROUND)


main_card = tk.Frame(
    window,
    bg=CARD
)

main_card.pack(
    padx=25,
    pady=25,
    fill="both",
    expand=True
)


title_label = tk.Label(
    main_card,
    text="🔐 Password Strength Checker",
    font=("Segoe UI", 21, "bold"),
    fg=DARK_PINK,
    bg=CARD
)

title_label.pack(pady=(25, 8))



subtitle_label = tk.Label(
    main_card,
    text="Create a stronger and safer password",
    font=("Segoe UI", 11),
    fg=TEXT,
    bg=CARD
)

subtitle_label.pack(pady=(0, 12))


password_label = tk.Label(
    main_card,
    text="Enter Password",
    font=("Segoe UI", 12, "bold"),
    fg=TEXT,
    bg=CARD
)

password_label.pack(pady=(0, 3))


password_frame = tk.Frame(
    main_card,
    bg="white",
    highlightbackground=PINK,
    highlightthickness=2
)

password_frame.pack(pady=10)


password_entry = tk.Entry(
    password_frame,
    width=32,
    font=("Segoe UI", 14),
    show="*",
    bd=0,
    bg="white",
    fg=TEXT
)

password_entry.pack(
    side="left",
    padx=(10, 0),
    pady=10
)


eye_button = tk.Button(
    password_frame,
    text="👁",
    command=toggle_password,
    bd=0,
    bg="white",
    activebackground="white",
    fg=GREY,
    font=("Segoe UI", 17),
    cursor="hand2"
)

eye_button.pack(
    side="right",
    padx=10
)


password_entry.bind("<KeyRelease>", update_requirements)


check_button = tk.Button(
    main_card,
    text="CHECK PASSWORD",
    command=check_password,
    width=25,
    font=("Segoe UI", 11, "bold"),
    bg=BUTTON,
    fg=BUTTON_TEXT,
    activebackground=PINK,
    activeforeground=TEXT,
    relief="flat",
    cursor="hand2"
)

check_button.pack(pady=(8, 5))


clear_button = tk.Button(
    main_card,
    text="CLEAR",
    command=clear_password,
    width=15,
    font=("Segoe UI", 10, "bold"),
    bg=BUTTON,
    fg=BUTTON_TEXT,
    activebackground=PINK,
    activeforeground=TEXT,
    relief="flat",
    cursor="hand2"
)

clear_button.pack(pady=(5, 18))


requirements_title = tk.Label(
    main_card,
    text="Password Requirements",
    font=("Segoe UI", 13, "bold"),
    fg=DARK_PINK,
    bg=CARD
)

requirements_title.pack(pady=(0, 8))


length_label = tk.Label(
    main_card,
    text="✗  At least 8 characters",
    font=("Segoe UI", 11, "bold"),
    fg=RED,
    bg=CARD
)

length_label.pack(
    anchor="w",
    padx=100,
    pady=1
)


uppercase_label = tk.Label(
    main_card,
    text="✗  Contains uppercase letter",
    font=("Segoe UI", 11, "bold"),
    fg=RED,
    bg=CARD
)

uppercase_label.pack(
    anchor="w",
    padx=100,
    pady=1
)


lowercase_label = tk.Label(
    main_card,
    text="✗  Contains lowercase letter",
    font=("Segoe UI", 11, "bold"),
    fg=RED,
    bg=CARD
)

lowercase_label.pack(
    anchor="w",
    padx=100,
    pady=1
)


number_label = tk.Label(
    main_card,
    text="✗  Contains a number",
    font=("Segoe UI", 11, "bold"),
    fg=RED,
    bg=CARD
)

number_label.pack(
    anchor="w",
    padx=100,
    pady=1
)


symbol_label = tk.Label(
    main_card,
    text="✗  Contains a symbol",
    font=("Segoe UI", 11, "bold"),
    fg=RED,
    bg=CARD
)

symbol_label.pack(
    anchor="w",
    padx=100,
    pady=1
)


space_label = tk.Label(
    main_card,
    text="✗  No spaces",
    font=("Segoe UI", 11, "bold"),
    fg=RED,
    bg=CARD
)

space_label.pack(
    anchor="w",
    padx=100,
    pady=1
)


result_label = tk.Label(
    main_card,
    text="",
    font=("Segoe UI", 17, "bold"),
    bg=CARD
)

result_label.pack(pady=(18, 5))


password_entry.focus()

window.mainloop()
