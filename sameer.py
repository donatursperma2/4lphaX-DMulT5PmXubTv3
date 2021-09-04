# Copyright (C) 2020 by DeadlyTeam@Github, < https://github.com/sameerpanthi/DEADLY-SPAM-BOT >.
#
# This file is part of < https://github.com/sameerpanthi/DEADLY-SPAM-BOT > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/sameerpanthi/DEADLY-SPAM-BOT >
#
# All rights reserved.
#
# Created by : https://t.me/AlphaXProject 
# Support by : https://t.me/CariTemanLink 
# Version : 3.1.0.0


import os
import sys
import random
from datetime import datetime
from os import execl
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.functions.account import UpdateProfileRequest
from Config import STRING, SUDO, BIO_MESSAGE, API_ID, API_HASH, STRING2, STRING3, STRING4 ,STRING5, STRING6, STRING7, STRING8 ,STRING9, STRING10, STRING11, STRING12, STRING13, STRING14, STRING15, STRING16, STRING17, STRING18, STRING19, STRING20, STRING21, STRING22, STRING23, STRING24, STRING25, STRING26, STRING27, STRING28, STRING29 ,STRING30, STRING31, STRING32, STRING33 ,STRING34, STRING35, STRING36, STRING37, STRING38, STRING39, STRING40, STRING41, STRING42, STRING43, STRING44, STRING45, STRING46, STRING47, STRING48, STRING49, STRING50, HEROKU_API_KEY, UPSTREAM_REPO, HEROKU_APP_NAME
import asyncio
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from Utils import RAID, RRAID
import git
import heroku3



a = API_ID
b = API_HASH
smex = STRING
smexx = STRING2
smexxx = STRING3
smexxxx = STRING4
smexxxxx = STRING5
sixth = STRING6
seven = STRING7
eight = STRING8
ninth = STRING9
tenth = STRING10
eleve = STRING11
twelv = STRING12
thirt = STRING13
forte = STRING14
fifth = STRING15
sieee = STRING16
seeee = STRING17
eieee = STRING18
nieee = STRING19
gandu = STRING20
ekish = STRING21
baish = STRING22
teish = STRING23
tfour = STRING24
tfive = STRING25
tsixt = STRING26
tseve = STRING27
teigh = STRING28
tnine = STRING29
trtty = STRING30
trone = STRING31
trtwo = STRING32
trtre = STRING33
trfrr = STRING34
trfiv = STRING35
trsix = STRING36
trsev = STRING37
treig = STRING38
trnin = STRING39
furth = STRING40
foron = STRING41
fortw = STRING42
fortr = STRING43
forfr = STRING44
forfv = STRING45
forsx = STRING46
forsv = STRING47
forig = STRING48
fornn = STRING49
fivty = STRING50


idk = ""
ydk = ""
wdk = ""
sdk = ""
hdk = ""
adk = ""
bdk = ""
cdk = ""
edk = ""
ddk = ""
vkk = ""
kkk = ""
lkk = ""
mkk = ""
sid = ""
shy = ""
aan = ""
ake = ""
eel = ""
khu = ""
shi = ""
yaa = ""
dav = ""
raj = ""
put = ""
tsi = ""
tsv = ""
teg = ""
tnn = ""
tth = ""
ton = ""
ttw = ""
ttr = ""
tfr = ""
tfv = ""
tsx = ""
tsv = ""
ttg = ""
ttn = ""
fft = ""
ffo = ""
ftw = ""
ftr = ""
ffr = ""
ffv = ""
fsx = ""
fsv = ""
feg = ""
fnn = ""
fvt = ""


que = {}

SMEX_USERS = []
for x in SUDO: 
    SMEX_USERS.append(x)
    
async def start_yukki():
    global idk
    global ydk
    global wdk
    global sdk
    global hdk
    global adk
    global bdk
    global cdk
    global ddk
    global edk
    global vkk
    global kkk
    global lkk
    global mkk
    global sid
    global shy
    global aan
    global ake
    global eel
    global khu
    global shi
    global yaa
    global dav
    global raj
    global put
    global tsi


    print("\n💥💥 BOT DEADLY ALPHA-X MULTI 5P4MX UBOT v3.1.0.0  IS STARTING... 💥💥💥\n")
    
    
    if smex:
        session_name = str(smex)
        print("String 1 Found")
        idk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 1")
            await idk.start()
            botme = await idk.get_me()
            await idk(functions.channels.JoinChannelRequest(channel="@caritemanlink"))
            await idk(functions.channels.JoinChannelRequest(channel="@cariteman1"))
            await idk(functions.channels.JoinChannelRequest(channel="@tgreceh"))
            await idk(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            idk = "smex"
            print(e)
            pass
    else:
        print("Session 1 not Found")
        session_name = "startup"
        idk = TelegramClient(session_name, a, b)
        try:
            await idk.start()
        except Exception as e:
            pass
   
    if smexx:
        session_name = str(smexx)
        print("String 2 Found")
        ydk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 2")
            await ydk.start()
            await ydk(functions.channels.JoinChannelRequest(channel="@caritemanlink"))
            await ydk(functions.channels.JoinChannelRequest(channel="@cariteman1"))
            await ydk(functions.channels.JoinChannelRequest(channel="@tgreceh"))
            await ydk(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
            botme = await ydk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 2 not Found")
        pass
        session_name = "startup"
        ydk = TelegramClient(session_name, a, b)
        try:
            await ydk.start()
        except Exception as e:
            pass

    if smexxx:
        session_name = str(smexxx)
        print("String 3 Found")
        wdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 3")
            await  wdk.start()
            await wdk(functions.channels.JoinChannelRequest(channel="@caritemanlink"))
            await wdk(functions.channels.JoinChannelRequest(channel="@cariteman1"))
            await wdk(functions.channels.JoinChannelRequest(channel="@tgreceh"))
            await wdk(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
            botme = await wdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 3 not Found")
        pass
        session_name = "startup"
        wdk = TelegramClient(session_name, a, b)
        try:
            await wdk.start()
        except Exception as e:
            pass

    if smexxxx:
        session_name = str(smexxxx)
        print("String 4 Found")
        hdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 4")
            await hdk.start()
            await hdk(functions.channels.JoinChannelRequest(channel="@caritemanlink"))
            await hdk(functions.channels.JoinChannelRequest(channel="@cariteman1"))
            await hdk(functions.channels.JoinChannelRequest(channel="@tgreceh"))
            await hdk(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
            botme = await hdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 4 not Found")
        pass
        session_name = "startup"
        hdk = TelegramClient(session_name, a, b)
        try:
            await hdk.start()
        except Exception as e:
            pass

    if smexxxxx:
        session_name = str(smexxxxx)
        print("String 5 Found")
        sdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 5")
            await sdk.start()
            await sdk(functions.channels.JoinChannelRequest(channel="@caritemanlink"))
            await sdk(functions.channels.JoinChannelRequest(channel="@cariteman1"))
            await sdk(functions.channels.JoinChannelRequest(channel="@tgreceh"))
            await sdk(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
            botme = await sdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 5 not Found")
        pass
        session_name = "startup"
        sdk = TelegramClient(session_name, a, b)
        try:
            await sdk.start()
        except Exception as e:
            pass
                  
    if sixth:
        session_name = str(sixth)
        print("String 6 Found")
        adk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 6")
            await adk.start()
            await adk(functions.channels.JoinChannelRequest(channel="@caritemanlink"))
            await adk(functions.channels.JoinChannelRequest(channel="@cariteman1"))
            await adk(functions.channels.JoinChannelRequest(channel="@tgreceh"))
            await adk(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
            botme = await adk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 6 not Found")
        pass
        session_name = "startup"
        adk = TelegramClient(session_name, a, b)
        try:
            await adk.start()
        except Exception as e:
            pass

    if seven:
        session_name = str(seven)
        print("String 7 Found")
        bdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 7")
            await bdk.start()
            await bdk(functions.channels.JoinChannelRequest(channel="@caritemanlink"))
            await bdk(functions.channels.JoinChannelRequest(channel="@cariteman1"))
            await bdk(functions.channels.JoinChannelRequest(channel="@tgreceh"))
            await bdk(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
            botme = await bdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 7 not Found")
        pass
        session_name = "startup"
        bdk = TelegramClient(session_name, a, b)
        try:
            await bdk.start()
        except Exception as e:
            pass    
        
    
    if eight:
        session_name = str(eight)
        print("String 8 Found")
        cdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 8")
            await cdk.start()
            await cdk(functions.channels.JoinChannelRequest(channel="@caritemanlink"))
            await cdk(functions.channels.JoinChannelRequest(channel="@cariteman1"))
            await cdk(functions.channels.JoinChannelRequest(channel="@tgreceh"))
            await cdk(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
            botme = await cdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 8 not Found")
        pass
        session_name = "startup"
        cdk = TelegramClient(session_name, a, b)
        try:
            await cdk.start()
        except Exception as e:
            pass   
        
    if ninth:
        session_name = str(ninth)
        print("String 9 Found")
        ddk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 9")
            await ddk.start()
            await ddk(functions.channels.JoinChannelRequest(channel="@caritemanlink"))
            await ddk(functions.channels.JoinChannelRequest(channel="@cariteman1"))
            await ddk(functions.channels.JoinChannelRequest(channel="@tgreceh"))
            await ddk(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
            botme = await ddk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 9 not Found")
        pass
        session_name = "startup"
        ddk = TelegramClient(session_name, a, b)
        try:
            await ddk.start()
        except Exception as e:
            pass   
    
  
    if tenth:
        session_name = str(tenth)
        print("String 10 Found")
        edk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 10")
            await edk.start()
            await edk(functions.channels.JoinChannelRequest(channel="@caritemanlink"))
            await edk(functions.channels.JoinChannelRequest(channel="@cariteman1"))
            await edk(functions.channels.JoinChannelRequest(channel="@tgreceh"))
            await edk(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
            botme = await edk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 10 not Found")
        pass
        session_name = "startup"
        edk = TelegramClient(session_name, a, b)
        try:
            await edk.start()
        except Exception as e:
            pass 
        
    
    if eleve:
        session_name = str(eleve)
        print("String 11 Found")
        vkk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 11")
            await vkk.start()
            await vkk(functions.channels.JoinChannelRequest(channel="@caritemanlink"))
            await vkk(functions.channels.JoinChannelRequest(channel="@cariteman1"))
            await vkk(functions.channels.JoinChannelRequest(channel="@tgreceh"))
            await vkk(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
            botme = await vkk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 11 not Found")
        pass
        session_name = "startup"
        vkk = TelegramClient(session_name, a, b)
        try:
            await vkk.start()
        except Exception as e:
            pass
        
    
    if twelv:
        session_name = str(twelv)
        print("String 12 Found")
        kkk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 12")
            await kkk.start()
            await kkk(functions.channels.JoinChannelRequest(channel="@caritemanlink"))
            await kkk(functions.channels.JoinChannelRequest(channel="@cariteman1"))
            await kkk(functions.channels.JoinChannelRequest(channel="@tgreceh"))
            await kkk(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
            botme = await kkk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 12 not Found")
        pass
        session_name = "startup"
        kkk = TelegramClient(session_name, a, b)
        try:
            await kkk.start()
        except Exception as e:
            pass   
    
  
    if thirt:
        session_name = str(thirt)
        print("String 13  Found")
        lkk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 13")
            await lkk.start()
            await lkk(functions.channels.JoinChannelRequest(channel="@caritemanlink"))
            await lkk(functions.channels.JoinChannelRequest(channel="@cariteman1"))
            await lkk(functions.channels.JoinChannelRequest(channel="@tgreceh"))
            await lkk(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
            botme = await lkk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 13 not Found")
        pass
        session_name = "startup"
        lkk = TelegramClient(session_name, a, b)
        try:
            await lkk.start()
        except Exception as e:
            pass 
        
    
    if forte:
        session_name = str(forte)
        print("String 14 Found")
        mkk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 14")
            await mkk.start()
            await mkk(functions.channels.JoinChannelRequest(channel="@caritemanlink"))
            await mkk(functions.channels.JoinChannelRequest(channel="@cariteman1"))
            await mkk(functions.channels.JoinChannelRequest(channel="@tgreceh"))
            await mkk(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
            botme = await mkk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 14 not Found")
        pass
        session_name = "startup"
        mkk = TelegramClient(session_name, a, b)
        try:
            await mkk.start()
        except Exception as e:
            pass
        
    
    if fifth:
        session_name = str(fifth)
        print("String 15 Found")
        sid = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 15")
            await sid.start()
            await sid(functions.channels.JoinChannelRequest(channel="@caritemanlink"))
            await sid(functions.channels.JoinChannelRequest(channel="@cariteman1"))
            await sid(functions.channels.JoinChannelRequest(channel="@tgreceh"))
            await sid(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
            botme = await sid.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 15 not Found")
        pass
        session_name = "startup"
        sid = TelegramClient(session_name, a, b)
        try:
            await sid.start()
        except Exception as e:
            pass


    if sieee:
        session_name = str(sieee)
        print("String 16 Found")
        shy = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 16")
            await shy.start()
            botme = await shy.get_me()
            await shy(functions.channels.JoinChannelRequest(channel="@caritemanlink"))
            await shy(functions.channels.JoinChannelRequest(channel="@cariteman1"))
            await shy(functions.channels.JoinChannelRequest(channel="@tgreceh"))
            await shy(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 16 not Found")
        session_name = "startup"
        shy = TelegramClient(session_name, a, b)
        try:
            await shy.start()
        except Exception as e:
            pass
   
    if seeee:
        session_name = str(seeee)
        print("String 17 Found")
        aan = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 17")
            await aan.start()
            botme = await aan.get_me()
            await aan(functions.channels.JoinChannelRequest(channel="@caritemanlink"))
            await aan(functions.channels.JoinChannelRequest(channel="@cariteman1"))
            await aan(functions.channels.JoinChannelRequest(channel="@tgreceh"))
            await aan(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 17 not Found")
        session_name = "startup"
        aan = TelegramClient(session_name, a, b)
        try:
            await aan.start()
        except Exception as e:
            pass
   
    if eieee:
        session_name = str(eieee)
        print("String 18 Found")
        ake = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 18")
            await ake.start()
            botme = await ake.get_me()
            await ake(functions.channels.JoinChannelRequest(channel="@caritemanlink"))
            await ake(functions.channels.JoinChannelRequest(channel="@cariteman1"))
            await ake(functions.channels.JoinChannelRequest(channel="@tgreceh"))
            await ake(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 18 not Found")
        session_name = "startup"
        ake = TelegramClient(session_name, a, b)
        try:
            await ake.start()
        except Exception as e:
            pass
   
    if nieee:
        session_name = str(nieee)
        print("String 19 Found")
        eel = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 19")
            await eel.start()
            botme = await eel.get_me()
            await eel(functions.channels.JoinChannelRequest(channel="@caritemanlink"))
            await eel(functions.channels.JoinChannelRequest(channel="@cariteman1"))
            await eel(functions.channels.JoinChannelRequest(channel="@tgreceh"))
            await eel(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 19 not Found")
        session_name = "startup"
        eel = TelegramClient(session_name, a, b)
        try:
            await eel.start()
        except Exception as e:
            pass
   
    if gandu:
        session_name = str(gandu)
        print("String 20 Found")
        khu = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 20")
            await khu.start()
            botme = await khu.get_me()
            await khu(functions.channels.JoinChannelRequest(channel="@caritemanlink"))
            await khu(functions.channels.JoinChannelRequest(channel="@cariteman1"))
            await khu(functions.channels.JoinChannelRequest(channel="@tgreceh"))
            await khu(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 20 not Found")
        session_name = "startup"
        khu = TelegramClient(session_name, a, b)
        try:
            await khu.start()
        except Exception as e:
            pass
   
    if ekish:
        session_name = str(ekish)
        print("String 21 Found")
        shi = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 21")
            await shi.start()
            botme = await shi.get_me()
            await shi(functions.channels.JoinChannelRequest(channel="@caritemanlink"))
            await shi(functions.channels.JoinChannelRequest(channel="@cariteman1"))
            await shi(functions.channels.JoinChannelRequest(channel="@tgreceh"))
            await shi(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 21 not Found")
        session_name = "startup"
        shi = TelegramClient(session_name, a, b)
        try:
            await shi.start()
        except Exception as e:
            pass
   
    if baish:
        session_name = str(baish)
        print("String 22 Found")
        yaa = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 22")
            await yaa.start()
            botme = await yaa.get_me()
            await yaa(functions.channels.JoinChannelRequest(channel="@caritemanlink"))
            await yaa(functions.channels.JoinChannelRequest(channel="@cariteman1"))
            await yaa(functions.channels.JoinChannelRequest(channel="@tgreceh"))
            await yaa(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 22 not Found")
        session_name = "startup"
        yaa = TelegramClient(session_name, a, b)
        try:
            await yaa.start()
        except Exception as e:
            pass
   
    if teish:
        session_name = str(teish)
        print("String 23 Found")
        dav = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 23")
            await dav.start()
            botme = await dav.get_me()
            await dav(functions.channels.JoinChannelRequest(channel="@caritemanlink"))
            await dav(functions.channels.JoinChannelRequest(channel="@cariteman1"))
            await dav(functions.channels.JoinChannelRequest(channel="@tgreceh"))
            await dav(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 23 not Found")
        session_name = "startup"
        dav = TelegramClient(session_name, a, b)
        try:
            await dav.start()
        except Exception as e:
            pass
   
    if tfour:
        session_name = str(tfour)
        print("String 24 Found")
        raj = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 24")
            await raj.start()
            botme = await raj.get_me()
            await raj(functions.channels.JoinChannelRequest(channel="@caritemanlink"))
            await raj(functions.channels.JoinChannelRequest(channel="@cariteman1"))
            await raj(functions.channels.JoinChannelRequest(channel="@tgreceh"))
            await raj(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 24 not Found")
        session_name = "startup"
        raj = TelegramClient(session_name, a, b)
        try:
            await raj.start()
        except Exception as e:
            pass
   
    if tfive:
        session_name = str(tfive)
        print("String 25 Found")
        put = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 25")
            await put.start()
            botme = await put.get_me()
            await put(functions.channels.JoinChannelRequest(channel="@caritemanlink"))
            await put(functions.channels.JoinChannelRequest(channel="@cariteman1"))
            await put(functions.channels.JoinChannelRequest(channel="@tgreceh"))
            await put(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 25 not Found")
        session_name = "startup"
        put = TelegramClient(session_name, a, b)
        try:
            await put.start()
        except Exception as e:
            pass

    if tsixt:
        session_name = str(tsixt)
        print("String 26 Found")
        tsi = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 26")
            await tsi.start()
            botme = await tsi.get_me()
            await tsi(functions.channels.JoinChannelRequest(channel="@caritemanlink"))
            await tsi(functions.channels.JoinChannelRequest(channel="@cariteman1"))
            await tsi(functions.channels.JoinChannelRequest(channel="@tgreceh"))
            await tsi(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 26 not Found")
        session_name = "startup"
        tsi = TelegramClient(session_name, a, b)
        try:
            await tsi.start()
        except Exception as e:
            pass
   
    if tseve:
        session_name = str(tseve)
        print("String 27 Found")
        tsv = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 27")
            await tsv.start()
            botme = await tsv.get_me()
            await tsv(functions.channels.JoinChannelRequest(channel="@caritemanlink"))
            await tsv(functions.channels.JoinChannelRequest(channel="@cariteman1"))
            await tsv(functions.channels.JoinChannelRequest(channel="@tgreceh"))
            await tsv(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 27 not Found")
        session_name = "startup"
        tsv = TelegramClient(session_name, a, b)
        try:
            await tsv.start()
        except Exception as e:
            pass
   
    if teigh:
        session_name = str(teigh)
        print("String 28 Found")
        teg = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 28")
            await teg.start()
            await teg(functions.channels.JoinChannelRequest(channel="@caritemanlink"))
            await teg(functions.channels.JoinChannelRequest(channel="@cariteman1"))
            await teg(functions.channels.JoinChannelRequest(channel="@tgreceh"))
            await teg(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
            botme = await teg.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 28 not Found")
        pass
        session_name = "startup"
        teg = TelegramClient(session_name, a, b)
        try:
            await teg.start()
        except Exception as e:
            pass

    if tnine:
        session_name = str(tnine)
        print("String 29 Found")
        tnn = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 29")
            await  tnn.start()
            await tnn(functions.channels.JoinChannelRequest(channel="@caritemanlink"))
            await tnn(functions.channels.JoinChannelRequest(channel="@cariteman1"))
            await tnn(functions.channels.JoinChannelRequest(channel="@tgreceh"))
            await tnn(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
            botme = await tnn.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 29 not Found")
        pass
        session_name = "startup"
        tnn = TelegramClient(session_name, a, b)
        try:
            await tnn.start()
        except Exception as e:
            pass

    if trtty:
        session_name = str(trtty)
        print("String 30 Found")
        tth = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 30")
            await tth.start()
            await tth(functions.channels.JoinChannelRequest(channel="@caritemanlink"))
            await tth(functions.channels.JoinChannelRequest(channel="@cariteman1"))
            await tth(functions.channels.JoinChannelRequest(channel="@tgreceh"))
            await tth(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
            botme = await tth.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 30 not Found")
        pass
        session_name = "startup"
        tth = TelegramClient(session_name, a, b)
        try:
            await tth.start()
        except Exception as e:
            pass

    if trone:
        session_name = str(trone)
        print("String 31 Found")
        ton = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 31")
            await ton.start()
            await ton(functions.channels.JoinChannelRequest(channel="@caritemanlink"))
            await ton(functions.channels.JoinChannelRequest(channel="@cariteman1"))
            await ton(functions.channels.JoinChannelRequest(channel="@tgreceh"))
            await ton(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
            botme = await ton.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 31 not Found")
        pass
        session_name = "startup"
        ton = TelegramClient(session_name, a, b)
        try:
            await ton.start()
        except Exception as e:
            pass
                  
    if trtwo:
        session_name = str(trtwo)
        print("String 32 Found")
        ttw = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 32")
            await ttw.start()
            await ttw(functions.channels.JoinChannelRequest(channel="@caritemanlink"))
            await ttw(functions.channels.JoinChannelRequest(channel="@cariteman1"))
            await ttw(functions.channels.JoinChannelRequest(channel="@tgreceh"))
            await ttw(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
            botme = await ttw.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 32 not Found")
        pass
        session_name = "startup"
        ttw = TelegramClient(session_name, a, b)
        try:
            await ttw.start()
        except Exception as e:
            pass

    if trtre:
        session_name = str(trtre)
        print("String 33 Found")
        ttr = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 33")
            await ttr.start()
            await ttr(functions.channels.JoinChannelRequest(channel="@caritemanlink"))
            await ttr(functions.channels.JoinChannelRequest(channel="@cariteman1"))
            await ttr(functions.channels.JoinChannelRequest(channel="@tgreceh"))
            await ttr(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
            botme = await ttr.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 33 not Found")
        pass
        session_name = "startup"
        ttr = TelegramClient(session_name, a, b)
        try:
            await ttr.start()
        except Exception as e:
            pass    
        
    
    if trfrr:
        session_name = str(trfrr)
        print("String 34 Found")
        tfr = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 34")
            await tfr.start()
            await tfr(functions.channels.JoinChannelRequest(channel="@caritemanlink"))
            await tfr(functions.channels.JoinChannelRequest(channel="@cariteman1"))
            await tfr(functions.channels.JoinChannelRequest(channel="@tgreceh"))
            await tfr(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
            botme = await tfr.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 34 not Found")
        pass
        session_name = "startup"
        tfr = TelegramClient(session_name, a, b)
        try:
            await tfr.start()
        except Exception as e:
            pass   
        
    if trfiv:
        session_name = str(trfiv)
        print("String 35 Found")
        tfv = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 35")
            await tfv.start()
            await tfv(functions.channels.JoinChannelRequest(channel="@caritemanlink"))
            await tfv(functions.channels.JoinChannelRequest(channel="@cariteman1"))
            await tfv(functions.channels.JoinChannelRequest(channel="@tgreceh"))
            await tfv(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
            botme = await tfv.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 35 not Found")
        pass
        session_name = "startup"
        tfv = TelegramClient(session_name, a, b)
        try:
            await tfv.start()
        except Exception as e:
            pass   
    
  
    if trsix:
        session_name = str(trsix)
        print("String 36 Found")
        tsx = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 36")
            await tsx.start()
            await tsx(functions.channels.JoinChannelRequest(channel="@caritemanlink"))
            await tsx(functions.channels.JoinChannelRequest(channel="@cariteman1"))
            await tsx(functions.channels.JoinChannelRequest(channel="@tgreceh"))
            await tsx(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
            botme = await tsx.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 36 not Found")
        pass
        session_name = "startup"
        tsx = TelegramClient(session_name, a, b)
        try:
            await tsx.start()
        except Exception as e:
            pass 
        
    
    if trsev:
        session_name = str(trsev)
        print("String 37 Found")
        vkk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 37")
            await vkk.start()
            await vkk(functions.channels.JoinChannelRequest(channel="@caritemanlink"))
            await vkk(functions.channels.JoinChannelRequest(channel="@cariteman1"))
            await vkk(functions.channels.JoinChannelRequest(channel="@tgreceh"))
            await vkk(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
            botme = await vkk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 37 not Found")
        pass
        session_name = "startup"
        vkk = TelegramClient(session_name, a, b)
        try:
            await vkk.start()
        except Exception as e:
            pass
        
    
    if treig:
        session_name = str(treig)
        print("String 38 Found")
        ttg = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 38")
            await ttg.start()
            await ttg(functions.channels.JoinChannelRequest(channel="@caritemanlink"))
            await ttg(functions.channels.JoinChannelRequest(channel="@cariteman1"))
            await ttg(functions.channels.JoinChannelRequest(channel="@tgreceh"))
            await ttg(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
            botme = await ttg.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 38 not Found")
        pass
        session_name = "startup"
        ttg = TelegramClient(session_name, a, b)
        try:
            await ttg.start()
        except Exception as e:
            pass   
    
  
    if trnin:
        session_name = str(trnin)
        print("String 39  Found")
        ttn = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 39")
            await ttn.start()
            await ttn(functions.channels.JoinChannelRequest(channel="@caritemanlink"))
            await ttn(functions.channels.JoinChannelRequest(channel="@cariteman1"))
            await ttn(functions.channels.JoinChannelRequest(channel="@tgreceh"))
            await ttn(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
            botme = await ttn.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 39 not Found")
        pass
        session_name = "startup"
        ttn = TelegramClient(session_name, a, b)
        try:
            await ttn.start()
        except Exception as e:
            pass 
        
    
    if furth:
        session_name = str(furth)
        print("String 40 Found")
        fft = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 40")
            await fft.start()
            await fft(functions.channels.JoinChannelRequest(channel="@caritemanlink"))
            await fft(functions.channels.JoinChannelRequest(channel="@cariteman1"))
            await fft(functions.channels.JoinChannelRequest(channel="@tgreceh"))
            await fft(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
            botme = await fft.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 40 not Found")
        pass
        session_name = "startup"
        fft = TelegramClient(session_name, a, b)
        try:
            await fft.start()
        except Exception as e:
            pass
        
    
    if foron:
        session_name = str(foron)
        print("String 41 Found")
        ffo = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 41")
            await ffo.start()
            await ffo(functions.channels.JoinChannelRequest(channel="@caritemanlink"))
            await ffo(functions.channels.JoinChannelRequest(channel="@cariteman1"))
            await ffo(functions.channels.JoinChannelRequest(channel="@tgreceh"))
            await ffo(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
            botme = await ffo.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 41 not Found")
        pass
        session_name = "startup"
        ffo = TelegramClient(session_name, a, b)
        try:
            await ffo.start()
        except Exception as e:
            pass


    if fortw:
        session_name = str(fortw)
        print("String 42 Found")
        ftw = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 42")
            await ftw.start()
            botme = await ftw.get_me()
            await ftw(functions.channels.JoinChannelRequest(channel="@caritemanlink"))
            await ftw(functions.channels.JoinChannelRequest(channel="@cariteman1"))
            await ftw(functions.channels.JoinChannelRequest(channel="@tgreceh"))
            await ftw(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 42 not Found")
        session_name = "startup"
        ftw = TelegramClient(session_name, a, b)
        try:
            await ftw.start()
        except Exception as e:
            pass
   
    if fortr:
        session_name = str(fortr)
        print("String 43 Found")
        ftr = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 43")
            await ftr.start()
            botme = await ftr.get_me()
            await ftr(functions.channels.JoinChannelRequest(channel="@caritemanlink"))
            await ftr(functions.channels.JoinChannelRequest(channel="@cariteman1"))
            await ftr(functions.channels.JoinChannelRequest(channel="@tgreceh"))
            await ftr(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 43 not Found")
        session_name = "startup"
        ftr = TelegramClient(session_name, a, b)
        try:
            await ftr.start()
        except Exception as e:
            pass
   
    if forfr:
        session_name = str(forfr)
        print("String 44 Found")
        ffr = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 44")
            await ffr.start()
            botme = await ffr.get_me()
            await ffr(functions.channels.JoinChannelRequest(channel="@caritemanlink"))
            await ffr(functions.channels.JoinChannelRequest(channel="@cariteman1"))
            await ffr(functions.channels.JoinChannelRequest(channel="@tgreceh"))
            await ffr(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 44 not Found")
        session_name = "startup"
        ffr = TelegramClient(session_name, a, b)
        try:
            await ffr.start()
        except Exception as e:
            pass
   
    if forfv:
        session_name = str(forfv)
        print("String 45 Found")
        ffv = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 45")
            await ffv.start()
            botme = await ffv.get_me()
            await ffv(functions.channels.JoinChannelRequest(channel="@caritemanlink"))
            await ffv(functions.channels.JoinChannelRequest(channel="@cariteman1"))
            await ffv(functions.channels.JoinChannelRequest(channel="@tgreceh"))
            await ffv(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 45 not Found")
        session_name = "startup"
        ffv = TelegramClient(session_name, a, b)
        try:
            await ffv.start()
        except Exception as e:
            pass
   
    if forsx:
        session_name = str(forsx)
        print("String 46 Found")
        fsx = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 46")
            await fsx.start()
            botme = await fsx.get_me()
            await fsx(functions.channels.JoinChannelRequest(channel="@caritemanlink"))
            await fsx(functions.channels.JoinChannelRequest(channel="@cariteman1"))
            await fsx(functions.channels.JoinChannelRequest(channel="@tgreceh"))
            await fsx(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 46 not Found")
        session_name = "startup"
        fsx = TelegramClient(session_name, a, b)
        try:
            await fsx.start()
        except Exception as e:
            pass
   
    if forsv:
        session_name = str(forsv)
        print("String 47 Found")
        fsv = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 47")
            await fsv.start()
            botme = await fsv.get_me()
            await fsv(functions.channels.JoinChannelRequest(channel="@caritemanlink"))
            await fsv(functions.channels.JoinChannelRequest(channel="@cariteman1"))
            await fsv(functions.channels.JoinChannelRequest(channel="@tgreceh"))
            await fsv(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 47 not Found")
        session_name = "startup"
        fsv = TelegramClient(session_name, a, b)
        try:
            await fsv.start()
        except Exception as e:
            pass
   
    if forig:
        session_name = str(forig)
        print("String 48 Found")
        feg = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 48")
            await feg.start()
            botme = await feg.get_me()
            await feg(functions.channels.JoinChannelRequest(channel="@caritemanlink"))
            await feg(functions.channels.JoinChannelRequest(channel="@cariteman1"))
            await feg(functions.channels.JoinChannelRequest(channel="@tgreceh"))
            await feg(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 48 not Found")
        session_name = "startup"
        feg = TelegramClient(session_name, a, b)
        try:
            await feg.start()
        except Exception as e:
            pass
   
    if fornn:
        session_name = str(fornn)
        print("String 49 Found")
        fnn = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 49")
            await fnn.start()
            botme = await fnn.get_me()
            await fnn(functions.channels.JoinChannelRequest(channel="@caritemanlink"))
            await fnn(functions.channels.JoinChannelRequest(channel="@cariteman1"))
            await fnn(functions.channels.JoinChannelRequest(channel="@tgreceh"))
            await fnn(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 49 not Found")
        session_name = "startup"
        fnn = TelegramClient(session_name, a, b)
        try:
            await fnn.start()
        except Exception as e:
            pass
   
    if fivty:
        session_name = str(fivty)
        print("String 50 Found")
        fvt = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 50")
            await fvt.start()
            botme = await fvt.get_me()
            await fvt(functions.channels.JoinChannelRequest(channel="@caritemanlink"))
            await fvt(functions.channels.JoinChannelRequest(channel="@cariteman1"))
            await fvt(functions.channels.JoinChannelRequest(channel="@tgreceh"))
            await fvt(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 50 not Found")
        session_name = "startup"
        fvt = TelegramClient(session_name, a, b)
        try:
            await fvt.start()
        except Exception as e:
            pass

   
loop = asyncio.get_event_loop()
loop.run_until_complete(start_yukki())       

async def gifspam(e, smex):
    try:
        await e.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=sandy.media.document.id,
                    access_hash=smex.media.document.access_hash,
                    file_reference=smex.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception as e:
        pass


# ======[BIO]======


@idk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@tsi.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@tsv.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@teg.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@tnn.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@tth.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@ton.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@ttw.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@ttr.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@tfr.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@tfv.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@tsx.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@tsv.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@ttg.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@ttn.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@fft.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@ffo.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@ftw.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@ftr.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@ffr.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@ffv.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@fsx.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@fsv.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@feg.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@fnn.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@fvt.on(events.NewMessage(incoming=True, pattern=r"\.bio"))

async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗕𝗶𝗼\n\nCommand:\n\n.bio <Message to set Bio of Userbot accounts>"
    if e.sender_id in SMEX_USERS:
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)     
        if len(e.text) > 5:
            bio = str(yukki[0])
            text = "Changing Bio"
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(functions.account.UpdateProfileRequest(about=bio))
                await event.edit("Succesfully Changed Bio By MULTI 5P4MXUBOT")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

# ======[JOIN]======
            
@idk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@tsi.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@tsv.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@teg.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@tnn.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@tth.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@ton.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@ttw.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@ttr.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@tfr.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@tfv.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@tsx.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@tsv.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@ttg.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@ttn.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@fft.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@ffo.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@ftw.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@ftr.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@ffr.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@ffv.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@fsx.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@fsv.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@feg.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@fnn.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@fvt.on(events.NewMessage(incoming=True, pattern=r"\.join"))

async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗝𝗼𝗶𝗻\n\nCommand:\n\n.join <Public Channel or Group Link/Username>"
    if e.sender_id in SMEX_USERS:
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 6:
            bc = yukki[0]
            text = "Joining..."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(functions.channels.JoinChannelRequest(channel=bc))
                await event.edit("Succesfully Joined")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

# ======[PJOIN]======
            
@idk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@tsi.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@tsv.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@teg.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@tnn.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@tth.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@ton.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@ttw.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@ttr.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@tfr.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@tfv.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@tsx.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@tsv.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@ttg.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@ttn.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@fft.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@ffo.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@ftw.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@ftr.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@ffr.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@ffv.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@fsx.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@fsv.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@feg.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@fnn.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@fvt.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))


async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗣𝗿𝗶𝘃𝗮𝘁𝗲 𝗝𝗼𝗶𝗻\n\nCommand:\n\n.pjoin <Private Channel or Group's access hash>\n\nExample :\nLink = https://t.me/joinchat/HGYs1wvsPUplMmM1\n\n.pjoin HGYs1wvsPUplMmM1"
    if e.sender_id in SMEX_USERS:
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = yukki[0]
            text = "Joining...."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(ImportChatInviteRequest(bc))
                await event.edit("Succesfully Joined")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
# ======[LEAVE]======
        
@idk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@tsi.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@tsv.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@teg.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@tnn.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@tth.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@ton.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@ttw.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@ttr.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@tfr.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@tfv.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@tsx.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@tsv.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@ttg.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@ttn.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@fft.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@ffo.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@ftw.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@ftr.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@ffr.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@ffv.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@fsx.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@fsv.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@feg.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@fnn.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@fvt.on(events.NewMessage(incoming=True, pattern=r"\.leave"))

async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗟𝗲𝗮𝘃𝗲\n\nCommand:\n\n.leave <Channel or Chat ID>"
    if e.sender_id in SMEX_USERS:
        ustad = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = ustad[0]
            bc = int(bc)
            text = "Leaving....."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await event.client(LeaveChannelRequest(bc))
                await event.edit("Succesfully Left")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

# ======[ALIVE]======            

USTAD_PIC = "https://telegra.ph/file/36eb117322594ce579f66.jpg"
@idk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@tsi.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@tsv.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@teg.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@tnn.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@tth.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@ton.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@ttw.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@ttr.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@tfr.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@tfv.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@tsx.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@tsv.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@ttg.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@ttn.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@fft.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@ffo.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@ftw.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@ftr.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@ffr.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@ffv.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@fsx.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@fsv.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@feg.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@fnn.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@fvt.on(events.NewMessage(incoming=True, pattern=r"\.alive"))

async def start(event):
    if event.sender_id in SMEX_USERS:
     await idk.send_file(event.chat_id, USTAD_PIC, caption="╭┈─╼━━━━━━━━━━━━━╾─┈ \n│ 𝐇𝐄𝐋𝐋𝐎 𝐌𝐘 𝐌𝐀𝐒𝐓𝐄𝐑 🔥\n│ 𝐈 𝐀𝐌 𝐀𝐋𝐈𝐕𝐄 🔥\n│ 𝐑𝐄𝐀𝐃𝐘 𝐓𝐎 𝐅𝐔𝐂𝐊 𝐘𝐎𝐔𝐑 𝐇𝐀𝐓𝐄𝐑𝐒 🔥\n├┈─╼━━━━━━━━━━━━━╾─┈  \n│ 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲 : \n│ ⚡️ 𝐀𝐋𝐏𝐇𝐀-𝐗𝐏𝐑𝐎𝐉𝐄𝐂𝐓  ͭ ͤ ͣ ͫ\n╰┈─────────────┈\n" )
     await ydk.send_file(event.chat_id, USTAD_PIC, caption="╭┈─╼━━━━━━━━━━━━━╾─┈ \n│ 𝐇𝐄𝐋𝐋𝐎 𝐌𝐘 𝐌𝐀𝐒𝐓𝐄𝐑 🔥\n│ 𝐈 𝐀𝐌 𝐀𝐋𝐈𝐕𝐄 🔥\n│ 𝐑𝐄𝐀𝐃𝐘 𝐓𝐎 𝐅𝐔𝐂𝐊 𝐘𝐎𝐔𝐑 𝐇𝐀𝐓𝐄𝐑𝐒 🔥\n├┈─╼━━━━━━━━━━━━━╾─┈  \n│ 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲 : \n│ ⚡️ 𝐀𝐋𝐏𝐇𝐀-𝐗𝐏𝐑𝐎𝐉𝐄𝐂𝐓  ͭ ͤ ͣ ͫ\n╰┈─────────────┈\n" )
     await wdk.send_file(event.chat_id, USTAD_PIC, caption="╭┈─╼━━━━━━━━━━━━━╾─┈ \n│ 𝐇𝐄𝐋𝐋𝐎 𝐌𝐘 𝐌𝐀𝐒𝐓𝐄𝐑 🔥\n│ 𝐈 𝐀𝐌 𝐀𝐋𝐈𝐕𝐄 🔥\n│ 𝐑𝐄𝐀𝐃𝐘 𝐓𝐎 𝐅𝐔𝐂𝐊 𝐘𝐎𝐔𝐑 𝐇𝐀𝐓𝐄𝐑𝐒 🔥\n├┈─╼━━━━━━━━━━━━━╾─┈  \n│ 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲 : \n│ ⚡️ 𝐀𝐋𝐏𝐇𝐀-𝐗𝐏𝐑𝐎𝐉𝐄𝐂𝐓  ͭ ͤ ͣ ͫ\n╰┈─────────────┈\n" )
     await hdk.send_file(event.chat_id, USTAD_PIC, caption="╭┈─╼━━━━━━━━━━━━━╾─┈ \n│ 𝐇𝐄𝐋𝐋𝐎 𝐌𝐘 𝐌𝐀𝐒𝐓𝐄𝐑 🔥\n│ 𝐈 𝐀𝐌 𝐀𝐋𝐈𝐕𝐄 🔥\n│ 𝐑𝐄𝐀𝐃𝐘 𝐓𝐎 𝐅𝐔𝐂𝐊 𝐘𝐎𝐔𝐑 𝐇𝐀𝐓𝐄𝐑𝐒 🔥\n├┈─╼━━━━━━━━━━━━━╾─┈  \n│ 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲 : \n│ ⚡️ 𝐀𝐋𝐏𝐇𝐀-𝐗𝐏𝐑𝐎𝐉𝐄𝐂𝐓  ͭ ͤ ͣ ͫ\n╰┈─────────────┈\n" )
     await sdk.send_file(event.chat_id, USTAD_PIC, caption="╭┈─╼━━━━━━━━━━━━━╾─┈ \n│ 𝐇𝐄𝐋𝐋𝐎 𝐌𝐘 𝐌𝐀𝐒𝐓𝐄𝐑 🔥\n│ 𝐈 𝐀𝐌 𝐀𝐋𝐈𝐕𝐄 🔥\n│ 𝐑𝐄𝐀𝐃𝐘 𝐓𝐎 𝐅𝐔𝐂𝐊 𝐘𝐎𝐔𝐑 𝐇𝐀𝐓𝐄𝐑𝐒 🔥\n├┈─╼━━━━━━━━━━━━━╾─┈  \n│ 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲 : \n│ ⚡️ 𝐀𝐋𝐏𝐇𝐀-𝐗𝐏𝐑𝐎𝐉𝐄𝐂𝐓  ͭ ͤ ͣ ͫ\n╰┈─────────────┈\n" )
     await adk.send_file(event.chat_id, USTAD_PIC, caption="╭┈─╼━━━━━━━━━━━━━╾─┈ \n│ 𝐇𝐄𝐋𝐋𝐎 𝐌𝐘 𝐌𝐀𝐒𝐓𝐄𝐑 🔥\n│ 𝐈 𝐀𝐌 𝐀𝐋𝐈𝐕𝐄 🔥\n│ 𝐑𝐄𝐀𝐃𝐘 𝐓𝐎 𝐅𝐔𝐂𝐊 𝐘𝐎𝐔𝐑 𝐇𝐀𝐓𝐄𝐑𝐒 🔥\n├┈─╼━━━━━━━━━━━━━╾─┈  \n│ 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲 : \n│ ⚡️ 𝐀𝐋𝐏𝐇𝐀-𝐗𝐏𝐑𝐎𝐉𝐄𝐂𝐓  ͭ ͤ ͣ ͫ\n╰┈─────────────┈\n" )
     await bdk.send_file(event.chat_id, USTAD_PIC, caption="╭┈─╼━━━━━━━━━━━━━╾─┈ \n│ 𝐇𝐄𝐋𝐋𝐎 𝐌𝐘 𝐌𝐀𝐒𝐓𝐄𝐑 🔥\n│ 𝐈 𝐀𝐌 𝐀𝐋𝐈𝐕𝐄 🔥\n│ 𝐑𝐄𝐀𝐃𝐘 𝐓𝐎 𝐅𝐔𝐂𝐊 𝐘𝐎𝐔𝐑 𝐇𝐀𝐓𝐄𝐑𝐒 🔥\n├┈─╼━━━━━━━━━━━━━╾─┈  \n│ 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲 : \n│ ⚡️ 𝐀𝐋𝐏𝐇𝐀-𝐗𝐏𝐑𝐎𝐉𝐄𝐂𝐓  ͭ ͤ ͣ ͫ\n╰┈─────────────┈\n" )
     await cdk.send_file(event.chat_id, USTAD_PIC, caption="╭┈─╼━━━━━━━━━━━━━╾─┈ \n│ 𝐇𝐄𝐋𝐋𝐎 𝐌𝐘 𝐌𝐀𝐒𝐓𝐄𝐑 🔥\n│ 𝐈 𝐀𝐌 𝐀𝐋𝐈𝐕𝐄 🔥\n│ 𝐑𝐄𝐀𝐃𝐘 𝐓𝐎 𝐅𝐔𝐂𝐊 𝐘𝐎𝐔𝐑 𝐇𝐀𝐓𝐄𝐑𝐒 🔥\n├┈─╼━━━━━━━━━━━━━╾─┈  \n│ 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲 : \n│ ⚡️ 𝐀𝐋𝐏𝐇𝐀-𝐗𝐏𝐑𝐎𝐉𝐄𝐂𝐓  ͭ ͤ ͣ ͫ\n╰┈─────────────┈\n" )
     await edk.send_file(event.chat_id, USTAD_PIC, caption="╭┈─╼━━━━━━━━━━━━━╾─┈ \n│ 𝐇𝐄𝐋𝐋𝐎 𝐌𝐘 𝐌𝐀𝐒𝐓𝐄𝐑 🔥\n│ 𝐈 𝐀𝐌 𝐀𝐋𝐈𝐕𝐄 🔥\n│ 𝐑𝐄𝐀𝐃𝐘 𝐓𝐎 𝐅𝐔𝐂𝐊 𝐘𝐎𝐔𝐑 𝐇𝐀𝐓𝐄𝐑𝐒 🔥\n├┈─╼━━━━━━━━━━━━━╾─┈  \n│ 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲 : \n│ ⚡️ 𝐀𝐋𝐏𝐇𝐀-𝐗𝐏𝐑𝐎𝐉𝐄𝐂𝐓  ͭ ͤ ͣ ͫ\n╰┈─────────────┈\n" )
     await ddk.send_file(event.chat_id, USTAD_PIC, caption="╭┈─╼━━━━━━━━━━━━━╾─┈ \n│ 𝐇𝐄𝐋𝐋𝐎 𝐌𝐘 𝐌𝐀𝐒𝐓𝐄𝐑 🔥\n│ 𝐈 𝐀𝐌 𝐀𝐋𝐈𝐕𝐄 🔥\n│ 𝐑𝐄𝐀𝐃𝐘 𝐓𝐎 𝐅𝐔𝐂𝐊 𝐘𝐎𝐔𝐑 𝐇𝐀𝐓𝐄𝐑𝐒 🔥\n├┈─╼━━━━━━━━━━━━━╾─┈  \n│ 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲 : \n│ ⚡️ 𝐀𝐋𝐏𝐇𝐀-𝐗𝐏𝐑𝐎𝐉𝐄𝐂𝐓  ͭ ͤ ͣ ͫ\n╰┈─────────────┈\n" )
     await vkk.send_file(event.chat_id, USTAD_PIC, caption="╭┈─╼━━━━━━━━━━━━━╾─┈ \n│ 𝐇𝐄𝐋𝐋𝐎 𝐌𝐘 𝐌𝐀𝐒𝐓𝐄𝐑 🔥\n│ 𝐈 𝐀𝐌 𝐀𝐋𝐈𝐕𝐄 🔥\n│ 𝐑𝐄𝐀𝐃𝐘 𝐓𝐎 𝐅𝐔𝐂𝐊 𝐘𝐎𝐔𝐑 𝐇𝐀𝐓𝐄𝐑𝐒 🔥\n├┈─╼━━━━━━━━━━━━━╾─┈  \n│ 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲 : \n│ ⚡️ 𝐀𝐋𝐏𝐇𝐀-𝐗𝐏𝐑𝐎𝐉𝐄𝐂𝐓  ͭ ͤ ͣ ͫ\n╰┈─────────────┈\n" )
     await kkk.send_file(event.chat_id, USTAD_PIC, caption="╭┈─╼━━━━━━━━━━━━━╾─┈ \n│ 𝐇𝐄𝐋𝐋𝐎 𝐌𝐘 𝐌𝐀𝐒𝐓𝐄𝐑 🔥\n│ 𝐈 𝐀𝐌 𝐀𝐋𝐈𝐕𝐄 🔥\n│ 𝐑𝐄𝐀𝐃𝐘 𝐓𝐎 𝐅𝐔𝐂𝐊 𝐘𝐎𝐔𝐑 𝐇𝐀𝐓𝐄𝐑𝐒 🔥\n├┈─╼━━━━━━━━━━━━━╾─┈  \n│ 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲 : \n│ ⚡️ 𝐀𝐋𝐏𝐇𝐀-𝐗𝐏𝐑𝐎𝐉𝐄𝐂𝐓  ͭ ͤ ͣ ͫ\n╰┈─────────────┈\n" )
     await lkk.send_file(event.chat_id, USTAD_PIC, caption="╭┈─╼━━━━━━━━━━━━━╾─┈ \n│ 𝐇𝐄𝐋𝐋𝐎 𝐌𝐘 𝐌𝐀𝐒𝐓𝐄𝐑 🔥\n│ 𝐈 𝐀𝐌 𝐀𝐋𝐈𝐕𝐄 🔥\n│ 𝐑𝐄𝐀𝐃𝐘 𝐓𝐎 𝐅𝐔𝐂𝐊 𝐘𝐎𝐔𝐑 𝐇𝐀𝐓𝐄𝐑𝐒 🔥\n├┈─╼━━━━━━━━━━━━━╾─┈  \n│ 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲 : \n│ ⚡️ 𝐀𝐋𝐏𝐇𝐀-𝐗𝐏𝐑𝐎𝐉𝐄𝐂𝐓  ͭ ͤ ͣ ͫ\n╰┈─────────────┈\n" )
     await mkk.send_file(event.chat_id, USTAD_PIC, caption="╭┈─╼━━━━━━━━━━━━━╾─┈ \n│ 𝐇𝐄𝐋𝐋𝐎 𝐌𝐘 𝐌𝐀𝐒𝐓𝐄𝐑 🔥\n│ 𝐈 𝐀𝐌 𝐀𝐋𝐈𝐕𝐄 🔥\n│ 𝐑𝐄𝐀𝐃𝐘 𝐓𝐎 𝐅𝐔𝐂𝐊 𝐘𝐎𝐔𝐑 𝐇𝐀𝐓𝐄𝐑𝐒 🔥\n├┈─╼━━━━━━━━━━━━━╾─┈  \n│ 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲 : \n│ ⚡️ 𝐀𝐋𝐏𝐇𝐀-𝐗𝐏𝐑𝐎𝐉𝐄𝐂𝐓  ͭ ͤ ͣ ͫ\n╰┈─────────────┈\n" )
     await sid.send_file(event.chat_id, USTAD_PIC, caption="╭┈─╼━━━━━━━━━━━━━╾─┈ \n│ 𝐇𝐄𝐋𝐋𝐎 𝐌𝐘 𝐌𝐀𝐒𝐓𝐄𝐑 🔥\n│ 𝐈 𝐀𝐌 𝐀𝐋𝐈𝐕𝐄 🔥\n│ 𝐑𝐄𝐀𝐃𝐘 𝐓𝐎 𝐅𝐔𝐂𝐊 𝐘𝐎𝐔𝐑 𝐇𝐀𝐓𝐄𝐑𝐒 🔥\n├┈─╼━━━━━━━━━━━━━╾─┈  \n│ 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲 : \n│ ⚡️ 𝐀𝐋𝐏𝐇𝐀-𝐗𝐏𝐑𝐎𝐉𝐄𝐂𝐓  ͭ ͤ ͣ ͫ\n╰┈─────────────┈\n" )
     await shy.send_file(event.chat_id, USTAD_PIC, caption="╭┈─╼━━━━━━━━━━━━━╾─┈ \n│ 𝐇𝐄𝐋𝐋𝐎 𝐌𝐘 𝐌𝐀𝐒𝐓𝐄𝐑 🔥\n│ 𝐈 𝐀𝐌 𝐀𝐋𝐈𝐕𝐄 🔥\n│ 𝐑𝐄𝐀𝐃𝐘 𝐓𝐎 𝐅𝐔𝐂𝐊 𝐘𝐎𝐔𝐑 𝐇𝐀𝐓𝐄𝐑𝐒 🔥\n├┈─╼━━━━━━━━━━━━━╾─┈  \n│ 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲 : \n│ ⚡️ 𝐀𝐋𝐏𝐇𝐀-𝐗𝐏𝐑𝐎𝐉𝐄𝐂𝐓  ͭ ͤ ͣ ͫ\n╰┈─────────────┈\n" )
     await aan.send_file(event.chat_id, USTAD_PIC, caption="╭┈─╼━━━━━━━━━━━━━╾─┈ \n│ 𝐇𝐄𝐋𝐋𝐎 𝐌𝐘 𝐌𝐀𝐒𝐓𝐄𝐑 🔥\n│ 𝐈 𝐀𝐌 𝐀𝐋𝐈𝐕𝐄 🔥\n│ 𝐑𝐄𝐀𝐃𝐘 𝐓𝐎 𝐅𝐔𝐂𝐊 𝐘𝐎𝐔𝐑 𝐇𝐀𝐓𝐄𝐑𝐒 🔥\n├┈─╼━━━━━━━━━━━━━╾─┈  \n│ 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲 : \n│ ⚡️ 𝐀𝐋𝐏𝐇𝐀-𝐗𝐏𝐑𝐎𝐉𝐄𝐂𝐓  ͭ ͤ ͣ ͫ\n╰┈─────────────┈\n" )
     await ake.send_file(event.chat_id, USTAD_PIC, caption="╭┈─╼━━━━━━━━━━━━━╾─┈ \n│ 𝐇𝐄𝐋𝐋𝐎 𝐌𝐘 𝐌𝐀𝐒𝐓𝐄𝐑 🔥\n│ 𝐈 𝐀𝐌 𝐀𝐋𝐈𝐕𝐄 🔥\n│ 𝐑𝐄𝐀𝐃𝐘 𝐓𝐎 𝐅𝐔𝐂𝐊 𝐘𝐎𝐔𝐑 𝐇𝐀𝐓𝐄𝐑𝐒 🔥\n├┈─╼━━━━━━━━━━━━━╾─┈  \n│ 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲 : \n│ ⚡️ 𝐀𝐋𝐏𝐇𝐀-𝐗𝐏𝐑𝐎𝐉𝐄𝐂𝐓  ͭ ͤ ͣ ͫ\n╰┈─────────────┈\n" )
     await eel.send_file(event.chat_id, USTAD_PIC, caption="╭┈─╼━━━━━━━━━━━━━╾─┈ \n│ 𝐇𝐄𝐋𝐋𝐎 𝐌𝐘 𝐌𝐀𝐒𝐓𝐄𝐑 🔥\n│ 𝐈 𝐀𝐌 𝐀𝐋𝐈𝐕𝐄 🔥\n│ 𝐑𝐄𝐀𝐃𝐘 𝐓𝐎 𝐅𝐔𝐂𝐊 𝐘𝐎𝐔𝐑 𝐇𝐀𝐓𝐄𝐑𝐒 🔥\n├┈─╼━━━━━━━━━━━━━╾─┈  \n│ 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲 : \n│ ⚡️ 𝐀𝐋𝐏𝐇𝐀-𝐗𝐏𝐑𝐎𝐉𝐄𝐂𝐓  ͭ ͤ ͣ ͫ\n╰┈─────────────┈\n" )
     await khu.send_file(event.chat_id, USTAD_PIC, caption="╭┈─╼━━━━━━━━━━━━━╾─┈ \n│ 𝐇𝐄𝐋𝐋𝐎 𝐌𝐘 𝐌𝐀𝐒𝐓𝐄𝐑 🔥\n│ 𝐈 𝐀𝐌 𝐀𝐋𝐈𝐕𝐄 🔥\n│ 𝐑𝐄𝐀𝐃𝐘 𝐓𝐎 𝐅𝐔𝐂𝐊 𝐘𝐎𝐔𝐑 𝐇𝐀𝐓𝐄𝐑𝐒 🔥\n├┈─╼━━━━━━━━━━━━━╾─┈  \n│ 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲 : \n│ ⚡️ 𝐀𝐋𝐏𝐇𝐀-𝐗𝐏𝐑𝐎𝐉𝐄𝐂𝐓  ͭ ͤ ͣ ͫ\n╰┈─────────────┈\n" )
     await shi.send_file(event.chat_id, USTAD_PIC, caption="╭┈─╼━━━━━━━━━━━━━╾─┈ \n│ 𝐇𝐄𝐋𝐋𝐎 𝐌𝐘 𝐌𝐀𝐒𝐓𝐄𝐑 🔥\n│ 𝐈 𝐀𝐌 𝐀𝐋𝐈𝐕𝐄 🔥\n│ 𝐑𝐄𝐀𝐃𝐘 𝐓𝐎 𝐅𝐔𝐂𝐊 𝐘𝐎𝐔𝐑 𝐇𝐀𝐓𝐄𝐑𝐒 🔥\n├┈─╼━━━━━━━━━━━━━╾─┈  \n│ 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲 : \n│ ⚡️ 𝐀𝐋𝐏𝐇𝐀-𝐗𝐏𝐑𝐎𝐉𝐄𝐂𝐓  ͭ ͤ ͣ ͫ\n╰┈─────────────┈\n" )
     await yaa.send_file(event.chat_id, USTAD_PIC, caption="╭┈─╼━━━━━━━━━━━━━╾─┈ \n│ 𝐇𝐄𝐋𝐋𝐎 𝐌𝐘 𝐌𝐀𝐒𝐓𝐄𝐑 🔥\n│ 𝐈 𝐀𝐌 𝐀𝐋𝐈𝐕𝐄 🔥\n│ 𝐑𝐄𝐀𝐃𝐘 𝐓𝐎 𝐅𝐔𝐂𝐊 𝐘𝐎𝐔𝐑 𝐇𝐀𝐓𝐄𝐑𝐒 🔥\n├┈─╼━━━━━━━━━━━━━╾─┈  \n│ 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲 : \n│ ⚡️ 𝐀𝐋𝐏𝐇𝐀-𝐗𝐏𝐑𝐎𝐉𝐄𝐂𝐓  ͭ ͤ ͣ ͫ\n╰┈─────────────┈\n" )
     await dav.send_file(event.chat_id, USTAD_PIC, caption="╭┈─╼━━━━━━━━━━━━━╾─┈ \n│ 𝐇𝐄𝐋𝐋𝐎 𝐌𝐘 𝐌𝐀𝐒𝐓𝐄𝐑 🔥\n│ 𝐈 𝐀𝐌 𝐀𝐋𝐈𝐕𝐄 🔥\n│ 𝐑𝐄𝐀𝐃𝐘 𝐓𝐎 𝐅𝐔𝐂𝐊 𝐘𝐎𝐔𝐑 𝐇𝐀𝐓𝐄𝐑𝐒 🔥\n├┈─╼━━━━━━━━━━━━━╾─┈  \n│ 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲 : \n│ ⚡️ 𝐀𝐋𝐏𝐇𝐀-𝐗𝐏𝐑𝐎𝐉𝐄𝐂𝐓  ͭ ͤ ͣ ͫ\n╰┈─────────────┈\n" )
     await raj.send_file(event.chat_id, USTAD_PIC, caption="╭┈─╼━━━━━━━━━━━━━╾─┈ \n│ 𝐇𝐄𝐋𝐋𝐎 𝐌𝐘 𝐌𝐀𝐒𝐓𝐄𝐑 🔥\n│ 𝐈 𝐀𝐌 𝐀𝐋𝐈𝐕𝐄 🔥\n│ 𝐑𝐄𝐀𝐃𝐘 𝐓𝐎 𝐅𝐔𝐂𝐊 𝐘𝐎𝐔𝐑 𝐇𝐀𝐓𝐄𝐑𝐒 🔥\n├┈─╼━━━━━━━━━━━━━╾─┈  \n│ 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲 : \n│ ⚡️ 𝐀𝐋𝐏𝐇𝐀-𝐗𝐏𝐑𝐎𝐉𝐄𝐂𝐓  ͭ ͤ ͣ ͫ\n╰┈─────────────┈\n" )
     await put.send_file(event.chat_id, USTAD_PIC, caption="╭┈─╼━━━━━━━━━━━━━╾─┈ \n│ 𝐇𝐄𝐋𝐋𝐎 𝐌𝐘 𝐌𝐀𝐒𝐓𝐄𝐑 🔥\n│ 𝐈 𝐀𝐌 𝐀𝐋𝐈𝐕𝐄 🔥\n│ 𝐑𝐄𝐀𝐃𝐘 𝐓𝐎 𝐅𝐔𝐂𝐊 𝐘𝐎𝐔𝐑 𝐇𝐀𝐓𝐄𝐑𝐒 🔥\n├┈─╼━━━━━━━━━━━━━╾─┈  \n│ 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲 : \n│ ⚡️ 𝐀𝐋𝐏𝐇𝐀-𝐗𝐏𝐑𝐎𝐉𝐄𝐂𝐓  ͭ ͤ ͣ ͫ\n╰┈─────────────┈\n" )   
     await tsi.send_file(event.chat_id, USTAD_PIC, caption="╭┈─╼━━━━━━━━━━━━━╾─┈ \n│ 𝐇𝐄𝐋𝐋𝐎 𝐌𝐘 𝐌𝐀𝐒𝐓𝐄𝐑 🔥\n│ 𝐈 𝐀𝐌 𝐀𝐋𝐈𝐕𝐄 🔥\n│ 𝐑𝐄𝐀𝐃𝐘 𝐓𝐎 𝐅𝐔𝐂𝐊 𝐘𝐎𝐔𝐑 𝐇𝐀𝐓𝐄𝐑𝐒 🔥\n├┈─╼━━━━━━━━━━━━━╾─┈  \n│ 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲 : \n│ ⚡️ 𝐀𝐋𝐏𝐇𝐀-𝐗𝐏𝐑𝐎𝐉𝐄𝐂𝐓  ͭ ͤ ͣ ͫ\n╰┈─────────────┈\n")
     await tsv.send_file(event.chat_id, USTAD_PIC, caption="╭┈─╼━━━━━━━━━━━━━╾─┈ \n│ 𝐇𝐄𝐋𝐋𝐎 𝐌𝐘 𝐌𝐀𝐒𝐓𝐄𝐑 🔥\n│ 𝐈 𝐀𝐌 𝐀𝐋𝐈𝐕𝐄 🔥\n│ 𝐑𝐄𝐀𝐃𝐘 𝐓𝐎 𝐅𝐔𝐂𝐊 𝐘𝐎𝐔𝐑 𝐇𝐀𝐓𝐄𝐑𝐒 🔥\n├┈─╼━━━━━━━━━━━━━╾─┈  \n│ 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲 : \n│ ⚡️ 𝐀𝐋𝐏𝐇𝐀-𝐗𝐏𝐑𝐎𝐉𝐄𝐂𝐓  ͭ ͤ ͣ ͫ\n╰┈─────────────┈\n" )
     await teg.send_file(event.chat_id, USTAD_PIC, caption="╭┈─╼━━━━━━━━━━━━━╾─┈ \n│ 𝐇𝐄𝐋𝐋𝐎 𝐌𝐘 𝐌𝐀𝐒𝐓𝐄𝐑 🔥\n│ 𝐈 𝐀𝐌 𝐀𝐋𝐈𝐕𝐄 🔥\n│ 𝐑𝐄𝐀𝐃𝐘 𝐓𝐎 𝐅𝐔𝐂𝐊 𝐘𝐎𝐔𝐑 𝐇𝐀𝐓𝐄𝐑𝐒 🔥\n├┈─╼━━━━━━━━━━━━━╾─┈  \n│ 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲 : \n│ ⚡️ 𝐀𝐋𝐏𝐇𝐀-𝐗𝐏𝐑𝐎𝐉𝐄𝐂𝐓  ͭ ͤ ͣ ͫ\n╰┈─────────────┈\n" )
     await tnn.send_file(event.chat_id, USTAD_PIC, caption="╭┈─╼━━━━━━━━━━━━━╾─┈ \n│ 𝐇𝐄𝐋𝐋𝐎 𝐌𝐘 𝐌𝐀𝐒𝐓𝐄𝐑 🔥\n│ 𝐈 𝐀𝐌 𝐀𝐋𝐈𝐕𝐄 🔥\n│ 𝐑𝐄𝐀𝐃𝐘 𝐓𝐎 𝐅𝐔𝐂𝐊 𝐘𝐎𝐔𝐑 𝐇𝐀𝐓𝐄𝐑𝐒 🔥\n├┈─╼━━━━━━━━━━━━━╾─┈  \n│ 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲 : \n│ ⚡️ 𝐀𝐋𝐏𝐇𝐀-𝐗𝐏𝐑𝐎𝐉𝐄𝐂𝐓  ͭ ͤ ͣ ͫ\n╰┈─────────────┈\n" )
     await tth.send_file(event.chat_id, USTAD_PIC, caption="╭┈─╼━━━━━━━━━━━━━╾─┈ \n│ 𝐇𝐄𝐋𝐋𝐎 𝐌𝐘 𝐌𝐀𝐒𝐓𝐄𝐑 🔥\n│ 𝐈 𝐀𝐌 𝐀𝐋𝐈𝐕𝐄 🔥\n│ 𝐑𝐄𝐀𝐃𝐘 𝐓𝐎 𝐅𝐔𝐂𝐊 𝐘𝐎𝐔𝐑 𝐇𝐀𝐓𝐄𝐑𝐒 🔥\n├┈─╼━━━━━━━━━━━━━╾─┈  \n│ 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲 : \n│ ⚡️ 𝐀𝐋𝐏𝐇𝐀-𝐗𝐏𝐑𝐎𝐉𝐄𝐂𝐓  ͭ ͤ ͣ ͫ\n╰┈─────────────┈\n" )
     await ton.send_file(event.chat_id, USTAD_PIC, caption="╭┈─╼━━━━━━━━━━━━━╾─┈ \n│ 𝐇𝐄𝐋𝐋𝐎 𝐌𝐘 𝐌𝐀𝐒𝐓𝐄𝐑 🔥\n│ 𝐈 𝐀𝐌 𝐀𝐋𝐈𝐕𝐄 🔥\n│ 𝐑𝐄𝐀𝐃𝐘 𝐓𝐎 𝐅𝐔𝐂𝐊 𝐘𝐎𝐔𝐑 𝐇𝐀𝐓𝐄𝐑𝐒 🔥\n├┈─╼━━━━━━━━━━━━━╾─┈  \n│ 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲 : \n│ ⚡️ 𝐀𝐋𝐏𝐇𝐀-𝐗𝐏𝐑𝐎𝐉𝐄𝐂𝐓  ͭ ͤ ͣ ͫ\n╰┈─────────────┈\n" )
     await ttw.send_file(event.chat_id, USTAD_PIC, caption="╭┈─╼━━━━━━━━━━━━━╾─┈ \n│ 𝐇𝐄𝐋𝐋𝐎 𝐌𝐘 𝐌𝐀𝐒𝐓𝐄𝐑 🔥\n│ 𝐈 𝐀𝐌 𝐀𝐋𝐈𝐕𝐄 🔥\n│ 𝐑𝐄𝐀𝐃𝐘 𝐓𝐎 𝐅𝐔𝐂𝐊 𝐘𝐎𝐔𝐑 𝐇𝐀𝐓𝐄𝐑𝐒 🔥\n├┈─╼━━━━━━━━━━━━━╾─┈  \n│ 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲 : \n│ ⚡️ 𝐀𝐋𝐏𝐇𝐀-𝐗𝐏𝐑𝐎𝐉𝐄𝐂𝐓  ͭ ͤ ͣ ͫ\n╰┈─────────────┈\n" )
     await ttr.send_file(event.chat_id, USTAD_PIC, caption="╭┈─╼━━━━━━━━━━━━━╾─┈ \n│ 𝐇𝐄𝐋𝐋𝐎 𝐌𝐘 𝐌𝐀𝐒𝐓𝐄𝐑 🔥\n│ 𝐈 𝐀𝐌 𝐀𝐋𝐈𝐕𝐄 🔥\n│ 𝐑𝐄𝐀𝐃𝐘 𝐓𝐎 𝐅𝐔𝐂𝐊 𝐘𝐎𝐔𝐑 𝐇𝐀𝐓𝐄𝐑𝐒 🔥\n├┈─╼━━━━━━━━━━━━━╾─┈  \n│ 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲 : \n│ ⚡️ 𝐀𝐋𝐏𝐇𝐀-𝐗𝐏𝐑𝐎𝐉𝐄𝐂𝐓  ͭ ͤ ͣ ͫ\n╰┈─────────────┈\n" )
     await tfr.send_file(event.chat_id, USTAD_PIC, caption="╭┈─╼━━━━━━━━━━━━━╾─┈ \n│ 𝐇𝐄𝐋𝐋𝐎 𝐌𝐘 𝐌𝐀𝐒𝐓𝐄𝐑 🔥\n│ 𝐈 𝐀𝐌 𝐀𝐋𝐈𝐕𝐄 🔥\n│ 𝐑𝐄𝐀𝐃𝐘 𝐓𝐎 𝐅𝐔𝐂𝐊 𝐘𝐎𝐔𝐑 𝐇𝐀𝐓𝐄𝐑𝐒 🔥\n├┈─╼━━━━━━━━━━━━━╾─┈  \n│ 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲 : \n│ ⚡️ 𝐀𝐋𝐏𝐇𝐀-𝐗𝐏𝐑𝐎𝐉𝐄𝐂𝐓  ͭ ͤ ͣ ͫ\n╰┈─────────────┈\n" )
     await tfv.send_file(event.chat_id, USTAD_PIC, caption="╭┈─╼━━━━━━━━━━━━━╾─┈ \n│ 𝐇𝐄𝐋𝐋𝐎 𝐌𝐘 𝐌𝐀𝐒𝐓𝐄𝐑 🔥\n│ 𝐈 𝐀𝐌 𝐀𝐋𝐈𝐕𝐄 🔥\n│ 𝐑𝐄𝐀𝐃𝐘 𝐓𝐎 𝐅𝐔𝐂𝐊 𝐘𝐎𝐔𝐑 𝐇𝐀𝐓𝐄𝐑𝐒 🔥\n├┈─╼━━━━━━━━━━━━━╾─┈  \n│ 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲 : \n│ ⚡️ 𝐀𝐋𝐏𝐇𝐀-𝐗𝐏𝐑𝐎𝐉𝐄𝐂𝐓  ͭ ͤ ͣ ͫ\n╰┈─────────────┈\n" )
     await tsx.send_file(event.chat_id, USTAD_PIC, caption="╭┈─╼━━━━━━━━━━━━━╾─┈ \n│ 𝐇𝐄𝐋𝐋𝐎 𝐌𝐘 𝐌𝐀𝐒𝐓𝐄𝐑 🔥\n│ 𝐈 𝐀𝐌 𝐀𝐋𝐈𝐕𝐄 🔥\n│ 𝐑𝐄𝐀𝐃𝐘 𝐓𝐎 𝐅𝐔𝐂𝐊 𝐘𝐎𝐔𝐑 𝐇𝐀𝐓𝐄𝐑𝐒 🔥\n├┈─╼━━━━━━━━━━━━━╾─┈  \n│ 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲 : \n│ ⚡️ 𝐀𝐋𝐏𝐇𝐀-𝐗𝐏𝐑𝐎𝐉𝐄𝐂𝐓  ͭ ͤ ͣ ͫ\n╰┈─────────────┈\n" )
     await tsv.send_file(event.chat_id, USTAD_PIC, caption="╭┈─╼━━━━━━━━━━━━━╾─┈ \n│ 𝐇𝐄𝐋𝐋𝐎 𝐌𝐘 𝐌𝐀𝐒𝐓𝐄𝐑 🔥\n│ 𝐈 𝐀𝐌 𝐀𝐋𝐈𝐕𝐄 🔥\n│ 𝐑𝐄𝐀𝐃𝐘 𝐓𝐎 𝐅𝐔𝐂𝐊 𝐘𝐎𝐔𝐑 𝐇𝐀𝐓𝐄𝐑𝐒 🔥\n├┈─╼━━━━━━━━━━━━━╾─┈  \n│ 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲 : \n│ ⚡️ 𝐀𝐋𝐏𝐇𝐀-𝐗𝐏𝐑𝐎𝐉𝐄𝐂𝐓  ͭ ͤ ͣ ͫ\n╰┈─────────────┈\n" )
     await ttg.send_file(event.chat_id, USTAD_PIC, caption="╭┈─╼━━━━━━━━━━━━━╾─┈ \n│ 𝐇𝐄𝐋𝐋𝐎 𝐌𝐘 𝐌𝐀𝐒𝐓𝐄𝐑 🔥\n│ 𝐈 𝐀𝐌 𝐀𝐋𝐈𝐕𝐄 🔥\n│ 𝐑𝐄𝐀𝐃𝐘 𝐓𝐎 𝐅𝐔𝐂𝐊 𝐘𝐎𝐔𝐑 𝐇𝐀𝐓𝐄𝐑𝐒 🔥\n├┈─╼━━━━━━━━━━━━━╾─┈  \n│ 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲 : \n│ ⚡️ 𝐀𝐋𝐏𝐇𝐀-𝐗𝐏𝐑𝐎𝐉𝐄𝐂𝐓  ͭ ͤ ͣ ͫ\n╰┈─────────────┈\n" )
     await ttn.send_file(event.chat_id, USTAD_PIC, caption="╭┈─╼━━━━━━━━━━━━━╾─┈ \n│ 𝐇𝐄𝐋𝐋𝐎 𝐌𝐘 𝐌𝐀𝐒𝐓𝐄𝐑 🔥\n│ 𝐈 𝐀𝐌 𝐀𝐋𝐈𝐕𝐄 🔥\n│ 𝐑𝐄𝐀𝐃𝐘 𝐓𝐎 𝐅𝐔𝐂𝐊 𝐘𝐎𝐔𝐑 𝐇𝐀𝐓𝐄𝐑𝐒 🔥\n├┈─╼━━━━━━━━━━━━━╾─┈  \n│ 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲 : \n│ ⚡️ 𝐀𝐋𝐏𝐇𝐀-𝐗𝐏𝐑𝐎𝐉𝐄𝐂𝐓  ͭ ͤ ͣ ͫ\n╰┈─────────────┈\n" )
     await fft.send_file(event.chat_id, USTAD_PIC, caption="╭┈─╼━━━━━━━━━━━━━╾─┈ \n│ 𝐇𝐄𝐋𝐋𝐎 𝐌𝐘 𝐌𝐀𝐒𝐓𝐄𝐑 🔥\n│ 𝐈 𝐀𝐌 𝐀𝐋𝐈𝐕𝐄 🔥\n│ 𝐑𝐄𝐀𝐃𝐘 𝐓𝐎 𝐅𝐔𝐂𝐊 𝐘𝐎𝐔𝐑 𝐇𝐀𝐓𝐄𝐑𝐒 🔥\n├┈─╼━━━━━━━━━━━━━╾─┈  \n│ 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲 : \n│ ⚡️ 𝐀𝐋𝐏𝐇𝐀-𝐗𝐏𝐑𝐎𝐉𝐄𝐂𝐓  ͭ ͤ ͣ ͫ\n╰┈─────────────┈\n" )
     await ffo.send_file(event.chat_id, USTAD_PIC, caption="╭┈─╼━━━━━━━━━━━━━╾─┈ \n│ 𝐇𝐄𝐋𝐋𝐎 𝐌𝐘 𝐌𝐀𝐒𝐓𝐄𝐑 🔥\n│ 𝐈 𝐀𝐌 𝐀𝐋𝐈𝐕𝐄 🔥\n│ 𝐑𝐄𝐀𝐃𝐘 𝐓𝐎 𝐅𝐔𝐂𝐊 𝐘𝐎𝐔𝐑 𝐇𝐀𝐓𝐄𝐑𝐒 🔥\n├┈─╼━━━━━━━━━━━━━╾─┈  \n│ 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲 : \n│ ⚡️ 𝐀𝐋𝐏𝐇𝐀-𝐗𝐏𝐑𝐎𝐉𝐄𝐂𝐓  ͭ ͤ ͣ ͫ\n╰┈─────────────┈\n" )
     await ftw.send_file(event.chat_id, USTAD_PIC, caption="╭┈─╼━━━━━━━━━━━━━╾─┈ \n│ 𝐇𝐄𝐋𝐋𝐎 𝐌𝐘 𝐌𝐀𝐒𝐓𝐄𝐑 🔥\n│ 𝐈 𝐀𝐌 𝐀𝐋𝐈𝐕𝐄 🔥\n│ 𝐑𝐄𝐀𝐃𝐘 𝐓𝐎 𝐅𝐔𝐂𝐊 𝐘𝐎𝐔𝐑 𝐇𝐀𝐓𝐄𝐑𝐒 🔥\n├┈─╼━━━━━━━━━━━━━╾─┈  \n│ 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲 : \n│ ⚡️ 𝐀𝐋𝐏𝐇𝐀-𝐗𝐏𝐑𝐎𝐉𝐄𝐂𝐓  ͭ ͤ ͣ ͫ\n╰┈─────────────┈\n" )
     await ftr.send_file(event.chat_id, USTAD_PIC, caption="╭┈─╼━━━━━━━━━━━━━╾─┈ \n│ 𝐇𝐄𝐋𝐋𝐎 𝐌𝐘 𝐌𝐀𝐒𝐓𝐄𝐑 🔥\n│ 𝐈 𝐀𝐌 𝐀𝐋𝐈𝐕𝐄 🔥\n│ 𝐑𝐄𝐀𝐃𝐘 𝐓𝐎 𝐅𝐔𝐂𝐊 𝐘𝐎𝐔𝐑 𝐇𝐀𝐓𝐄𝐑𝐒 🔥\n├┈─╼━━━━━━━━━━━━━╾─┈  \n│ 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲 : \n│ ⚡️ 𝐀𝐋𝐏𝐇𝐀-𝐗𝐏𝐑𝐎𝐉𝐄𝐂𝐓  ͭ ͤ ͣ ͫ\n╰┈─────────────┈\n" )
     await ffr.send_file(event.chat_id, USTAD_PIC, caption="╭┈─╼━━━━━━━━━━━━━╾─┈ \n│ 𝐇𝐄𝐋𝐋𝐎 𝐌𝐘 𝐌𝐀𝐒𝐓𝐄𝐑 🔥\n│ 𝐈 𝐀𝐌 𝐀𝐋𝐈𝐕𝐄 🔥\n│ 𝐑𝐄𝐀𝐃𝐘 𝐓𝐎 𝐅𝐔𝐂𝐊 𝐘𝐎𝐔𝐑 𝐇𝐀𝐓𝐄𝐑𝐒 🔥\n├┈─╼━━━━━━━━━━━━━╾─┈  \n│ 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲 : \n│ ⚡️ 𝐀𝐋𝐏𝐇𝐀-𝐗𝐏𝐑𝐎𝐉𝐄𝐂𝐓  ͭ ͤ ͣ ͫ\n╰┈─────────────┈\n" )
     await ffv.send_file(event.chat_id, USTAD_PIC, caption="╭┈─╼━━━━━━━━━━━━━╾─┈ \n│ 𝐇𝐄𝐋𝐋𝐎 𝐌𝐘 𝐌𝐀𝐒𝐓𝐄𝐑 🔥\n│ 𝐈 𝐀𝐌 𝐀𝐋𝐈𝐕𝐄 🔥\n│ 𝐑𝐄𝐀𝐃𝐘 𝐓𝐎 𝐅𝐔𝐂𝐊 𝐘𝐎𝐔𝐑 𝐇𝐀𝐓𝐄𝐑𝐒 🔥\n├┈─╼━━━━━━━━━━━━━╾─┈  \n│ 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲 : \n│ ⚡️ 𝐀𝐋𝐏𝐇𝐀-𝐗𝐏𝐑𝐎𝐉𝐄𝐂𝐓  ͭ ͤ ͣ ͫ\n╰┈─────────────┈\n" )
     await fsx.send_file(event.chat_id, USTAD_PIC, caption="╭┈─╼━━━━━━━━━━━━━╾─┈ \n│ 𝐇𝐄𝐋𝐋𝐎 𝐌𝐘 𝐌𝐀𝐒𝐓𝐄𝐑 🔥\n│ 𝐈 𝐀𝐌 𝐀𝐋𝐈𝐕𝐄 🔥\n│ 𝐑𝐄𝐀𝐃𝐘 𝐓𝐎 𝐅𝐔𝐂𝐊 𝐘𝐎𝐔𝐑 𝐇𝐀𝐓𝐄𝐑𝐒 🔥\n├┈─╼━━━━━━━━━━━━━╾─┈  \n│ 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲 : \n│ ⚡️ 𝐀𝐋𝐏𝐇𝐀-𝐗𝐏𝐑𝐎𝐉𝐄𝐂𝐓  ͭ ͤ ͣ ͫ\n╰┈─────────────┈\n" )
     await fsv.send_file(event.chat_id, USTAD_PIC, caption="╭┈─╼━━━━━━━━━━━━━╾─┈ \n│ 𝐇𝐄𝐋𝐋𝐎 𝐌𝐘 𝐌𝐀𝐒𝐓𝐄𝐑 🔥\n│ 𝐈 𝐀𝐌 𝐀𝐋𝐈𝐕𝐄 🔥\n│ 𝐑𝐄𝐀𝐃𝐘 𝐓𝐎 𝐅𝐔𝐂𝐊 𝐘𝐎𝐔𝐑 𝐇𝐀𝐓𝐄𝐑𝐒 🔥\n├┈─╼━━━━━━━━━━━━━╾─┈  \n│ 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲 : \n│ ⚡️ 𝐀𝐋𝐏𝐇𝐀-𝐗𝐏𝐑𝐎𝐉𝐄𝐂𝐓  ͭ ͤ ͣ ͫ\n╰┈─────────────┈\n" )
     await feg.send_file(event.chat_id, USTAD_PIC, caption="╭┈─╼━━━━━━━━━━━━━╾─┈ \n│ 𝐇𝐄𝐋𝐋𝐎 𝐌𝐘 𝐌𝐀𝐒𝐓𝐄𝐑 🔥\n│ 𝐈 𝐀𝐌 𝐀𝐋𝐈𝐕𝐄 🔥\n│ 𝐑𝐄𝐀𝐃𝐘 𝐓𝐎 𝐅𝐔𝐂𝐊 𝐘𝐎𝐔𝐑 𝐇𝐀𝐓𝐄𝐑𝐒 🔥\n├┈─╼━━━━━━━━━━━━━╾─┈  \n│ 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲 : \n│ ⚡️ 𝐀𝐋𝐏𝐇𝐀-𝐗𝐏𝐑𝐎𝐉𝐄𝐂𝐓  ͭ ͤ ͣ ͫ\n╰┈─────────────┈\n" )
     await fnn.send_file(event.chat_id, USTAD_PIC, caption="╭┈─╼━━━━━━━━━━━━━╾─┈ \n│ 𝐇𝐄𝐋𝐋𝐎 𝐌𝐘 𝐌𝐀𝐒𝐓𝐄𝐑 🔥\n│ 𝐈 𝐀𝐌 𝐀𝐋𝐈𝐕𝐄 🔥\n│ 𝐑𝐄𝐀𝐃𝐘 𝐓𝐎 𝐅𝐔𝐂𝐊 𝐘𝐎𝐔𝐑 𝐇𝐀𝐓𝐄𝐑𝐒 🔥\n├┈─╼━━━━━━━━━━━━━╾─┈  \n│ 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲 : \n│ ⚡️ 𝐀𝐋𝐏𝐇𝐀-𝐗𝐏𝐑𝐎𝐉𝐄𝐂𝐓  ͭ ͤ ͣ ͫ\n╰┈─────────────┈\n" )
     await fvt.send_file(event.chat_id, USTAD_PIC, caption="╭┈─╼━━━━━━━━━━━━━╾─┈ \n│ 𝐇𝐄𝐋𝐋𝐎 𝐌𝐘 𝐌𝐀𝐒𝐓𝐄𝐑 🔥\n│ 𝐈 𝐀𝐌 𝐀𝐋𝐈𝐕𝐄 🔥\n│ 𝐑𝐄𝐀𝐃𝐘 𝐓𝐎 𝐅𝐔𝐂𝐊 𝐘𝐎𝐔𝐑 𝐇𝐀𝐓𝐄𝐑𝐒 🔥\n├┈─╼━━━━━━━━━━━━━╾─┈  \n│ 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲 : \n│ ⚡️ 𝐀𝐋𝐏𝐇𝐀-𝐗𝐏𝐑𝐎𝐉𝐄𝐂𝐓  ͭ ͤ ͣ ͫ\n╰┈─────────────┈\n" )

# ======[SPAM]======    
        
@idk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@tsi.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@tsv.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@teg.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@tnn.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@tth.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@ton.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@ttw.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@ttr.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@tfr.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@tfv.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@tsx.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@tsv.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@ttg.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@ttn.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@fft.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@ffo.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@ftw.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@ftr.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@ffr.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@ffv.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@fsx.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@fsv.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@feg.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@fnn.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@fvt.on(events.NewMessage(incoming=True, pattern=r"\.spam"))

async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗦𝗽𝗮𝗺\n\nCommand:\n\n.spam <count> <message to spam>\n\n.spam <count> <reply to a message>\n\nCount must be a integer."
    error = "Spam Module can only be used till 100 count. For bigger spams use BigSpam."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(yukki) == 2:
            message = str(yukki[1])
            counter = int(yukki[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None )
            await asyncio.wait([e.respond(message) for i in range(counter)])
        elif e.reply_to_msg_id and smex.media:  
            counter = int(yukki[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None )
            for _ in range(counter):
                smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                await gifspam(e, smex)  
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(yukki[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None )
            await asyncio.wait([e.respond(message) for i in range(counter)])
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
# ======[DELAYSPAM]======    

@idk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@tsi.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@tsv.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@teg.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@tnn.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@tth.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@ton.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@ttw.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@ttr.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@tfr.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@tfv.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@tsx.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@tsv.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@ttg.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@ttn.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@fft.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@ffo.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@ftw.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@ftr.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@ffr.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@ffv.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@fsx.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@fsv.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@feg.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@fnn.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@fvt.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))

async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗹𝗮𝘆𝗦𝗽𝗮𝗺\n\nCommand:\n\n.delayspam <sleep time> <count> <message to spam>\n\n.delayspam <sleep time> <count> <reply to a message>\n\nCount and Sleeptime must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        smex = await e.get_reply_message()
        yukki = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
        yukkisexy = yukki[1:]
        if len(yukkisexy) == 2:
            message = str(yukkisexy[1])
            counter = int(yukkisexy[0])
            sleeptime = float(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.media:  
            counter = int(yukkisexy[0])
            sleeptime = float(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex) 
                await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(yukkisexy[0])
            sleeptime = float(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

# ======[BIGSPAM]======    

@idk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@tsi.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@tsv.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@teg.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@tnn.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@tth.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@ton.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@ttw.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@ttr.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@tfr.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@tfv.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@tsx.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@tsv.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@ttg.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@ttn.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@fft.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@ffo.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@ftw.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@ftr.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@ffr.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@ffv.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@fsx.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@fsv.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@feg.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@fnn.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@fvt.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))

async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗕𝗶𝗴𝗦𝗽𝗮𝗺\n\nCommand:\n\n.bigspam <count> <message to spam>\n\n.bigspam <count> <reply to a message>\n\nCount must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(yukki) == 2:
            message = str(yukki[1])
            counter = int(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.1)
        elif e.reply_to_msg_id and smex.media:  
            counter = int(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex) 
                await asyncio.sleep(0.1)  
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

# ======[RAID]======

@idk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@tsi.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@tsv.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@teg.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@tnn.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@tth.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@ton.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@ttw.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@ttr.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@tfr.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@tfv.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@tsx.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@tsv.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@ttg.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@ttn.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@fft.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@ffo.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@ftw.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@ftr.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@ffr.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@ffv.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@fsx.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@fsv.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@feg.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@fnn.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@fvt.on(events.NewMessage(incoming=True, pattern=r"\.raid"))

async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗮𝗶𝗱\n\nCommand:\n\n.raid <count> <Username of User>\n\n.raid <count> <reply to a User>\n\nCount must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(yukki) == 2:
            message = str(yukki[1])
            print(message)
            a = await e.client.get_entity(message)
            g = a.id
            c = a.first_name
            username = f"[{c}](tg://user?id={g})"
            counter = int(yukki[0])
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            c = b.first_name
            counter = int(yukki[0])
            username = f"[{c}](tg://user?id={g})"
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


# ======[ACTION]======


@idk.on(events.NewMessage(incoming=True))
@ydk.on(events.NewMessage(incoming=True))
@wdk.on(events.NewMessage(incoming=True))
@sdk.on(events.NewMessage(incoming=True))
@adk.on(events.NewMessage(incoming=True))
@bdk.on(events.NewMessage(incoming=True))
@cdk.on(events.NewMessage(incoming=True))
@edk.on(events.NewMessage(incoming=True))
@hdk.on(events.NewMessage(incoming=True))
@ddk.on(events.NewMessage(incoming=True))
@vkk.on(events.NewMessage(incoming=True))
@kkk.on(events.NewMessage(incoming=True))
@lkk.on(events.NewMessage(incoming=True))
@mkk.on(events.NewMessage(incoming=True))
@sid.on(events.NewMessage(incoming=True))
@shy.on(events.NewMessage(incoming=True))
@aan.on(events.NewMessage(incoming=True))
@ake.on(events.NewMessage(incoming=True))
@eel.on(events.NewMessage(incoming=True))
@khu.on(events.NewMessage(incoming=True))
@shi.on(events.NewMessage(incoming=True))
@yaa.on(events.NewMessage(incoming=True))
@dav.on(events.NewMessage(incoming=True))
@raj.on(events.NewMessage(incoming=True))
@put.on(events.NewMessage(incoming=True))
@tsi.on(events.NewMessage(incoming=True))
@tsv.on(events.NewMessage(incoming=True))
@teg.on(events.NewMessage(incoming=True))
@tnn.on(events.NewMessage(incoming=True))
@tth.on(events.NewMessage(incoming=True))
@ton.on(events.NewMessage(incoming=True))
@ttw.on(events.NewMessage(incoming=True))
@ttr.on(events.NewMessage(incoming=True))
@tfr.on(events.NewMessage(incoming=True))
@tfv.on(events.NewMessage(incoming=True))
@tsx.on(events.NewMessage(incoming=True))
@tsv.on(events.NewMessage(incoming=True))
@ttg.on(events.NewMessage(incoming=True))
@ttn.on(events.NewMessage(incoming=True))
@fft.on(events.NewMessage(incoming=True))
@ffo.on(events.NewMessage(incoming=True))
@ftw.on(events.NewMessage(incoming=True))
@ftr.on(events.NewMessage(incoming=True))
@ffr.on(events.NewMessage(incoming=True))
@ffv.on(events.NewMessage(incoming=True))
@fsx.on(events.NewMessage(incoming=True))
@fsv.on(events.NewMessage(incoming=True))
@feg.on(events.NewMessage(incoming=True))
@fnn.on(events.NewMessage(incoming=True))
@fvt.on(events.NewMessage(incoming=True))


async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(0.2)
    async with event.client.action(event.chat_id, "typing"):
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(random.choice(RRAID)),
            reply_to=event.message.id,
        )           
            
# ======[ACTION]======

           
@idk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@tsi.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@tsv.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@teg.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@tnn.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@tth.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@ton.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@ttw.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@ttr.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@tfr.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@tfv.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@tsx.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@tsv.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@ttg.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@ttn.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@fft.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@ffo.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@ftw.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@ftr.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@ffr.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@ffv.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@fsx.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@fsv.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@feg.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@fnn.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@fvt.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))


async def _(e):
    global que
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱\n\nCommand:\n\n.replyraid <Username of User>\n\n.replyraid <reply to a User>"
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 11:
            message = str(yukki[0])
            a = await e.client.get_entity(message)
            g = a.id
            que[g] = []
            qeue = que.get(g)
            appendable = [g]
            qeue.append(appendable)
            text = "Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            que[g] = []
            qeue = que.get(g)
            appendable = [g]
            qeue.append(appendable)
            text = "Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

# ======[DREPLYRAID]======

              
@idk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@tsi.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@tsv.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@teg.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@tnn.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@tth.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@ton.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@ttw.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@ttr.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@tfr.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@tfv.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@tsx.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@tsv.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@ttg.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@ttn.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@fft.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@ffo.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@ftw.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@ftr.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@ffr.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@ffv.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@fsx.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@fsv.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@feg.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@fnn.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@fvt.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))

async def _(e):
    global que
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗮𝗰𝘁𝗶𝘃𝗮𝘁𝗲 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱\n\nCommand:\n\n.dreplyraid <Username of User>\n\n.dreplyraid <reply to a User>"
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 12:
            message = str(yukki[0])
            a = await e.client.get_entity(message)
            g = a.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "De-Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "De-Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

            
# ======[PING!]======       

@idk.on(events.NewMessage(incoming=True, pattern=r"\.ping$"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.ping$"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.ping$"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.ping$"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.ping$"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.ping$"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.ping$"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.ping$"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.ping$"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.ping$"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.ping$"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.ping$"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.ping$"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.ping$"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.ping$"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.ping$"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.ping$"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.ping$"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.ping$"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.ping$"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.ping$"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.ping$"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.ping$"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.ping$"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.ping$"))
@tsi.on(events.NewMessage(incoming=True, pattern=r"\.ping$"))
@tsv.on(events.NewMessage(incoming=True, pattern=r"\.ping$"))
@teg.on(events.NewMessage(incoming=True, pattern=r"\.ping$"))
@tnn.on(events.NewMessage(incoming=True, pattern=r"\.ping$"))
@tth.on(events.NewMessage(incoming=True, pattern=r"\.ping$"))
@ton.on(events.NewMessage(incoming=True, pattern=r"\.ping$"))
@ttw.on(events.NewMessage(incoming=True, pattern=r"\.ping$"))
@ttr.on(events.NewMessage(incoming=True, pattern=r"\.ping$"))
@tfr.on(events.NewMessage(incoming=True, pattern=r"\.ping$"))
@tfv.on(events.NewMessage(incoming=True, pattern=r"\.ping$"))
@tsx.on(events.NewMessage(incoming=True, pattern=r"\.ping$"))
@tsv.on(events.NewMessage(incoming=True, pattern=r"\.ping$"))
@ttg.on(events.NewMessage(incoming=True, pattern=r"\.ping$"))
@ttn.on(events.NewMessage(incoming=True, pattern=r"\.ping$"))
@fft.on(events.NewMessage(incoming=True, pattern=r"\.ping$"))
@ffo.on(events.NewMessage(incoming=True, pattern=r"\.ping$"))
@ftw.on(events.NewMessage(incoming=True, pattern=r"\.ping$"))
@ftr.on(events.NewMessage(incoming=True, pattern=r"\.ping$"))
@ffr.on(events.NewMessage(incoming=True, pattern=r"\.ping$"))
@ffv.on(events.NewMessage(incoming=True, pattern=r"\.ping$"))
@fsx.on(events.NewMessage(incoming=True, pattern=r"\.ping$"))
@fsv.on(events.NewMessage(incoming=True, pattern=r"\.ping$"))
@feg.on(events.NewMessage(incoming=True, pattern=r"\.ping$"))
@fnn.on(events.NewMessage(incoming=True, pattern=r"\.ping$"))
@fvt.on(events.NewMessage(incoming=True, pattern=r"\.ping$"))

async def ping(e):
    if e.sender_id in SMEX_USERS:
        start = datetime.now()
        text = "Pong!"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"🤖 𝗣𝗼𝗻𝗴!\n`{ms}` 𝗺𝘀")

        
# ======[PINX!]======       

@idk.on(events.NewMessage(incoming=True, pattern=r"\.pinx$"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.pinx$"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.pinx$"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.pinx$"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.pinx$"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.pinx$"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.pinx$"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.pinx$"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.pinx$"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.pinx$"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.pinx$"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.pinx$"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.pinx$"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.pinx$"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.pinx$"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.pinx$"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.pinx$"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.pinx$"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.pinx$"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.pinx$"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.pinx$"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.pinx$"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.pinx$"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.pinx$"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.pinx$"))
@tsi.on(events.NewMessage(incoming=True, pattern=r"\.pinx$"))
@tsv.on(events.NewMessage(incoming=True, pattern=r"\.pinx$"))
@teg.on(events.NewMessage(incoming=True, pattern=r"\.pinx$"))
@tnn.on(events.NewMessage(incoming=True, pattern=r"\.pinx$"))
@tth.on(events.NewMessage(incoming=True, pattern=r"\.pinx$"))
@ton.on(events.NewMessage(incoming=True, pattern=r"\.pinx$"))
@ttw.on(events.NewMessage(incoming=True, pattern=r"\.pinx$"))
@ttr.on(events.NewMessage(incoming=True, pattern=r"\.pinx$"))
@tfr.on(events.NewMessage(incoming=True, pattern=r"\.pinx$"))
@tfv.on(events.NewMessage(incoming=True, pattern=r"\.pinx$"))
@tsx.on(events.NewMessage(incoming=True, pattern=r"\.pinx$"))
@tsv.on(events.NewMessage(incoming=True, pattern=r"\.pinx$"))
@ttg.on(events.NewMessage(incoming=True, pattern=r"\.pinx$"))
@ttn.on(events.NewMessage(incoming=True, pattern=r"\.pinx$"))
@fft.on(events.NewMessage(incoming=True, pattern=r"\.pinx$"))
@ffo.on(events.NewMessage(incoming=True, pattern=r"\.pinx$"))
@ftw.on(events.NewMessage(incoming=True, pattern=r"\.pinx$"))
@ftr.on(events.NewMessage(incoming=True, pattern=r"\.pinx$"))
@ffr.on(events.NewMessage(incoming=True, pattern=r"\.pinx$"))
@ffv.on(events.NewMessage(incoming=True, pattern=r"\.pinx$"))
@fsx.on(events.NewMessage(incoming=True, pattern=r"\.pinx$"))
@fsv.on(events.NewMessage(incoming=True, pattern=r"\.pinx$"))
@feg.on(events.NewMessage(incoming=True, pattern=r"\.pinx$"))
@fnn.on(events.NewMessage(incoming=True, pattern=r"\.pinx$"))
@fvt.on(events.NewMessage(incoming=True, pattern=r"\.pinx$"))

async def ping(e):
    if e.sender_id in SMEX_USERS:
        start = datetime.now()
        text = "Ponx!"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"『 P͛o͛n͛x͛ 』⏤⏤͟͟★\n`{ms}` 𝗺𝘀")

        
# =====[ABSEN]=====        
        
@idk.on(events.NewMessage(incoming=True, pattern=r"\.absen$"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.absen$"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.absen$"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.absen$"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.absen$"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.absen$"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.absen$"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.absen$"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.absen$"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.absen$"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.absen$"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.absen$"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.absen$"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.absen$"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.absen$"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.absen$"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.absen$"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.absen$"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.absen$"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.absen$"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.absen$"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.absen$"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.absen$"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.absen$"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.absen$"))
@tsi.on(events.NewMessage(incoming=True, pattern=r"\.absen$"))
@tsv.on(events.NewMessage(incoming=True, pattern=r"\.absen$"))
@teg.on(events.NewMessage(incoming=True, pattern=r"\.absen$"))
@tnn.on(events.NewMessage(incoming=True, pattern=r"\.absen$"))
@tth.on(events.NewMessage(incoming=True, pattern=r"\.absen$"))
@ton.on(events.NewMessage(incoming=True, pattern=r"\.absen$"))
@ttw.on(events.NewMessage(incoming=True, pattern=r"\.absen$"))
@ttr.on(events.NewMessage(incoming=True, pattern=r"\.absen$"))
@tfr.on(events.NewMessage(incoming=True, pattern=r"\.absen$"))
@tfv.on(events.NewMessage(incoming=True, pattern=r"\.absen$"))
@tsx.on(events.NewMessage(incoming=True, pattern=r"\.absen$"))
@tsv.on(events.NewMessage(incoming=True, pattern=r"\.absen$"))
@ttg.on(events.NewMessage(incoming=True, pattern=r"\.absen$"))
@ttn.on(events.NewMessage(incoming=True, pattern=r"\.absen$"))
@fft.on(events.NewMessage(incoming=True, pattern=r"\.absen$"))
@ffo.on(events.NewMessage(incoming=True, pattern=r"\.absen$"))
@ftw.on(events.NewMessage(incoming=True, pattern=r"\.absen$"))
@ftr.on(events.NewMessage(incoming=True, pattern=r"\.absen$"))
@ffr.on(events.NewMessage(incoming=True, pattern=r"\.absen$"))
@ffv.on(events.NewMessage(incoming=True, pattern=r"\.absen$"))
@fsx.on(events.NewMessage(incoming=True, pattern=r"\.absen$"))
@fsv.on(events.NewMessage(incoming=True, pattern=r"\.absen$"))
@feg.on(events.NewMessage(incoming=True, pattern=r"\.absen$"))
@fnn.on(events.NewMessage(incoming=True, pattern=r"\.absen$"))
@fvt.on(events.NewMessage(incoming=True, pattern=r"\.absen$"))

async def absen(e):
    if e.sender_id in SMEX_USERS:
        start = datetime.now()
        text = "Hadir!"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"𝙃𝙖𝙙𝙞𝙧 ˁ˚ᴥ˚ˀ\n`{ms}` 𝗺𝘀")
    
        
# INVITE ALL OP

from telethon.errors import (
    ChannelInvalidError,
    ChannelPrivateError,
    ChannelPublicGroupNaError,
)
from telethon.tl import functions
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.functions.messages import GetFullChatRequest


async def get_chatinfo(event):
    chat = event.pattern_match.group(1)
    chat_info = None
    if chat:
        try:
            chat = int(chat)
        except ValueError:
            pass
    if not chat:
        if event.reply_to_msg_id:
            replied_msg = await event.get_reply_message()
            if replied_msg.fwd_from and replied_msg.fwd_from.channel_id is not None:
                chat = replied_msg.fwd_from.channel_id
        else:
            chat = event.chat_id
    try:
        chat_info = await event.client(GetFullChatRequest(chat))
    except:
        try:
            chat_info = await event.client(GetFullChannelRequest(chat))
        except ChannelInvalidError:
            await event.reply("`Invalid channel/group`")
            return None
        except ChannelPrivateError:
            await event.reply(
                "`This is a private channel/group or I am banned from there`"
            )
            return None
        except ChannelPublicGroupNaError:
            await event.reply("`Channel or supergroup doesn't exist`")
            return None
        except (TypeError, ValueError):
            await event.reply("`Invalid channel/group`")
            return None
    return chat_info


def make_mention(user):
    if user.username:
        return f"@{user.username}"
    else:
        return inline_mention(user)


def inline_mention(user):
    full_name = user_full_name(user) or "No Name"
    return f"[{full_name}](tg://user?id={user.id})"


def user_full_name(user):
    names = [user.first_name, user.last_name]
    names = [i for i in list(names) if i]
    full_name = " ".join(names)
    return full_name

# =====[INVITEALL]=====  
            
@idk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@tsi.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@tsv.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@teg.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@tnn.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@tth.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@ton.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@ttw.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@ttr.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@tfr.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@tfv.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@tsx.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@tsv.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@ttg.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@ttn.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@fft.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@ffo.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@ftw.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@ftr.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@ffr.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@ffv.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@fsx.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@fsv.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@feg.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@fnn.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@fvt.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))

async def get_users(event):
    if event.sender_id in SMEX_USERS:
        rkp = await event.reply("`processing...`")
    else:
        rkp = await event.edit("`processing...`")
    rk1 = await get_chatinfo(event)
    chat = await event.get_chat()
    if event.is_private:
        return await rkp.edit("`Sorry, Can add users here`")
    s = 0
    f = 0
    error = "None"

    await rkp.edit("**TerminalStatus**\n\n`Collecting Users.......`")
    async for user in event.client.iter_participants(rk1.full_chat.id):
        try:
            if error.startswith("Too"):
                return await rkp.edit(
                    f"**Terminal Finished With Error**\n(`May Got Limit Error from telethon Please try agin Later`)\n**Error** : \n`{error}`\n\n• Invited `{s}` people \n• Failed to Invite `{f}` people"
                )
            await event.client(
                functions.channels.InviteToChannelRequest(channel=chat, users=[user.id])
            )
            s = s + 1
            await rkp.edit(
                f"**Terminal Running...**\n\n• Invited `{s}` people \n• Failed to Invite `{f}` people\n\n**× LastError:** `{error}`"
            )
        except Exception as e:
            error = str(e)
            f = f + 1
    return await rkp.edit(
        f"**Terminal Finished** \n\n• Successfully Invited `{s}` people \n• failed to invite `{f}` people"
    )        

# =====[RESTART]=====  

@idk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@tsi.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@tsv.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@teg.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@tnn.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@tth.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ton.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ttw.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ttr.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@tfr.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@tfv.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@tsx.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@tsv.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ttg.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ttn.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@fft.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ffo.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ftw.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ftr.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ffr.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ffv.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@fsx.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@fsv.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@feg.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@fnn.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@fvt.on(events.NewMessage(incoming=True, pattern=r"\.restart"))

async def restart(e):
    if e.sender_id in SMEX_USERS:
        text = "𝙍𝙚𝙨𝙩𝙖𝙧𝙩𝙚𝙙\n\nPlease wait till it reboots..."
        await e.reply(text, parse_mode=None, link_preview=None )
        try:
            await idk.disconnect()
        except Exception as e:
            pass
        try:
            await ydk.disconnect()
        except Exception as e:
            pass
        try:
            await wdk.disconnect()
        except Exception as e:
            pass
        try:
            await hdk.disconnect()
        except Exception as e:
            pass
        try:
            await sdk.disconnect()
        except Exception as e:
            pass
        try:
            await adk.disconnect()
        except Exception as e:
            pass
        try:
            await bdk.disconnect()
        except Exception as e:
            pass
        try:
            await cdk.disconnect()
        except Exception as e:
            pass
        try:
            await ddk.disconnect()
        except Exception as e:
            pass
        try:
            await edk.disconnect()
        except Exception as e:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()

        
        
# =========[HELP]=========     
        
        
@idk.on(events.NewMessage(incoming=True, pattern=r"\.help$"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.help$"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.help$"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.help$"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.help$"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.help$"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.help$"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.help$"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.help$"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.help$"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.help$"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.help$"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.help$"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.help$"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.help$"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.help$"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.help$"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.help$"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.help$"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.help$"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.help$"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.help$"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.help$"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.help$"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.help$"))
@tsi.on(events.NewMessage(incoming=True, pattern=r"\.help$"))
@tsv.on(events.NewMessage(incoming=True, pattern=r"\.help$"))
@teg.on(events.NewMessage(incoming=True, pattern=r"\.help$"))
@tnn.on(events.NewMessage(incoming=True, pattern=r"\.help$"))
@tth.on(events.NewMessage(incoming=True, pattern=r"\.help$"))
@ton.on(events.NewMessage(incoming=True, pattern=r"\.help$"))
@ttw.on(events.NewMessage(incoming=True, pattern=r"\.help$"))
@ttr.on(events.NewMessage(incoming=True, pattern=r"\.help$"))
@tfr.on(events.NewMessage(incoming=True, pattern=r"\.help$"))
@tfv.on(events.NewMessage(incoming=True, pattern=r"\.help$"))
@tsx.on(events.NewMessage(incoming=True, pattern=r"\.help$"))
@tsv.on(events.NewMessage(incoming=True, pattern=r"\.help$"))
@ttg.on(events.NewMessage(incoming=True, pattern=r"\.help$"))
@ttn.on(events.NewMessage(incoming=True, pattern=r"\.help$"))
@fft.on(events.NewMessage(incoming=True, pattern=r"\.help$"))
@ffo.on(events.NewMessage(incoming=True, pattern=r"\.help$"))
@ftw.on(events.NewMessage(incoming=True, pattern=r"\.help$"))
@ftr.on(events.NewMessage(incoming=True, pattern=r"\.help$"))
@ffr.on(events.NewMessage(incoming=True, pattern=r"\.help$"))
@ffv.on(events.NewMessage(incoming=True, pattern=r"\.help$"))
@fsx.on(events.NewMessage(incoming=True, pattern=r"\.help$"))
@fsv.on(events.NewMessage(incoming=True, pattern=r"\.help$"))
@feg.on(events.NewMessage(incoming=True, pattern=r"\.help$"))
@fnn.on(events.NewMessage(incoming=True, pattern=r"\.help$"))
@fvt.on(events.NewMessage(incoming=True, pattern=r"\.help$"))

async def help(e):
    if e.sender_id in SMEX_USERS:
       text = "🔰 𝗔𝘃𝗮𝗶𝗹𝗮𝗯𝗹𝗲 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀\n\n𝙐𝙩𝙞𝙡𝙨 𝘾𝙤𝙢𝙢𝙖𝙣𝙙:\n.ping\n.restart\n.absen\n.pinx\n\n𝙐𝙨𝙚𝙧𝙗𝙤𝙩 𝘾𝙤𝙢𝙢𝙖𝙣𝙙:\n.bio\n.join\n.pjoin\n.leave\n\n𝙎𝙥𝙖𝙢 𝘾𝙤𝙢𝙢𝙖𝙣𝙙:\n.spam\n.delayspam\n.bigspam\n.raid\n.replyraid\n.dreplyraid\n\n\nFor more help regarding usage of plugins type plugins name\n\nBot Version: 3.0.0.1"
       await e.reply(text, parse_mode=None, link_preview=None )

        

    
        
text = """

💥💥 CONGRATULATIONS UR DEADLY ALPHA-X MULTI 5P4MX UBOT v3.1.0.0  IS READY! 💥💥💥
💥💥💥💥💥💥 Original Code By OP Sameer from Deadly Team 💥💥💥💥💥💥
💥💥💥💥💥💥 Modded Code By @AlphaxProject Team 💥💥💥💥💥💥"""

print(text)
print("")
print("🙏🔥🔥 SMEX! DEADLY ALPHA-X MULTI 5P4MX UBOT v3.1.0.0 STARTED SUCCESFULLY!. 🔥🔥🙏")
if len(sys.argv) not in (1, 3, 4):
    try:
        idk.disconnect()
    except Exception as e:
        pass
    try:
        ydk.disconnect()
    except Exception as e:
        pass
    try:
        wdk.disconnect()
    except Exception as e:
        pass
    try:
        hdk.disconnect()
    except Exception as e:
        pass
    try:
        sdk.disconnect()
    except Exception as e:
        pass
    try:
        adk.disconnect()
    except Exception as e:
        pass
    try:
        bdk.disconnect()
    except Exception as e:
        pass
    try:
        cdk.disconnect()
    except Exception as e:
        pass
    try:
        edk.disconnect()
    except Exception as e:
        pass
    try:
        ddk.disconnect()
    except Exception as e:
        pass
    try:
        vkk.disconnect()
    except Exception as e:
        pass 
    try:
        kkk.disconnect()
    except Exception as e:
        pass
    try:
        lkk.disconnect()
    except Exception as e:
        pass 
    try:
        mkk.disconnect()
    except Exception as e:
        pass
    try:
        sid.disconnect()
    except Exception as e:
        pass
    try:
        shy.disconnect()
    except Exception as e:
        pass
    try:
        aan.disconnect()
    except Exception as e:
        pass
    try:
        ake.disconnect()
    except Exception as e:
        pass
    try:
        eel.disconnect()
    except Exception as e:
        pass
    try:
        khu.disconnect()
    except Exception as e:
        pass
    try:
        shi.disconnect()
    except Exception as e:
        pass
    try:
        yaa.disconnect()
    except Exception as e:
        pass
    try:
        dav.disconnect()
    except Exception as e:
        pass
    try:
        raj.disconnect()
    except Exception as e:
        pass
    try:
        put.disconnect()
    except Exception as e:
        pass
    try:
        tsi.disconnect()
    except Exception as e:
        pass
    try:
        tsv.disconnect()
    except Exception as e:
        pass
    try:
        teg.disconnect()
    except Exception as e:
        pass
    try:
        tnn.disconnect()
    except Exception as e:
        pass
    try:
        tth.disconnect()
    except Exception as e:
        pass
    try:
        ton.disconnect()
    except Exception as e:
        pass
    try:
        ttw.disconnect()
    except Exception as e:
        pass
    try:
        ttr.disconnect()
    except Exception as e:
        pass
    try:
        tfr.disconnect()
    except Exception as e:
        pass
    try:
        tfv.disconnect()
    except Exception as e:
        pass
    try:
        tsx.disconnect()
    except Exception as e:
        pass 
    try:
        tsv.disconnect()
    except Exception as e:
        pass
    try:
        ttg.disconnect()
    except Exception as e:
        pass 
    try:
        ttn.disconnect()
    except Exception as e:
        pass
    try:
        fft.disconnect()
    except Exception as e:
        pass
    try:
        ffo.disconnect()
    except Exception as e:
        pass
    try:
        ftw.disconnect()
    except Exception as e:
        pass
    try:
        ftr.disconnect()
    except Exception as e:
        pass
    try:
        ffr.disconnect()
    except Exception as e:
        pass
    try:
        ffv.disconnect()
    except Exception as e:
        pass
    try:
        fsx.disconnect()
    except Exception as e:
        pass
    try:
        fsv.disconnect()
    except Exception as e:
        pass
    try:
        feg.disconnect()
    except Exception as e:
        pass
    try:
        fnn.disconnect()
    except Exception as e:
        pass
    try:
        fvt.disconnect()
    except Exception as e:
        pass
else:
    try:
        idk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        ydk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        wdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        hdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        sdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        adk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        cdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        edk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        ddk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        vkk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        kkk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        lkk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        mkk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        sid.run_until_disconnected()
    except Exception as e:
        pass
    try:
        shy.run_until_disconnected()
    except Exception as e:
        pass
    try:
        aan.run_until_disconnected()
    except Exception as e:
        pass
    try:
        ake.run_until_disconnected()
    except Exception as e:
        pass
    try:
        eel.run_until_disconnected()
    except Exception as e:
        pass
    try:
        khu.run_until_disconnected()
    except Exception as e:
        pass
    try:
        shi.run_until_disconnected()
    except Exception as e:
        pass
    try:
        yaa.run_until_disconnected()
    except Exception as e:
        pass
    try:
        dav.run_until_disconnected()
    except Exception as e:
        pass
    try:
        raj.run_until_disconnected()
    except Exception as e:
        pass
    try:
        put.run_until_disconnected()
    except Exception as e:
        pass
    try:
        tsi.run_until_disconnected()
    except Exception as e:
        pass
    try:
        tsv.run_until_disconnected()
    except Exception as e:
        pass
    try:
        teg.run_until_disconnected()
    except Exception as e:
        pass
    try:
        tnn.run_until_disconnected()
    except Exception as e:
        pass
    try:
        tth.run_until_disconnected()
    except Exception as e:
        pass
    try:
        ton.run_until_disconnected()
    except Exception as e:
        pass
    try:
        ttw.run_until_disconnected()
    except Exception as e:
        pass
    try:
        ttr.run_until_disconnected()
    except Exception as e:
        pass
    try:
        tfr.run_until_disconnected()
    except Exception as e:
        pass
    try:
        tfv.run_until_disconnected()
    except Exception as e:
        pass
    try:
        tsx.run_until_disconnected()
    except Exception as e:
        pass
    try:
        tsv.run_until_disconnected()
    except Exception as e:
        pass
    try:
        ttg.run_until_disconnected()
    except Exception as e:
        pass
    try:
        ttn.run_until_disconnected()
    except Exception as e:
        pass
    try:
        fft.run_until_disconnected()
    except Exception as e:
        pass
    try:
        ffo.run_until_disconnected()
    except Exception as e:
        pass
    try:
        ftw.run_until_disconnected()
    except Exception as e:
        pass
    try:
        ftr.run_until_disconnected()
    except Exception as e:
        pass
    try:
        ffr.run_until_disconnected()
    except Exception as e:
        pass
    try:
        ffv.run_until_disconnected()
    except Exception as e:
        pass
    try:
        fsx.run_until_disconnected()
    except Exception as e:
        pass
    try:
        fsv.run_until_disconnected()
    except Exception as e:
        pass
    try:
        feg.run_until_disconnected()
    except Exception as e:
        pass
    try:
        fnn.run_until_disconnected()
    except Exception as e:
        pass
    try:
        fvt.run_until_disconnected()
    except Exception as e:
        pass
