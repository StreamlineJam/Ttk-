import ttkbootstrap as tb
from ttkbootstrap.constants import *


class App(tb.Window):

    def __init__(self):
        super().__init__()

        self.title("Makeup QUIZ")
        self.geometry("300x250")

        self.label_Username = tb.Label(
            self,
            text="Username",
            bootstyle=(PRIMARY),
        )
        self.entry = tb.Entry(
            self,
            bootstyle=(PRIMARY)
        )
        self.Password = tb.Label(
            self,
            text="Password",
            bootstyle=(PRIMARY),
        )
        self.entry_2 = tb.Entry(
            self,
        )
        self.Submit = tb.Button(
            self,
            text="Enter",
            bootstyle=(PRIMARY)
        )

        self.label_Username.pack(anchor=W, padx=15, pady=15)
        self.entry.pack(anchor=W, padx=15, fill=X)
        self.Password.pack(anchor=W, padx=15, pady=15)
        self.entry_2.pack(anchor=W, padx=15, fill=X)
        self.Submit.pack(anchor=NE, padx=15, pady=20)


if __name__ == '__main__':
    app = App()
    app.place_window_center()
    app.mainloop()
