import customtkinter as ctk

from gui.input_frame import InputFrame
from gui.result_frame import ResultFrame

from lib.mood_ring import compute_mood_and_subjectivity

from lib.map import process_mood,process_subjectivity

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
    self.result_frame=ResultFrame(self)
    self.result_frame.grid(
      row=0,
      column=1,
      padx=(10,0),
      sticky='nsew'
    )

  def handle_compute(self):
    user_text=self.input_frame.textbox.get('1.0','end-1c')

    mood,subjectivity=compute_mood_and_subjectivity(user_text)
    mood_text,mood_color=process_mood(mood)
    subjectivity_text,subjectivity_color=process_subjectivity(subjectivity)

    self.result_frame.update(
      mood,
      mood_text,
      mood_color,
      subjectivity,
      subjectivity_text,
      subjectivity_color
    )

  def input(self,text:str):
    self.input_frame.textbox.delete('0.0','end') 
    self.input_frame.textbox.insert('0.0',text)
    self.handle_compute()
