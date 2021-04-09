import discord
from discord.ext.commands import Bot
import random

def file_len():
    with open(r"C:\Users\recep\Desktop\sozler.txt") as f:
        for i, l in enumerate(f):
            pass
    return i + 1

sayi = file_len()


client = Bot("!db ") #duygusal bot'un kısaltması. String ifademizin sonunda boşluk bırakma sebebimiz, komutlarımızı girerken prefix değerimiz ile komutumuzun kolay okunabilmesidir.

@client.event
async def on_ready():
      print("Ben Hazırım!")

@client.command()
async def soz_al(msg):

    r_sayi = random.randint(0,sayi)
    print(r_sayi)

    f = open(r"C:\Users\recep\Desktop\sozler.txt","r")

    read = f.read()

    liste = read.split("-")

    eleman = liste[r_sayi]

    await msg.send(eleman)

client.run("TOKEN")