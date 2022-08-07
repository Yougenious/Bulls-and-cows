import tkinter as tk
import tkinter.messagebox as mb

class BackgroundColour(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Select Background Colour')
        self.geometry('500x300')
        infobtn=tk.Button(self, text='Set Background colour', command=self.setbackgroundcolour)
        infobtn.grid(row=1, column=1)

        self.colour=tk.StringVar()

        radiobutton2 = tk.Radiobutton(self, text="Yellow", value='#F9F500', variable=self.colour,padx=15, pady=10)
        radiobutton2.grid(row=0, column=0, pady=2)

        radiobutton3 = tk.Radiobutton(self, text="LimeGreen", value='#26F900', variable=self.colour, padx=15, pady=10)
        radiobutton3.grid(row=1, column=0, pady=2)

        radiobutton4 = tk.Radiobutton(self, text="LightPink", value='#FCB5EB', variable=self.colour, padx=15, pady=10)
        radiobutton4.grid(row=2, column=0, pady=2)

    def showinfo(self):
        msg="Settings applied"
        mb.showinfo("Attention!", msg)

    def setbackgroundcolour(self):
        with open ('backgroundcolour.txt', 'w') as file:
            file.writelines([self.colour.get()])


if __name__ == "__main__":
    wnd = BackgroundColour()
    wnd.mainloop()