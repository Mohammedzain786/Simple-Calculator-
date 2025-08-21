import tkinter as tk
from tkinter import ttk

# Function to perform calculation
def calculate(operation):
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "×":
            result = num1 * num2
        elif operation == "÷":
            if num2 == 0:
                result_label.config(text="Error! Division by zero.")
                return
            result = num1 / num2

        # Format result nicely
        if result.is_integer():
            result = int(result)
        result_label.config(text=f"Result: {result}")

    except ValueError:
        result_label.config(text="Invalid input! Enter numbers.")

# Clear inputs
def clear_fields():
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    result_label.config(text="Result: ")

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("350x320")
root.configure(bg="black")

# Custom style for operation buttons
style = ttk.Style()
style.configure(
    "Op.TButton",
    font=("Arial", 14, "bold"),
    foreground="white",
    background="skyblue",
    padding=10
)
style.map(
    "Op.TButton",
    background=[("active", "#3399ff")],
    foreground=[("active", "white")]
)

# Number entries
tk.Label(root, text="Enter first number:", bg="black", fg="white").pack(pady=5)
entry_num1 = tk.Entry(root, justify="center", font=("Arial", 12), bg="black", fg="white", insertbackground="white")
entry_num1.pack(pady=5)

tk.Label(root, text="Enter second number:", bg="black", fg="white").pack(pady=5)
entry_num2 = tk.Entry(root, justify="center", font=("Arial", 12), bg="black", fg="white", insertbackground="white")
entry_num2.pack(pady=5)

# Operation buttons
tk.Label(root, text="Choose operation:", bg="black", fg="white").pack(pady=5)
button_frame = tk.Frame(root, bg="black")
button_frame.pack(pady=5)

ttk.Button(button_frame, text="+", style="Op.TButton", command=lambda: calculate("+")).grid(row=0, column=0, padx=5, pady=5)
ttk.Button(button_frame, text="-", style="Op.TButton", command=lambda: calculate("-")).grid(row=0, column=1, padx=5, pady=5)
ttk.Button(button_frame, text="×", style="Op.TButton", command=lambda: calculate("×")).grid(row=0, column=2, padx=5, pady=5)
ttk.Button(button_frame, text="÷", style="Op.TButton", command=lambda: calculate("÷")).grid(row=0, column=3, padx=5, pady=5)

# Clear button (red, ttk style)
style.configure("Clr.TButton", font=("Arial", 11, "bold"), foreground="white", background="#ff4444", padding=8)
style.map("Clr.TButton", background=[("active", "#cc0000")])

ttk.Button(root, text="Clear", style="Clr.TButton", command=clear_fields).pack(pady=10)

# Result label (highlighted)
result_label = tk.Label(root, text="Result: ", font=("Arial", 14, "bold"),
                        bg="white", fg="black", relief="solid", padx=10, pady=5)
result_label.pack(pady=15)

root.mainloop()
