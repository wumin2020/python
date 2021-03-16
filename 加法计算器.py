from tkinter import *

master = Tk()

frame = Frame(master)
frame.pack(padx=10, pady=10)


def test(
        content):  # 有些人可能会用输入框的get方法来获取内容，再通过将validate设置为key来判断输入参数合不合法。但是validate参数设置为key后，就不再能用输入框的get方法和textvariable.get方法获取输入内容。因为validate被指定为key时，有任何输入操作都会被拦截，然后调用验证函数，验证完后只有返回True才会将内容放到textvariable关联的变量中。
    return content.isdigit()  # 字符串的内置方法，是数字返回True；不是返回False


v1 = StringVar()
v2 = StringVar()
v3 = StringVar()

testCMD = master.register(test)
e1 = Entry(frame, width=10, textvariable=v1, validate='key', \
           validatecommand=(testCMD, '%P')).grid(row=0,
                                                 column=0)  # validate的值是key，那么输入框输入的内容如果是True会保留；是False会清除。设置输入框的宽度是10个字符

Label(frame, text='+').grid(row=0, column=1)

e2 = Entry(frame, width=10, textvariable=v2, validate='key', \
           validatecommand=(testCMD, '%P')).grid(row=0, column=2)

Label(frame, text='=').grid(row=0, column=3)

e3 = Entry(frame, width=10, textvariable=v3, state='readonly').grid(row=0, column=4)


def calc():
    result = int(v1.get()) + int(v2.get())
    v3.set(str(result))


Button(frame, text='计算结果', command=calc).grid(row=1, column=2, pady=5)

mainloop()