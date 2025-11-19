import tkinter as tk

from urllib.request import urlopen

from email_extractor import HTMLEmailParser

class App(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        self.parser = HTMLEmailParser()

        self.url_var = tk.StringVar(
            self,
            'https://maildiver.com/blog/mailto-links-complete-guide/')
        self.email_text = tk.Text(self)
        self.email_text.pack()

        go_button = tk.Button(self, text="Go!", command=lambda: go_click(self))
        go_button.pack()

        quit_button = tk.Button(self, text="Close", command=lambda: exit(self))
        quit_button.pack()

def exit(app):
    app.quit()
    app.destroy()
        
def go_click(app):
    app.email_text.config(state="normal")
    app.email_text.delete("1.0", tk.END)
    url = app.url_var.get()
    resp = urlopen(url)
    html = resp.read().decode().lower()
    app.parser.feed(html)
    for email in app.parser.emails:
        app.email_text.insert(tk.INSERT, email)
    app.email_text.pack()

    