import tkinter as tk
from tkinter import ttk

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")

        self.result_var = tk.StringVar()
        self.result_var.set('')

        self.result_entry = ttk.Entry(self.master, textvariable=self.result_var, justify='right')
        self.result_entry.grid(row=0, column=0, columnspan=4, sticky='nsew')

        # Define the buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+'
        ]

        # Create and place the buttons on the grid
        for i, button_text in enumerate(buttons):
            row = i // 4 + 1
            col = i % 4
            button = ttk.Button(self.master, text=button_text, command=lambda value=button_text: self.button_click(value))
            button.grid(row=row, column=col, sticky='nsew')

        # Configure row and column weights so that they expand proportionally
        for i in range(1, 6):
            self.master.grid_rowconfigure(i, weight=1)
            self.master.grid_columnconfigure(i, weight=1)

    def button_click(self, value):
        current_value = self.result_var.get()

        if value == 'C':
            self.result_var.set('')
        elif value == '=':
            try:
                result = str(eval(current_value))
                self.result_var.set(result)
            except:
                self.result_var.set('Error')
        elif value.isdigit():
        # Handle digit input separately
            self.result_var.set(value)
        else:
        # Handle operators (add, subtract, multiply, divide)
            if current_value.isdigit() or current_value == 'Error':
            # If the current value is a digit or an error, perform the calculation
                self.result_var.set(value)
            else:
            # If the current value is an operator, replace it with the new operator
                self.result_var.set(current_value[:-1] + value)




if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
