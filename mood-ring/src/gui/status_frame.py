import customtkinter as ctk

class StatusFrame(ctk.CTkFrame):
  def __init__(
    self,
    master,
    title:str='',
  ):
    super().__init__(master)
    self.grid_columnconfigure(0,weight=1)

    self.grid_rowconfigure(0,weight=1)
    self.grid_rowconfigure(5,weight=1)

    # Gauge Number
    self.status_gauge_number=ctk.CTkLabel(self,text_color='gray')
    self.status_gauge_number.grid(
      row=1,
      column=0,
      padx=10,
    )

    # Title
    self.status_title=ctk.CTkLabel(
      self,
      text=title
    )
    self.status_title.grid(
      row=2,
      column=0,
      padx=10,
    )

    # Description
    self.status_description=ctk.CTkLabel(self)
    self.status_description.grid(
      row=3,
      column=0,
      padx=10,
    )

    # Gauge Bar
    self.status_gauge_bar=ctk.CTkProgressBar(self)
    self.status_gauge_bar.grid(
      row=4,
      column=0,
      padx=10,
    )

  def update(
    self,
    description:str,
    color:str,
    gauge:float,
    alpha:float
  ):
    self.status_gauge_number.configure(text=gauge)

    self.status_description.configure(
      text=description,
      text_color=color
    )

    self.status_gauge_bar.set(alpha)
    self.status_gauge_bar.configure(progress_color=color)
