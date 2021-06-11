import requests
from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("500x500")
window.title("Weather App")
window.config(bg="black")

city = StringVar

def display_result():

    # initialize weather request from API
    try:
        get_city = city_entry.get()
        r = requests.get(
            "https://api.openweathermap.org/data/2.5/weather?q=" + get_city + "&appid=36e6aefc64df32f4ca03bd2cbd44d4d7")
        data = r.json()
        # display labels
        display_temp = Label(window, text=int(data['main']['temp'] - 273.15), textvariable=temp, font='Helvetica',
                                                                                                 fg="black",
                                 bg="white")
        display_temp.place(x=200, y=110)
        display_wind_speed = Label(window, text=str(data['wind']['speed']) + "KM/h",textvariable=wind_speed,
        font='Helvetica',
                                   fg="black",
                                   bg="white")
        display_wind_speed.place(x=200, y=200)
        display_humidity = Label(window, text=str(data['main']['humidity']), textvariable=humidity, font='Helvetica',
                                 fg="black",
                                 bg="white")
        display_humidity.place(x=200, y=150)
        display_cloud_cover = Label(window, text=str(data['weather'][0]['main'] + " skies"),textvariable=cloud_clover,
        font='Helvetica',
                                    fg="black",
                                    bg="white")
        display_cloud_cover.place(x=200, y=250)

    except KeyError:
         messagebox.showinfo("ERROR","PLEASE ENTER YOUR CITY")


def exiting():
    window.destroy()

# Widgets


city_entry=Entry(window, textvariable="city", bg="white")
city_entry.place(x=200, y=73, width=150)

label_Title = Label(window, text="WEATHER APPLICATION", bg="black", fg="white")
label_Title.place(x=200, y=10)
label_Choose = Label(window, text="Choose Location", bg="black", fg="white")
label_Choose.place(x=220, y=50)

label_Temperature = Label(window, text="Temperature", bg="black", fg="white")
label_Temperature.place(x=100, y=110)
label_Humidity = Label(window, text="Humidity", bg="black", fg="white")
label_Humidity.place(x=100, y=150)
label_Wind_speed = Label(window, text="Wind Speed", bg="black", fg="white")
label_Wind_speed.place(x=100, y=200)
label_Cloud_Cover = Label(window, text="Cloud Cover", bg="black", fg="white")
label_Cloud_Cover.place(x=100, y=250)
# Buttons
button_Display = Button(window, text="Display", bg="white", command=display_result)
button_Display.place(x=100, y=300)
# button_clear = Button(window, text="Clear", bg="white", )
# button_clear.place(x=200, y=300)
button_exit = Button(window, text="Exit", bg="white", command=exiting)
button_exit.place(x=300, y=300)
window.mainloop()
