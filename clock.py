
import tkinter as tk
from time import strftime

class DigitalClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Digital Clock")
        self.root.geometry("450x220")
        self.root.configure(bg="#101820")
        self.root.resizable(False, False)

        self.time_label = tk.Label(
            root,
            font=("Consolas", 42, "bold"),
            background="#101820",
            foreground="#00E5FF"
        )
        self.time_label.pack(pady=(35, 10))

        self.date_label = tk.Label(
            root,
            font=("Arial", 14),
            background="#101820",
            foreground="#FFFFFF"
        )
        self.date_label.pack()

        self.update_clock()

    def update_clock(self):
        current_time = strftime("%I:%M:%S %p")
        current_date = strftime("%A, %d %B %Y")

        self.time_label.config(text=current_time)
        self.date_label.config(text=current_date)

        self.root.after(1000, self.update_clock)


if __name__ == "__main__":
    root = tk.Tk()
    clock = DigitalClock(root)
    root.mainloop()
