import tkinter as tk
from functools import partial
import re

# Fungsi untuk menambahkan angka atau simbol ke layar
def click(event, expression):
    current_text = display.get()
    if current_text == "0":
        current_text = ""
    display.delete(0, tk.END)
    display.insert(tk.END, current_text + expression)

# Fungsi untuk menghitung hasil, termasuk perhitungan persentase
def calculate():
    try:
        # Deteksi jika ada persentase dalam ekspresi
        expression = display.get()
        expression = re.sub(r'(\d+)%', r'(\1/100)', expression)  # Ubah angka% menjadi angka/100
        
        result = str(eval(expression))
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    except Exception:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

# Fungsi untuk membersihkan layar
def clear():
    display.delete(0, tk.END)
    display.insert(tk.END, "0")

# Fungsi untuk mengubah nilai positif/negatif
def toggle_sign():
    current_text = display.get()
    if current_text.startswith("-"):
        display.delete(0, tk.END)
        display.insert(tk.END, current_text[1:])  # Hapus tanda negatif
    else:
        display.delete(0, tk.END)
        display.insert(tk.END, "-" + current_text)  # Tambahkan tanda negatif di depan

# Membuat jendela utama
root = tk.Tk()
root.title("Kalkulator")
root.geometry("300x400")

# Membuat layar kalkulator
display = tk.Entry(root, font=("Arial", 24), borderwidth=0, relief="solid", justify="right")
display.grid(row=0, column=0, columnspan=4, sticky="nsew")
display.insert(tk.END, "0")

# Daftar tombol
buttons = [
    ("AC", 1, 0, clear, "#f0f0f0"), ("+/-", 1, 1, toggle_sign, "#f0f0f0"),
    ("%", 1, 2, lambda: click(None, "%"), "#f0f0f0"), ("/", 1, 3, lambda: click(None, "/"), "#FFD700"),
    ("7", 2, 0, lambda: click(None, "7"), "#f0f0f0"), ("8", 2, 1, lambda: click(None, "8"), "#f0f0f0"),
    ("9", 2, 2, lambda: click(None, "9"), "#f0f0f0"), ("*", 2, 3, lambda: click(None, "*"), "#FFD700"),
    ("4", 3, 0, lambda: click(None, "4"), "#f0f0f0"), ("5", 3, 1, lambda: click(None, "5"), "#f0f0f0"),
    ("6", 3, 2, lambda: click(None, "6"), "#f0f0f0"), ("-", 3, 3, lambda: click(None, "-"), "#FFD700"),
    ("1", 4, 0, lambda: click(None, "1"), "#f0f0f0"), ("2", 4, 1, lambda: click(None, "2"), "#f0f0f0"),
    ("3", 4, 2, lambda: click(None, "3"), "#f0f0f0"), ("+", 4, 3, lambda: click(None, "+"), "#FFD700"),
    ("0", 5, 0, lambda: click(None, "0"), "#f0f0f0", 2), (",", 5, 2, lambda: click(None, "."), "#f0f0f0"),
    ("=", 5, 3, calculate, "#FFD700")
]

# Menambahkan tombol ke jendela
for button in buttons:
    if len(button) == 5:
        text, row, col, command, bg_color = button
        col_span = 1
    elif len(button) == 6:
        text, row, col, command, bg_color, col_span = button
    else:
        continue

    btn = tk.Button(root, text=text, command=command, font=("Arial", 18), borderwidth=0, relief="solid", bg=bg_color)
    btn.grid(row=row, column=col, columnspan=col_span, sticky="nsew", ipadx=10, ipady=10)

# Mengatur tata letak grid agar dapat diperluas
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# Menjalankan aplikasi
root.mainloop()