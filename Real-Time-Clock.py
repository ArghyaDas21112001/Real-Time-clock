from time import strftime
from tkinter import Label,Tk

window=Tk()
window.title("Real Time Clock")
window.geometry("200x80")
window.configure(bg="red")
window.resizable(True,False)

clock_label = Label(window,bg="red",fg="white",font=("Times",30,'bold'),relief='flat')
clock_label.place(x=20,y=30)

def updating_label():
    current_time=strftime('%H: %M: %S')
    clock_label.configure(text=current_time)
    clock_label.after(80,updating_label)

updating_label()
window.mainloop()
