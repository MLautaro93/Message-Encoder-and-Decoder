import tkinter as tk

# Create the window

root = tk.Tk()
root.geometry('512x368')
root.resizable(False, False)
root.title('Message encode and decode')

# Header

header = tk.Label(text = 'ENCODE AND DECODE', font = 'helvetica 15 bold')
header.place(x = 150, y = 25)

# Define the variables

text = tk.StringVar()
private_key = tk.StringVar()
mode = tk.StringVar(value = 'e')
result_text = tk.StringVar()

# Functions

def encode(message, key):
    enc = []
    for i in range(len(message)):
        enc.append(chr((ord(message[i]) + ord(key[i % len(key)])) % 256))
    return ''.join(enc)

def decode(message, key):
    dec = []
    for i in range(len(message)):
        dec.append(chr((ord(message[i]) - ord(key[i % len(key)])) % 256))
    return ''.join(dec)

def result(*args):
    if mode.get() == 'e':
        result_text.set(encode(text.get(), private_key.get()))
    elif mode.get() == 'd':
        result_text.set(decode(text.get(), private_key.get())) 

    result_box.configure(state = 'normal')
    result_box.delete(1.0, tk.END)
    result_box.insert(tk.END, result_text.get())
    result_box.configure(state = 'disabled')

def reset():
    text.set('')
    private_key.set('')
    result_text.set('')
    result_box.configure(state = 'normal')
    result_box.delete(1.0, tk.END)
    result_box.configure(state = 'disabled')

def exit():
    root.destroy()

# Labels

message_label = tk.Label(text = 'Message: ', font = 'helvetica 10 bold')
key_label = tk.Label(text = 'Key: ', font = 'helvetica 10 bold')
mode_label = tk.Label(text = 'Mode: ', font = 'helvetica 10 bold')
result_label = tk.Label(text = 'Result: ', font = 'helvetica 10 bold')

message_label.place(x = 150, y = 75)
key_label.place(x = 150, y = 100)
mode_label.place(x = 150, y = 125)
result_label.place(x = 150, y = 250)

# Entries

message_entry = tk.Entry(textvariable = text)
key_entry = tk.Entry(textvariable = private_key)
encode_radiobutton = tk.Radiobutton(text = 'Encode', variable = mode, value = 'e')
decode_radiobutton = tk.Radiobutton(text = 'Decode', variable = mode, value = 'd')
result_box = tk.Text(font = 'arial 8', width = 20, height = 1, state = 'disabled')

message_entry.place(x = 250, y = 75)
key_entry.place(x = 250, y = 100)
encode_radiobutton.place(x = 250, y = 125)
decode_radiobutton.place(x = 325, y = 125)
result_box.place(x = 250, y = 250)

# Buttons

result_button = tk.Button(text = 'RESULT', font = 'helvetica 10 bold', bg = 'grey', command = result)
root.bind('<Return>', result)
reset_button = tk.Button(text = 'RESET', font = 'helvetica 10 bold', bg = 'green', command = reset)
exit_button = tk.Button(text = 'EXIT', font = 'helvetica 10 bold', bg = 'red', command = exit)

result_button.place(x = 275, y = 200, anchor = tk.CENTER)
reset_button.place(x = 200, y = 300)
exit_button.place(x = 300, y = 300)


root.mainloop()