import customtkinter as ctk
import webbrowser

class HeaderFrame(ctk.CTkFrame):
  def __init__(self,master):
    super().__init__(
      master,
      fg_color='transparent'
    )

    # Title
    self.title=ctk.CTkLabel(
      self,
      text='Mood Ring'.upper(),
      font=('Arial',32,'bold')
    )
    self.title.pack(pady=(0,0))

    # Description
    self.description=ctk.CTkLabel(
      self,
      text='Give any text and check its mood. It can detect sarcams, Internet slangs, emojis, and much  more.'
    )
    self.description.pack()

    # Actions
    self.actions=ctk.CTkFrame(
      self,
      fg_color='transparent'
    )
    self.actions.pack(fill='x')
    self.actions.grid_columnconfigure(0,weight=1)

    # Read Docs
    self.github_link=self.build_action_btn('Source',self.open_source)
    self.github_link.grid(
      row=0,
      column=1,
      padx=(0,5)
    )

    # How to Use
    self.help_btn=self.build_action_btn('Help',self.open_help)
    self.help_btn.grid(
      row=0,
      column=2,
    )

  def build_action_btn(
    self,
    text:str,
    callback,
  ):
    return ctk.CTkButton(
      self.actions,
      text=text,
      cursor='hand2',
      font=('Arial',12,'bold'),
      command=callback
    )

  def open_source(self):
    webbrowser.open('https://youtube.com')

  def open_help(self):
    print('opening help modal...')
