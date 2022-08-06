import tkinter as tk
window=tk.Tk()
window.title('แม่สูตรคูณ')
window.minsize(width=400,height=200)

def output_number():
    number=int(input_number.get())
    output=''
    if number==0:
        text_output.configure(text='ไม่มีค่า')
        return

    for i in range(1,25):
        output += str(number)+ 'X' +str(i)
        output += '=' + str(number*i)+'\n'
    text_output.configure(text=output)


text_label=tk.Label(master=window,text='แม่สูตรคูณ')
text_label.pack(pady=20)

input_number=tk.Entry(master=window,width=20)
input_number.pack()

ok_button=tk.Button(master=window,text='ได้แก่',command=output_number,width=15)
ok_button.pack()

text_output=tk.Label(master=window)
text_output.pack(pady=20)

window.mainloop()
             
