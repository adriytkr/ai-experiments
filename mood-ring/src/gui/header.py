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
