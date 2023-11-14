import tkinter as tk

root = tk.Tk()
root.title("Simple Calculator")

display = tk.Entry(root, borderwidth=5, width=35)
display.grid(row=0, column=0, columnspan=3)


def digit(number):
    current = display.get()
    display.delete(0, 'end')
    display.insert(0, str(current) + str(number))


def clear():
    display.delete(0, 'end')


def add():
    first_number = display.get()
    global f_num
    f_num = int(first_number)
    display.delete(0, 'end')


def equals():
    second_number = display.get()
    display.delete(0, 'end')
    display.insert(0, f_num + int(second_number))


# Creating all buttons to be used
button1 = tk.Button(root, text=1, padx=40, pady=35, command=lambda: digit(1))
button2 = tk.Button(root, text=2, padx=40, pady=35, command=lambda: digit(2))
button3 = tk.Button(root, text=3, padx=40, pady=35, command=lambda: digit(3))
button4 = tk.Button(root, text=4, padx=40, pady=35, command=lambda: digit(4))
button5 = tk.Button(root, text=5, padx=40, pady=35, command=lambda: digit(5))
button6 = tk.Button(root, text=6, padx=40, pady=35, command=lambda: digit(6))
button7 = tk.Button(root, text=7, padx=40, pady=35, command=lambda: digit(7))
button8 = tk.Button(root, text=8, padx=40, pady=35, command=lambda: digit(8))
button9 = tk.Button(root, text=9, padx=40, pady=35, command=lambda: digit(9))
button0 = tk.Button(root, text=0, padx=40, pady=35, command=lambda: digit(0))
button_add = tk.Button(root, text="+", padx=40, pady=35, command=add)
button_equals = tk.Button(root, text="  = ", padx=85, pady=35, command=equals)
button_clear = tk.Button(root, text="Clear", padx=80, pady=35, command=clear)

# Displaying all created buttons
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
button0.grid(row=4, column=0)
button_add.grid(row=5, column=0)
button_equals.grid(row=4, column=1, columnspan=2)
button_clear.grid(row=5, column=1, columnspan=2)

root.mainloop()