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

class MainFrame(ctk.CTkFrame):
  def __init__(self,master):
    super().__init__(
      master,
      fg_color='transparent'
    )

    self.grid_columnconfigure(0,weight=1)
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
