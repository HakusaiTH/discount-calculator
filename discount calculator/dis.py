from tkinter import *
root = Tk()
root.title("โปรแกรมคำนวณส่วนลด")

root.option_add("*Font", "consolas 15")

Label(root,text="test_1",background="yellow",fg="red").grid(row=0,columnspan=3,padx=10,pady=10)

x_1 = IntVar()
x_2 = IntVar()
output_console = IntVar

def main() :
    x_1_get = x_1.get()
    x_2_get = x_2.get()

    c = (x_1_get*x_2_get)/100
    d = x_1_get-c

    Label(root, text="ส่วนลดที่คำนวณได้").grid(row=3, column=0, padx=5, pady=5)
    Label(root, text='%.2f' %(c)).grid(row=3, column=1, padx=5, pady=5)
    Label(root, text="บาท").grid(row=3, column=2, padx=5, pady=5)

    Label(root, text="ราคาขายสุทธิ").grid(row=4, column=0, padx=5, pady=5)
    Label(root, text='%.2f' %(d)).grid(row=4, column=1, padx=5, pady=5)
    Label(root, text="บาท").grid(row=4, column=2, padx=5, pady=5)

Label(root,text="ราคาขาย").grid(row=1,column=0,padx=5,pady=5)
Entry(root,textvariable=x_1).grid(row=1,column=1,padx=5,pady=5)
Label(root,text="บาท").grid(row=1,column=2,padx=5,pady=5)

Label(root,text="อัตตราส่วนลด").grid(row=2,column=0,padx=5,pady=5)
Entry(root,textvariable=x_2).grid(row=2,column=1,padx=5,pady=5)
Label(root,text="%").grid(row=2,column=2,padx=5,pady=5)

Button(root,text="คำนวณ",command=main,padx=10,pady=5,font=10).grid(row=5,columnspan=3,padx=10,pady=10)


root.mainloop()