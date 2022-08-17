# Importamos la librería instaloader necesaria para el funcionamiento del programa
# Si no posees la librería introduce este comando sin las comillas en tu terminal ↓↓↓
# comando "pip install instaloader"


import instaloader
from time import sleep
from tqdm import tqdm
import requests

#Ingreso de los datos del usuario 
parser = instaloader.Instaloader()
username = input("Introduzca el nombre del usuario: ")
print()
print("se comenzara a descargar el perfil de",username)
print()
parser.download_profile(username,profile_pic=True)
#Los archivos se descargaran en la ruta donde tenga el programa 
print("Se descargó por completo el perfil de ",username)
print()
print("Gracias por utilizar el programa :)")
