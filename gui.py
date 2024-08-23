# dev gui layout and components
# ensure proper event handling for user interaction
# setting up a virtual enviroment
from tkinter import messagebox
from tkinter import *
from configparser import ConfigParser
import requests
#import json



url_2 = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'



config_file = 'logic.ini'
config = ConfigParser()
config.read(config_file)
api_key = config['api_key']['key']
print(api_key)


def get_weather(city):
    result = requests.get(url_2.format(city, api_key))
    if result:
        #print(result.content)
        json = result.json()
        city = json['name']
        country = json['sys']['country']
        temp_kelvin = json['main']['temp']
        temp_celsuis = temp_kelvin -273.15
        temp_fahrenheit = (temp_kelvin - 273.15)*9/5+32
        icon = json['weather']['icon']
        weather = json['weather'][0]['main']
        final = [city, country, temp_celsuis, temp_fahrenheit, icon, weather]
        return final   
    else: 
        return None

#get_weather('newyork')


def search():
     city = city_text.get()
     weather = get_weather[city]
     if weather:
        location_lbl['text'] = '{}, {}', format(weather[0],weather[1])
        image['bitmap'] = 'weather_icons/{}.png'.format(weather[4])
        temp_lbl['text'] = '{:.2f}°C, {:.2f}°F'.format(weather[2], weather[3])
        weather_lbl['text'] = weather[5] 
        pass


     else:
        messagebox.showerror('Error','Cannot find city {}'.format(city))





def search():
    pass


app = Tk()
app.title("weather app")
app.geometry("700x350")

city_text = StringVar()
city_entry = Entry(app, textvariable=city_text)
city_entry.pack()
search_btn = Button(app, text='search weather', width=12, command=search)
search_btn.pack()



location_lbl = Label(app, text='Location', font=('bold', 20))
location_lbl.pack()

image = Label(app, bitmap='')
image.pack()

temp_lbl = Label(app, text='Temperature')
temp_lbl.pack()

weather_lbl = Label(app, text='Weather')
weather_lbl.pack()



app.mainloop()