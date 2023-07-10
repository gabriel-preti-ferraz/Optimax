from customtkinter import CTkImage
from PIL import Image
import os

general_configs = CTkImage(Image.open(os.path.join('assets/images/general-configs.png')), size=(50, 50))
advanced_configs = CTkImage(Image.open(os.path.join('assets/images/advanced-configs.png')), size=(50, 50))
clean_configs = CTkImage(Image.open(os.path.join('assets/images/clean-configs.png')), size=(50, 50))