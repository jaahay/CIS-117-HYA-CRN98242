import tkinter as tk

from collections import Counter
from urllib.request import urlopen

from html_email_parser import HTMLEmailParser

class App(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        self.parser = HTMLEmailParser()
        self.init_widgets()

    def init_widgets(self):
        self.url_var = tk.StringVar(
            self,
            'https://maildiver.com/blog/mailto-links-complete-guide/'
        )
        self.url_widget = tk.Entry(self, textvariable=self.url_var)
        self.url_widget.grid(row=0, column=0, sticky='ew')

        go_button = tk.Button(
            self,
            text="Go!",
            command=lambda: go_button_submit(self)
            )
        go_button.grid(row=0, column=1)

        quit_button = tk.Button(self, text="Close", command=lambda: exit(self))
        quit_button.grid(row=0, column=2)

        self.email_widget = tk.Text(self, wrap=tk.WORD)
        self.email_widget.grid(row=1, column=0)
        self.email_counter_widget = tk.Text(self, wrap=tk.WORD)
        self.email_counter_widget.grid(row=1, column=1)
        self.response_header_widget = tk.Text(self, wrap=tk.WORD)
        self.response_header_widget.grid(row=1, column=2)

def exit(app):
    app.quit()
    app.destroy()

def go_button_submit(self):
    self.parser.clear()
    url = self.url_widget.get()
    resp = urlopen(url)
    html = resp.read().decode().lower()
    self.parser.feed(html)
    emails = self.parser.emails

    email_widget_change(self.email_widget, emails)
    email_counter_widget_change(self.email_counter_widget, emails)
    response_header_widget_change(self.response_header_widget, resp.getheaders())

def email_widget_change(email_widget, emails):
    email_widget.config(state="normal")
    email_widget.delete("1.0", tk.END)

    email_widget.insert(tk.INSERT, "Emails\n\n", "bold_tag")
    email_widget.tag_config("bold_tag", font=("Arial", 12, "bold"))
    for email in emails[:-1]:
        email_widget.insert(tk.INSERT, f"{email}\n")
    email_widget.insert(tk.INSERT, f"{emails[-1]}")
    email_widget.grid(row=1, column=0)

def email_counter_widget_change(email_counter_widget, emails):
    email_counter_widget.config(state="normal")
    email_counter_widget.delete("1.0", tk.END)
    email_counter_widget.insert(tk.INSERT, "Email Frequencies\n\n", "bold_tag")
    email_counter_widget.tag_config("bold_tag", font=("Arial", 12, "bold"))

    email_keys = sorted(set(emails))
    email_counter = Counter(emails)
    for email in email_keys[:-1]:
        count = email_counter.get(email)
        email_counter_widget.insert(tk.INSERT, f"{email}:\n\t\t{count}\n")
    last_email = email_keys[-1]
    last_count = email_counter[last_email]
    email_counter_widget.insert(tk.INSERT, f"{last_email}:\n\t\t{last_count}")
    email_counter_widget.grid(row=1, column=1)

def response_header_widget_change(response_header_widget, headers):
    response_header_widget.config(state="normal")
    response_header_widget.delete("1.0", tk.END)

    response_header_widget.insert(tk.INSERT, "Headers\n\n", "bold_tag")
    response_header_widget.tag_config("bold_tag", font=("Arial", 12, "bold"))
    for name, value in headers[:-1]:
        response_header_widget.insert(tk.INSERT, f"{name}:\n\t{value}\n")
    last_name, last_value = headers[-1]
    response_header_widget.insert(tk.INSERT, f"{last_name}:\n\t{last_value}")
