import requests
import pystyle
from pystyle import *
import platform
import sys
import time
import datetime
System.Clear()
ascii = '''

██████╗░███████╗░█████╗░████████╗██╗░░██╗
██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██║░░██║
██║░░██║█████╗░░███████║░░░██║░░░███████║
██║░░██║██╔══╝░░██╔══██║░░░██║░░░██╔══██║
██████╔╝███████╗██║░░██║░░░██║░░░██║░░██║
╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝'''[1:]

print(Colorate.Horizontal(Colors.blue_to_cyan, Center.XCenter(ascii)))

def set_terminal_title(title):
    if platform.system() == 'Windows':
        sys.stdout.write("\033]0;{}\007".format(title))
    else:
        sys.stdout.write("\033]2;{}\007".format(title))
    sys.stdout.flush()

friends_count = ''

def tokenInfo(token):
    headr1 = {
    'Authorization': f'{token}',
    'Content-Type': 'application/json'
    }
    res = requests.get('https://discordapp.com/api/v6/users/@me', headers=headr1)
    if res.status_code == 200:
        print(f"Valid Token[collecting data...]")
        pass
    else:
        print(f"Invalid Token!")

    res_json = res.json()
    user = f'{res_json["username"]}#{res_json["discriminator"]}'
    uid = res_json['id']
    user_id = uid
    avatar_id = res_json['avatar']
    avatar_url = f'https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}.gif'
    pnum = res_json['phone']
    email = res_json['email']
    mfa_enabled = res_json['mfa_enabled']
    flags = res_json['flags']
    lang = res_json['locale']
    verified = res_json['verified']
    has_nitro = False
    res = requests.get('https://discordapp.com/api/v6/users/@me/billing/subscriptions', headers=headr1)
    nitro_data = res.json()
    has_nitro = bool(len(nitro_data) > 0)

    print( f"""\n
    Token: {token}
Username: {user}
User-ID: {uid}
Avatar-ID: {avatar_id}
Avatar-URL: {avatar_url}
Phone-Number: {pnum}
Email: {email}
2FA: {mfa_enabled}
Flags: {flags}
Language: {lang}
Verified: {verified}
Nitro: {has_nitro}
""")
"""
def tokenInfo(token):
    print(Colorate.Horizontal(Colors.blue_to_cyan,f'--------------------------------------------------------------------------------\nToken : {token} \n'))
    headers = {'Authorization': token, 'Content-Type': 'application/json'}  
    r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
    if r.status_code == 200:
            user_info = r.json()
            username = user_info['username'] + '#' + user_info['discriminator']
            ID = user_info['id']
            phone = user_info['phone']
            email = user_info['email']
            mfa = user_info['mfa_enabled']
            nitro = user_info['premium_since']            # Get server count
            r = requests.get('https://discord.com/api/v6/users/@me/guilds', headers=headers)
            if r.status_code == 200:
                servers = r.json()
                servers_count = len(servers)
                if servers_count == 0:
                    print(Colorate.Horizontal(Colors.blue_to_cyan,f'            [+]Server Number |  0 servers'))
                else:
                    print(Colorate.Horizontal(Colors.blue_to_cyan,f'            [+]Server Number |  {servers_count} servers'))

            # Get friends count
            r = requests.get('https://discord.com/api/v6/users/@me/friends', headers=headers)
            if r.status_code == 200:
                friends = r.json()
                friends_count = len(friends)
                if friends_count == 0:
                    print(Colorate.Horizontal(Colors.blue_to_cyan,f'            [+]Friends        |  0 friends'))
                else:
                    print(Colorate.Horizontal(Colors.blue_to_cyan,f'            [+]Friends        |  {friends_count} friends'))
            print(Colorate.Horizontal(Colors.blue_to_cyan,f'''
            [+]User ID       |  {ID}

            [+]User Name     |  {username}

            [+]2 Factor Auth |  {mfa}

            [+]Email         |  {email}

            [+]Phone number  |  {phone if phone else "No number phone on the account"}
            
            [+]Token         |  {token}
            
            '''))
"""

with open("tokens.txt", "r") as file:
    tokens = [line.replace('\n', '') for line in file.readlines() if line != '\n']
    valid_tokens = []
    invalid_tokens = []
    for token in tokens:
        r1 = requests.get('https://discord.com/api/v6/auth/login', headers={"Authorization": token})
        if r1.status_code <= 299:
            print(Colorate.Horizontal(Colors.blue_to_cyan, f"Valid token | {token}"))
            print(Colorate.Horizontal(Colors.blue_to_cyan,'------------------------------------------------------------------------------------------------------------'))
            set_terminal_title("Valid tokens = {} Invalid tokens = {}".format(len(valid_tokens), len(invalid_tokens)))
            valid_tokens.append(token)
        else:
            print(Colorate.Horizontal(Colors.blue_to_white, f"Invalid token | {token}"))
            print(Colorate.Horizontal(Colors.blue_to_cyan,'------------------------------------------------------------------------------------------------------------'))
            set_terminal_title("Valid tokens = {} Invalid tokens = {}".format(len(valid_tokens), len(invalid_tokens)))
            invalid_tokens.append(token)

with open("valid_tokens.txt", "w") as valid_file:
    for token in valid_tokens:
        valid_file.write(token + "\n")

with open("invalid_tokens.txt", "w") as invalid_file:
    for token in invalid_tokens:
        invalid_file.write(token + "\n")


choice = input(Colorate.Horizontal(Colors.blue_to_cyan,'Do you want tokens informations ? Yes [1] / No [2]'))
if choice == '1':

    with open("valid_tokens.txt", "r") as file:
            tokens = [line.replace('\n', '') for line in file.readlines() if line != '\n']
            for token in tokens:
                tokenInfo(token)

else:
    print('')


input(Colorate.Horizontal(Colors.blue_to_cyan, 'Working token saved in valid_tokens.txt \n\nInvalid token are saved in invalid_token \n\nPress any key to leave'))
System.Clear()