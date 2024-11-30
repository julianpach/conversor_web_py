"""calculator interface with customtkinter"""

import customtkinter as ctk

class calc(ctk.CTk):  
    def __init__(self):
        super()._init_()

        self.title('Calculator')
        self.geometry('340x500')
        self.set_appearance_mode('system')
        self.grid_columnconfigure((0, 1), weight=1)


calc = calc()
calc.mainloop()