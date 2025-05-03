import tkinter as tk
from tkinter import ttk, messagebox

# Function to calculate interest
def calculate_interest():
    try:
        p = float(entry_principal.get())
        r = float(entry_rate.get())
        t = float(entry_time.get())

        if interest_type.get() == "Simple Interest":
            interest = (p * r * t) / 100
            total = p + interest
        else:  # Compound Interest
            n = int(entry_frequency.get())
            interest = p * ((1 + r / (100 * n)) ** (n * t)) - p
            total = p + interest

        result_text.set(f"Interest: ₹{interest:.2f}\nTotal Amount: ₹{total:.2f}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

# GUI Setup
root = tk.Tk()
root.title("Interest Calculator")
root.geometry("450x550")
root.config(bg="#f7f7f7")

# Title
tk.Label(root, text="📊 Interest Calculator", font=("Helvetica", 20, "bold"), bg="#f7f7f7").pack(pady=15)

# Interest Type
interest_type = tk.StringVar(value="Simple Interest")
tk.Label(root, text="Choose Type:", font=("Helvetica", 12), bg="#f7f7f7").pack()
ttk.Combobox(root, textvariable=interest_type, values=["Simple Interest", "Compound Interest"], state="readonly", width=30).pack(pady=5)

# Inputs
def create_label_entry(text, var):
    tk.Label(root, text=text, font=("Helvetica", 12), bg="#f7f7f7").pack()
    entry = tk.Entry(root, font=("Helvetica", 12), textvariable=var, width=30)
    entry.pack(pady=5)
    return entry

principal_var = tk.StringVar()
rate_var = tk.StringVar()
time_var = tk.StringVar()
frequency_var = tk.StringVar(value="1")

entry_principal = create_label_entry("Principal Amount (₹):", principal_var)
entry_rate = create_label_entry("Annual Interest Rate (%):", rate_var)
entry_time = create_label_entry("Time (in years):", time_var)
entry_frequency = create_label_entry("Compounded (per year):", frequency_var)

# Calculate Button
tk.Button(root, text="Calculate", font=("Helvetica", 14, "bold"),
          bg="#4CAF50", fg="white", padx=20, pady=5, command=calculate_interest).pack(pady=20)

# Result Box (Larger and Centered)
result_text = tk.StringVar()
result_frame = tk.LabelFrame(root, text="Result", font=("Helvetica", 14, "bold"),
                             bg="white", fg="black", width=380, height=100, labelanchor='n', bd=2, relief=tk.GROOVE)
result_frame.pack(pady=10)

result_label = tk.Label(result_frame, textvariable=result_text, font=("Helvetica", 16),
                        bg="white", fg="#1e90ff", justify="center")
result_label.place(relx=0.5, rely=0.5, anchor="center")

# Run App
root.mainloop()
