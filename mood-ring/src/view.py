import customtkinter as ctk
import webbrowser
from PIL import Image

class HeaderFrame(ctk.CTkFrame):
  def __init__(self,master):
    super().__init__(
      master,
      fg_color='transparent'
    )

    self.title=ctk.CTkLabel(
      self,
      text='Mood Ring'.upper(),
      font=('Arial',32,'bold')
    )
    self.title.pack(pady=(0,0))

    self.description=ctk.CTkLabel(
      self,
      text='Give any text and check its mood. It can detect sarcams, Internet slangs, emojis, and much  more.'
    )
    self.description.pack()

    self.actions=ctk.CTkFrame(self)
    self.actions.pack()

    github_icon=ctk.CTkImage(
      light_image=Image.open('./icons/github-logo.png'),
      dark_image=Image.open('./icons/github-logo-white.png'),
      size=(25,25)
    )

    self.github_link=ctk.CTkButton(
      self.actions,
      image=github_icon,
      text='Documentation',
      fg_color='transparent',
      cursor='hand2',
      command=self.open_repository
    )
    self.github_link.pack(
      side='left'
    )

  def open_repository(self):
    webbrowser.open('https://youtube.com')

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

    self.subjectivity=ctk.CTkLabel(
      self,
      text='It feels like very subjective'
    )
    self.subjectivity.pack()

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

class App(ctk.CTk):
  def __init__(self):
    super().__init__()

    self.title('Mood Ring')
    self.geometry('800x400')

    self.grid_rowconfigure(0,weight=1)
    self.grid_columnconfigure(0,weight=1)
    self.centeredFrame=ctk.CTkFrame(self,fg_color='transparent')
    self.centeredFrame.grid(
      row=0,
      column=0,
    )

    self.headerFrame=HeaderFrame(self.centeredFrame)
    self.headerFrame.grid(
      row=0,
      column=0,
      sticky='ew'
    )

    self.mainFrame=MainFrame(self.centeredFrame)
    self.mainFrame.grid(
      row=1,
      column=0,
      sticky='ew'
    )

app=App()

app.mainloop()
