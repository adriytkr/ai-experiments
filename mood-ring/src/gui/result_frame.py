import customtkinter as ctk

from gui.status_frame import StatusFrame

from lib.utils import polarity_to_alpha

class ResultFrame(ctk.CTkFrame):
  def __init__(self,master):
    super().__init__(
      master,
      fg_color='transparent'
    )

    self.grid_columnconfigure(0,weight=1)
    self.grid_rowconfigure(0,weight=1,uniform='group2')
    self.grid_rowconfigure(1,weight=1,uniform='group2')

    # Mood Frame
    self.mood_frame=StatusFrame(
      self,
      title='Mood'
    )
    self.mood_frame.grid(
      row=0,
      column=0,
      pady=(0,10),
      sticky='nsew'
    )

    # Subjectivity Frame
    self.subjectivity_frame=StatusFrame(
      self,
      title='Subjectivity'
    )
    self.subjectivity_frame.grid(
      row=1,
      column=0,
      sticky='nsew'
    )

  def update(
    self,
    mood:float,
    mood_text:str,
    mood_color:str,
    subjectivity:float,
    subjectivity_text:str,
    subjectivity_color:str
  ):
    print(polarity_to_alpha(mood))
    self.mood_frame.update(
      description=mood_text,
      color=mood_color,
      gauge=mood,
      alpha=polarity_to_alpha(mood)
    )

    self.subjectivity_frame.update(
      description=subjectivity_text,
      color=subjectivity_color,
      gauge=subjectivity,
      alpha=subjectivity
    )
