import requests
import os
import random
import time
import pystyle
from pystyle import System, Colorate, Center, Colors
System.Clear()
ascii = '''

██████╗░███████╗░█████╗░████████╗██╗░░██╗
██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██║░░██║
██║░░██║█████╗░░███████║░░░██║░░░███████║
██║░░██║██╔══╝░░██╔══██║░░░██║░░░██╔══██║
██████╔╝███████╗██║░░██║░░░██║░░░██║░░██║
╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝'''[1:]

print(Colorate.Horizontal(Colors.blue_to_cyan, Center.XCenter(ascii)))

username = input(Colorate.Horizontal(Colors.blue_to_cyan, 'Username : '))
webhook = input(Colorate.Horizontal(Colors.blue_to_cyan,'Webhook -> '))
reason = input(Colorate.Horizontal(Colors.blue_to_cyan,'What message you want to say?'))
pfp = input(Colorate.Horizontal(Colors.blue_to_cyan,'Enter a image link for the PFP'))

try:
    requests.post(webhook, json={'content': f'{reason}', 'username': f'{username}','avatar_url':f'{pfp}'})
    print(f'Sent')
except Exception as e:
        print(f'Error: {e}')



