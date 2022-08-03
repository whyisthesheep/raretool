from dhooks import Webhook as w
from os import system as s

def statuscheck():
  try:
    hook.get_info()
  except:
    print("Error: Discord did not respond to the webhook, check your internet and confirm that you are using the correct webhook URL")
  else:
    print("No errors were raised, your webhook seems good!")
def printinfo():
    info = hook.get_info()
    print("Server ID: " + info.guild_id + "\nChannel ID: " + info.channel_id + "\nWebhook name: " + info.default_name)
def attacks():
    print("Attacks: \n>) 1: Send message\n>) 2: Manage previous message\n>) 3: (COMING SOON) Message loop\n>) 4: (COMING SOON) Embed")
    attack = int(input(">) "))
    if attack == 1:
      msg = input("Message: ")
      hook.send(msg)
    elif attack == 2:
      print("Options:\n>} 1: Delete\n>} 2: Edit")
      manage = int(input(">} "))
      if manage == 1:
        hook.delete()
      elif manage == 2:
        changes = input("Changes: ")
        hook.modify(changes)
dad = "gone"
title = """
    ____                  __              __
   / __ \____ _________  / /_____  ____  / /
  / /_/ / __ `/ ___/ _ \/ __/ __ \/ __ \/ /
 / _, _/ /_/ / /  /  __/ /_/ /_/ / /_/ / /
/_/ |_|\__,_/_/   \___/\__/\____/\____/_/
"""

while dad == "gone":
  s("cls")
  print(title)
  print("Remember to set the hook url")
  print(">] 1: Set webhook\n>] 2: Check webhook\n>] 3: Info\n>] 4: Attacks\n>] 5: All at once")
  menu = int(input(">] "))
  if menu == 1:
    hook = w(input("Paste URL: "))
    print("Hook set")
  elif menu == 2:
    statuscheck()
  elif menu == 3:
    printinfo()
  elif menu == 4:
    attacks()
  elif menu == 5:
    hook = w(input("Paste URL: "))
    print("Hook set")
    print("")
    statuscheck()
    print("")
    printinfo()
    print("")
    attacks()
