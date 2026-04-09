import customtkinter as ctk

from gui.input_frame import InputFrame
from gui.mood_frame import MoodFrame

class MainFrame(ctk.CTkFrame):
  def __init__(self,master):
    super().__init__(
      master,
      fg_color='transparent'
    )

    self.grid_columnconfigure(0,weight=1)
    self.grid_rowconfigure(0,weight=1)
    self.inputFrame=InputFrame(self)
    self.inputFrame.grid(
      row=0,
      column=0,
      sticky='nsew'
    )

    self.grid_columnconfigure(1,weight=1)
    self.moodFrame=MoodFrame(self)
    self.moodFrame.grid(
      row=0,
      column=1,
      sticky='nsew'
    )
