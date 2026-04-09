import customtkinter as ctk

from gui.input_frame import InputFrame
from gui.mood_frame import MoodFrame

class MainFrame(ctk.CTkFrame):
  def __init__(self,master):
    super().__init__(
      master,
      fg_color='transparent'
    )

    self.grid_columnconfigure(0,weight=1,uniform='group1')
    self.grid_columnconfigure(1,weight=1,uniform='group1')
    self.grid_rowconfigure(0,weight=1)
    
    # Input (Column 1)
    self.input_frame=InputFrame(
      self,
      compute=self.handle_compute
    )

    self.input_frame.grid(
      row=0,
      column=0,
      sticky='nsew'
    )

    # Mood (Column 2)
    self.grid_columnconfigure(1,weight=1)
    self.mood_frame=MoodFrame(self)
    self.mood_frame.grid(
      row=0,
      column=1,
      padx=(10,0),
      sticky='nsew'
    )

  def handle_compute(self):
    user_text=self.input_frame.textbox.get('1.0','end-1c')
    self.mood_frame.update_mood(user_text,'Very Subjective')
