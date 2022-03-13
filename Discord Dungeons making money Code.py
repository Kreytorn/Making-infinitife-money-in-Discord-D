from time import sleep
from pynput.keyboard import Key, Controller
import discord


TOKEN = "TYPE YOUR TOKEN HERE"#----------------------------------



client = discord.Client()

keyboard = Controller()

client.index1 = ""
client.index2 = ""
client.usermessageitemname = ""
client.usermessagequantity = ""


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel.name)

    if message.author == client.user:
        return

    if username == "DiscordRPG#0366":

        if message.channel.name == "discord-rpg-1":
            client.index1 = ""
            client.index2 = ""
            client.usermessageitemname = ""
            client.usermessagequantity = ""

            # !mine----------------------------------------------------------------------------------------------------

            if user_message[9] == "f" and  user_message[10] == "o" and user_message[11] == "u" and user_message[12] == "n" and user_message[13] == "d": #mine
                index = user_message.index(",")
                index2 = user_message.index("found ") + 5

                for i in range(index2, index):
                    if user_message[i].isdigit() == True:
                        client.usermessagequantity = client.usermessagequantity + user_message[i]
                        continue
                    client.usermessageitemname = client.usermessageitemname + user_message[i]

                client.usermessageitemname = client.usermessageitemname.strip()
                print(client.usermessagequantity)
                print(client.usermessageitemname)

                if client.usermessageitemname[-1] == "s":
                    client.usermessageitemname = client.usermessageitemname[:-1]

                sleep(10)

                keyboard.press("#")
                keyboard.release("#")

                keyboard.press("!")
                keyboard.release("!")

                keyboard.press("s")
                keyboard.release("s")

                keyboard.press("e")
                keyboard.release("e")

                keyboard.press("l")
                keyboard.release("l")

                keyboard.press("l")
                keyboard.release("l")

                keyboard.press(" ")
                keyboard.release(" ")


                for i in range(len(client.usermessageitemname)):
                    keyboard.press(client.usermessageitemname[i])
                    keyboard.release(client.usermessageitemname[i])

                keyboard.press(" ")
                keyboard.release(" ")

                for i in range(len(client.usermessagequantity)):
                    keyboard.press(client.usermessagequantity[i])
                    keyboard.release(client.usermessagequantity[i])

                keyboard.press(Key.enter)
                keyboard.release(Key.enter)
            #!mine-----------------------------------------------------------------------------------------------------

            #!chop-----------------------------------------------------------------------------------------------------
            if user_message[27] == "w" and user_message[28] == "o" and user_message[29] == "o" and user_message[30] == "d" and user_message[31] == " ":
                print("hey")

                index = user_message.index(",")
                index2 = user_message.index("wood and got ") + 13

                for i in range(index2, index):
                    if user_message[i].isdigit() == True:
                        client.usermessagequantity = client.usermessagequantity + user_message[i]
                        continue
                    client.usermessageitemname = client.usermessageitemname + user_message[i]


                client.usermessageitemname = client.usermessageitemname.strip()

                if client.usermessageitemname == "Regular logs":
                    client.usermessageitemname = "log"

                print(client.usermessagequantity)
                print(client.usermessageitemname)

                if client.usermessageitemname[-1] == "s":
                    client.usermessageitemname = client.usermessageitemname[:-1]

                sleep(10)

                keyboard.press("#")
                keyboard.release("#")

                keyboard.press("!")
                keyboard.release("!")

                keyboard.press("s")
                keyboard.release("s")

                keyboard.press("e")
                keyboard.release("e")

                keyboard.press("l")
                keyboard.release("l")

                keyboard.press("l")
                keyboard.release("l")

                keyboard.press(" ")
                keyboard.release(" ")

                keyboard.press(" ")
                keyboard.release(" ")

                for i in range(len(client.usermessageitemname)):
                    keyboard.press(client.usermessageitemname[i])
                    keyboard.release(client.usermessageitemname[i])

                keyboard.press(" ")
                keyboard.release(" ")

                for i in range(len(client.usermessagequantity)):
                    keyboard.press(client.usermessagequantity[i])
                    keyboard.release(client.usermessagequantity[i])

                keyboard.press(Key.enter)
                keyboard.release(Key.enter)
                #chop----------------------------------------------------------------------------------------------------

                #forage ----------------------------------------------------------------------------------------------------

            if user_message[18] == "g" and  user_message[19] == "i" and user_message[20] == "n" and user_message[21] == "g" and user_message[22] == " " and user_message[23] == "a" and user_message[24] == "n" and user_message[25] == "d":
                index = user_message.index(",")
                index2 = user_message.index("ging and got") + 12

                for i in range(index2, index):
                    if user_message[i].isdigit() == True:
                        client.usermessagequantity = client.usermessagequantity + user_message[i]
                        continue
                    client.usermessageitemname = client.usermessageitemname + user_message[i]

                client.usermessageitemname = client.usermessageitemname.strip()
                print(client.usermessagequantity)
                print(client.usermessageitemname)

                if client.usermessageitemname[-1] == "s":
                    client.usermessageitemname = client.usermessageitemname[:-1]

                sleep(10)

                keyboard.press("#")
                keyboard.release("#")

                keyboard.press("!")
                keyboard.release("!")

                keyboard.press("s")
                keyboard.release("s")

                keyboard.press("e")
                keyboard.release("e")

                keyboard.press("l")
                keyboard.release("l")

                keyboard.press("l")
                keyboard.release("l")

                keyboard.press(" ")
                keyboard.release(" ")

                keyboard.press(" ")
                keyboard.release(" ")

                for i in range(len(client.usermessageitemname)):
                    keyboard.press(client.usermessageitemname[i])
                    keyboard.release(client.usermessageitemname[i])

                keyboard.press(" ")
                keyboard.release(" ")

                for i in range(len(client.usermessagequantity)):
                    keyboard.press(client.usermessagequantity[i])
                    keyboard.release(client.usermessagequantity[i])

                keyboard.press(Key.enter)
                keyboard.release(Key.enter)


client.run(TOKEN)