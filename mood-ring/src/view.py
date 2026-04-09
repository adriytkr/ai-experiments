import customtkinter as ctk

class InputFrame(ctk.CTkFrame):
  def __init__(self,master):
    super().__init__(master)

    self.grid_columnconfigure(0,weight=1)
    self.grid_rowconfigure(0,weight=1)

    self.textbox=ctk.CTkTextbox(
      self,
      border_spacing=15
    )

    self.textbox.grid(
      row=0,
      column=0,
      padx=10,
      pady=10,
      sticky='nsew'
    )

    self.submitBtn=ctk.CTkButton(
      self,
      text='Compute Mood',
      border_spacing=8,
      font=('Arial',12,'bold')
    )

    self.submitBtn.grid(
      row=1,
      column=0,
      padx=10,
      pady=(0,10),
      sticky='ew'
    )

class App(ctk.CTk):
  def __init__(self):
    super().__init__()

    self.title('Mood Ring')
    self.geometry('800x400')

    self.grid_columnconfigure(0,weight=1)
    self.grid_columnconfigure(1,weight=1)
    self.grid_rowconfigure(0,weight=1)

    self.inputFrame=InputFrame(self)
    self.inputFrame.grid(
      row=0,
      column=0,
      padx=20,
      pady=20,
      sticky='nsew'
    )

app=App()
app.mainloop()
