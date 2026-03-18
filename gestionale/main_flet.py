
import flet as ft

from gestionale.view import View
from gestionale.controller import Controller

def main(page:ft.Page):
    v = View(page)
    c = Controller(v)    #per passare al controller view e alla view il controller, così che interagiscano
    v.set_controller(c)
    v.carica_interfaccia()

ft.app(target = main)    #chiamata al metodo app di flet, con argomento la funzione che regola il comportamento