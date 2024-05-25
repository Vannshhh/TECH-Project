#[project]

"""
a) Build a Temperature Conversion Application
Build a temperature conversion application that converts temperature from
degree Fahrenheit to degree Celcius and vice versa, using the python tkinter module."""


import tkinter as tk

def ftoc(fahrenheit):
    return (fahrenheit - 32) * 5/9

def ctof(celsius):
    return (celsius * 9/5) + 32

def convert_temperature():
    try:
        temperature = float(entry_temp.get())
        if choice.get() == "Fahrenheit to Celsius":
            converted_temp = ftoc(temperature)
            result_label.config(text=f"{temperature}°F is {converted_temp:.2f}°C")
        elif choice.get() == "Celsius to Fahrenheit":
            converted_temp = ctof(temperature)
            result_label.config(text=f"{temperature}°C is {converted_temp:.2f}°F")
    except ValueError:
        result_label.config(text="Please enter a valid temperature!")

root = tk.Tk()
root.title("Temperature Converter")

entry_temp = tk.Entry(root)
entry_temp.grid(row=0, column=0, padx=20, pady=20)

choice = tk.StringVar()
choice.set("Fahrenheit to Celsius")

f_to_c_radio = tk.Radiobutton(root, text="Fahrenheit to Celsius", variable=choice, value="Fahrenheit to Celsius")
f_to_c_radio.grid(row=1, column=0, padx=10, pady=10, sticky="w")

c_to_f_radio = tk.Radiobutton(root, text="Celsius to Fahrenheit", variable=choice, value="Celsius to Fahrenheit")
c_to_f_radio.grid(row=2, column=0, padx=10, pady=10, sticky="w")

convert_button = tk.Button(root, text="Convert", command=convert_temperature)
convert_button.grid(row=0, column=1, padx=20, pady=20)

result_label = tk.Label(root, text="")
result_label.grid(row=1, column=1, columnspan=2, padx=20, pady=20)

root.mainloop()
