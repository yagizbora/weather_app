from tkinter import *  # Importing necessary modules from tkinter
from tkinter import messagebox, Canvas, Tk, Entry, Text, Button
from PIL import Image, ImageTk
import requests

# Creating the main window of the application
main_window = Tk()
main_window.title("Weather App")  # Setting the window title
main_window.geometry("1100x621")  # Setting the window size

# Setting the application icon
ico = Image.open("icon.png")
photo = ImageTk.PhotoImage(ico)
main_window.iconphoto(True, photo)

# Loading weather icons
rain_icon = PhotoImage(file="rain.png")
sunny_icon = PhotoImage(file="sunny.png")
clouds_icon = PhotoImage(file="clouds.png")


# Function to fetch weather data from the OpenWeatherMap API
def get_weather(city):
    api_key = "YOUR_API_KEY"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather = {
            "description": data["weather"][0]["description"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "timezone": data["timezone"],
            "feelslike": data["main"]["feels_like"],
        }
        return weather
    else:
        messagebox.showerror(
            "Warning", f"Error fetching weather data: Error Code:{response.status_code}"
        )
        return None


# Function to display the weather data in the GUI
def show_weather():
    city_name = EntryBox.get()
    result = get_weather(city_name)

    if result is not None:
        Result.config(state="normal")
        Result.delete(1.0, END)
        Result.insert(END, f"Hava {city_name} şehri için:\n")
        Result.insert(END, f"Time Zone: {str(result['timezone'])}\n")
        Result.insert(END, "Durum: " + result["description"] + "\n")
        Result.insert(END, "Sıcaklık: " + str(result["temperature"]) + "°C\n")
        Result.insert(END, "Hissedilen Sıcaklık: " + str(result["feelslike"]) + "°C\n")
        Result.insert(END, "Nem: " + str(result["humidity"]) + "%\n")
        Result.insert(END, "Rüzgar Hızı: " + str(result["wind_speed"]) + "m/s\n")
        Result.config(state="disabled")
        descriptionstatus(result["description"])
    else:
        Result.config(state="normal")
        Result.delete(1.0, END)
        Result.insert(END, "Bulunamadı! Lütfen geçerli bir şehir adı girin.")
        Result.config(state="disabled")


# Function to update the weather icon based on the weather description
def descriptionstatus(weather_desc):
    canvas.delete("all")  # Clearing the current image
    weather_desc = weather_desc.lower()

    if any(
        keyword in weather_desc for keyword in ["sunny", "clear", "fair", "clear sky"]
    ):
        canvas.create_image(0, 0, anchor=NW, image=sunny_icon)
    elif any(
        keyword in weather_desc for keyword in ["cloud", "overcast", "mist", "fog"]
    ):
        canvas.create_image(0, 0, anchor=NW, image=clouds_icon)
    elif any(keyword in weather_desc for keyword in ["rain", "drizzle", "shower"]):
        canvas.create_image(0, 0, anchor=NW, image=rain_icon)


# Welcome label
Welcome = Label(main_window, text="Welcome to The Weather Application")
Welcome.pack(pady=20)

# City entry label and box
City = Label(main_window, text="Enter City Name:")
City.pack()
EntryBox = Entry(main_window)
EntryBox.pack()

# Weather result text box
Result = Text(main_window, height=10, width=50)
Result.pack(pady=10, padx=10)

# Canvas for displaying the weather icon
canvas = Canvas(main_window, width=sunny_icon.width(), height=sunny_icon.height())
canvas.pack()

# Show Weather button
Button = Button(main_window, text="Show Weather", command=show_weather)
Button.pack(pady=20)

# Running the main loop
main_window.mainloop()
