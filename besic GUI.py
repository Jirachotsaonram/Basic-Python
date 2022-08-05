import tkinter as tk
window = tk.Tk()
window.title('Pegasus')
window.minsize(width = 500,height = 500)

def set_message():
    text = text_input.get()
    title_label.configure(text=text)
    
title_label = tk.Label(master = window, text='pass code')
title_label.pack() #แสดงข้อความ

text_input = tk.Entry(master = window)
text_input.pack()

ok_button = tk.Button(master = window,text ='Okau',command=set_message)
ok_button.pack()

window.mainloop()
