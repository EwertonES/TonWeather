import shutil
import requests

icons = ["01d", "01n", "02d", "02n",
         "03d", "03n", "04d", "04n",
         "09d", "09n", "10d", "10n",
         "11d", "11n", "13d", "13n",
         "50d", "50n"]

for i in icons:
    url = f'http://openweathermap.org/img/wn/{i}@2x.png'
    response = requests.get(url, stream=True)
    file = open('./imgs/' + i + ".png", 'wb')
    response.raw.decode_content = True
    shutil.copyfileobj(response.raw, file)
    del response