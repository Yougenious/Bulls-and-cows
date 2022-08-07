import tkinter as tk
import tkinter.messagebox as mb

class FontSize(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Select Font Size')
        self.geometry('500x300')
        infobtn=tk.Button(self, text='Set Font Size', command=self.setfontsize)
        infobtn.grid(row=1, column=1)

        self.size=tk.IntVar()

        radiobutton2 = tk.Radiobutton(self, text="Small", value=16, variable=self.size,padx=15, pady=10)
        radiobutton2.grid(row=0, column=0, pady=2)

        radiobutton3 = tk.Radiobutton(self, text="Medium", value=24, variable=self.size, padx=15, pady=10)
        radiobutton3.grid(row=1, column=0, pady=2)

        radiobutton4 = tk.Radiobutton(self, text="Large", value=40, variable=self.size, padx=15, pady=10)
        radiobutton4.grid(row=2, column=0, pady=2)


    def setfontsize(self):
        with open ('fontsize.txt', 'w') as file:
            file.writelines([str(self.size.get())])


if __name__ == "__main__":
    wnd = FontSize()
    print(dir(wnd))
    wnd.mainloop()