import tkinter as tk
from tkinter import ttk

# ---------------------------
# Verhoeff algorithm for Aadhaar validation
# ---------------------------
d = [
    [0,1,2,3,4,5,6,7,8,9],
    [1,2,3,4,0,6,7,8,9,5],
    [2,3,4,0,1,7,8,9,5,6],
    [3,4,0,1,2,8,9,5,6,7],
    [4,0,1,2,3,9,5,6,7,8],
    [5,9,8,7,6,0,4,3,2,1],
    [6,5,9,8,7,1,0,4,3,2],
    [7,6,5,9,8,2,1,0,4,3],
    [8,7,6,5,9,3,2,1,0,4],
    [9,8,7,6,5,4,3,2,1,0]
]

p = [
    [0,1,2,3,4,5,6,7,8,9],
    [1,5,7,6,2,8,3,0,9,4],
    [5,8,0,3,7,9,6,1,4,2],
    [8,9,1,6,0,4,3,5,2,7],
    [9,4,5,3,1,2,6,8,7,0],
    [4,2,8,6,5,7,3,9,0,1],
    [2,7,9,3,8,0,6,4,1,5],
    [7,0,4,6,9,1,3,2,5,8]
]

inv = [0,4,3,2,1,5,6,7,8,9]

def validate_verhoeff(num):
    c = 0
    num = list(map(int, reversed(num)))
    for i, item in enumerate(num):
        c = d[c][p[(i % 8)][item]]
    return c == 0


# ---------------------------
# GUI App
# ---------------------------
class AadhaarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aadhaar Validator")
        self.root.resizable(False, False)

        # Center window
        w, h = 460, 520
        ws, hs = root.winfo_screenwidth(), root.winfo_screenheight()
        x, y = (ws // 2) - (w // 2), (hs // 2) - (h // 2)
        root.geometry(f"{w}x{h}+{x}+{y}")

        # Theme colors
        self.light_theme = {"bg": "#f8f9fa", "fg": "#212529", "entry": "white"}
        self.dark_theme = {"bg": "#212529", "fg": "#f8f9fa", "entry": "#343a40"}
        self.current_theme = self.light_theme
        root.configure(bg=self.current_theme["bg"])

        # Title
        self.title_label = tk.Label(
            root, text="Aadhaar Validator", font=("Arial", 18, "bold"),
            bg=self.current_theme["bg"], fg=self.current_theme["fg"]
        )
        self.title_label.pack(pady=10)

        # Instructions
        self.instructions = tk.Label(
            root, text="Enter your 12-digit Aadhaar number.\nOnly numeric input is allowed.",
            font=("Arial", 10), bg=self.current_theme["bg"], fg="gray"
        )
        self.instructions.pack()

        # Entry
        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(root, font=("Arial", 14), justify="center",
                              textvariable=self.entry_var,
                              bg=self.current_theme["entry"], fg=self.current_theme["fg"])
        self.entry.pack(pady=10, ipadx=10, ipady=5)
        self.entry.bind("<KeyRelease>", self.format_input)
        self.entry.bind("<Return>", lambda e: self.validate_aadhaar())

        # Buttons
        btn_frame = tk.Frame(root, bg=self.current_theme["bg"])
        btn_frame.pack(pady=10)

        self.validate_btn = tk.Button(btn_frame, text="Validate ✅", font=("Arial", 12, "bold"),
                                      bg="#0091ff", fg="white", width=12,
                                      command=self.validate_aadhaar, relief="flat", cursor="hand2")
        self.validate_btn.grid(row=0, column=0, padx=5)

        self.clear_btn = tk.Button(btn_frame, text="Clear ✖", font=("Arial", 12, "bold"),
                                   bg="#dc3545", fg="white", width=12,
                                   command=self.clear_input, relief="flat", cursor="hand2")
        self.clear_btn.grid(row=0, column=1, padx=5)

        self.theme_btn = tk.Button(root, text="🌙 Toggle Theme", font=("Arial", 10),
                                   bg="#6c757d", fg="white", command=self.toggle_theme, relief="flat")
        self.theme_btn.pack(pady=5)

        # Result label
        self.result_label = tk.Label(root, text="", font=("Arial", 14, "bold"),
                                     bg=self.current_theme["bg"])
        self.result_label.pack(pady=5)

        # Aadhaar Card Preview
        self.card_frame = tk.Frame(root, bd=2, relief="ridge", bg="white")
        self.card_frame.pack(pady=15, ipadx=10, ipady=10)

        tk.Label(self.card_frame, text="Government of India", font=("Arial", 12, "bold"),
                 fg="black", bg="white").pack(pady=(5,0))
        self.card_name = tk.Label(self.card_frame, text="Name: Demo User", font=("Arial", 11),
                                  fg="black", bg="white")
        self.card_name.pack()
        self.card_number = tk.Label(self.card_frame, text="XXXX XXXX XXXX", font=("Arial", 16, "bold"),
                                    fg="black", bg="white")
        self.card_number.pack(pady=5)

        # History
        self.history_label = tk.Label(root, text="Recent Validations:", font=("Arial", 10, "bold"),
                                      bg=self.current_theme["bg"], fg=self.current_theme["fg"])
        self.history_label.pack()
        self.history_box = tk.Listbox(root, height=4, width=40, font=("Arial", 10),
                                      bg=self.current_theme["entry"], fg=self.current_theme["fg"])
        self.history_box.pack(pady=5)

        # Status bar
        self.status = tk.Label(root, text="Ready", bd=1, relief="sunken", anchor="w",
                               bg=self.current_theme["bg"], fg=self.current_theme["fg"])
        self.status.pack(side="bottom", fill="x")

    def format_input(self, event=None):
        text = self.entry_var.get().replace(" ", "")
        if not text.isdigit() and text != "":
            self.entry_var.set("".join([c for c in text if c.isdigit()]))
            return

        self.entry_var.set(text[:12]) 

    def validate_aadhaar(self):
        aadhaar = self.entry_var.get().replace(" ", "")
        self.status.config(text="Validating...")

        if not aadhaar.isdigit():
            self.show_result("❌ Aadhaar must contain only digits.", "red", aadhaar, valid=False)
        elif len(aadhaar) != 12:
            self.show_result("❌ Aadhaar must be 12 digits long.", "red", aadhaar, valid=False)
        elif validate_verhoeff(aadhaar):
            self.show_result(f"✅ Aadhaar {aadhaar} is VALID", "green", aadhaar, valid=True)
        else:
            self.show_result(f"❌ Aadhaar {aadhaar} is INVALID", "red", aadhaar, valid=False)

        self.status.config(text="Ready")

    def show_result(self, text, color, aadhaar, valid):
        self.result_label.config(text=text, fg=color)
        masked = aadhaar if valid else aadhaar[:4] + " XXXX XXXX"
        self.card_number.config(text=self.format_card(masked), fg=color)
        self.card_frame.config(highlightthickness=2, highlightbackground=color)
        self.history_box.insert(0, text)
        if self.history_box.size() > 4:
            self.history_box.delete(tk.END)

    def clear_input(self):
        self.entry_var.set("")
        self.result_label.config(text="")
        self.card_number.config(text="XXXX XXXX XXXX", fg="black")
        self.card_frame.config(highlightthickness=0)

    def toggle_theme(self):
        self.current_theme = self.dark_theme if self.current_theme == self.light_theme else self.light_theme
        self.root.configure(bg=self.current_theme["bg"])
        self.title_label.config(bg=self.current_theme["bg"], fg=self.current_theme["fg"])
        self.instructions.config(bg=self.current_theme["bg"])
        self.entry.config(bg=self.current_theme["entry"], fg=self.current_theme["fg"])
        self.result_label.config(bg=self.current_theme["bg"])
        self.history_label.config(bg=self.current_theme["bg"], fg=self.current_theme["fg"])
        self.history_box.config(bg=self.current_theme["entry"], fg=self.current_theme["fg"])
        self.status.config(bg=self.current_theme["bg"], fg=self.current_theme["fg"])

    def format_card(self, aadhaar):
        """Format Aadhaar for card display: #### #### ####"""
        return " ".join([aadhaar[i:i+4] for i in range(0, len(aadhaar), 4)])


# Run app
if __name__ == "__main__":
    root = tk.Tk()
    app = AadhaarApp(root)
    root.mainloop()
