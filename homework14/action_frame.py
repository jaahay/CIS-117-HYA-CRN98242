import tkinter as tk

class ActionFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.url_widget = tk.Entry(master, textvariable=master.url_var)
        self.url_widget.grid(row=0, column=0, sticky='ew')
        go_button = tk.Button(
            master,
            text="Go!",
            command=lambda: master.go_button_submit(self)
            )
        go_button.grid(row=0, column=1)

        # reset_button = tk.Button(
        #     master,
        #     text="Reset",
        #     command=lambda: master.widget_reset(self)
        # )
        # reset_button.grid(row=0, column=1)

        quit_button = tk.Button(self.master, text="Close", command=lambda: exit(self.master))
        quit_button.grid(row=0, column=2)
