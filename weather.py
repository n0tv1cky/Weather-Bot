import requests
from datetime import datetime

apiKey = '57af060ec93e4b7aabf3d1cd0f3312f2'
city = input('Enter the name of the city: ')

sourceLink = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + apiKey
apiLink = requests.get(sourceLink)
apiData = apiLink.json()

try:
        descriptionVal = apiData['weather'][0]['description']
        temperatureVal = apiData['main']['temp'] - 273.15
        humidityVal = apiData['main']['humidity']
        windSpeedVal = apiData['wind']['speed']
except:
        print("INVALID City name")
        exit()

time = datetime.now().strftime("%H:%M:%S, %d %B %Y")

data = ["Showing weather details for {} at {}".format(city.upper(), time) + '\n',
        "Current Temperature: {:.2f} degree Celsius" .format(temperatureVal) + '\n',
        "Current Humidity   : {}%" .format(humidityVal) + '\n',
        "Current Wind Speed : {}kmph" .format(windSpeedVal) + '\n',
        "Weather Description: {}" .format(descriptionVal) + '\n',
        '\n']

file = open('weatherData.txt', 'a+')
file.writelines(data)
print("Successfully written Weather Data for {} in weatherData.txt".format(city.upper()))
file.close()