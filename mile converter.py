import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    mile_input = entry_Int.get()
    km_output = mile_input * 1.61  
    output_string.set(f"{km_output:.2f} km")  

# Window
window = ttk.Window(themename = "superhero")
window.title('Miles Converter - by Ninja')
window.geometry("400x150")

# Title
title_label = ttk.Label(master=window, text="Miles to Kilometers", font=("Calibri", 24, "bold"))
title_label.pack()

# Input field
input_frame = ttk.Frame(master=window)
entry_Int = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_Int)
button = ttk.Button(master=input_frame, text="Convert", command=convert)  
entry.pack(side="left", padx=5)
button.pack(side="left")
input_frame.pack(pady=10)

# Output
output_string = tk.StringVar()
output_label = ttk.Label(master=window,
                          text="Output",
                          font=("Calibri", 20),  
                          textvariable=output_string)
output_label.pack(pady=5)

# Run
window.mainloop()
