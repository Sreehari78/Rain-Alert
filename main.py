import requests
from twilio.rest import Client

# Constants
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "69f04e4613056b159c2761a9d9e664d2"
WEATHER_PARAMETERS = {
    "lat": 9.9833,
    "lon": 76.2833,
    "exclude": "current,minutely,daily",
    "appid": API_KEY
}
ACCOUNT_SID = "AC9b9d4239d48cff5946bbacb81a6ab373"
AUTH_TOKEN = "c2a5cfc99c8720e97ba1af4a8ef31438"

will_rain = False

# Get response and raise for any status if failed to get the response
response = requests.get(url=OWM_ENDPOINT, params=WEATHER_PARAMETERS)
response.raise_for_status()

# Storing the json data and slicing the required data
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

# Checking if it will rain in next 12 hours
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages \
        .create(
            body="It's gonna rain today! Remember to take an umbrella ☂️",
            from_='+14158494010',
            to='+919567111909'
        )

    print(message.status)
