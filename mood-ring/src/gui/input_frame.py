import customtkinter as ctk

class InputFrame(ctk.CTkFrame):
  def __init__(
    self,
    master,
    compute
  ):
    super().__init__(
      master,
      fg_color='transparent'
    )

    self.grid_columnconfigure(0,weight=1)
    self.grid_rowconfigure(0,weight=1)

    # TextBox
    self.textbox=ctk.CTkTextbox(
      self,
      border_spacing=15
    )

    self.textbox.grid(
      row=0,
      column=0,
      sticky='nsew'
    )

    # Compute Button
    self.compute_btn=ctk.CTkButton(
      self,
      text='Compute Mood',
      border_spacing=8,
      font=('Arial',12,'bold'),
      command=compute
    )

    self.compute_btn.grid(
      row=1,
      column=0,
      pady=(10,0),
      sticky='ew'
    )
