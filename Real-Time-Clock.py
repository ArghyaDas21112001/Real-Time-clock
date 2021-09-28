from time import strftime
from tkinter import Label,Tk
import datetime as date

window=Tk()
window.title("Real Time Clock")
window.geometry("500x150")
window.configure(bg="red")
window.resizable(True,True)

clock_label = Label(window,bg="red",fg="white",font=("Times",30,'bold'),relief='flat')
clock_label.place(x=20,y=50)
date=date.datetime.now()

format_date=f"{date:%a, %b %d %Y}"

label=Label(window, text=format_date, font=("Times",30,'bold'))
label.grid(padx=(0, 0), pady=(200, 0))
label.pack()

def updating_label():
    current_time=strftime('%H: %M: %S')
    clock_label.configure(text=current_time)
    clock_label.after(80,updating_label)
    

updating_label()
window.mainloop()
