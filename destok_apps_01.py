# se importa la libreria tkinter con todsas sus funciones
from tkinter import *

# --------------------------------------------------------
# funciones de la app
#---------------------------------------------------------

#---------------------------------------------------------
# ventana principal
#---------------------------------------------------------

# se declara una variable llamada ventana_principal,
#  que adquiere las carateristicas de un objeto Tk ()
ventana_principal = Tk()

# Titulo de la ventana

ventana_principal.title("sistemas UIS socorro")

# tamaño de la venta
ventana_principal.geometry("500x500")

#desabilitar boton de maximizar
ventana_principal.resizable(0,0)

#color de fondo de la ventana
ventana_principal.config(bg= "white")
#run
# se ejecuta la funcion(metodo) mainloop() de la clase Tk()
#atraves de la instancia ventana principal. Este metodo despliega una ventana simple en la pantalla,
#  y queda a la espera de lo que el usuario haga. Cada accion del usuario se conoce como evento.
# El metodo mainloop() es una bucle infinito.
ventana_principal.mainloop()

