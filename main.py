import pyfiglet
import colorama
from colorama import Fore, Style
import aminofix
import threading

print(Fore.GREEN)
print(Style.BRIGHT)

Introduction = pyfiglet.figlet_format("FlashAd", font="colossal")
print(Introduction)
print("Made by sneed#4975")
print("Made with Amino.fix.")
print("Have fun (:")

email = input("Email: ")
password = input("Password: ")
client = aminofix.Client()
client.login(email=email, password=password)
print(f"Logged into {email}")
subclients = client.sub_clients()
for name, id in zip(subclients.name, subclients.comId):
    print(name, id)
comId = input("Community ID: ")
subclient = aminofix.SubClient(comId=comId, profile=client.profile)

def Option1():
    amountofmembers = int(input("How many members do you want to advertise to: "))
    userIds = subclient.get_online_users(start=0, size=amountofmembers).profile.userId
    message = input("""Advertisement Message: """)
    for userId in userIds:
        try:
            subclient.start_chat(userId=userId, message=message, publishToGlobal=False, isGlobal=False)
            print(f"Sending message to {userId}")
        except aminofix.exceptions.ChatInvitesDisabled:
            print("User has disabled chat invites. Moving onto the next user")
        except aminofix.exceptions.ActionNotAllowed:
            print("Action not allowed.")

def Option2():
    amountofmembers = int(input("How many members do you want to advertise to: "))
    userIds = subclient.get_all_users(start=0, size=amountofmembers).profile.userId
    message = input("""Advertisement Message: """)
    for userId in userIds:
        try:
            subclient.start_chat(userId=userId, message=message, publishToGlobal=False, isGlobal=False)
            print(f"Sending message to {userId}")
        except aminofix.exceptions.ChatInvitesDisabled:
            print("User has disabled chat invites. Moving onto the next user.")
        except aminofix.exceptions.ActionNotAllowed:
            print("Action not allowed.")

print('''[1] - Advertise to Online Users
[2] - Advertise to Offline Users''')

choice = input("Select: ")

if choice == "1":
    Option1()

if choice == "2":
    Option2()

threads = []

for i in range(10):
    t = threading.Thread(target=Option1)
    t.daemon = True
    threads.append(t)

for i in range(10):
    threads[i].start()

for i in range(10):
    threads[i].join()

for i in range(10):
    t = threading.Thread(target=Option2)
    t.daemon = True
    threads.append(t)

for i in range(10):
    threads[i].start()

for i in range(10):
    threads[i].join()


