from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import Canvas, PhotoImage, Tk
import requests

# Ana pencere oluşturuluyor
main_window = Tk()
main_window.title("Weather App")  # Pencere başlığı
main_window.geometry("1100x621")  # Pencere boyutu
main_window.resizable(0, 0)
# Uygulama ikonu belirleniyor
ico = Image.open("icon.png")
photo = ImageTk.PhotoImage(ico)
main_window.iconphoto(True, photo)

# Arkaplan fotoğrafını yükle
background_image = Image.open("background.png")
background_photo = ImageTk.PhotoImage(background_image)

# Label widget'ı oluşturup arka plana fotoğrafı yerleştir
background_label = Label(main_window, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

rain_icon = PhotoImage(file="rain.png")
sunny_icon = PhotoImage(file="sunny.png")
clouds_icon = PhotoImage(file="clouds.png")


# Hava durumu bilgisi almak için bir fonksiyon tanımlanıyor
def get_weather(city):
    api_key = "YOUR_API_KEY"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = {
            f"description": data["weather"][0]["main"],
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


# Hoşgeldiniz etiketi
Welcome = Label(main_window, text="Welcome to The Weather Application")
Welcome.pack(pady=20)
# Şehir giriş etiketi ve kutusu
City = Label(main_window, text="Enter City Name:")
City.pack()
EntryBox = Entry(main_window)
EntryBox.pack()
# Hava durumu sonuç kutusu


# Hava durumu gösterme fonksiyonu
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
    else:
        Result.config(state="normal")
        Result.delete(1.0, END)
        Result.insert(END, "Bulunamadı! Lütfen geçerli bir şehir adı girin.")
        Result.config(state="disabled")


# Hava durumu gösterme düğmesi
Button = Button(main_window, text="Show Weather", command=lambda: show_weather())
Button.pack(pady=10)

Result = Text(main_window, height=10, width=50)
Result.pack(pady=10, padx=10)

frame = Frame(main_window)
frame.pack(pady=10, padx=10)

# Ana döngü
main_window.mainloop()
