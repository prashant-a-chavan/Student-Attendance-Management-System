import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

# Create the main window
root = tk.Tk()
root.title("Registration Form")
root.geometry("500x400")

# Load the background image
bg_image = Image.open("background.jpg")
bg_image = bg_image.resize((500, 400), Image.LANCZOS)  # Use LANCZOS for resampling filter
bg_image = ImageTk.PhotoImage(bg_image)

# Create a canvas and add the background image
canvas = tk.Canvas(root, width=500, height=400)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_image, anchor="nw")

# Create a label for the title
title_label = tk.Label(canvas, text="Registration Form", font=("Arial", 24), bg="#F4A460")
title_label.place(relx=0.5, rely=0.1, anchor="center", relwidth=0.8)

# Create a frame for the form inputs
form_frame = tk.Frame(canvas, bg="#F5DEB3")
form_frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.8, relheight=0.6)

# Create labels and entry boxes for the form inputs
name_label = tk.Label(form_frame, text="Name:", font=("Arial", 16), bg="#F5DEB3")
name_label.grid(row=0, column=0, padx=10, pady=10)
name_entry = tk.Entry(form_frame, font=("Arial", 16), bg="#FFEFD5", highlightthickness=0, borderwidth=2)
name_entry.grid(row=0, column=1, padx=10, pady=10)

email_label = tk.Label(form_frame, text="Email:", font=("Arial", 16), bg="#F5DEB3")
email_label.grid(row=1, column=0, padx=10, pady=10)
email_entry = tk.Entry(form_frame, font=("Arial", 16), bg="#FFEFD5", highlightthickness=0, borderwidth=2)
email_entry.grid(row=1, column=1, padx=10, pady=10)

password_label = tk.Label(form_frame, text="Password:", font=("Arial", 16), bg="#F5DEB3")
password_label.grid(row=2, column=0, padx=10, pady=10)
password_entry = tk.Entry(form_frame, show="*", font=("Arial", 16), bg="#FFEFD5", highlightthickness=0, borderwidth=2)
password_entry.grid(row=2, column=1, padx=10, pady=10)

confirm_password_label = tk.Label(form_frame, text="Confirm Password:", font=("Arial", 16), bg="#F5DEB3")
confirm_password_label.grid(row=3, column=0, padx=10, pady=10)
confirm_password_entry = tk.Entry(form_frame, show="*", font=("Arial", 16), bg="#FFEFD5", highlightthickness=0, borderwidth=2)
confirm_password_entry.grid(row=3, column=1, padx=10, pady=10)

# Create a button
submit_button = tk.Button(form_frame, text="Submit", font=("Arial", 16), bg="#F4A460", fg="white", activebackground="#FFDAB9", padx=10, pady=5)
submit_button.grid(row=4, column=1, padx=10, pady=20, sticky="e")

# Start the main
root.mainloop()