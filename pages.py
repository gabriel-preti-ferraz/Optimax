from customtkinter import *

def general_configs(container):
    frame = CTkFrame(master=container)
    label = CTkLabel(master=frame, text="Configurações Gerais")
    label.pack(pady=10, padx=10)
    return frame

def advanced_configs(container):
    frame = CTkFrame(master=container)
    label = CTkLabel(master=frame, text="Configurações Avançadas")
    label.pack(pady=10, padx=10)
    return frame

def clean_configs(container):
    frame = CTkFrame(master=container)
    label = CTkLabel(master=frame, text="Configurações de Limpeza")
    label.pack(pady=10, padx=10)
    return frame