
import customtkinter

"""
def button_action():
    print("Button pressed")
# probar si esta funcionando la app # 
app = customtkinter.CTk() # iniciador
app.title ('Ventana Ejemplo') # titulo de la ventana 
app.geometry('340x500') # tamaño de la ventana 

button = customtkinter.CTkButton(app,text='Click here!', command= button_action) # asignacion de un botton y su funcion 
button.grid(row = 0 , column = 0, padx = 20, pady = 20, sticky="ew", columnspan = 2) # posicion y modificacion del boton en el grid, You can also configure the button to expand with it's grid cell if you add a sticky argument

app.grid_columnconfigure(0,weight=1)
### Adicionando check boxes
checkbox_1 = customtkinter.CTkCheckBox(app, text="checkbox 1") # cargar la too con funcion.ctkcheckbox()
checkbox_1.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w") # posicionamiento de la checkboc
checkbox_2 = customtkinter.CTkCheckBox(app, text="checkbox 2")
checkbox_2.grid(row=1, column=1, padx=20, pady=(0, 20), sticky="w")

app.mainloop() # keep the window open // Siempre al ultimo */ # """


"""To complete this introduction, we want to structure this program into a class.
   It is highly recommended to use classes which inherit from CTk for the main window or CTkFrame for a frame,
   because it highly increases the readability of the code and the code becomes easily extendable, because classes 
   can be easily distributed to multiple files."""
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("my app")
        self.geometry("340x500")
        self.grid_columnconfigure((0, 1), weight=1)

        self.checkbox_frame = customtkinter.CTkFrame(self)
        self.checkbox_frame.grid(row=0, column=0, padx=50, pady=(30, 0), sticky="nsw")
        self.checkbox_1 = customtkinter.CTkCheckBox(self.checkbox_frame, text="checkbox 1")
        self.checkbox_1.grid(row=0, column=0, padx=50, pady=(20, 0), sticky="w")
        self.checkbox_2 = customtkinter.CTkCheckBox(self.checkbox_frame, text="checkbox 2")
        self.checkbox_2.grid(row=1, column=0, padx=50, pady=(20, 0), sticky="w")
        self.checkbox_3 = customtkinter.CTkCheckBox(self.checkbox_frame, text="checkbox 3")
        self.checkbox_3.grid(row=2, column=0, padx=50, pady=(20, 0), sticky="w" )

        def hello():
            my_label.configure(text=self.button.cget('hell yeah!'))

        self.button = customtkinter.CTkButton(self, text='Hell yeah+', command=self.button_callback)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")
        
    def button_callback(self):
        print("Hell yeah!")

app = App()
app.mainloop()