from tkinter import *
import tkinter as tk
from tkinter import scrolledtext
from tkinter import Spinbox
from tkinter import BooleanVar

import genAI

console_text = None
input_entry = None
temperature_spinbox = None
max_new_tokens_spinbox = None
top_k_spinbox = None
top_p_spinbox = None
do_sample_var = None

dot_line = '.'.join('' for x in range(50))

# Define the range for the settings
TEMPERATURE_MIN = 0.01
TEMPERATURE_DEFAULT = 1.0
TEMPERATURE_MAX = 10.0

MAX_NEW_TOKENS_MIN = 0
MAX_NEW_TOKENS_DEFAULT = 20
MAX_NEW_TOKENS_MAX = 512

TOP_K_MIN = 0
TOP_K_DEFAULT = 50
TOP_K_MAX = 512

TOP_P_MIN = 0
TOP_P_DEFAULT = 1.0
TOP_P_MAX = 512

def get_config():
    temperature = float(temperature_spinbox.get())
    max_new_tokens = int(max_new_tokens_spinbox.get())
    top_k = int(top_k_spinbox.get())
    top_p = float(top_p_spinbox.get())

    do_sample = do_sample_var.get()

    return max_new_tokens, do_sample, temperature, top_k, top_p

def generate_text(event=None):
    user_input = input_entry.get("1.0", "end-1c")
    input_entry.delete("1.0", "end")
    if not user_input:
        return

    max_new_tokens, do_sample, temperature, top_k, top_p = get_config()
    output = genAI.generate(user_input, max_new_tokens, do_sample, temperature, top_k, top_p)
    append_to_console("> " + user_input + "\n" + dot_line + "\n" + output + "\n" + dot_line + "\n")

def append_to_console(text):
    console_text.config(state=tk.NORMAL)  # Enable text insertion
    console_text.insert("end", text)
    print(text)
    console_text.config(state=tk.DISABLED)  # Disable text editing

def ui():
    global console_text
    global input_entry
    global temperature_spinbox
    global max_new_tokens_spinbox
    global do_sample_var
    global top_k_spinbox
    global top_p_spinbox

    root = Tk()
    root.title("Generative AI Playground")
    root.resizable(False, False)

    # Create Frame widget
    main_frame = Frame(root)
    main_frame.grid(row=0, column=0)

    # Left panel - settings
    setting_frame = Frame(main_frame, width=90, height=640)
    setting_frame.grid(row=0, column=0, sticky='nsew')
    Label(setting_frame, text="Settings").grid(row=0, column=0, padx=5, pady=5)

    # Temperature Spinbox
    Label(setting_frame, text="Temperature:").grid(row=1, column=0, padx=5, pady=5)
    temperature_spinbox = Spinbox(setting_frame, from_=TEMPERATURE_MIN, to=TEMPERATURE_MAX, increment=0.01, format="%.2f")
    temperature_spinbox.grid(row=1, column=1, padx=5, pady=5)
    temperature_spinbox.delete(0, "end")  # Clear the initial content
    temperature_spinbox.insert(0, TEMPERATURE_DEFAULT)  # Set the default value

    # top_k Spinbox
    Label(setting_frame, text="Top K:").grid(row=2, column=0, padx=5, pady=5)
    top_k_spinbox = Spinbox(setting_frame, from_=TOP_K_MIN, to=TOP_K_MAX, increment=1)
    top_k_spinbox.grid(row=2, column=1, padx=5, pady=5)
    top_k_spinbox.delete(0, "end")  # Clear the initial content
    top_k_spinbox.insert(0, TOP_K_DEFAULT)  # Set the default value

    # top_p Spinbox
    Label(setting_frame, text="Top P:").grid(row=3, column=0, padx=5, pady=5)
    top_p_spinbox = Spinbox(setting_frame, from_=TOP_P_MIN, to=TOP_P_MAX, increment=0.01, format="%.2f")
    top_p_spinbox.grid(row=3, column=1, padx=5, pady=5)
    top_p_spinbox.delete(0, "end")  # Clear the initial content
    top_p_spinbox.insert(0, TOP_P_DEFAULT)  # Set the default value

    # Max_new_tokens Spinbox
    Label(setting_frame, text="Max New Tokens:").grid(row=4, column=0, padx=5, pady=5)
    max_new_tokens_spinbox = Spinbox(setting_frame, from_=MAX_NEW_TOKENS_MIN, to=MAX_NEW_TOKENS_MAX, increment=1)
    max_new_tokens_spinbox.grid(row=4, column=1, padx=5, pady=5)
    max_new_tokens_spinbox.delete(0, "end")  # Clear the initial content
    max_new_tokens_spinbox.insert(0, MAX_NEW_TOKENS_DEFAULT)  # Set the default value

    # Do Sample Checkbox
    do_sample_var = BooleanVar()
    do_sample_checkbox = Checkbutton(setting_frame, text="Do Sample", variable=do_sample_var, onvalue=True, offvalue=False)
    do_sample_checkbox.grid(row=5, column=0, padx=5, pady=5)
    do_sample_checkbox.select()  # Default to checked

    # Right panel - top - output
    interaction_frame = Frame(main_frame)
    interaction_frame.grid(row=0, column=1, padx=5, pady=5, sticky='nsew')

    output_frame = Frame(interaction_frame, width=580, height=440, bg="white")
    output_frame.grid(row=0, column=0, sticky='nsew')
    console_text = scrolledtext.ScrolledText(output_frame, wrap=tk.WORD)
    console_text.pack(side="left", fill="both", expand="True")
    console_text.config(state=tk.DISABLED)  # Disable text editing

    # Right panel - bottom - input
    input_frame = Frame(interaction_frame, width=580, height=200)
    input_frame.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')
    input_entry = tk.Text(input_frame, height=4)
    input_entry.pack(side="left", fill="both", expand="True")
    input_entry.bind("<Shift-Return>", generate_text)
    generate_button = tk.Button(input_frame, text="Generate", command=generate_text)
    generate_button.pack(side="right", fill="both", expand="True")

    root.mainloop()

ui()
