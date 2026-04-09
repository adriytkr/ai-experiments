import customtkinter as ctk
import webbrowser
from PIL import Image

class HeaderFrame(ctk.CTkFrame):
  def __init__(self,master):
    super().__init__(master,fg_color='transparent')

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

    github_icon=ctk.CTkImage(
      light_image=Image.open('./icons/github-logo.png'),
      dark_image=Image.open('./icons/github-logo-white.png'),
      size=(25,25)
    )

    self.github_link=ctk.CTkButton(
      self,
      image=github_icon,
      text='Source',
      fg_color='transparent',
      cursor='hand2',
      command=self.open_repository
    )
    self.github_link.pack()

  def open_repository(self):
    webbrowser.open('https://youtube.com')

class MainFrame(ctk.CTkFrame):
  def __init__(self,master):
    super().__init__(master,fg_color='transparent')

class InputFrame(ctk.CTkFrame):
  def __init__(self,master):
    super().__init__(master)

    self.grid_columnconfigure(0,weight=1)
    self.grid_rowconfigure(0,weight=1)

    self.textbox=ctk.CTkTextbox(
      self,
      border_spacing=15
    )

    self.textbox.grid(
      row=0,
      column=0,
      padx=10,
      pady=10,
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
      padx=10,
      pady=(0,10),
      sticky='ew'
    )

class MoodFrame(ctk.CTkFrame):
  def __init__(self,master):
    pass

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
      column=0
    )

    self.centeredFrame.grid_columnconfigure(0,weight=1)
    self.headerFrame=HeaderFrame(self.centeredFrame)
    self.headerFrame.grid(
      row=0,
      column=0,
      padx=10,
      pady=10,
    )

    self.mainFrame=MainFrame(self.centeredFrame)
    self.mainFrame.grid(
      row=1,
      column=0
    )

app=App()

app.mainloop()
