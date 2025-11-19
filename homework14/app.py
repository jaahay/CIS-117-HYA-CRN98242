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
            'https://maildiver.com/blog/mailto-links-complete-guide/'
        )
        self.url_widget = tk.Entry(self, textvariable=self.url_var)
        self.url_widget.pack()
        self.email_widget = tk.Text(self, wrap=tk.WORD)
        self.email_widget.pack()

        go_button = tk.Button(self, text="Go!", command=lambda: go_click(self))
        go_button.pack()

        quit_button = tk.Button(self, text="Close", command=lambda: exit(self))
        quit_button.pack()

def exit(app):
    app.quit()
    app.destroy()
        
def go_click(app):
    app.email_widget.config(state="normal")
    app.email_widget.delete("1.0", tk.END)
    url = app.url_widget.get()
    resp = urlopen(url)
    html = resp.read().decode().lower()
    app.parser.feed(html)

    emails = list(app.parser.emails)
    emails.sort()
    for i in range(len(emails) - 1):
        email = emails[i]
        app.email_widget.insert(tk.INSERT, email)
        app.email_widget.insert(tk.INSERT, '\n')
    app.email_widget.insert(tk.INSERT, emails[-1])
    app.email_widget.pack()

    