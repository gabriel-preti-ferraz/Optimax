from customtkinter import *
import commands
import images

set_appearance_mode('dark')
set_default_color_theme('dark-blue')

window = CTk()
window.geometry('1200x900')
window.title('Optimax')

class Sidebar():
    sidebar = CTkFrame(master=window, width=140)
    sidebar.pack(fill='y', side='left')

    general_configs = CTkButton(master=sidebar, fg_color='transparent', image=images.general_configs, text='Configurações Gerais', command=commands.Sidebar.general_configs)
    general_configs.pack(pady=30, padx=10)

    advanced_configs = CTkButton(master=sidebar, fg_color='transparent', image=images.advanced_configs, text='Configurações Avançadas', command=commands.Sidebar.advanced_configs)
    advanced_configs.pack(pady=20, padx=10)

    clean_configs = CTkButton(master=sidebar, fg_color='transparent', image=images.clean_configs, text='Configurações de Limpeza', command=commands.Sidebar.clean_configs)
    clean_configs.pack(pady=20, padx=10)

frame = CTkFrame(master=window)
frame.pack(pady=40, padx=60, fill='both', expand=True)

window.mainloop()