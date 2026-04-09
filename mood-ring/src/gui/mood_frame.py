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
    self.mood.pack()

    self.moodGauge=ctk.CTkProgressBar(
      self,
      width=30
    )
    self.moodGauge.pack()

    self.subjectivity=ctk.CTkLabel(
      self,
      text='It feels like very subjective'
    )
    self.subjectivity.pack()
    self.subjectivityGauge=ctk.CTkProgressBar(
      self,
      width=30
    )
    self.subjectivityGauge.pack()
