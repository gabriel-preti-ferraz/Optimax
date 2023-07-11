from customtkinter import *
from commands import *
import images
import pages

set_appearance_mode('dark')
set_default_color_theme('dark-blue')

window = CTk()
window.geometry('1200x900')
window.title('Optimax')

class Sidebar():
    sidebar = CTkFrame(master=window, width=140)
    sidebar.pack(fill='y', side='left')

    general_configs = CTkButton(master=sidebar, fg_color='transparent', image=images.general_configs, text='Configurações Gerais', command=lambda: Navigation.show_page(Navigation.get_page(container=window, page_name='general')))
    general_configs.pack(pady=30, padx=10)

    advanced_configs = CTkButton(master=sidebar, fg_color='transparent', image=images.advanced_configs, text='Configurações Avançadas', command=lambda: Navigation.show_page(Navigation.get_page(container=window, page_name='advanced')))
    advanced_configs.pack(pady=20, padx=10)

    clean_configs = CTkButton(master=sidebar, fg_color='transparent', image=images.clean_configs, text='Configurações de Limpeza', command=lambda: Navigation.show_page(Navigation.get_page(container=window, page_name='clean')))
    clean_configs.pack(pady=20, padx=10)

window.mainloop()