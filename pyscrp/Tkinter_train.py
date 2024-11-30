
"""this is a notebook used specially for anotatios in reference to a different
configurations and practices on python lenguage """
# for libreries like Tkinter or customtkintes (which I use), then we got: #
import customtkinter as ctk # import the libreries
wndw = ctk.CTK() # this command create a new window (this is not incharge to keep it working all the time

wndw._set_appearence_mode("light") # could be light or dark (this is the theme of the window

 #btn = Button(wndw, text = "Hell Yeah!") 
# btn.pack() --- thats the way to create buttons 


""" Modifications and configurations of the window"""
wndw.title("Windows CTK") # provide a name on the top side of the wndwsa
wndw.geometry("340x500") #.geometry define the resolution and aspect ratio of the window 
# even with the resolution setted by .geometry, its still possible change with the mause the aspect of the wndw
# if you wanna control the size of the screem use .maxsize() or . minsize for the counter case 
wndw.maxsize(width = 840, height = 1000)
wndw.minsize(width = 140, height = 300)
wndw.resizable(width = true, height = true) # this line of code allows the modifications of each 
# side in a independant way. The =true provide the habillity of change the length and false blocks the side making
# unable elong or cut distance in one of the selected axis
 # wndw.iconify() / wndw.deiconfy() clos inmediatly and opeen inmediatly thhe window#
 
 """ Config of theme"""
# es lo mismo aplicado en wndw._set_appearence_mode("light"), aqui podriaponerse 'system'

""" creating new windows"""
# top level # 
# with a press of a button we open a new screem
def n_scrm():
    n_wndw = ctk.CTkToplevel(wndw,fg_color='teal') # construct a toplevel widget
    n_wndw.geometry(200x200) # providing the geometry to the new janela

# calling the function to expand a new janela 

a_interf = ctk.CTkButton( master = wndw, text = 'expand concept', command = n_scrm).place(x=240,y=400)

""" creation and management of frames"""
frame_1 = ctk.CTkFrame(master = wndw, width = 200, height = 330, fg_color = 'teal').place(x = 10 , y = 60)
frame_2 = ctk.CTkFrame(wndw, width = 200, height = 250, fg_color = 'teal').place(x = 220,y = 60)

wndw.mainloop()