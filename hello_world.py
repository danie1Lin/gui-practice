import tkinter


def resize(env=None):
    label.config(font='Helvetica -%d bold' % scale.get())


top = tkinter.Tk()
label = tkinter.Label(top,
                      text='Hello world!'
                      )
label.pack()
scale = tkinter.Scale(top,
                      from_=10,
                      to=40,
                      orient=tkinter.HORIZONTAL,
                      command=resize
                      )
scale.set(12)
scale.pack(fill=tkinter.X, expand=1)
quit = tkinter.Button(top,
                      text='Hello world!',
                      command=top.quit,
                      bg='red',
                      fg='white'
                      )
quit.pack(fill=tkinter.X, expand=1)

tkinter.mainloop()
