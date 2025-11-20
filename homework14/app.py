import tkinter as tk

from urllib.request import urlopen

from frame import Frame
from html_email_parser import HTMLEmailParser

class App(tk.Tk):

    def __init__(self, master=None):
        super().__init__(master)
        self.init_root()
        self.init_vars()
        self.parser = HTMLEmailParser()
        self.frame = Frame(self)

    def init_vars(self):
        self.url_var = tk.StringVar(
            self,
            'https://maildiver.com/blog/mailto-links-complete-guide/'
        )

    def init_root(self):
        self.title = "HTML Email Parser"
        
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure((0, 1, 2), weight=1)

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        window_width = int(screen_width * 0.8)
        window_height = int(screen_height * 0.7)
        self.geometry(f"{window_width}x{window_height}")
    
    def parser_submit(self):
        self.parser.clear()
        url = self.url_var.get()
        resp = urlopen(url)
        html = resp.read().decode().lower()
        self.parser.feed(html)
        return self.parser.emails, resp.getheaders()
   