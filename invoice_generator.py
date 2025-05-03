import tkinter as tk
from tkinter import messagebox
from datetime import date

def generate_invoice():
    client = client_name.get()
    hours = float(hours_worked.get())
    rate = float(hourly_rate.get())
    total = hours * rate
    today = date.today().strftime("%Y-%m-%d")

    invoice_text = f"""
    Freelancer Invoice
    ----------------------
    Date: {today}
    Client: {client}
    Hours Worked: {hours}
    Hourly Rate: ${rate:.2f}
    Total: ${total:.2f}
    """
    messagebox.showinfo("Invoice", invoice_text)

root = tk.Tk()
root.title("Invoice Generator")
root.geometry("300x250")

tk.Label(root, text="Client Name:").pack()
client_name = tk.Entry(root)
client_name.pack()

tk.Label(root, text="Hours Worked:").pack()
hours_worked = tk.Entry(root)
hours_worked.pack()

tk.Label(root, text="Hourly Rate:").pack()
hourly_rate = tk.Entry(root)
hourly_rate.pack()

tk.Button(root, text="Generate Invoice", command=generate_invoice).pack(pady=10)

root.mainloop()