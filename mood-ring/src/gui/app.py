import customtkinter as ctk

from gui.header_frame import HeaderFrame
from gui.main_frame import MainFrame

class App(ctk.CTk):
  def __init__(self):
    super().__init__()

    self.title('Mood Ring')
    self.geometry('960x540')

    self.grid_rowconfigure(0,weight=1)
    self.grid_columnconfigure(0,weight=1)

    self.centered_frame=ctk.CTkFrame(
      self,
      fg_color='transparent'
    )
    self.centered_frame.grid(
      row=0,
      column=0,
      padx=40,
      pady=40,
      sticky='nsew'
    )

    self.centered_frame.grid_columnconfigure(0,weight=1)
    self.centered_frame.grid_rowconfigure(1,weight=1)

    self.header_frame=HeaderFrame(self.centered_frame)
    self.header_frame.grid(
      row=0,
      column=0,
      pady=(0,24),
      sticky='n'
    )

    self.main_frame=MainFrame(self.centered_frame)
    self.main_frame.grid(
      row=1,
      column=0,
      sticky='nsew'
    )
  
  def input(self,text:str):
    self.main_frame.input(text)
