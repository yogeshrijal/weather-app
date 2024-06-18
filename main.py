import requests
import tkinter as tk
from tkinter import messagebox

def fetch_weather():
    api_key = '30d4741c779ba94c470ca1f63045390a'
    city = city_entry.get()

    try:
        # API request
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={api_key}"
        response = requests.get(url)
        response.raise_for_status()  # Check for errors in the request

        # Process API response
        data = response.json()
        if data['cod'] == '404':
            messagebox.showerror("Error", "City not found. Please check your spelling.")
        else:
            weather = data['weather'][0]['main']
            temp = round(data['main']['temp'])
            result_text.set(f"The weather in {city} is: {weather}\n"
                            f"The temperature is: {temp}°C")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Error fetching data: {e}")

# Create the main window
root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")
root.configure(bg="sky blue")

# Widgets
label = tk.Label(root, text="Enter city:", font=("Arial", 14), bg="sky blue")
label.pack(pady=20)

city_entry = tk.Entry(root, width=30, font=("Arial", 12))
city_entry.pack()

fetch_button = tk.Button(root, text="Check Weather", command=fetch_weather, bg="#592f2a", fg="white", font=("Arial", 12))
fetch_button.pack(pady=10)

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, wraplength=350, font=("Arial", 12), bg="sky blue")
result_label.pack(pady=20)

# Run the application
root.mainloop()
