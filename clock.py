import time
from datetime import datetime
import customtkinter as ctk
def clear():
    global log
    log = []
    marcador.configure(text="\nCleared",)
def click(h, m, s):
    global log
    log.append(f"{h:02}:{m:02}:{s:02}")
    if len(log) > 5:
        log.pop(0)
    marcador.configure(text="\n".join(log))
def clockstart():
    global s, m, h
    s = s + 1
    if s >= 60:
        m = m + 1
        s = 0
    if m >= 60:
        h = h + 1
        m = 0   
    if h >= 24:
        h = 0
    clock.configure(text=f"{h:02}:{m:02}:{s:02}")
    wid.after(1000, clockstart)
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")
recive = datetime.now()
h, m, s = recive.hour, recive.minute, recive.second
log = []
wid = ctk.CTk()
wid.title("clock-beta-v0.02")
wid.geometry("600x600")
clock = ctk.CTkLabel(wid, text="00:00:00", font=("Arial", 50, "bold"))
clock.pack(pady=20)
area_marcador = ctk.CTkFrame(wid, width=300, height=180)
area_marcador.pack(pady=20)
area_marcador.pack_propagate(False)
marcador = ctk.CTkLabel(area_marcador, text=log, font=("Arial", 20, "bold"))
marcador.pack(pady=20)
bot = ctk.CTkButton(wid, width=150, height=40, text="MARCAR", font=("Arial", 10, "bold"), command=lambda: click(h, m, s))
bot.pack()
cleartask = ctk.CTkButton(wid, width=150, height=40, text="CLEAR", font=("Arial", 10, "bold"), command=clear)
cleartask.pack(pady=20)
clockstart()
wid.mainloop()