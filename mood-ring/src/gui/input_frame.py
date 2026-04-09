import customtkinter as ctk

class InputFrame(ctk.CTkFrame):
  def __init__(self,master):
    super().__init__(
      master,
      fg_color='transparent'
    )

    self.grid_columnconfigure(0,weight=1)
    self.grid_rowconfigure(0,weight=1)

    self.textbox=ctk.CTkTextbox(
      self,
      border_spacing=15
    )

    self.textbox.grid(
      row=0,
      column=0,
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
      pady=(10,0),
      sticky='ew'
    )
