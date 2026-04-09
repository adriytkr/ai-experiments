from gui.app import App

app=App()

app.input('Hi, I am very happy to see you!')
app.wm_iconbitmap('./mood-ring.ico')

app.mainloop()
