import tkinter as tk

def say_hello():
    hello_label.config(text="Hello, GUI!")

# Create the main window
root = tk.Tk()
root.title("Hello GUI")

# Create a label widget
hello_label = tk.Label(root, text="Hello, world!")
hello_label.pack(padx=20, pady=20)

# Create a button widget
hello_button = tk.Button(root, text="Say Hello", command=say_hello)
hello_button.pack(padx=10, pady=10)

# Start the main loop
root.mainloop()
