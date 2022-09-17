from telethon import TelegramClient, events, sync
from telethon.tl.types import DocumentAttributeVideo

api_id = yourAPIIDInteger
api_hash = yourAPIhashString
client = TelegramClient('session_name', api_id, api_hash)
client.start()
ids=[]
firstnames=[]
lastnames=[]
usernames=[]
bots=[]
phones=[]
for u in client.iter_participants('FranTereveni', aggressive=True):
    ids.append(u.id)
    firstnames.append(u.first_name)
    lastnames.append(u.last_name)
    usernames.append(u.username)
    bots.append(u.bot)
    phones.append(u.phone)
print(len(bots))

allmessages=[]
for m in client.iter_messages('SkrypinUA', limit=50):
    allmessages.append(m)

import os
import pandas as pd
homefold="C:\\path"


df = pd.DataFrame()
df["First name"]=firstnames
df["Last name"]=lastnames
df["Username"]=usernames
df["ID"]=ids
df["Bot or human"]=bots
df["Phone"]=phones
df.to_excel(os.path.join(homefold,'FranTereveniUsers.xlsx'),index=False)

client.disconnect()