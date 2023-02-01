# Dependency 
import random, secrets, requests, string, pystyle, keyboard, faker, pathlib
from pystyle import *
from faker import *

# Directory
dir = pathlib.Path.cwd()

System.Clear()
ascii = '''

██████╗░███████╗░█████╗░████████╗██╗░░██╗
██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██║░░██║
██║░░██║█████╗░░███████║░░░██║░░░███████║
██║░░██║██╔══╝░░██╔══██║░░░██║░░░██╔══██║
██████╔╝███████╗██║░░██║░░░██║░░░██║░░██║
╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝'''[1:]
print(Colorate.Horizontal(Colors.blue_to_cyan, Center.XCenter(ascii)))
# Billing Faker
bi = ""
bill = ""
rdm = random.randint(0, 2)
if rdm == 0:
  bi = " 🟦 Paypal "
elif rdm == 1:
  bi = " 💳 Credit card"
else:
  bi = " 🟦 Paypal and 💳 Credit card"
bill = ""
if random.randint(0, 1) == 0:
    bill = f"Billing method is : {bi}"
else:
    bill = "No billing method 😔"

# Fake Country
faker = Faker()
country = faker.country()
country = country.replace(" ", "_")


ip = faker.ipv4()
r = requests.get('http://ip-api.com/json/' + ip).json()
region = r['regionName']
timezone = r['timezone']



token = "NT"+random.choice(string.ascii_letters)+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(21))+"."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
url = Write.Input("Enter Webhook ->", Colors.red_to_purple, interval=0.01)
img = Write.Input("\nEnter Image URL Link ->", Colors.red_to_purple, interval=0.01)
img_data = requests.get(img).content
with open('Image149.jpg', 'wb') as handler:
    handler.write(img_data)

Write.Print(f"\nImage Saved in {dir} \n\n", Colors.red_to_purple, interval=0.01)

cpu_list = ["Intel Core i9", "AMD Ryzen 9", "Intel Core i7", "AMD Ryzen 7", "Intel Core i5", "AMD Ryzen 5"]
ram_list = ["32GB DDR4", "16GB DDR4", "8GB DDR4"]
storage_list = ["1TB NVMe SSD", "512GB NVMe SSD", "256GB NVMe SSD"]

cpu = random.choice(cpu_list)
ram = random.choice(ram_list)
storage = random.choice(storage_list)


while True:
  if keyboard.is_pressed('r'):  # if key 'q' is pressed 
    data = {
  "username": "Death Image Grabber",
  "avatar_url": "https://mcdn.wallpapersafari.com/medium/87/48/1O4pLm.png",
  "embeds": [
    {
      "author": {
        "name": "Someone clicked you're image",
        "icon_url": "https://thumbs.dreamstime.com/b/stupid-text-blue-grungy-round-vintage-stamp-stupid-text-blue-grungy-round-stamp-213094072.jpg"
      },
      "title": "🧍 ALL DATA : ",
      "description": f"⚠️ GRABBED⚠️ Clicked at {current_time} \n Token : ⚠️ {token} ⚠️",
      "color": 15258703,
      "fields": [
        {
          "name": "🌍 IP + Country : ",
          "value": ip + f' | [{region}](https://en.wikipedia.org/wiki/{region}) \n Timezone : {timezone}',
        },
        {
          "name": "💸 Billing :",
          "value": f"{bill}",
        },
        {
          "name": "🖥️ Component",
          "value": f"CPU {cpu} \n Storage : {storage} \n Ram : {ram}",
        },
        {
          "name": "Thanks!",
          "value": "You're welcome :wink:"
        }
      ],
      "thumbnail": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/3/38/4-Nature-Wallpapers-2014-1_ukaavUI.jpg"
      },
      "image": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/5/5a/A_picture_from_China_every_day_108.jpg"
      },
      "footer": {
        "text": "Woah! So cool! :smirk:",
        "icon_url": "https://i.imgur.com/fKL31aD.jpg"
      }
    }
  ]
}

    result = requests.post(url, json = data)

    try:
      result.raise_for_status()
    except requests.exceptions.HTTPError as err:
      print(err)
    else:
      print('IMAGE CLICKED')
    break