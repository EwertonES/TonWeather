#######################################################################################################################
#   Ton Tempo - App de previsão do tempo usando OpenWeatherAPI e Tkinter                                              #
#   Data: 05 / 03 / 2020                                                                                              #
#   Autor: Ewerton Evangelista de Souza                                                                               #
#   Objetivo: Criei para aprender a utilizar a ferramenta Tkinter na criação de interfaces                            #
#######################################################################################################################

import requests
import tkinter as tk
from PIL import Image, ImageTk

# CONSTANTS
WIDTH = 600  # Window width
HEIGHT = 280  # Window height
OPENWEATHERAPIKEY = "03217d7d54e1c2a2d6908b25ad7c73da"


# Get Open Weather data from entry
def get_weather(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHERAPIKEY}&units=metric&lang=pt_br'

    weather_json = requests.get(url).json()

    if weather_json["cod"] == 200:
        label['text'] = format_response(weather_json)
        # Weather condition png image
        icon_url = f'./imgs/{weather_json["weather"][0]["icon"]}.png'
        weather_icon = ImageTk.PhotoImage(Image.open(icon_url))
        weather_label = tk.Label(frameBottom, image=weather_icon, bg='#FAFCFB', anchor='e')
        weather_label.image = weather_icon
        weather_label.place(relx=.6, relwidth=.4, relheight=1)

    elif weather_json["cod"] == '404':
        label['text'] = "404: Cidade não encontrada."

    label['bg'] = '#FAFCFB'
    label['justify'] = 'left'


# Format to label
def format_response(weather_json):
    city_name = weather_json["name"]
    city_country = weather_json["sys"]["country"]
    city_temperature = weather_json["main"]

    return (f'{city_name}, {city_country}\n\n'
            f'Temperatura:\nAtual: {city_temperature["temp"]} °C\n'
            f'Mínima: {city_temperature["temp_min"]} °C\n'
            f'Máxima: {city_temperature["temp_max"]} °C')


# Create main window
root = tk.Tk()
root.wm_title("Ton Weather")  # Changes title
root.iconbitmap("./imgs/icon.ico")  # Changes .ico

# Create canvas with background img
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()
backgroundImage = ImageTk.PhotoImage(Image.open('./imgs/landscape.jpg'))
backgroundLabel = tk.Label(root, image=backgroundImage)
backgroundLabel.place(relwidth=1, relheight=1)

# Create containers for  widgets
frameTop = tk.Frame(root, bg='#4C97DB')  # No cross-platform way to do transparency using tkinter
frameTop.place(relx=.05, rely=.05, relwidth=.9, relheight=.3)

frameBottom = tk.Frame(root, bg='#4C97DB')
frameBottom.place(relx=.05, rely=.4, relwidth=.9, relheight=.55)

# Create city field
entry = tk.Entry(frameTop, font=('Courier', 30))
entry.place(relwidth=.75, relheight=1)

# Create 'Search' button
button = tk.Button(frameTop, text='Pesquisar', font=('Courier', 15), command=lambda: get_weather(entry.get()))
button.place(relx=.75, relwidth=.25, relheight=1)

# Create field to display result
label = tk.Label(frameBottom, font=('Courier', 15), bg='#4C97DB', anchor='w')
label.place(relwidth=1, relheight=1)

# Start app
root.mainloop()
