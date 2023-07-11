from customtkinter import *
import pages

class Navigation():
    def show_page(frame):
        frame.pack(pady=40, padx=60, fill='both', expand=True)

    def get_page(container, page_name):
        if page_name == 'general':
            return pages.general_configs(container=container)

        elif page_name == 'advanced':
            return pages.advanced_configs(container=container)

        elif page_name == 'clean':
            return pages.clean_configs(container=container)