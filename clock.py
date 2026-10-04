import time
from datetime import datetime
import tkinter as tk
recive = datetime.now()
h, m, s = recive.hour, recive.minute, recive.second
log = []
wid = tk.Tk()
wid.title("clock")
wid.geometry("600x600")
wid.configure(bg="black")
clock = tk.Label(wid, text="00:00:00", bg="black", fg="white", font=("Arial", 50, "bold"))
clock.pack(expand=True)
marcador = tk.Label(wid, text=log, bg="black", fg="grey", font=("Arial", 20, "bold"))
marcador.pack(expand="True")
def click(h, m, s):
    global log
    log.append(f"{h:02}:{m:02}:{s:02}")
    if len(log) > 5:
        log.pop(0)
    print(log)
    marcador.config(text="\n".join(log))
bot = tk.Button(wid, text="MARCAR", bg="white", fg="black", font=("Segoe UI", 10, "bold"), command=lambda: click(h, m, s))
bot.pack(expand=True)
def clockstart():
    global s, m, h
    s = s + 1
    if s >= 60:
        m =+ 1
        s = 0
        if m >= 60:
            h =+ 1
            m = 0
        if h >= 24:
            h = 0    
    clock.config(text=f"{h:02}:{m:02}:{s:02}")
    wid.after(1000, clockstart)
clockstart()
wid.mainloop()