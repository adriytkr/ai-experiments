import customtkinter as ctk

class MoodFrame(ctk.CTkFrame):
  def __init__(self,master):
    super().__init__(
      master,
      fg_color='transparent'
    )

    self.mood=ctk.CTkLabel(
      self,
      text='I sense a very good feeling'
    )
    self.mood.grid(
      row=0,
      column=0,
      sticky='ew'
    )

    self.subjectivity=ctk.CTkLabel(
      self,
      text='It feels like very subjective'
    )
    self.subjectivity.grid(
      row=1,
      column=0,
      sticky='ew'
    )

  def update_mood(
    self,
    mood:str,
    subjectivity:str
  ):
    self.mood.configure(text=mood)
    self.subjectivity.configure(text=subjectivity)
