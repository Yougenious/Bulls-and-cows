import tkinter as tk
import tkinter.messagebox as mb

class FontColour(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Select Font Colour')
        self.geometry('500x300')
        infobtn=tk.Button(self, text='Set Font Colour', command=self.setfontcolour)
        infobtn.grid(row=1, column=1)

        self.colour=tk.StringVar()

        with open("fontcolour.txt", 'r') as file:
            self.color = file.readline()

        radiobutton = tk.Radiobutton(self, text="Current", value='#000000', variable=self.colour,padx=15, pady=10)
        radiobutton.grid(row=3, columnspan=0)

        radiobutton2 = tk.Radiobutton(self, text="Red", value='#FD0101', variable=self.colour,padx=15, pady=10)
        radiobutton2.grid(row=0, column=0, pady=2)

        radiobutton3 = tk.Radiobutton(self, text="Blue", value='#01BCFD', variable=self.colour, padx=15, pady=10)
        radiobutton3.grid(row=1, column=0, pady=2)

        radiobutton4 = tk.Radiobutton(self, text="Orange", value='#F97500', variable=self.colour, padx=15, pady=10)
        radiobutton4.grid(row=2, column=0, pady=2)


    def setfontcolour(self):
        self.color = self.colour.get()
        with open ('fontcolour.txt', 'w') as file:
            file.writelines([self.color])


if __name__ == "__main__":
    wnd = FontColour()
    wnd.mainloop()