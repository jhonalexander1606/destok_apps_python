from tkinter import *

ventana_principal = Tk()

ventana_principal.title("sistemas UIS socorro")

ventana_principal.geometry("580x400")

ventana_principal.resizable(0,0)

ventana_principal.config(bg= "midnight blue")

frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg = "white", width = 220, height=175)
frame_entrada.place(x= 0, y = 0)

frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg = "white", width = 220, height=175)
frame_entrada.place(x= 0, y = 225)

frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg = "white", width = 310, height=175)
frame_entrada.place(x= 270, y = 225)

frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg = "white", width = 310, height=175)
frame_entrada.place(x= 270, y = 0)

frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg = "red", width = 195, height=150)
frame_entrada.place(x= 0, y = 0)

frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg = "red", width = 195, height=150)
frame_entrada.place(x= 0, y = 250)

frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg = "red", width = 280, height=150)
frame_entrada.place(x= 300, y = 250)

frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg = "red", width = 280, height=150)
frame_entrada.place(x= 300, y = 0)


ventana_principal.mainloop()