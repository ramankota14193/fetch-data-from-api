  # Sample data for multiple cities
  cities = ['London', 'Paris', 'New York']
  temperatures = []
  humidities = []

  for city in cities:
      data = fetch_weather_data(city, api_key)
      info = extract_weather_info(data)
      if info:
          temperatures.append(info['temperature'])
          humidities.append(info['humidity'])

  # Create a dashboard
  plt.figure(figsize=(12, 6))

  plt.subplot(1, 2, 1)
  sns.barplot(x=cities, y=temperatures, palette='coolwarm')
  plt.title("Temperature Comparison")
  plt.ylabel("Temperature (°C)")

  plt.subplot(1, 2, 2)
  sns.barplot(x=cities, y=humidities, palette='Blues')
  plt.title("Humidity Comparison")
  plt.ylabel("Humidity (%)")

  plt.tight_layout()
  plt.show()
  