# AI-Ml-Project
# Weather Prediction without CSV (Hardcoded Dataset)

# Step 1: Dataset (you can edit/add more data here)
data = [
    {"Temperature": 30, "Humidity": 70, "Wind": 10, "Weather": "Sunny"},
    {"Temperature": 25, "Humidity": 80, "Wind": 15, "Weather": "Rainy"},
    {"Temperature": 32, "Humidity": 65, "Wind": 8, "Weather": "Sunny"},
    {"Temperature": 24, "Humidity": 85, "Wind": 12, "Weather": "Rainy"},
    {"Temperature": 28, "Humidity": 75, "Wind": 9, "Weather": "Sunny"},
]

# Step 2: Separate data
sunny_temp, rainy_temp = [], []
sunny_humidity, rainy_humidity = [], []
sunny_wind, rainy_wind = [], []

for row in data:
    if row["Weather"] == "Sunny":
        sunny_temp.append(row["Temperature"])
        sunny_humidity.append(row["Humidity"])
        sunny_wind.append(row["Wind"])
    else:
        rainy_temp.append(row["Temperature"])
        rainy_humidity.append(row["Humidity"])
        rainy_wind.append(row["Wind"])

# Step 3: Calculate averages
avg_sunny = [
    sum(sunny_temp) / len(sunny_temp),
    sum(sunny_humidity) / len(sunny_humidity),
    sum(sunny_wind) / len(sunny_wind)
]

avg_rainy = [
    sum(rainy_temp) / len(rainy_temp),
    sum(rainy_humidity) / len(rainy_humidity),
    sum(rainy_wind) / len(rainy_wind)
]

# Step 4: Prediction function
def predict_weather(temp, humidity, wind):
    dist_sunny = ((temp - avg_sunny[0])**2 +
                  (humidity - avg_sunny[1])**2 +
                  (wind - avg_sunny[2])**2) ** 0.5

    dist_rainy = ((temp - avg_rainy[0])**2 +
                  (humidity - avg_rainy[1])**2 +
                  (wind - avg_rainy[2])**2) ** 0.5

    return "Sunny" if dist_sunny < dist_rainy else "Rainy"

# Step 5: Show averages
print("Average values:")
print("Sunny:", avg_sunny)
print("Rainy:", avg_rainy)

# Step 6: User input
print("\n--- Weather Prediction ---")

try:
    temp = float(input("Enter Temperature: "))
    humidity = float(input("Enter Humidity: "))
    wind = float(input("Enter Wind Speed: "))

    result = predict_weather(temp, humidity, wind)
    print("\nPredicted Weather:", result)

except:
    print("Invalid input! Please enter numbers.")
