import tkinter as tk
window = tk.Tk()
window.title("Hello World")

def set_clickme(text):
    print(text)

we = tk.Label(window,text="Wecome to you").pack()
click_bt = tk.Button(window,text="Click me!",command= lambda : set_clickme
                     ('HELLO !')).pack()
window.mainloop()
