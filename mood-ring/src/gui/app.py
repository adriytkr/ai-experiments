import customtkinter as ctk

from gui.header_frame import HeaderFrame
from gui.main_frame import MainFrame

class App(ctk.CTk):
  def __init__(self):
    super().__init__()

    self.title('Mood Ring')
    self.geometry('800x500')

    self.grid_rowconfigure(0,weight=1)
    self.grid_columnconfigure(0,weight=1)

    self.centeredFrame=ctk.CTkFrame(
      self,
      fg_color='transparent'
    )
    self.centeredFrame.grid(
      row=0,
      column=0,
      padx=40,
      pady=40,
      sticky='nsew'
    )

    self.centeredFrame.grid_columnconfigure(0,weight=1)
    self.centeredFrame.grid_rowconfigure(1,weight=1)

    self.headerFrame=HeaderFrame(self.centeredFrame)
    self.headerFrame.grid(
      row=0,
      column=0,
      pady=(0, 20),
      sticky='n'
    )

    self.mainFrame=MainFrame(self.centeredFrame)
    self.mainFrame.grid(
      row=1,
      column=0,
      sticky='nsew'
    )
