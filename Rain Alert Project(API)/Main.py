import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

Api_Key = os.environ.get("OW_API_KEY") # Kindly put your verified Key if you use my Api key it may not work.
account_sid="AC400f7d9583a38e759641eafd3413b724"
auth_token= os.environ.get("AUTH_TOKEN") # I have  used environmental variables to hide my API keys and Auth token for safety issues.
Twilio_Api="AQ9MMLCNM2HYHHY1JLW45SCB"


OW_endpoint="https://api.openweathermap.org/data/2.5/forecast?"


parameter={ "lat": 55.673820,
            "lon": 12.598730,
            "appid": Api_Key,
            "cnt" : 4

}


response= requests.get(OW_endpoint,params=parameter,)
data= response.json()

will_rain= False
for hour_data in data["list"]:
    condition_code=hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
       will_rain=True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client =Client(account_sid,auth_token,http_client=proxy_client)
    message = client.messages.create(
    from_="whatsapp:+14155238886",
    body="It's going to rain today. Remember to bring an umbrella",
    to =   "whatsapp:Your Verified Number "

    )

    print(message.status)
