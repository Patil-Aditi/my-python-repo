
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import time
import threading
import winsound  # Windows only


class AlarmClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Alarm Clock")
        self.root.geometry("400x300")
        self.root.configure(bg="#101820")
        self.alarm_running = False

        tk.Label(
            root, text="ALARM CLOCK",
            font=("Arial", 22, "bold"),
            fg="#00E5FF", bg="#101820"
        ).pack(pady=20)

        tk.Label(
            root, text="Enter alarm time (HH:MM, 24-hour format)",
            fg="white", bg="#101820"
        ).pack()

        self.time_entry = tk.Entry(
            root, font=("Arial", 18), justify="center"
        )
        self.time_entry.pack(pady=10)
        self.time_entry.insert(0, "07:00")

        tk.Button(
            root, text="Set Alarm",
            command=self.set_alarm,
            font=("Arial", 12, "bold"),
            bg="#00E5FF", fg="#101820"
        ).pack(pady=10)

        self.status = tk.Label(
            root, text="No alarm set",
            fg="white", bg="#101820"
        )
        self.status.pack(pady=10)

    def set_alarm(self):
        alarm_time = self.time_entry.get().strip()

        try:
            datetime.strptime(alarm_time, "%H:%M")
        except ValueError:
            messagebox.showerror(
                "Invalid Time",
                "Enter a valid time, such as 07:30 or 18:45."
            )
            return

        self.alarm_running = True
        self.status.config(text=f"Alarm set for {alarm_time}")
        threading.Thread(
            target=self.check_alarm,
            args=(alarm_time,),
            daemon=True
        ).start()

    def check_alarm(self, alarm_time):
        while self.alarm_running:
            if datetime.now().strftime("%H:%M") == alarm_time:
                self.alarm_running = False
                self.root.after(0, self.ring_alarm)
                return
            time.sleep(1)

    def ring_alarm(self):
        self.status.config(text="⏰ ALARM! Wake up!")
        messagebox.showinfo("Alarm", "⏰ Time to wake up!")

        # Repeat beeps until the user stops them.
        for _ in range(10):
            winsound.Beep(1000, 700)
            if not self.root.winfo_exists():
                break


if __name__ == "__main__":
    root = tk.Tk()
    app = AlarmClock(root)
    root.mainloop()
