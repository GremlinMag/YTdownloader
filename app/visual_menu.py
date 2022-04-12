from tkinter import *
from tkinter import ttk
from app.check_input import Check_input
check_input = Check_input()

class Visual_menu():
    def get_link(self):
        only_audio = self.audio_only.get()
        url = self.entry.get()
        check_input.check_params(url, only_audio)

    def __init__(self):
        self.window = Tk()
        self.audio_only = IntVar()
        self.window.geometry("650x150")
        self.window.title('YTdownloader')
        self.audio_only = IntVar()
        self.label = ttk.Label(text="Paste link here and press Download", font=('Arial 15 bold'))
        self.entry = ttk.Entry(self.window, font=('Arial 12'), width=40)
        self.checkbox = Checkbutton(self.window, text="Audio Only", variable=self.audio_only)
        self.button = ttk.Button(text="Download", command=self.get_link)
        self.label.pack()
        self.entry.pack(pady=20)
        self.button.pack()
        self.checkbox.pack()
        self.window.mainloop()




