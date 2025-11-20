import tkinter as tk

from collections import Counter

class Frame(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)

        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure((0, 1, 2), weight=1)

        self.url_widget = tk.Entry(self.master, textvariable=master.url_var)
        self.url_widget.grid(row=0, column=0, sticky='ew')

        go_button = tk.Button(
            self.master,
            text="Go!",
            command=lambda: go_button_submit(self)
            )
        go_button.grid(row=0, column=1)

        quit_button = tk.Button(self.master, text="Close", command=lambda: exit(self.master))
        quit_button.grid(row=0, column=2)

        self.email_widget = tk.Text(self.master, wrap=tk.WORD)
        self.email_widget.grid(row=1, column=0)
        self.email_counter_widget = tk.Text(self.master, wrap=tk.WORD)
        self.email_counter_widget.grid(row=1, column=1)
        self.response_header_widget = tk.Text(self.master, wrap=tk.WORD)
        self.response_header_widget.grid(row=1, column=2)

def exit(app):
    app.quit()
    app.destroy()

def go_button_submit(self):
    widget_reset(self.response_header_widget, self.email_widget, self.email_counter_widget)

    emails, headers = self.master.parser_submit()
    response_header_widget_change(self.response_header_widget, headers)
    email_widget_change(self.email_widget, emails)
    email_counter_widget_change(self.email_counter_widget, emails)

def widget_reset(response_header_widget, email_widget, email_counter_widget):
    response_header_widget.config(state="normal")
    response_header_widget.delete("1.0", tk.END)
    email_widget.config(state="normal")
    email_widget.delete("1.0", tk.END)
    email_counter_widget.config(state="normal")
    email_counter_widget.delete("1.0", tk.END)

    response_header_widget.insert(tk.INSERT, "Headers\n\n", "bold_tag")
    response_header_widget.tag_config("bold_tag", font=("Arial", 12, "bold"))
    email_widget.insert(tk.INSERT, "Emails\n\n", "bold_tag")
    email_widget.tag_config("bold_tag", font=("Arial", 12, "bold"))
    email_counter_widget.insert(tk.INSERT, "Email Frequencies\n\n", "bold_tag")
    email_counter_widget.tag_config("bold_tag", font=("Arial", 12, "bold"))

    response_header_widget.grid(row=1, column=0)
    email_widget.grid(row=1, column=1)
    email_counter_widget.grid(row=1, column=2)


def response_header_widget_change(response_header_widget, headers):
    for name, value in headers[:-1]:
        response_header_widget.insert(tk.INSERT, f"{name}:\n\t{value}\n")
    last_name, last_value = headers[-1]
    response_header_widget.insert(tk.INSERT, f"{last_name}:\n\t{last_value}")
    response_header_widget.grid(row=1, column=0)

def email_widget_change(email_widget, emails):
    for email in emails[:-1]:
        email_widget.insert(tk.INSERT, f"{email}\n")
    email_widget.insert(tk.INSERT, f"{emails[-1]}")
    email_widget.grid(row=1, column=1)

def email_counter_widget_change(email_counter_widget, emails):

    email_keys = sorted(set(emails))
    email_counter = Counter(emails)
    for email in email_keys[:-1]:
        count = email_counter.get(email)
        email_counter_widget.insert(tk.INSERT, f"{email}:\n\t\t{count}\n")
    last_email = email_keys[-1]
    last_count = email_counter[last_email]
    email_counter_widget.insert(tk.INSERT, f"{last_email}:\n\t\t{last_count}")
    email_counter_widget.grid(row=1, column=2)
