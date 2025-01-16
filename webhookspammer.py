"""
Credits: Webhook spammer made by Sai
Discord: lyxscasemenov
Github: lyxscaxd
"""
print("""

  _                          
 | |_   ___  _____  ___ __ _ 
 | | | | \ \/ / __|/ __/ _` |
 | | |_| |>  <\__ \ (_| (_| |
 |_|\__, /_/\_\___/\___\__,_|
    |___/                    
                           

                                    Made by lyxsca
                                   Github: lyxscaxd
""")

#imports
from dhooks import Webhook
import time

#prompts
message = input("What do you want to spam?: ")
webhookurl = Webhook(input("Enter webhook: "))
delay = int(input("Enter a delay: "))

#webhook spamming time
while True:
    time.sleep(delay)
    webhookurl.send(message)
    print("Sent. Sub to lyxscaxd")
