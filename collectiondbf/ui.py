from tkinter import *


class DetailsInput():
    def __init__(self):
        self.top = Tk()
        self._api_token = StringVar()
        self._api_secret = StringVar()
        self._collection = StringVar()
        L1 = Label(self.top, text="API Token", textvariable=self._api_token)
        L1.pack()
        E1 = Entry(self.top, bd =5)
        E1.pack()
        L2 = Label(self.top, text="API Secret", textvariable=self._api_secret)
        L2.pack()
        E2 = Entry(self.top, bd =5)
        E2.pack()
        L3 = Label(self.top, text="Collection ID", textvariable=self._collection)
        L3.pack()
        E3 = Entry(self.top, bd =5)
        E3.insert(END, 'N:collection:0eed07e7-d147-4a2c-9411-1ea8f9ceffa5')
        E3.pack()
        B = Button(self.top, text='Retrieve all files', command=self.finish)
        B.pack()       
        self.top.mainloop()

    def finish(self):
        self.api_token   = self._api_token.get()
        self.api_secret  = self._api_secret.get()
        self.collection  = self._collection.get()
        self.top.destroy()

    def values(self):
        return self.api_token, self.api_secret, self.collection

