# Copyright (C) 2020 by AlphaXProject @Github, 
#
# This file is part of https://t.me/AlphaXProject  project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://t.me/AlphaXProject  >
#
# All rights reserved.
#
# Created by : https://t.me/AlphaXProject 
# Support by : https://t.me/CariTemanLink 



import os
import sys
import random
from datetime import datetime
from os import execl
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.functions.account import UpdateProfileRequest
from Config import HNDLR, ALIVE_NAME, HASH_CHAT, REPO_LINK, STRING, SUDO, BIO_MESSAGE, API_ID, API_HASH, STRING2, STRING3, STRING4 ,STRING5, STRING6, STRING7, STRING8 ,STRING9, STRING10, STRING11, STRING12, STRING13, STRING14, STRING15, STRING16, STRING17, STRING18, STRING19, STRING20, STRING21, STRING22, STRING23, STRING24, STRING25, STRING26, STRING27, STRING28, STRING29 ,STRING30, STRING31, STRING32, STRING33 ,STRING34, STRING35, STRING36, STRING37, STRING38, STRING39, STRING40, STRING41, STRING42, STRING43, STRING44, STRING45, STRING46, STRING47, STRING48, STRING49, STRING50, HEROKU_API_KEY, UPSTREAM_REPO, HEROKU_APP_NAME
import asyncio
import telethon.utils

from telethon.tl.types import InputPeerUser, ChatBannedRights
from telethon.tl.functions.channels import (
    InviteToChannelRequest,
    EditBannedRequest,
    GetFullChannelRequest,
    LeaveChannelRequest)
from telethon.tl import functions
from telethon.tl.functions.messages import GetFullChatRequest
from telethon.errors import (
    ChannelInvalidError,
    ChannelPrivateError,
    ChannelPublicGroupNaError)

from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from Utils import RAID, RRAID, RABSEN
import git
import heroku3
from asyncio import sleep

import html

from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.photos import DeletePhotosRequest, UploadProfilePhotoRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName

from telethon.errors import ImageProcessFailedError, PhotoCropSizeSmallError

from telethon.errors.rpcerrorlist import (PhotoExtInvalidError,
                                          UsernameOccupiedError)

from telethon.tl.functions.account import (UpdateProfileRequest,
                                           UpdateUsernameRequest)

from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest

from telethon.tl.functions.photos import (DeletePhotosRequest,
                                          GetUserPhotosRequest,
                                          UploadProfilePhotoRequest)

from telethon.tl.types import InputPhoto, MessageMediaPhoto, User, Chat, Channel
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from telethon.utils import get_input_location
import time
from telethon.tl.functions.photos import DeletePhotosRequest, GetUserPhotosRequest
from telethon.tl.types import Channel, Chat, InputPhoto, User
from telethon.errors.rpcerrorlist import UsernameOccupiedError
from telethon.tl.functions.account import UpdateUsernameRequest
from telethon.errors import rpcbaseerrors
import requests



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
ubversi = "Beta v3.1.1.28 [build 0.1]" #versi
LOG_GROUP = HASH_CHAT


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
tsf = ""
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
    global put #batas 25
    global tsi
    global tsf
    global teg
    global tnn
    global tth
    global ton
    global ttw
    global ttr
    global tfr
    global tfv
    global tsx
    global tsv
    global ttg
    global ttn
    global fft
    global ffo
    global ftw
    global ftr
    global ffr
    global ffv
    global fsx
    global fsv
    global feg
    global fnn
    global fvt
    global ubversi
    global LOG_GROUP
 


    print(f"\n⏳ 「 ⚡️𝘿𝙇-𝙓𝟓𝟎 𝙐𝘽⚡️ 」 {ubversi} IS STARTING...\n")

    
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
            await idk(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
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
            await ydk(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
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
            await wdk(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
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
            await hdk(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
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
            await sdk(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
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
            await adk(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
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
            await bdk(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
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
            await cdk(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
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
            await ddk(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
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
            await edk(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
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
            await vkk(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
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
            await kkk(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
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
            await lkk(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
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
            await mkk(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
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
            await sid(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
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
            await shy(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
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
            await aan(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
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
            await ake(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
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
            await eel(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
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
            await khu(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
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
            await shi(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
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
            await yaa(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
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
            await dav(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
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
            await raj(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
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
            await put(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
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
            await tsi(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
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
        tsf = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 27")
            await tsf.start()
            botme = await tsf.get_me()
            await tsf(functions.channels.JoinChannelRequest(channel="@caritemanlink"))
            await tsf(functions.channels.JoinChannelRequest(channel="@cariteman1"))
            await tsf(functions.channels.JoinChannelRequest(channel="@tgreceh"))
            await tsf(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
            await tsf(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 27 not Found")
        session_name = "startup"
        tsf = TelegramClient(session_name, a, b)
        try:
            await tsf.start()
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
            await teg(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
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
            await tnn(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
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
            await tth(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
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
            await ton(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
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
            await ttw(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
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
            await ttr(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
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
            await tfr(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
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
            await tfv(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
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
            await tsx(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
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
        tsv = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 37")
            await tsv.start()
            await tsv(functions.channels.JoinChannelRequest(channel="@caritemanlink"))
            await tsv(functions.channels.JoinChannelRequest(channel="@cariteman1"))
            await tsv(functions.channels.JoinChannelRequest(channel="@tgreceh"))
            await tsv(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
            await tsv(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
            botme = await tsv.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 37 not Found")
        pass
        session_name = "startup"
        tsv = TelegramClient(session_name, a, b)
        try:
            await tsv.start()
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
            await ttg(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
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
            await ttn(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
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
            await fft(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
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
            await ffo(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
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
            await ftw(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
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
            await ftr(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
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
            await ffr(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
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
            await ffv(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
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
            await fsx(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
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
            await fsv(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
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
            await feg(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
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
            await fnn(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
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
            await fvt(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
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


@idk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bio"))
@ydk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bio"))
@wdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bio"))
@sdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bio"))
@adk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bio"))
@bdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bio"))
@cdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bio"))
@edk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bio"))
@hdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bio"))
@ddk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bio"))
@vkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bio"))
@kkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bio"))
@lkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bio"))
@mkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bio"))
@sid.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bio"))
@shy.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bio"))
@aan.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bio"))
@ake.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bio"))
@eel.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bio"))
@khu.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bio"))
@shi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bio"))
@yaa.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bio"))
@dav.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bio"))
@raj.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bio"))
@put.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bio"))
@tsi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bio"))
@tsf.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bio"))
@teg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bio"))
@tnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bio"))
@tth.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bio"))
@ton.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bio"))
@ttw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bio"))
@ttr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bio"))
@tfr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bio"))
@tfv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bio"))
@tsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bio"))
@tsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bio"))
@ttg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bio"))
@ttn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bio"))
@fft.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bio"))
@ffo.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bio"))
@ftw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bio"))
@ftr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bio"))
@ffr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bio"))
@ffv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bio"))
@fsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bio"))
@fsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bio"))
@feg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bio"))
@fnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bio"))
@fvt.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bio"))


async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗕𝗶𝗼\n\nCommand:\n\n.bio <Message to set Bio of Userbot accounts>"
    if e.sender_id in SMEX_USERS:
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)     
        if len(e.text) > 5:
            bio = str(yukki[0])
            text = "Changing Bio.."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(functions.account.UpdateProfileRequest(about=bio))
                await event.edit("Succesfully Changed Bio!")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

# ======[JOIN]======
            
@idk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}join"))
@ydk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}join"))
@wdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}join"))
@sdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}join"))
@adk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}join"))
@bdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}join"))
@cdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}join"))
@edk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}join"))
@hdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}join"))
@ddk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}join"))
@vkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}join"))
@kkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}join"))
@lkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}join"))
@mkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}join"))
@sid.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}join"))
@shy.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}join"))
@aan.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}join"))
@ake.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}join"))
@eel.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}join"))
@khu.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}join"))
@shi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}join"))
@yaa.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}join"))
@dav.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}join"))
@raj.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}join"))
@put.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}join"))
@tsi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}join"))
@tsf.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}join"))
@teg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}join"))
@tnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}join"))
@tth.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}join"))
@ton.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}join"))
@ttw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}join"))
@ttr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}join"))
@tfr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}join"))
@tfv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}join"))
@tsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}join"))
@tsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}join"))
@ttg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}join"))
@ttn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}join"))
@fft.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}join"))
@ffo.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}join"))
@ftw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}join"))
@ftr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}join"))
@ffr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}join"))
@ffv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}join"))
@fsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}join"))
@fsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}join"))
@feg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}join"))
@fnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}join"))
@fvt.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}join"))


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

            
@idk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pjoin"))
@ydk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pjoin"))
@wdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pjoin"))
@sdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pjoin"))
@adk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pjoin"))
@bdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pjoin"))
@cdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pjoin"))
@edk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pjoin"))
@hdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pjoin"))
@ddk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pjoin"))
@vkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pjoin"))
@kkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pjoin"))
@lkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pjoin"))
@mkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pjoin"))
@sid.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pjoin"))
@shy.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pjoin"))
@aan.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pjoin"))
@ake.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pjoin"))
@eel.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pjoin"))
@khu.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pjoin"))
@shi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pjoin"))
@yaa.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pjoin"))
@dav.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pjoin"))
@raj.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pjoin"))
@put.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pjoin"))
@tsi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pjoin"))
@tsf.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pjoin"))
@teg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pjoin"))
@tnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pjoin"))
@tth.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pjoin"))
@ton.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pjoin"))
@ttw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pjoin"))
@ttr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pjoin"))
@tfr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pjoin"))
@tfv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pjoin"))
@tsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pjoin"))
@tsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pjoin"))
@ttg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pjoin"))
@ttn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pjoin"))
@fft.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pjoin"))
@ffo.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pjoin"))
@ftw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pjoin"))
@ftr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pjoin"))
@ffr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pjoin"))
@ffv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pjoin"))
@fsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pjoin"))
@fsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pjoin"))
@feg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pjoin"))
@fnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pjoin"))
@fvt.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pjoin"))


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
        
@idk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}leave"))
@ydk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}leave"))
@wdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}leave"))
@sdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}leave"))
@adk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}leave"))
@bdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}leave"))
@cdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}leave"))
@edk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}leave"))
@hdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}leave"))
@ddk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}leave"))
@vkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}leave"))
@kkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}leave"))
@lkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}leave"))
@mkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}leave"))
@sid.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}leave"))
@shy.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}leave"))
@aan.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}leave"))
@ake.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}leave"))
@eel.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}leave"))
@khu.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}leave"))
@shi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}leave"))
@yaa.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}leave"))
@dav.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}leave"))
@raj.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}leave"))
@put.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}leave"))
@tsi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}leave"))
@tsf.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}leave"))
@teg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}leave"))
@tnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}leave"))
@tth.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}leave"))
@ton.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}leave"))
@ttw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}leave"))
@ttr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}leave"))
@tfr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}leave"))
@tfv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}leave"))
@tsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}leave"))
@tsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}leave"))
@ttg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}leave"))
@ttn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}leave"))
@fft.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}leave"))
@ffo.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}leave"))
@ftw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}leave"))
@ftr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}leave"))
@ffr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}leave"))
@ffv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}leave"))
@fsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}leave"))
@fsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}leave"))
@feg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}leave"))
@fnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}leave"))
@fvt.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}leave"))


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
caption_alive = f"""
╭┈─╼━━━━━━━━━━━━━╾─┈
│ 
│     「 ⚡️𝘿𝙇-𝙓 𝙐𝙎𝙀𝙍𝘽𝙊𝙏⚡️ 」
│ 
├┈─╼━━━━━━━━━━━━━╾─┈  
│ 𝙃𝙚𝙡𝙡𝙤 𝙈𝙖𝙨𝙩𝙚𝙧
│ 𝙄 𝙖𝙢 𝙖𝙡𝙞𝙫𝙚
│ 𝙍𝙚𝙖𝙙𝙮 𝙩𝙤 𝙛𝙪𝙘𝙠 𝙮𝙤𝙪𝙧 𝙃𝙖𝙩𝙚𝙧𝙨
│ 
│ 𝙋𝙤𝙬𝙚𝙧𝙚𝙙 𝙗𝙮: 
│   𝘼𝙇𝙋𝙃𝘼-𝙓 𝙋𝙧𝙤𝙟𝙚𝙘𝙩  ͭ ͤ ͣ ͫ
╰┈─╼━━━━━━━━━━━━━╾─┈
"""

USTAD_PIC = "https://telegra.ph/file/36eb117322594ce579f66.jpg"

"""
async def reply_id(event):
    reply_to_id = None
    if event.sender_id in Config.SUDO:
        reply_to_id = event.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    return reply_to_id
"""

@idk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}alive"))
@ydk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}alive"))
@wdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}alive"))
@sdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}alive"))
@adk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}alive"))
@bdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}alive"))
@cdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}alive"))
@edk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}alive"))
@hdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}alive"))
@ddk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}alive"))
@vkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}alive"))
@kkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}alive"))
@lkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}alive"))
@mkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}alive"))
@sid.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}alive"))
@shy.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}alive"))
@aan.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}alive"))
@ake.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}alive"))
@eel.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}alive"))
@khu.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}alive"))
@shi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}alive"))
@yaa.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}alive"))
@dav.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}alive"))
@raj.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}alive"))
@put.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}alive"))
@tsi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}alive"))
@tsf.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}alive"))
@teg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}alive"))
@tnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}alive"))
@tth.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}alive"))
@ton.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}alive"))
@ttw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}alive"))
@ttr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}alive"))
@tfr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}alive"))
@tfv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}alive"))
@tsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}alive"))
@tsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}alive"))
@ttg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}alive"))
@ttn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}alive"))
@fft.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}alive"))
@ffo.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}alive"))
@ftw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}alive"))
@ftr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}alive"))
@ffr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}alive"))
@ffv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}alive"))
@fsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}alive"))
@fsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}alive"))
@feg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}alive"))
@fnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}alive"))
@fvt.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}alive"))


async def start(event):
    if event.sender_id in SMEX_USERS:
        alv = await event.client.send_file(event.chat_id, USTAD_PIC, caption=f"{caption_alive}")
        await event.reply(alv)
        # os.remove(alv)
        await alv.delete()






# ======[SPAM]======    
        
@idk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spam"))
@ydk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spam"))
@wdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spam"))
@sdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spam"))
@adk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spam"))
@bdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spam"))
@cdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spam"))
@edk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spam"))
@hdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spam"))
@ddk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spam"))
@vkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spam"))
@kkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spam"))
@lkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spam"))
@mkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spam"))
@sid.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spam"))
@shy.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spam"))
@aan.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spam"))
@ake.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spam"))
@eel.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spam"))
@khu.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spam"))
@shi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spam"))
@yaa.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spam"))
@dav.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spam"))
@raj.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spam"))
@put.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spam"))
@tsi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spam"))
@tsf.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spam"))
@teg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spam"))
@tnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spam"))
@tth.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spam"))
@ton.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spam"))
@ttw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spam"))
@ttr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spam"))
@tfr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spam"))
@tfv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spam"))
@tsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spam"))
@tsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spam"))
@ttg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spam"))
@ttn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spam"))
@fft.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spam"))
@ffo.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spam"))
@ftw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spam"))
@ftr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spam"))
@ffr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spam"))
@ffv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spam"))
@fsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spam"))
@fsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spam"))
@feg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spam"))
@fnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spam"))
@fvt.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spam"))


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

@idk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delayspam"))
@ydk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delayspam"))
@wdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delayspam"))
@sdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delayspam"))
@adk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delayspam"))
@bdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delayspam"))
@cdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delayspam"))
@edk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delayspam"))
@hdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delayspam"))
@ddk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delayspam"))
@vkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delayspam"))
@kkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delayspam"))
@lkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delayspam"))
@mkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delayspam"))
@sid.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delayspam"))
@shy.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delayspam"))
@aan.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delayspam"))
@ake.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delayspam"))
@eel.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delayspam"))
@khu.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delayspam"))
@shi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delayspam"))
@yaa.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delayspam"))
@dav.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delayspam"))
@raj.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delayspam"))
@put.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delayspam"))
@tsi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delayspam"))
@tsf.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delayspam"))
@teg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delayspam"))
@tnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delayspam"))
@tth.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delayspam"))
@ton.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delayspam"))
@ttw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delayspam"))
@ttr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delayspam"))
@tfr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delayspam"))
@tfv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delayspam"))
@tsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delayspam"))
@tsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delayspam"))
@ttg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delayspam"))
@ttn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delayspam"))
@fft.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delayspam"))
@ffo.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delayspam"))
@ftw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delayspam"))
@ftr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delayspam"))
@ffr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delayspam"))
@ffv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delayspam"))
@fsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delayspam"))
@fsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delayspam"))
@feg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delayspam"))
@fnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delayspam"))
@fvt.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delayspam"))


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

@idk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bigspam"))
@ydk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bigspam"))
@wdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bigspam"))
@sdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bigspam"))
@adk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bigspam"))
@bdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bigspam"))
@cdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bigspam"))
@edk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bigspam"))
@hdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bigspam"))
@ddk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bigspam"))
@vkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bigspam"))
@kkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bigspam"))
@lkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bigspam"))
@mkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bigspam"))
@sid.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bigspam"))
@shy.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bigspam"))
@aan.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bigspam"))
@ake.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bigspam"))
@eel.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bigspam"))
@khu.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bigspam"))
@shi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bigspam"))
@yaa.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bigspam"))
@dav.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bigspam"))
@raj.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bigspam"))
@put.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bigspam"))
@tsi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bigspam"))
@tsf.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bigspam"))
@teg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bigspam"))
@tnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bigspam"))
@tth.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bigspam"))
@ton.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bigspam"))
@ttw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bigspam"))
@ttr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bigspam"))
@tfr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bigspam"))
@tfv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bigspam"))
@tsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bigspam"))
@tsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bigspam"))
@ttg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bigspam"))
@ttn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bigspam"))
@fft.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bigspam"))
@ffo.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bigspam"))
@ftw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bigspam"))
@ftr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bigspam"))
@ffr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bigspam"))
@ffv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bigspam"))
@fsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bigspam"))
@fsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bigspam"))
@feg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bigspam"))
@fnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bigspam"))
@fvt.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}bigspam"))

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

@idk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}raid"))
@ydk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}raid"))
@wdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}raid"))
@sdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}raid"))
@adk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}raid"))
@bdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}raid"))
@cdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}raid"))
@edk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}raid"))
@hdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}raid"))
@ddk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}raid"))
@vkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}raid"))
@kkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}raid"))
@lkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}raid"))
@mkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}raid"))
@sid.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}raid"))
@shy.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}raid"))
@aan.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}raid"))
@ake.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}raid"))
@eel.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}raid"))
@khu.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}raid"))
@shi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}raid"))
@yaa.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}raid"))
@dav.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}raid"))
@raj.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}raid"))
@put.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}raid"))
@tsi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}raid"))
@tsf.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}raid"))
@teg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}raid"))
@tnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}raid"))
@tth.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}raid"))
@ton.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}raid"))
@ttw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}raid"))
@ttr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}raid"))
@tfr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}raid"))
@tfv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}raid"))
@tsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}raid"))
@tsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}raid"))
@ttg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}raid"))
@ttn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}raid"))
@fft.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}raid"))
@ffo.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}raid"))
@ftw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}raid"))
@ftr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}raid"))
@ffr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}raid"))
@ffv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}raid"))
@fsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}raid"))
@fsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}raid"))
@feg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}raid"))
@fnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}raid"))
@fvt.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}raid"))


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
@tsf.on(events.NewMessage(incoming=True))
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

            
# ======[REPLYRAID]======

           
@idk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}replyraid"))
@ydk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}replyraid"))
@wdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}replyraid"))
@sdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}replyraid"))
@adk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}replyraid"))
@bdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}replyraid"))
@cdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}replyraid"))
@edk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}replyraid"))
@hdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}replyraid"))
@ddk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}replyraid"))
@vkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}replyraid"))
@kkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}replyraid"))
@lkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}replyraid"))
@mkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}replyraid"))
@sid.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}replyraid"))
@shy.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}replyraid"))
@aan.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}replyraid"))
@ake.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}replyraid"))
@eel.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}replyraid"))
@khu.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}replyraid"))
@shi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}replyraid"))
@yaa.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}replyraid"))
@dav.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}replyraid"))
@raj.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}replyraid"))
@put.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}replyraid"))
@tsi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}replyraid"))
@tsf.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}replyraid"))
@teg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}replyraid"))
@tnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}replyraid"))
@tth.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}replyraid"))
@ton.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}replyraid"))
@ttw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}replyraid"))
@ttr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}replyraid"))
@tfr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}replyraid"))
@tfv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}replyraid"))
@tsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}replyraid"))
@tsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}replyraid"))
@ttg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}replyraid"))
@ttn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}replyraid"))
@fft.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}replyraid"))
@ffo.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}replyraid"))
@ftw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}replyraid"))
@ftr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}replyraid"))
@ffr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}replyraid"))
@ffv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}replyraid"))
@fsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}replyraid"))
@fsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}replyraid"))
@feg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}replyraid"))
@fnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}replyraid"))
@fvt.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}replyraid"))

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

              
@idk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dreplyraid"))
@ydk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dreplyraid"))
@wdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dreplyraid"))
@sdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dreplyraid"))
@adk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dreplyraid"))
@bdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dreplyraid"))
@cdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dreplyraid"))
@edk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dreplyraid"))
@hdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dreplyraid"))
@ddk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dreplyraid"))
@vkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dreplyraid"))
@kkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dreplyraid"))
@lkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dreplyraid"))
@mkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dreplyraid"))
@sid.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dreplyraid"))
@shy.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dreplyraid"))
@aan.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dreplyraid"))
@ake.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dreplyraid"))
@eel.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dreplyraid"))
@khu.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dreplyraid"))
@shi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dreplyraid"))
@yaa.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dreplyraid"))
@dav.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dreplyraid"))
@raj.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dreplyraid"))
@put.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dreplyraid"))
@tsi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dreplyraid"))
@tsf.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dreplyraid"))
@teg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dreplyraid"))
@tnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dreplyraid"))
@tth.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dreplyraid"))
@ton.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dreplyraid"))
@ttw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dreplyraid"))
@ttr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dreplyraid"))
@tfr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dreplyraid"))
@tfv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dreplyraid"))
@tsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dreplyraid"))
@tsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dreplyraid"))
@ttg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dreplyraid"))
@ttn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dreplyraid"))
@fft.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dreplyraid"))
@ffo.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dreplyraid"))
@ftw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dreplyraid"))
@ftr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dreplyraid"))
@ffr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dreplyraid"))
@ffv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dreplyraid"))
@fsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dreplyraid"))
@fsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dreplyraid"))
@feg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dreplyraid"))
@fnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dreplyraid"))
@fvt.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dreplyraid"))


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


@idk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ping$"))
@ydk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ping$"))
@wdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ping$"))
@sdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ping$"))
@adk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ping$"))
@bdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ping$"))
@cdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ping$"))
@edk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ping$"))
@hdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ping$"))
@ddk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ping$"))
@vkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ping$"))
@kkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ping$"))
@lkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ping$"))
@mkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ping$"))
@sid.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ping$"))
@shy.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ping$"))
@aan.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ping$"))
@ake.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ping$"))
@eel.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ping$"))
@khu.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ping$"))
@shi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ping$"))
@yaa.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ping$"))
@dav.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ping$"))
@raj.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ping$"))
@put.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ping$"))
@tsi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ping$"))
@tsf.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ping$"))
@teg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ping$"))
@tnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ping$"))
@tth.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ping$"))
@ton.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ping$"))
@ttw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ping$"))
@ttr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ping$"))
@tfr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ping$"))
@tfv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ping$"))
@tsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ping$"))
@tsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ping$"))
@ttg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ping$"))
@ttn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ping$"))
@fft.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ping$"))
@ffo.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ping$"))
@ftw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ping$"))
@ftr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ping$"))
@ffr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ping$"))
@ffv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ping$"))
@fsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ping$"))
@fsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ping$"))
@feg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ping$"))
@fnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ping$"))
@fvt.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ping$"))


async def ping(e):
    if e.sender_id in SMEX_USERS:
        start = datetime.now()
        text = "Pong!"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"🤖 𝗣𝗼𝗻𝗴!\n`{ms}` 𝗺𝘀")


# ======PURGEME

@idk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}purgeme"))
@ydk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}purgeme"))
@wdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}purgeme"))
@sdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}purgeme"))
@adk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}purgeme"))
@bdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}purgeme"))
@cdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}purgeme"))
@edk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}purgeme"))
@hdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}purgeme"))
@ddk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}purgeme"))
@vkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}purgeme"))
@kkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}purgeme"))
@lkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}purgeme"))
@mkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}purgeme"))
@sid.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}purgeme"))
@shy.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}purgeme"))
@aan.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}purgeme"))
@ake.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}purgeme"))
@eel.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}purgeme"))
@khu.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}purgeme"))
@shi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}purgeme"))
@yaa.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}purgeme"))
@dav.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}purgeme"))
@raj.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}purgeme"))
@put.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}purgeme"))
@tsi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}purgeme"))
@tsf.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}purgeme"))
@teg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}purgeme"))
@tnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}purgeme"))
@tth.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}purgeme"))
@ton.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}purgeme"))
@ttw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}purgeme"))
@ttr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}purgeme"))
@tfr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}purgeme"))
@tfv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}purgeme"))
@tsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}purgeme"))
@tsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}purgeme"))
@ttg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}purgeme"))
@ttn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}purgeme"))
@fft.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}purgeme"))
@ffo.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}purgeme"))
@ftw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}purgeme"))
@ftr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}purgeme"))
@ffr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}purgeme"))
@ffv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}purgeme"))
@fsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}purgeme"))
@fsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}purgeme"))
@feg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}purgeme"))
@fnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}purgeme"))


async def purgeme(delme):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝙋𝙪𝙧𝙜𝙚𝙢𝙚\n\nCommand:\n\n.purgeme <count> | delete x count of your latest message."
    if delme.sender_id in SMEX_USERS:
        """ For .purgeme, delete x count of your latest message."""
        message = delme.text
        count = int(message[9:])
        i = 1

        async for message in delme.client.iter_messages(delme.chat_id,
                                                    from_user='me'):
            if i > count + 1:
                break
            i = i + 1
            await message.delete()

        smsg = await delme.client.send_message(
            delme.chat_id,
            "`Purge complete!` Purged " + str(count) + " messages.",
        )
        """
        if BOTLOG:
            await delme.client.send_message(
                BOTLOG_CHATID,
                "#PURGEME \nPurge of " + str(count) + " messages done successfully.")
        """
        await sleep(2)
        i = 1
        await smsg.delete()        

        
# ======SPURGEME [SILENT PURGEME]

@idk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spurgeme"))
@ydk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spurgeme"))
@wdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spurgeme"))
@sdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spurgeme"))
@adk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spurgeme"))
@bdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spurgeme"))
@cdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spurgeme"))
@edk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spurgeme"))
@hdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spurgeme"))
@ddk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spurgeme"))
@vkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spurgeme"))
@kkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spurgeme"))
@lkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spurgeme"))
@mkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spurgeme"))
@sid.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spurgeme"))
@shy.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spurgeme"))
@aan.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spurgeme"))
@ake.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spurgeme"))
@eel.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spurgeme"))
@khu.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spurgeme"))
@shi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spurgeme"))
@yaa.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spurgeme"))
@dav.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spurgeme"))
@raj.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spurgeme"))
@put.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spurgeme"))
@tsi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spurgeme"))
@tsf.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spurgeme"))
@teg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spurgeme"))
@tnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spurgeme"))
@tth.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spurgeme"))
@ton.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spurgeme"))
@ttw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spurgeme"))
@ttr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spurgeme"))
@tfr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spurgeme"))
@tfv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spurgeme"))
@tsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spurgeme"))
@tsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spurgeme"))
@ttg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spurgeme"))
@ttn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spurgeme"))
@fft.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spurgeme"))
@ffo.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spurgeme"))
@ftw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spurgeme"))
@ftr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spurgeme"))
@ffr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spurgeme"))
@ffv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spurgeme"))
@fsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spurgeme"))
@fsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spurgeme"))
@feg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spurgeme"))
@fnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spurgeme"))
@fvt.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}spurgeme"))

# @fvt.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}purgeme"))

async def spurgeme(delme):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = Spurgeme\n\nCommand:\n\n.spurgeme <count> | silent delete x count of your latest message."
    if delme.sender_id in SMEX_USERS:
        """ For .purgeme, delete x count of your latest message."""
        message = delme.text
        count = int(message[10:])
        i = 1

        async for message in delme.client.iter_messages(delme.chat_id,
                                                    from_user='me'):
            if i > count + 1:
                break
            i = i + 1
            await message.delete()

        """
        smsg = await delme.client.send_message(
            delme.chat_id,
            "`Purge complete!` Purged " + str(count) + " messages.",
        )
        
        if BOTLOG:
            await delme.client.send_message(
                BOTLOG_CHATID,
                "#PURGEME \nPurge of " + str(count) + " messages done successfully.")

        await sleep(2)
        i = 1
        await smsg.delete()
        """


# ======================== [PINX!]========================     
# v3.0
# var handler



@idk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pinx$"))
@ydk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pinx$"))
@wdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pinx$"))
@sdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pinx$"))
@adk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pinx$"))
@bdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pinx$"))
@cdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pinx$"))
@edk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pinx$"))
@hdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pinx$"))
@ddk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pinx$"))
@vkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pinx$"))
@kkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pinx$"))
@lkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pinx$"))
@mkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pinx$"))
@sid.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pinx$"))
@shy.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pinx$"))
@aan.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pinx$"))
@ake.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pinx$"))
@eel.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pinx$"))
@khu.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pinx$"))
@shi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pinx$"))
@yaa.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pinx$"))
@dav.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pinx$"))
@raj.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pinx$"))
@put.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pinx$"))
@tsi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pinx$"))
@tsf.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pinx$"))
@teg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pinx$"))
@tnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pinx$"))
@tth.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pinx$"))
@ton.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pinx$"))
@ttw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pinx$"))
@ttr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pinx$"))
@tfr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pinx$"))
@tfv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pinx$"))
@tsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pinx$"))
@tsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pinx$"))
@ttg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pinx$"))
@ttn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pinx$"))
@fft.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pinx$"))
@ffo.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pinx$"))
@ftw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pinx$"))
@ftr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pinx$"))
@ffr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pinx$"))
@ffv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pinx$"))
@fsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pinx$"))
@fsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pinx$"))
@feg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pinx$"))
@fnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pinx$"))
@fvt.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pinx$"))


async def ping(e):
    if e.sender_id in SMEX_USERS:
        start = datetime.now()
        text = "Ponx!"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"『 P͛o͛n͛x͛ 』⏤⏤͟͟★\n`{ms}` 𝗺𝘀")

"""        
# =====[ABSEN V1.0]=====        
        
@idk.on(events.NewMessage(incoming=True, pattern=r"[\.\/\!]absen((1)$|(\s+.*))"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"[\.\/\!]absen((2)$|(\s+.*))"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"[\.\/\!]absen((3)$|(\s+.*))"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"[\.\/\!]absen((4)$|(\s+.*))"))
@adk.on(events.NewMessage(incoming=True, pattern=r"[\.\/\!]absen((5)$|(\s+.*))"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"[\.\/\!]absen((6)$|(\s+.*))"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"[\.\/\!]absen((7)$|(\s+.*))"))
@edk.on(events.NewMessage(incoming=True, pattern=r"[\.\/\!]absen((8)$|(\s+.*))"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"[\.\/\!]absen((9)$|(\s+.*))"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"[\.\/\!]absen((10)$|(\s+.*))"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"[\.\/\!]absen((11)$|(\s+.*))"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"[\.\/\!]absen((12)$|(\s+.*))"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"[\.\/\!]absen((13)$|(\s+.*))"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"[\.\/\!]absen((14)$|(\s+.*))"))
@sid.on(events.NewMessage(incoming=True, pattern=r"[\.\/\!]absen((15)$|(\s+.*))"))
@shy.on(events.NewMessage(incoming=True, pattern=r"[\.\/\!]absen((16)$|(\s+.*))"))
@aan.on(events.NewMessage(incoming=True, pattern=r"[\.\/\!]absen((17)$|(\s+.*))"))
@ake.on(events.NewMessage(incoming=True, pattern=r"[\.\/\!]absen((18)$|(\s+.*))"))
@eel.on(events.NewMessage(incoming=True, pattern=r"[\.\/\!]absen((19)$|(\s+.*))"))
@khu.on(events.NewMessage(incoming=True, pattern=r"[\.\/\!]absen((20)$|(\s+.*))"))
@shi.on(events.NewMessage(incoming=True, pattern=r"[\.\/\!]absen((21)$|(\s+.*))"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"[\.\/\!]absen((22)$|(\s+.*))"))
@dav.on(events.NewMessage(incoming=True, pattern=r"[\.\/\!]absen((23)$|(\s+.*))"))
@raj.on(events.NewMessage(incoming=True, pattern=r"[\.\/\!]absen((24)$|(\s+.*))"))
@put.on(events.NewMessage(incoming=True, pattern=r"[\.\/\!]absen((25)$|(\s+.*))"))
@tsi.on(events.NewMessage(incoming=True, pattern=r"[\.\/\!]absen((26)$|(\s+.*))"))
@tsf.on(events.NewMessage(incoming=True, pattern=r"[\.\/\!]absen((27)$|(\s+.*))"))
@teg.on(events.NewMessage(incoming=True, pattern=r"[\.\/\!]absen((28)$|(\s+.*))"))
@tnn.on(events.NewMessage(incoming=True, pattern=r"[\.\/\!]absen((29)$|(\s+.*))"))
@tth.on(events.NewMessage(incoming=True, pattern=r"[\.\/\!]absen((30)$|(\s+.*))"))
@ton.on(events.NewMessage(incoming=True, pattern=r"[\.\/\!]absen((31)$|(\s+.*))"))
@ttw.on(events.NewMessage(incoming=True, pattern=r"[\.\/\!]absen((32)$|(\s+.*))"))
@ttr.on(events.NewMessage(incoming=True, pattern=r"[\.\/\!]absen((33)$|(\s+.*))"))
@tfr.on(events.NewMessage(incoming=True, pattern=r"[\.\/\!]absen((34)$|(\s+.*))"))
@tfv.on(events.NewMessage(incoming=True, pattern=r"[\.\/\!]absen((35)$|(\s+.*))"))
@tsx.on(events.NewMessage(incoming=True, pattern=r"[\.\/\!]absen((36)$|(\s+.*))"))
@tsv.on(events.NewMessage(incoming=True, pattern=r"[\.\/\!]absen((37)$|(\s+.*))"))
@ttg.on(events.NewMessage(incoming=True, pattern=r"[\.\/\!]absen((38)$|(\s+.*))"))
@ttn.on(events.NewMessage(incoming=True, pattern=r"[\.\/\!]absen((39)$|(\s+.*))"))
@fft.on(events.NewMessage(incoming=True, pattern=r"[\.\/\!]absen((40)$|(\s+.*))"))
@ffo.on(events.NewMessage(incoming=True, pattern=r"[\.\/\!]absen((41)$|(\s+.*))"))
@ftw.on(events.NewMessage(incoming=True, pattern=r"[\.\/\!]absen((42)$|(\s+.*))"))
@ftr.on(events.NewMessage(incoming=True, pattern=r"[\.\/\!]absen((43)$|(\s+.*))"))
@ffr.on(events.NewMessage(incoming=True, pattern=r"[\.\/\!]absen((44)$|(\s+.*))"))
@ffv.on(events.NewMessage(incoming=True, pattern=r"[\.\/\!]absen((45)$|(\s+.*))"))
@fsx.on(events.NewMessage(incoming=True, pattern=r"[\.\/\!]absen((46)$|(\s+.*))"))
@fsv.on(events.NewMessage(incoming=True, pattern=r"[\.\/\!]absen((47)$|(\s+.*))"))
@feg.on(events.NewMessage(incoming=True, pattern=r"[\.\/\!]absen((48)$|(\s+.*))"))
@fnn.on(events.NewMessage(incoming=True, pattern=r"[\.\/\!]absen((49)$|(\s+.*))"))
@fvt.on(events.NewMessage(incoming=True, pattern=r"[\.\/\!]absen((50)$|(\s+.*))")) 

async def absen(e):
    if e.sender_id in SMEX_USERS:
        start = datetime.now()
        text = "Hadir!"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"𝙃𝙖𝙙𝙞𝙧 ˁ˚ᴥ˚ˀ\n`{ms}` 𝗺𝘀")
"""    

# =====[RABSEN V2.0]=====  


@idk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabsen((01)$|(\s+.*))"))
@ydk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabsen((02)$|(\s+.*))"))
@wdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabsen((03)$|(\s+.*))"))
@sdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabsen((04)$|(\s+.*))"))
@adk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabsen((05)$|(\s+.*))"))
@bdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabsen((06)$|(\s+.*))"))
@cdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabsen((07)$|(\s+.*))"))
@edk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabsen((08)$|(\s+.*))"))
@hdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabsen((09)$|(\s+.*))"))
@ddk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabsen((10)$|(\s+.*))"))
@vkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabsen((11)$|(\s+.*))"))
@kkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabsen((12)$|(\s+.*))"))
@lkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabsen((13)$|(\s+.*))"))
@mkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabsen((14)$|(\s+.*))"))
@sid.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabsen((15)$|(\s+.*))"))
@shy.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabsen((16)$|(\s+.*))"))
@aan.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabsen((17)$|(\s+.*))"))
@ake.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabsen((18)$|(\s+.*))"))
@eel.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabsen((19)$|(\s+.*))"))
@khu.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabsen((20)$|(\s+.*))"))
@shi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabsen((21)$|(\s+.*))"))
@yaa.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabsen((22)$|(\s+.*))"))
@dav.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabsen((23)$|(\s+.*))"))
@raj.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabsen((24)$|(\s+.*))"))
@put.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabsen((25)$|(\s+.*))"))
@tsi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabsen((26)$|(\s+.*))"))
@tsf.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabsen((27)$|(\s+.*))"))
@teg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabsen((28)$|(\s+.*))"))
@tnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabsen((29)$|(\s+.*))"))
@tth.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabsen((30)$|(\s+.*))"))
@ton.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabsen((31)$|(\s+.*))"))
@ttw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabsen((32)$|(\s+.*))"))
@ttr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabsen((33)$|(\s+.*))"))
@tfr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabsen((34)$|(\s+.*))"))
@tfv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabsen((35)$|(\s+.*))"))
@tsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabsen((36)$|(\s+.*))"))
@tsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabsen((37)$|(\s+.*))"))
@ttg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabsen((38)$|(\s+.*))"))
@ttn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabsen((39)$|(\s+.*))"))
@fft.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabsen((40)$|(\s+.*))"))
@ffo.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabsen((41)$|(\s+.*))"))
@ftw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabsen((42)$|(\s+.*))"))
@ftr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabsen((43)$|(\s+.*))"))
@ffr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabsen((44)$|(\s+.*))"))
@ffv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabsen((45)$|(\s+.*))"))
@fsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabsen((46)$|(\s+.*))"))
@fsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabsen((47)$|(\s+.*))"))
@feg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabsen((48)$|(\s+.*))"))
@fnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabsen((49)$|(\s+.*))"))
@fvt.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabsen((50)$|(\s+.*))"))


async def rabsen(e):
    if e.sender_id in SMEX_USERS:
        reply = random.choice(RABSEN)
        start = datetime.now()
        text = "Hadir!"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"**{reply}**\n`{ms}` 𝗺𝘀")
    
        
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


# =====[INVITEALL V2.0]=====  
            
@idk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}inviteall(01)?(?: |$)(.*)"))
@ydk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}inviteall(02)?(?: |$)(.*)"))
@wdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}inviteall(03)?(?: |$)(.*)"))
@sdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}inviteall(04)?(?: |$)(.*)"))
@adk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}inviteall(05)?(?: |$)(.*)"))
@bdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}inviteall(06)?(?: |$)(.*)"))
@cdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}inviteall(07)?(?: |$)(.*)"))
@edk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}inviteall(08)?(?: |$)(.*)"))
@hdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}inviteall(09)?(?: |$)(.*)"))
@ddk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}inviteall(10)?(?: |$)(.*)"))
@vkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}inviteall(11)?(?: |$)(.*)"))
@kkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}inviteall(12)?(?: |$)(.*)"))
@lkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}inviteall(13)?(?: |$)(.*)"))
@mkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}inviteall(14)?(?: |$)(.*)"))
@sid.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}inviteall(15)?(?: |$)(.*)"))
@shy.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}inviteall(16)?(?: |$)(.*)"))
@aan.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}inviteall(17)?(?: |$)(.*)"))
@ake.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}inviteall(18)?(?: |$)(.*)"))
@eel.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}inviteall(19)?(?: |$)(.*)"))
@khu.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}inviteall(20)?(?: |$)(.*)"))
@shi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}inviteall(21)?(?: |$)(.*)"))
@yaa.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}inviteall(22)?(?: |$)(.*)"))
@dav.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}inviteall(23)?(?: |$)(.*)"))
@raj.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}inviteall(24)?(?: |$)(.*)"))
@put.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}inviteall(25)?(?: |$)(.*)"))
@tsi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}inviteall(26)?(?: |$)(.*)"))
@tsf.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}inviteall(27)?(?: |$)(.*)"))
@teg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}inviteall(28)?(?: |$)(.*)"))
@tnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}inviteall(29)?(?: |$)(.*)"))
@tth.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}inviteall(30)?(?: |$)(.*)"))
@ton.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}inviteall(31)?(?: |$)(.*)"))
@ttw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}inviteall(32)?(?: |$)(.*)"))
@ttr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}inviteall(33)?(?: |$)(.*)"))
@tfr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}inviteall(34)?(?: |$)(.*)"))
@tfv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}inviteall(35)?(?: |$)(.*)"))
@tsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}inviteall(36)?(?: |$)(.*)"))
@tsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}inviteall(37)?(?: |$)(.*)"))
@ttg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}inviteall(38)?(?: |$)(.*)"))
@ttn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}inviteall(39)?(?: |$)(.*)"))
@fft.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}inviteall(40)?(?: |$)(.*)"))
@ffo.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}inviteall(41)?(?: |$)(.*)"))
@ftw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}inviteall(42)?(?: |$)(.*)"))
@ftr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}inviteall(43)?(?: |$)(.*)"))
@ffr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}inviteall(44)?(?: |$)(.*)"))
@ffv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}inviteall(45)?(?: |$)(.*)"))
@fsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}inviteall(46)?(?: |$)(.*)"))
@fsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}inviteall(47)?(?: |$)(.*)"))
@feg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}inviteall(48)?(?: |$)(.*)"))
@fnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}inviteall(49)?(?: |$)(.*)"))
@fvt.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}inviteall(50)?(?: |$)(.*)"))



async def get_users(event):
    if event.sender_id in SMEX_USERS:
        rkp = await event.reply("`processing...`")
    else:
        rkp = await event.reply("`processing...`")
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



# ====================== CONSTANT ===============================
INVALID_MEDIA = "```The extension of the media entity is invalid.```"
PP_CHANGED = "```Profile picture changed successfully.```"
PP_TOO_SMOL = "```This image is too small, use a bigger image.```"
PP_ERROR = "```Failure occured while processing image.```"

BIO_SUCCESS = "```Successfully edited Bio.```"

NAME_OK = "```Your name was succesfully changed.```"
USERNAME_SUCCESS = "```Your username was succesfully changed.```"
USERNAME_TAKEN = "```This username is already taken.```"
# ===============================================================

# ==== SET PHOTO PROFIL


@idk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setpfp$"))
@ydk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setpfp$"))
@wdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setpfp$"))
@sdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setpfp$"))
@adk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setpfp$"))
@bdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setpfp$"))
@cdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setpfp$"))
@edk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setpfp$"))
@hdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setpfp$"))
@ddk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setpfp$"))
@vkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setpfp$"))
@kkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setpfp$"))
@lkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setpfp$"))
@mkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setpfp$"))
@sid.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setpfp$"))
@shy.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setpfp$"))
@aan.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setpfp$"))
@ake.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setpfp$"))
@eel.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setpfp$"))
@khu.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setpfp$"))
@shi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setpfp$"))
@yaa.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setpfp$"))
@dav.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setpfp$"))
@raj.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setpfp$"))
@put.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setpfp$"))
@tsi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setpfp$"))
@tsf.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setpfp$"))
@teg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setpfp$"))
@tnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setpfp$"))
@tth.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setpfp$"))
@ton.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setpfp$"))
@ttw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setpfp$"))
@ttr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setpfp$"))
@tfr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setpfp$"))
@tfv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setpfp$"))
@tsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setpfp$"))
@tsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setpfp$"))
@ttg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setpfp$"))
@ttn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setpfp$"))
@fft.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setpfp$"))
@ffo.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setpfp$"))
@ftw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setpfp$"))
@ftr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setpfp$"))
@ffr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setpfp$"))
@ffv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setpfp$"))
@fsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setpfp$"))
@fsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setpfp$"))
@feg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setpfp$"))
@fnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setpfp$"))
@fvt.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setpfp$"))


# @bot.on(geezbot_cmd(outgoing=True, pattern="setpfp$"))
async def set_profilepic(propic):
    if propic.sender_id in SMEX_USERS:    
        """ For .profilepic command, change your profile picture in Telegram. """
        replymsg = await propic.get_reply_message()
        photo = None
        if replymsg.media:
            if isinstance(replymsg.media, MessageMediaPhoto):
                photo = await propic.client.download_media(message=replymsg.photo)
            elif "image" in replymsg.media.document.mime_type.split('/'):
                photo = await propic.client.download_file(replymsg.media.document)
            else:
                await propic.reply(INVALID_MEDIA)

        if photo:
            try:
                await propic.client(
                    UploadProfilePhotoRequest(await
                                              propic.client.upload_file(photo)))
                os.remove(photo)
                await propic.reply(PP_CHANGED)
            except PhotoCropSizeSmallError:
                await propic.reply(PP_TOO_SMOL)
            except ImageProcessFailedError:
                await propic.reply(PP_ERROR)
            except PhotoExtInvalidError:
                await propic.reply(INVALID_MEDIA)


# ==== DELETE PHOTO PROFIL

@idk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delpfp ?(.*)"))
@ydk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delpfp ?(.*)"))
@wdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delpfp ?(.*)"))
@sdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delpfp ?(.*)"))
@adk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delpfp ?(.*)"))
@bdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delpfp ?(.*)"))
@cdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delpfp ?(.*)"))
@edk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delpfp ?(.*)"))
@hdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delpfp ?(.*)"))
@ddk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delpfp ?(.*)"))
@vkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delpfp ?(.*)"))
@kkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delpfp ?(.*)"))
@lkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delpfp ?(.*)"))
@mkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delpfp ?(.*)"))
@sid.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delpfp ?(.*)"))
@shy.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delpfp ?(.*)"))
@aan.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delpfp ?(.*)"))
@ake.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delpfp ?(.*)"))
@eel.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delpfp ?(.*)"))
@khu.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delpfp ?(.*)"))
@shi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delpfp ?(.*)"))
@yaa.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delpfp ?(.*)"))
@dav.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delpfp ?(.*)"))
@raj.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delpfp ?(.*)"))
@put.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delpfp ?(.*)"))
@tsi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delpfp ?(.*)"))
@tsf.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delpfp ?(.*)"))
@teg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delpfp ?(.*)"))
@tnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delpfp ?(.*)"))
@tth.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delpfp ?(.*)"))
@ton.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delpfp ?(.*)"))
@ttw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delpfp ?(.*)"))
@ttr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delpfp ?(.*)"))
@tfr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delpfp ?(.*)"))
@tfv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delpfp ?(.*)"))
@tsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delpfp ?(.*)"))
@tsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delpfp ?(.*)"))
@ttg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delpfp ?(.*)"))
@ttn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delpfp ?(.*)"))
@fft.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delpfp ?(.*)"))
@ffo.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delpfp ?(.*)"))
@ftw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delpfp ?(.*)"))
@ftr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delpfp ?(.*)"))
@ffr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delpfp ?(.*)"))
@ffv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delpfp ?(.*)"))
@fsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delpfp ?(.*)"))
@fsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delpfp ?(.*)"))
@feg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delpfp ?(.*)"))
@fnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delpfp ?(.*)"))
@fvt.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}delpfp ?(.*)"))

# credit to geez, ultroid

async def remove_profilepic(delpfp):
    if delpfp.sender_id in SMEX_USERS:
        """ For .delpfp command, delete your current profile picture in Telegram. """
        ok = await delpfp.reply("...")
        group = delpfp.text[8:]
        if group == 'all':
            lim = 0
        elif group.isdigit():
            lim = int(group)
        else:
            lim = 1

        pfplist = await delpfp.client.get_profile_photos("me", limit=lim)

        await delpfp.client(DeletePhotosRequest(pfplist))
        await ok.edit(
            f"`Successfully deleted {len(pfplist)} profile picture(s).`")




# ==== SET USERNAME

@idk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}username (.*)"))
@ydk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}username (.*)"))
@wdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}username (.*)"))
@sdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}username (.*)"))
@adk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}username (.*)"))
@bdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}username (.*)"))
@cdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}username (.*)"))
@edk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}username (.*)"))
@hdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}username (.*)"))
@ddk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}username (.*)"))
@vkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}username (.*)"))
@kkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}username (.*)"))
@lkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}username (.*)"))
@mkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}username (.*)"))
@sid.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}username (.*)"))
@shy.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}username (.*)"))
@aan.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}username (.*)"))
@ake.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}username (.*)"))
@eel.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}username (.*)"))
@khu.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}username (.*)"))
@shi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}username (.*)"))
@yaa.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}username (.*)"))
@dav.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}username (.*)"))
@raj.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}username (.*)"))
@put.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}username (.*)"))
@tsi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}username (.*)"))
@tsf.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}username (.*)"))
@teg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}username (.*)"))
@tnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}username (.*)"))
@tth.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}username (.*)"))
@ton.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}username (.*)"))
@ttw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}username (.*)"))
@ttr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}username (.*)"))
@tfr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}username (.*)"))
@tfv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}username (.*)"))
@tsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}username (.*)"))
@tsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}username (.*)"))
@ttg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}username (.*)"))
@ttn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}username (.*)"))
@fft.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}username (.*)"))
@ffo.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}username (.*)"))
@ftw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}username (.*)"))
@ftr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}username (.*)"))
@ffr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}username (.*)"))
@ffv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}username (.*)"))
@fsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}username (.*)"))
@fsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}username (.*)"))
@feg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}username (.*)"))
@fnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}username (.*)"))
@fvt.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}username (.*)"))

# credit to geez, ultroid, man userbot

async def update_username(username):
    if username.sender_id in SMEX_USERS:
        """ For .username command, set a new username in Telegram. """
        newusername = username.pattern_match.group(1)
        try:
            await username.client(UpdateUsernameRequest(newusername))
            await username.reply(USERNAME_SUCCESS)
        except UsernameOccupiedError:
            await username.reply(USERNAME_TAKEN)



# =======================[SET BIOGRAPH]=======================
# Credits to Paperplane, Geez


@idk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setbio (.*)"))
@ydk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setbio (.*)"))
@wdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setbio (.*)"))
@sdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setbio (.*)"))
@adk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setbio (.*)"))
@bdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setbio (.*)"))
@cdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setbio (.*)"))
@edk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setbio (.*)"))
@hdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setbio (.*)"))
@ddk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setbio (.*)"))
@vkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setbio (.*)"))
@kkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setbio (.*)"))
@lkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setbio (.*)"))
@mkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setbio (.*)"))
@sid.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setbio (.*)"))
@shy.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setbio (.*)"))
@aan.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setbio (.*)"))
@ake.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setbio (.*)"))
@eel.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setbio (.*)"))
@khu.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setbio (.*)"))
@shi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setbio (.*)"))
@yaa.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setbio (.*)"))
@dav.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setbio (.*)"))
@raj.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setbio (.*)"))
@put.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setbio (.*)"))
@tsi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setbio (.*)"))
@tsf.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setbio (.*)"))
@teg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setbio (.*)"))
@tnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setbio (.*)"))
@tth.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setbio (.*)"))
@ton.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setbio (.*)"))
@ttw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setbio (.*)"))
@ttr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setbio (.*)"))
@tfr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setbio (.*)"))
@tfv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setbio (.*)"))
@tsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setbio (.*)"))
@tsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setbio (.*)"))
@ttg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setbio (.*)"))
@ttn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setbio (.*)"))
@fft.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setbio (.*)"))
@ffo.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setbio (.*)"))
@ftw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setbio (.*)"))
@ftr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setbio (.*)"))
@ffr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setbio (.*)"))
@ffv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setbio (.*)"))
@fsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setbio (.*)"))
@fsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setbio (.*)"))
@feg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setbio (.*)"))
@fnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setbio (.*)"))
@fvt.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setbio (.*)"))

async def set_biograph(setbio):
    if setbio.sender_id in SMEX_USERS:
        """ For .setbio command, set a new bio for your profile in Telegram. """
        newbio = setbio.pattern_match.group(1)
        await setbio.client(UpdateProfileRequest(about=newbio))
        await setbio.edit(BIO_SUCCESS)




# ==== COUNT CHATS

# STRINGS
STAT_INDICATION = "`Collecting stats, Please wait....`"

# Functions
def user_full_name(user):
    names = [user.first_name, user.last_name]
    names = [i for i in list(names) if i]
    return " ".join(names)


def inline_mention(user):
    full_name = user_full_name(user) or "No Name"
    return f"[{full_name}](tg://user?id={user.id})"


# ====== STATS

@idk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}stats$"))
@ydk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}stats$"))
@wdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}stats$"))
@sdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}stats$"))
@adk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}stats$"))
@bdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}stats$"))
@cdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}stats$"))
@edk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}stats$"))
@hdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}stats$"))
@ddk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}stats$"))
@vkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}stats$"))
@kkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}stats$"))
@lkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}stats$"))
@mkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}stats$"))
@sid.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}stats$"))
@shy.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}stats$"))
@aan.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}stats$"))
@ake.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}stats$"))
@eel.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}stats$"))
@khu.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}stats$"))
@shi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}stats$"))
@yaa.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}stats$"))
@dav.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}stats$"))
@raj.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}stats$"))
@put.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}stats$"))
@tsi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}stats$"))
@tsf.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}stats$"))
@teg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}stats$"))
@tnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}stats$"))
@tth.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}stats$"))
@ton.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}stats$"))
@ttw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}stats$"))
@ttr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}stats$"))
@tfr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}stats$"))
@tfv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}stats$"))
@tsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}stats$"))
@tsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}stats$"))
@ttg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}stats$"))
@ttn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}stats$"))
@fft.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}stats$"))
@ffo.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}stats$"))
@ftw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}stats$"))
@ftr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}stats$"))
@ffr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}stats$"))
@ffv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}stats$"))
@fsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}stats$"))
@fsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}stats$"))
@feg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}stats$"))
@fnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}stats$"))
@fvt.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}stats$"))

# credit to geez, ultroid, man userbot

async def stats(event):
    if event.sender_id in SMEX_USERS:
        stat = await event.reply(STAT_INDICATION)
        start_time = time.time()
        private_chats = 0
        bots = 0
        groups = 0
        broadcast_channels = 0
        admin_in_groups = 0
        creator_in_groups = 0
        admin_in_broadcast_channels = 0
        creator_in_channels = 0
        unread_mentions = 0
        unread = 0
        dialog: Dialog
        async for dialog in event.client.iter_dialogs():
            entity = dialog.entity
            if isinstance(entity, Channel) and entity.broadcast:
                broadcast_channels += 1
                if entity.creator or entity.admin_rights:
                    admin_in_broadcast_channels += 1
                if entity.creator:
                    creator_in_channels += 1
            elif (
                isinstance(entity, Channel)
                and entity.megagroup
                or not isinstance(entity, Channel)
                and not isinstance(entity, User)
                and isinstance(entity, Chat)
            ):
                groups += 1
                if entity.creator or entity.admin_rights:
                    admin_in_groups += 1
                if entity.creator:
                    creator_in_groups += 1
            elif not isinstance(entity, Channel) and isinstance(entity, User):
                private_chats += 1
                if entity.bot:
                    bots += 1
            unread_mentions += dialog.unread_mentions_count
            unread += dialog.unread_count
        stop_time = time.time() - start_time
        full_name = inline_mention(await event.client.get_me())
        response = f"📊 **Stats for {full_name}** \n\n"
        response += f"**Private Chats:** {private_chats} \n"
        response += f"   • `Users: {private_chats - bots}` \n"
        response += f"   • `Bots: {bots}` \n"
        response += f"**Groups:** {groups} \n"
        response += f"**Channels:** {broadcast_channels} \n"
        response += f"**Admin in Groups:** {admin_in_groups} \n"
        response += f"   • `Creator: {creator_in_groups}` \n"
        response += f"   • `Admin Rights: {admin_in_groups - creator_in_groups}` \n"
        response += f"**Admin in Channels:** {admin_in_broadcast_channels} \n"
        response += f"   • `Creator: {creator_in_channels}` \n"
        response += (
            f"   • `Admin Rights: {admin_in_broadcast_channels - creator_in_channels}` \n"
        )
        response += f"**Unread:** {unread} \n"
        response += f"**Unread Mentions:** {unread_mentions} \n\n"
        response += f"⏱ __It Took:__ {stop_time:.02f}s \n"
        await stat.edit(response)



# ========[name changer]


@idk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setname ?((.|//)*)"))
@ydk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setname ?((.|//)*)"))
@wdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setname ?((.|//)*)"))
@sdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setname ?((.|//)*)"))
@adk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setname ?((.|//)*)"))
@bdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setname ?((.|//)*)"))
@cdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setname ?((.|//)*)"))
@edk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setname ?((.|//)*)"))
@hdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setname ?((.|//)*)"))
@ddk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setname ?((.|//)*)"))
@vkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setname ?((.|//)*)"))
@kkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setname ?((.|//)*)"))
@lkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setname ?((.|//)*)"))
@mkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setname ?((.|//)*)"))
@sid.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setname ?((.|//)*)"))
@shy.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setname ?((.|//)*)"))
@aan.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setname ?((.|//)*)"))
@ake.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setname ?((.|//)*)"))
@eel.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setname ?((.|//)*)"))
@khu.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setname ?((.|//)*)"))
@shi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setname ?((.|//)*)"))
@yaa.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setname ?((.|//)*)"))
@dav.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setname ?((.|//)*)"))
@raj.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setname ?((.|//)*)"))
@put.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setname ?((.|//)*)"))
@tsi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setname ?((.|//)*)"))
@tsf.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setname ?((.|//)*)"))
@teg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setname ?((.|//)*)"))
@tnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setname ?((.|//)*)"))
@tth.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setname ?((.|//)*)"))
@ton.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setname ?((.|//)*)"))
@ttw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setname ?((.|//)*)"))
@ttr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setname ?((.|//)*)"))
@tfr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setname ?((.|//)*)"))
@tfv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setname ?((.|//)*)"))
@tsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setname ?((.|//)*)"))
@tsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setname ?((.|//)*)"))
@ttg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setname ?((.|//)*)"))
@ttn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setname ?((.|//)*)"))
@fft.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setname ?((.|//)*)"))
@ffo.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setname ?((.|//)*)"))
@ftw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setname ?((.|//)*)"))
@ftr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setname ?((.|//)*)"))
@ffr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setname ?((.|//)*)"))
@ffv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setname ?((.|//)*)"))
@fsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setname ?((.|//)*)"))
@fsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setname ?((.|//)*)"))
@feg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setname ?((.|//)*)"))
@fnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setname ?((.|//)*)"))
@fvt.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}setname ?((.|//)*)"))


# ported by @AlphaXProject from ultroid plugin

async def setname(event):
    if event.sender_id in SMEX_USERS:
        ok = await event.reply("...")
        names = event.pattern_match.group(1)
        first_name = names
        last_name = ""
        if "//" in names:
            first_name, last_name = names.split("//", 1)
        try:
            await event.client(
                UpdateProfileRequest(
                    first_name=first_name,
                    last_name=last_name,
                ),
            )
            await ok.edit(f"Name changed to `{names}`")
        except Exception as ex:
            await ok.edit("Error occured.\n`{}`".format(str(ex)))


# ===== DM ========


@idk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dm(?: |$)(.*)"))
@ydk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dm(?: |$)(.*)"))
@wdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dm(?: |$)(.*)"))
@sdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dm(?: |$)(.*)"))
@adk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dm(?: |$)(.*)"))
@bdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dm(?: |$)(.*)"))
@cdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dm(?: |$)(.*)"))
@edk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dm(?: |$)(.*)"))
@hdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dm(?: |$)(.*)"))
@ddk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dm(?: |$)(.*)"))
@vkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dm(?: |$)(.*)"))
@kkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dm(?: |$)(.*)"))
@lkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dm(?: |$)(.*)"))
@mkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dm(?: |$)(.*)"))
@sid.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dm(?: |$)(.*)"))
@shy.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dm(?: |$)(.*)"))
@aan.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dm(?: |$)(.*)"))
@ake.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dm(?: |$)(.*)"))
@eel.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dm(?: |$)(.*)"))
@khu.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dm(?: |$)(.*)"))
@shi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dm(?: |$)(.*)"))
@yaa.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dm(?: |$)(.*)"))
@dav.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dm(?: |$)(.*)"))
@raj.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dm(?: |$)(.*)"))
@put.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dm(?: |$)(.*)"))
@tsi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dm(?: |$)(.*)"))
@tsf.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dm(?: |$)(.*)"))
@teg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dm(?: |$)(.*)"))
@tnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dm(?: |$)(.*)"))
@tth.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dm(?: |$)(.*)"))
@ton.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dm(?: |$)(.*)"))
@ttw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dm(?: |$)(.*)"))
@ttr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dm(?: |$)(.*)"))
@tfr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dm(?: |$)(.*)"))
@tfv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dm(?: |$)(.*)"))
@tsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dm(?: |$)(.*)"))
@tsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dm(?: |$)(.*)"))
@ttg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dm(?: |$)(.*)"))
@ttn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dm(?: |$)(.*)"))
@fft.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dm(?: |$)(.*)"))
@ffo.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dm(?: |$)(.*)"))
@ftw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dm(?: |$)(.*)"))
@ftr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dm(?: |$)(.*)"))
@ffr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dm(?: |$)(.*)"))
@ffv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dm(?: |$)(.*)"))
@fsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dm(?: |$)(.*)"))
@fsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dm(?: |$)(.*)"))
@feg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dm(?: |$)(.*)"))
@fnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dm(?: |$)(.*)"))
@fvt.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}dm(?: |$)(.*)"))


# credit to geez, ultroid, man userbot

async def remoteaccess(event):
    if event.sender_id in SMEX_USERS:
        p = event.pattern_match.group(1)
        m = p.split(" ")

        chat_id = m[0]
        try:
            chat_id = int(chat_id)
        except BaseException:

            pass

        msg = ""
        mssg = await event.get_reply_message()
        if event.reply_to_msg_id:
            await event.client.send_message(chat_id, mssg)
            await event.reply("`Success Mengirim Pesan Anda.`")
        for i in m[1:]:
            msg += i + " "
        if msg == "":
            return
        try:
            await event.client.send_message(chat_id, msg)
            await event.reply("`Success Mengirim Pesan Anda.`")
        except BaseException:
            await event.reply("**Terjadi Error. Gagal Mengirim Pesan.**")



# ===== GET MEMBER

@idk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}getmemb$"))
@ydk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}getmemb$"))
@wdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}getmemb$"))
@sdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}getmemb$"))
@adk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}getmemb$"))
@bdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}getmemb$"))
@cdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}getmemb$"))
@edk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}getmemb$"))
@hdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}getmemb$"))
@ddk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}getmemb$"))
@vkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}getmemb$"))
@kkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}getmemb$"))
@lkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}getmemb$"))
@mkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}getmemb$"))
@sid.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}getmemb$"))
@shy.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}getmemb$"))
@aan.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}getmemb$"))
@ake.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}getmemb$"))
@eel.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}getmemb$"))
@khu.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}getmemb$"))
@shi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}getmemb$"))
@yaa.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}getmemb$"))
@dav.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}getmemb$"))
@raj.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}getmemb$"))
@put.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}getmemb$"))
@tsi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}getmemb$"))
@tsf.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}getmemb$"))
@teg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}getmemb$"))
@tnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}getmemb$"))
@tth.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}getmemb$"))
@ton.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}getmemb$"))
@ttw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}getmemb$"))
@ttr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}getmemb$"))
@tfr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}getmemb$"))
@tfv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}getmemb$"))
@tsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}getmemb$"))
@tsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}getmemb$"))
@ttg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}getmemb$"))
@ttn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}getmemb$"))
@fft.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}getmemb$"))
@ffo.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}getmemb$"))
@ftw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}getmemb$"))
@ftr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}getmemb$"))
@ffr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}getmemb$"))
@ffv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}getmemb$"))
@fsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}getmemb$"))
@fsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}getmemb$"))
@feg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}getmemb$"))
@fnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}getmemb$"))
@fvt.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}getmemb$"))

# credit to geez, ultroid, man userbot, abdul

async def scrapmem(event):
    if event.sender_id in SMEX_USERS:
        # text = "`Mohon tunggu...`"
        chat = event.chat_id
        y = await event.reply("`Mohon tunggu...`" )
        client = event.client
        members = await client.get_participants(chat, aggressive=True)

        with open("members.csv", "w", encoding="UTF-8") as f:
            writer = csv.writer(f, delimiter=",", lineterminator="\n")
            writer.writerow(["user_id", "hash"])
            for member in members:
                writer.writerow([member.id, member.access_hash])
        await y.edit(f"`Berhasil Mengumpulkan Member..`")


# ===== ADD MEMBER

@idk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}addmemb$"))
@ydk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}addmemb$"))
@wdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}addmemb$"))
@sdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}addmemb$"))
@adk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}addmemb$"))
@bdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}addmemb$"))
@cdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}addmemb$"))
@edk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}addmemb$"))
@hdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}addmemb$"))
@ddk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}addmemb$"))
@vkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}addmemb$"))
@kkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}addmemb$"))
@lkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}addmemb$"))
@mkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}addmemb$"))
@sid.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}addmemb$"))
@shy.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}addmemb$"))
@aan.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}addmemb$"))
@ake.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}addmemb$"))
@eel.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}addmemb$"))
@khu.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}addmemb$"))
@shi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}addmemb$"))
@yaa.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}addmemb$"))
@dav.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}addmemb$"))
@raj.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}addmemb$"))
@put.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}addmemb$"))
@tsi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}addmemb$"))
@tsf.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}addmemb$"))
@teg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}addmemb$"))
@tnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}addmemb$"))
@tth.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}addmemb$"))
@ton.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}addmemb$"))
@ttw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}addmemb$"))
@ttr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}addmemb$"))
@tfr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}addmemb$"))
@tfv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}addmemb$"))
@tsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}addmemb$"))
@tsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}addmemb$"))
@ttg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}addmemb$"))
@ttn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}addmemb$"))
@fft.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}addmemb$"))
@ffo.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}addmemb$"))
@ftw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}addmemb$"))
@ftr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}addmemb$"))
@ffr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}addmemb$"))
@ffv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}addmemb$"))
@fsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}addmemb$"))
@fsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}addmemb$"))
@feg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}addmemb$"))
@fnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}addmemb$"))
@fvt.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}addmemb$"))

# credit to geez, ultroid, man userbot, abdul

async def admem(event):
    if event.sender_id in SMEX_USERS:
        # text = "`Proses Menambahkan 0 Member...`"
        x = await event.reply("`Proses Menambahkan 0 Member...`")
        chat = await event.get_chat()
        client = event.client
        users = []
        with open("members.csv", encoding="UTF-8") as f:
            rows = csv.reader(f, delimiter=",", lineterminator="\n")
            next(rows, None)
            for row in rows:
                user = {'id': int(row[0]), 'hash': int(row[1])}
                users.append(user)
        n = 0
        for user in users:
            n += 1
            if n % 10 == 0:
                await x.edit(f"`Mencapai 10 anggota, tunggu selama {900/60} menit`")
                await asyncio.sleep(900)
            try:
                userin = InputPeerUser(user['id'], user['hash'])
                await event.client(InviteToChannelRequest(chat, [userin]))
                await asyncio.sleep(random.randrange(5, 7))
                await x.edit(f"`Prosess Menambahkan {n} Member...`")
            except TypeError:
                n -= 1
                continue
            except UserAlreadyParticipantError:
                n -= 1
                continue
            except UserPrivacyRestrictedError:
                n -= 1
                continue
            except UserNotMutualContactError:
                n -= 1
                continue






# ========================[EVAL, EXEC, TERM]========================

# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#



import asyncio
from os import remove
from sys import executable



# ======[EVAL]======

@idk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}eval(?: |$|\n)([\s\S]*)"))
@ydk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}eval(?: |$|\n)([\s\S]*)"))
@wdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}eval(?: |$|\n)([\s\S]*)"))
@sdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}eval(?: |$|\n)([\s\S]*)"))
@adk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}eval(?: |$|\n)([\s\S]*)"))
@bdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}eval(?: |$|\n)([\s\S]*)"))
@cdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}eval(?: |$|\n)([\s\S]*)"))
@edk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}eval(?: |$|\n)([\s\S]*)"))
@hdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}eval(?: |$|\n)([\s\S]*)"))
@ddk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}eval(?: |$|\n)([\s\S]*)"))
@vkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}eval(?: |$|\n)([\s\S]*)"))
@kkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}eval(?: |$|\n)([\s\S]*)"))
@lkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}eval(?: |$|\n)([\s\S]*)"))
@mkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}eval(?: |$|\n)([\s\S]*)"))
@sid.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}eval(?: |$|\n)([\s\S]*)"))
@shy.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}eval(?: |$|\n)([\s\S]*)"))
@aan.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}eval(?: |$|\n)([\s\S]*)"))
@ake.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}eval(?: |$|\n)([\s\S]*)"))
@eel.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}eval(?: |$|\n)([\s\S]*)"))
@khu.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}eval(?: |$|\n)([\s\S]*)"))
@shi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}eval(?: |$|\n)([\s\S]*)"))
@yaa.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}eval(?: |$|\n)([\s\S]*)"))
@dav.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}eval(?: |$|\n)([\s\S]*)"))
@raj.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}eval(?: |$|\n)([\s\S]*)"))
@put.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}eval(?: |$|\n)([\s\S]*)"))
@tsi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}eval(?: |$|\n)([\s\S]*)"))
@tsf.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}eval(?: |$|\n)([\s\S]*)"))
@teg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}eval(?: |$|\n)([\s\S]*)"))
@tnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}eval(?: |$|\n)([\s\S]*)"))
@tth.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}eval(?: |$|\n)([\s\S]*)"))
@ton.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}eval(?: |$|\n)([\s\S]*)"))
@ttw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}eval(?: |$|\n)([\s\S]*)"))
@ttr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}eval(?: |$|\n)([\s\S]*)"))
@tfr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}eval(?: |$|\n)([\s\S]*)"))
@tfv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}eval(?: |$|\n)([\s\S]*)"))
@tsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}eval(?: |$|\n)([\s\S]*)"))
@tsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}eval(?: |$|\n)([\s\S]*)"))
@ttg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}eval(?: |$|\n)([\s\S]*)"))
@ttn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}eval(?: |$|\n)([\s\S]*)"))
@fft.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}eval(?: |$|\n)([\s\S]*)"))
@ffo.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}eval(?: |$|\n)([\s\S]*)"))
@ftw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}eval(?: |$|\n)([\s\S]*)"))
@ftr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}eval(?: |$|\n)([\s\S]*)"))
@ffr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}eval(?: |$|\n)([\s\S]*)"))
@ffv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}eval(?: |$|\n)([\s\S]*)"))
@fsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}eval(?: |$|\n)([\s\S]*)"))
@fsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}eval(?: |$|\n)([\s\S]*)"))
@feg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}eval(?: |$|\n)([\s\S]*)"))
@fnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}eval(?: |$|\n)([\s\S]*)"))
@fvt.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}eval(?: |$|\n)([\s\S]*)"))

async def evaluate(query):
    # eval
    usage = """✘ Plugin : Eval Teks
•  Perintah : <code>.eval 2 + 3</code>
•  Function : Evaluasi ekspresi mini"""
    if query.sender_id in SMEX_USERS:
        if query.is_channel and not query.is_group:
            return await query.reply("`Eval isn't permitted on channels`")

        if query.pattern_match.group(1):
            expression = query.pattern_match.group(1)
        else:
            return await query.reply(usage, parse_mode='html', link_preview=None)

        if expression in ("userbot.session", "config.env"):
            return await query.reply("`Itu evaluasi yang berbahaya! Tidak diperbolehkan!`")

        try:
            evaluation = str(eval(expression))
            if evaluation:
                if isinstance(evaluation, str):
                    if len(evaluation) >= 4096:
                        file = open("output.txt", "w+")
                        file.write(evaluation)
                        file.close()
                        await query.client.send_file(
                            query.chat_id,
                            "output.txt",
                            reply_to=query.id,
                            caption="`Output terlalu besar, mengirim sebagai file`",
                        )
                        remove("output.txt")
                        return
                    await query.reply(
                        "**Query : **\n`"
                        f"{expression}"
                        "`\n\n**Result : **\n`"
                        f"{evaluation}"
                        "`"
                    )
            else:
                await query.reply(
                    "**Query : **\n`"
                    f"{expression}"
                    "`\n\n**Result : **\n`Tidak Ada Hasil yang Dikembalikan/Salah`"
                )
        except Exception as err:
            await query.reply(
                "**Query : **\n`" f"{expression}" "`\n**Exception : **\n\n" f"`{err}`"
            )


# ======[EXEC]======


@idk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}exec(?: |$)([\s\S]*)"))
@ydk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}exec(?: |$)([\s\S]*)"))
@wdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}exec(?: |$)([\s\S]*)"))
@sdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}exec(?: |$)([\s\S]*)"))
@adk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}exec(?: |$)([\s\S]*)"))
@bdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}exec(?: |$)([\s\S]*)"))
@cdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}exec(?: |$)([\s\S]*)"))
@edk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}exec(?: |$)([\s\S]*)"))
@hdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}exec(?: |$)([\s\S]*)"))
@ddk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}exec(?: |$)([\s\S]*)"))
@vkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}exec(?: |$)([\s\S]*)"))
@kkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}exec(?: |$)([\s\S]*)"))
@lkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}exec(?: |$)([\s\S]*)"))
@mkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}exec(?: |$)([\s\S]*)"))
@sid.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}exec(?: |$)([\s\S]*)"))
@shy.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}exec(?: |$)([\s\S]*)"))
@aan.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}exec(?: |$)([\s\S]*)"))
@ake.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}exec(?: |$)([\s\S]*)"))
@eel.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}exec(?: |$)([\s\S]*)"))
@khu.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}exec(?: |$)([\s\S]*)"))
@shi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}exec(?: |$)([\s\S]*)"))
@yaa.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}exec(?: |$)([\s\S]*)"))
@dav.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}exec(?: |$)([\s\S]*)"))
@raj.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}exec(?: |$)([\s\S]*)"))
@put.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}exec(?: |$)([\s\S]*)"))
@tsi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}exec(?: |$)([\s\S]*)"))
@tsf.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}exec(?: |$)([\s\S]*)"))
@teg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}exec(?: |$)([\s\S]*)"))
@tnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}exec(?: |$)([\s\S]*)"))
@tth.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}exec(?: |$)([\s\S]*)"))
@ton.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}exec(?: |$)([\s\S]*)"))
@ttw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}exec(?: |$)([\s\S]*)"))
@ttr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}exec(?: |$)([\s\S]*)"))
@tfr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}exec(?: |$)([\s\S]*)"))
@tfv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}exec(?: |$)([\s\S]*)"))
@tsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}exec(?: |$)([\s\S]*)"))
@tsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}exec(?: |$)([\s\S]*)"))
@ttg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}exec(?: |$)([\s\S]*)"))
@ttn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}exec(?: |$)([\s\S]*)"))
@fft.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}exec(?: |$)([\s\S]*)"))
@ffo.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}exec(?: |$)([\s\S]*)"))
@ftw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}exec(?: |$)([\s\S]*)"))
@ftr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}exec(?: |$)([\s\S]*)"))
@ffr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}exec(?: |$)([\s\S]*)"))
@ffv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}exec(?: |$)([\s\S]*)"))
@fsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}exec(?: |$)([\s\S]*)"))
@fsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}exec(?: |$)([\s\S]*)"))
@feg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}exec(?: |$)([\s\S]*)"))
@fnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}exec(?: |$)([\s\S]*)"))
@fvt.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}exec(?: |$)([\s\S]*)"))


async def run(run_q):
    # exec
    usage = """✘ Plugin : Exec Teks
•  Perintah : <code>.exec print('hello')</code>
•  Function : Jalankan skript python kecil"""
    if run_q.sender_id in SMEX_USERS:
        code = run_q.pattern_match.group(1)

        if run_q.is_channel and not run_q.is_group:
            return await run_q.reply("`Exec tidak diizinkan di saluran!`")

        if not code:
            return await run_q.reply(usage, parse_mode='html', link_preview=None)

        if code in ("userbot.session", "config.env"):
            return await run_q.reply("`Itu exec yang berbahaya! Tidak diperbolehkan!`")

        if len(code.splitlines()) <= 5:
            codepre = code
        else:
            clines = code.splitlines()
            codepre = (
                clines[0] +
                "\n" +
                clines[1] +
                "\n" +
                clines[2] +
                "\n" +
                clines[3] +
                "...")

        command = "".join(f"\n {l}" for l in code.split("\n.strip()"))
        process = await asyncio.create_subprocess_exec(
            executable,
            "-c",
            command.strip(),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        result = str(stdout.decode().strip()) + str(stderr.decode().strip())

        if result:
            if len(result) > 4096:
                file = open("output.txt", "w+")
                file.write(result)
                file.close()
                await run_q.client.send_file(
                    run_q.chat_id,
                    "output.txt",
                    reply_to=run_q.id,
                    caption="`Output too large, sending as file`",
                )
                remove("output.txt")
                return
            await run_q.reply(
                "**Query : **\n`" f"{codepre}" "`\n\n**Result : **\n`" f"{result}" "`"
            )
        else:
            await run_q.reply(
                "**Query : **\n`" f"{codepre}" "`\n\n**Result : **\n\n`Tidak Ada Hasil yang Dikembalikan/Salah`"
            )



# ======[TERM]======

@idk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}term(?: |$)(.*)"))
@ydk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}term(?: |$)(.*)"))
@wdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}term(?: |$)(.*)"))
@sdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}term(?: |$)(.*)"))
@adk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}term(?: |$)(.*)"))
@bdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}term(?: |$)(.*)"))
@cdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}term(?: |$)(.*)"))
@edk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}term(?: |$)(.*)"))
@hdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}term(?: |$)(.*)"))
@ddk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}term(?: |$)(.*)"))
@vkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}term(?: |$)(.*)"))
@kkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}term(?: |$)(.*)"))
@lkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}term(?: |$)(.*)"))
@mkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}term(?: |$)(.*)"))
@sid.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}term(?: |$)(.*)"))
@shy.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}term(?: |$)(.*)"))
@aan.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}term(?: |$)(.*)"))
@ake.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}term(?: |$)(.*)"))
@eel.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}term(?: |$)(.*)"))
@khu.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}term(?: |$)(.*)"))
@shi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}term(?: |$)(.*)"))
@yaa.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}term(?: |$)(.*)"))
@dav.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}term(?: |$)(.*)"))
@raj.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}term(?: |$)(.*)"))
@put.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}term(?: |$)(.*)"))
@tsi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}term(?: |$)(.*)"))
@tsf.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}term(?: |$)(.*)"))
@teg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}term(?: |$)(.*)"))
@tnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}term(?: |$)(.*)"))
@tth.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}term(?: |$)(.*)"))
@ton.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}term(?: |$)(.*)"))
@ttw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}term(?: |$)(.*)"))
@ttr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}term(?: |$)(.*)"))
@tfr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}term(?: |$)(.*)"))
@tfv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}term(?: |$)(.*)"))
@tsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}term(?: |$)(.*)"))
@tsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}term(?: |$)(.*)"))
@ttg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}term(?: |$)(.*)"))
@ttn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}term(?: |$)(.*)"))
@fft.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}term(?: |$)(.*)"))
@ffo.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}term(?: |$)(.*)"))
@ftw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}term(?: |$)(.*)"))
@ftr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}term(?: |$)(.*)"))
@ffr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}term(?: |$)(.*)"))
@ffv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}term(?: |$)(.*)"))
@fsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}term(?: |$)(.*)"))
@fsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}term(?: |$)(.*)"))
@feg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}term(?: |$)(.*)"))
@fnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}term(?: |$)(.*)"))
@fvt.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}term(?: |$)(.*)"))


async def terminal_runner(term):
    # term
    usage = """✘ Plugin : Term Teks
•  Perintah : <code>.term <cmd></code>
•  Function : Jalankan perintah dan skript bash di server Anda"""
    if term.sender_id in SMEX_USERS:
        # curruser = TERM_ALIAS
        command = term.pattern_match.group(1)
        try:
            from os import geteuid

            uid = geteuid()
        except ImportError:
            uid = "Ini bukan kepala!"

        if term.is_channel and not term.is_group:
            return await term.reply("`Perintah istilah tidak diizinkan di saluran!`")

        if not command:
            return await term.reply(usage, parse_mode='html', link_preview=None)

        if command in ("userbot.session", "config.env"):
            return await term.reply("`Itu term yang berbahaya! Tidak diperbolehkan!`")

        process = await asyncio.create_subprocess_shell(
            command, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        result = str(stdout.decode().strip()) + str(stderr.decode().strip())

        if len(result) > 4096:
            output = open("output.txt", "w+")
            output.write(result)
            output.close()
            await term.client.send_file(
                term.chat_id,
                "output.txt",
                reply_to=term.id,
                caption="`Output terlalu besar, mengirim sebagai file`",
            )
            remove("output.txt")
            return

        if uid == 0:
            await term.reply("`" f"{curruser} :~# {command}" f"\n{result}" "`")
        else:
            await term.reply("`" f"{curruser} :~$ {command}" f"\n{result}" "`")

# ==================================================================

# =======================[LS = LIST DIRECTORY]=======================
# credits to Cat, Geez

import io
import os
from glob import glob
from math import ceil, floor
import os.path
import time
from os.path import basename, dirname, exists, isdir, isfile, join, relpath, splitext
from pathlib import Path
from os.path import exists, isdir
from typing import Optional, Union, List, Sequence, Tuple

# from userbot.events import register
# from userbot.utils import humanbytes

# function
def humanbytes(size: Union[int, float]) -> str:
    if size is None or isinstance(size, str):
        return ""

    power = 2**10
    raised_to_pow = 0
    dict_power_n = {0: "", 1: "Ki", 2: "Mi", 3: "Gi", 4: "Ti"}
    while size > power:
        size /= power
        raised_to_pow += 1
    return str(round(size, 2)) + " " + dict_power_n[raised_to_pow] + "B"

MAX_MESSAGE_SIZE_LIMIT = 4095


@idk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ls ?(.*)"))
@ydk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ls ?(.*)"))
@wdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ls ?(.*)"))
@sdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ls ?(.*)"))
@adk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ls ?(.*)"))
@bdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ls ?(.*)"))
@cdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ls ?(.*)"))
@edk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ls ?(.*)"))
@hdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ls ?(.*)"))
@ddk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ls ?(.*)"))
@vkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ls ?(.*)"))
@kkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ls ?(.*)"))
@lkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ls ?(.*)"))
@mkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ls ?(.*)"))
@sid.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ls ?(.*)"))
@shy.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ls ?(.*)"))
@aan.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ls ?(.*)"))
@ake.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ls ?(.*)"))
@eel.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ls ?(.*)"))
@khu.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ls ?(.*)"))
@shi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ls ?(.*)"))
@yaa.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ls ?(.*)"))
@dav.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ls ?(.*)"))
@raj.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ls ?(.*)"))
@put.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ls ?(.*)"))
@tsi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ls ?(.*)"))
@tsf.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ls ?(.*)"))
@teg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ls ?(.*)"))
@tnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ls ?(.*)"))
@tth.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ls ?(.*)"))
@ton.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ls ?(.*)"))
@ttw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ls ?(.*)"))
@ttr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ls ?(.*)"))
@tfr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ls ?(.*)"))
@tfv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ls ?(.*)"))
@tsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ls ?(.*)"))
@tsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ls ?(.*)"))
@ttg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ls ?(.*)"))
@ttn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ls ?(.*)"))
@fft.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ls ?(.*)"))
@ffo.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ls ?(.*)"))
@ftw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ls ?(.*)"))
@ftr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ls ?(.*)"))
@ffr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ls ?(.*)"))
@ffv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ls ?(.*)"))
@fsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ls ?(.*)"))
@fsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ls ?(.*)"))
@feg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ls ?(.*)"))
@fnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ls ?(.*)"))
@fvt.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ls ?(.*)"))


async def lst(event):
    if event.sender_id in SMEX_USERS:
        if event.fwd_from:
            return
        cat = event.pattern_match.group(1)
        path = cat if cat else os.getcwd()
        if not exists(path):
            await event.edit(
                f"**There is no such directory or file with the name `{cat}` check again!**"
            )
            return
        if isdir(path):
            if cat:
                msg = "**Folders and Files in `{}`** :\n\n".format(path)
            else:
                msg = "**Folders and Files in Current Directory** :\n\n"
            lists = os.listdir(path)
            files = ""
            folders = ""
            for contents in sorted(lists):
                catpath = path + "/" + contents
                if not isdir(catpath):
                    size = os.stat(catpath).st_size
                    if contents.endswith((".mp3", ".flac", ".wav", ".m4a")):
                        files += "🎵 " + f"`{contents}`\n"
                    if contents.endswith((".opus")):
                        files += "🎙 " + f"`{contents}`\n"
                    elif contents.endswith(
                        (".mkv", ".mp4", ".webm", ".avi", ".mov", ".flv")
                    ):
                        files += "🎞 " + f"`{contents}`\n"
                    elif contents.endswith(
                        (".zip", ".tar", ".tar.gz", ".rar", ".7z", ".xz")
                    ):
                        files += "🗜 " + f"`{contents}`\n"
                    elif contents.endswith(
                        (".jpg", ".jpeg", ".png", ".gif", ".bmp", ".ico", ".webp")
                    ):
                        files += "🖼 " + f"`{contents}`\n"
                    elif contents.endswith((".exe", ".deb")):
                        files += "⚙️ " + f"`{contents}`\n"
                    elif contents.endswith((".iso", ".img")):
                        files += "💿 " + f"`{contents}`\n"
                    elif contents.endswith((".apk", ".xapk")):
                        files += "📱 " + f"`{contents}`\n"
                    elif contents.endswith((".py")):
                        files += "🐍 " + f"`{contents}`\n"
                    else:
                        files += "📄 " + f"`{contents}`\n"
                else:
                    folders += f"📁 `{contents}`\n"
            msg = msg + folders + files if files or folders else msg + "__empty path__"
        else:
            size = os.stat(path).st_size
            msg = "**The details of given file** :\n\n"
            if path.endswith((".mp3", ".flac", ".wav", ".m4a")):
                mode = "🎵 "
            if path.endswith((".opus")):
                mode = "🎙 "
            elif path.endswith((".mkv", ".mp4", ".webm", ".avi", ".mov", ".flv")):
                mode = "🎞 "
            elif path.endswith((".zip", ".tar", ".tar.gz", ".rar", ".7z", ".xz")):
                mode = "🗜 "
            elif path.endswith((".jpg", ".jpeg", ".png", ".gif", ".bmp", ".ico", ".webp")):
                mode = "🖼 "
            elif path.endswith((".exe", ".deb")):
                mode = "⚙️ "
            elif path.endswith((".iso", ".img")):
                mode = "💿 "
            elif path.endswith((".apk", ".xapk")):
                mode = "📱 "
            elif path.endswith((".py")):
                mode = "🐍 "
            else:
                mode = "📄 "
            time.ctime(os.path.getctime(path))
            time2 = time.ctime(os.path.getmtime(path))
            time3 = time.ctime(os.path.getatime(path))
            msg += f"**Location :** `{path}`\n"
            msg += f"**Icon :** `{mode}`\n"
            msg += f"**Size :** `{humanbytes(size)}`\n"
            msg += f"**Last Modified Time:** `{time2}`\n"
            msg += f"**Last Accessed Time:** `{time3}`"

        if len(msg) > MAX_MESSAGE_SIZE_LIMIT:
            with io.BytesIO(str.encode(msg)) as out_file:
                out_file.name = "ls.txt"
                await event.client.send_file(
                    event.chat_id,
                    out_file,
                    force_document=True,
                    allow_cache=False,
                    caption=path,
                )
                await event.delete()
        else:
            await event.edit(msg)

# ========================[COOL PROFILE PICS]========================

# credits to the respective owner xD
# imported by @heyworld
import requests
import re
import random

import urllib
import os

from telethon.tl import functions

import asyncio


COLLECTION_STRING = [
    "epic-fantasy-wallpaper",
    "castle-in-the-sky-wallpaper",
    "fantasy-forest-wallpaper",
    "fantasy-wallpaper-1080p",
    "toothless-wallpaper-hd",
    "japanese-art-wallpaper",
    "star-wars-landscape-wallpaper",
    "4k-sci-fi-wallpaper",
    "minion-screensavers-wallpaper",
    "zootopia-hd-wallpaper",
    "gravity-falls-hd-wallpaper",
    "cool-cartoon-wallpaper",
    "disney-movie-wallpaper",
    "cute-pokemon-wallpapers",
    "4k-anime-wallpaper",
    "balance-druid-wallpaper",
    "harry-potter-wallpaper",
    "funny-meme-wallpaper",
    "minimalist-hd-wallpaper",
    "cute-animal-wallpaper-backgrounds",
    "3840-x-1080-wallpaper",
    "wallpaper-outer-space",
    "best-wallpapers-in-the-world",
    "funny-desktop-backgrounds",
    "funny-cats-wallpapers",
    "cool-cat-wallpaper",
    "doge-wallpaper-hd",
    "ice-cream-cone-wallpaper",
    "food-wallpaper-background",
    "snowy-christmas-scenes-wallpaper",
    "life-quotes-wallpaper"
]


async def animepp():

    os.system("rm -rf donot.jpg")
    rnd = random.randint(0, len(COLLECTION_STRING) - 1)
    pack = COLLECTION_STRING[rnd]
    pc = requests.get("http://getwallpapers.com/collection/" + pack).text
    f = re.compile(r'/\w+/full.+.jpg')
    f = f.findall(pc)
    fy = "http://getwallpapers.com" + random.choice(f)
    print(fy)

    if not os.path.exists("f.ttf"):
        urllib.request.urlretrieve(
            "https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf", "f.ttf")
    urllib.request.urlretrieve(fy, "donottouch.jpg")


@idk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pprandom(?: |$)(.*)"))
@ydk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pprandom(?: |$)(.*)"))
@wdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pprandom(?: |$)(.*)"))
@sdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pprandom(?: |$)(.*)"))
@adk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pprandom(?: |$)(.*)"))
@bdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pprandom(?: |$)(.*)"))
@cdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pprandom(?: |$)(.*)"))
@edk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pprandom(?: |$)(.*)"))
@hdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pprandom(?: |$)(.*)"))
@ddk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pprandom(?: |$)(.*)"))
@vkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pprandom(?: |$)(.*)"))
@kkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pprandom(?: |$)(.*)"))
@lkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pprandom(?: |$)(.*)"))
@mkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pprandom(?: |$)(.*)"))
@sid.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pprandom(?: |$)(.*)"))
@shy.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pprandom(?: |$)(.*)"))
@aan.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pprandom(?: |$)(.*)"))
@ake.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pprandom(?: |$)(.*)"))
@eel.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pprandom(?: |$)(.*)"))
@khu.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pprandom(?: |$)(.*)"))
@shi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pprandom(?: |$)(.*)"))
@yaa.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pprandom(?: |$)(.*)"))
@dav.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pprandom(?: |$)(.*)"))
@raj.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pprandom(?: |$)(.*)"))
@put.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pprandom(?: |$)(.*)"))
@tsi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pprandom(?: |$)(.*)"))
@tsf.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pprandom(?: |$)(.*)"))
@teg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pprandom(?: |$)(.*)"))
@tnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pprandom(?: |$)(.*)"))
@tth.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pprandom(?: |$)(.*)"))
@ton.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pprandom(?: |$)(.*)"))
@ttw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pprandom(?: |$)(.*)"))
@ttr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pprandom(?: |$)(.*)"))
@tfr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pprandom(?: |$)(.*)"))
@tfv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pprandom(?: |$)(.*)"))
@tsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pprandom(?: |$)(.*)"))
@tsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pprandom(?: |$)(.*)"))
@ttg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pprandom(?: |$)(.*)"))
@ttn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pprandom(?: |$)(.*)"))
@fft.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pprandom(?: |$)(.*)"))
@ffo.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pprandom(?: |$)(.*)"))
@ftw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pprandom(?: |$)(.*)"))
@ftr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pprandom(?: |$)(.*)"))
@ffr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pprandom(?: |$)(.*)"))
@ffv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pprandom(?: |$)(.*)"))
@fsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pprandom(?: |$)(.*)"))
@fsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pprandom(?: |$)(.*)"))
@feg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pprandom(?: |$)(.*)"))
@fnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pprandom(?: |$)(.*)"))
@fvt.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pprandom(?: |$)(.*)"))


# @register(outgoing=True, pattern=r"^\.pprandom(?: |$)(.*)")
async def main(event):
    if event.sender_id in SMEX_USERS:
        await event.edit("`Sedang Mengubah Photo Profile Anda...`")

        while True:
            await animepp()
            file = await event.client.upload_file("donottouch.jpg")

            await event.client(functions.photos.UploadProfilePhotoRequest(file))
            os.system("rm -rf donottouch.jpg")
            await asyncio.sleep(3600)  # Edit this to your required needs


# ========================[SELF DESTRUCT MESSAGE]========================

# credits to the respective owner xD
# v2.5
from asyncio import sleep


@idk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sd (\d*) (.*)"))
@ydk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sd (\d*) (.*)"))
@wdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sd (\d*) (.*)"))
@sdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sd (\d*) (.*)"))
@adk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sd (\d*) (.*)"))
@bdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sd (\d*) (.*)"))
@cdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sd (\d*) (.*)"))
@edk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sd (\d*) (.*)"))
@hdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sd (\d*) (.*)"))
@ddk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sd (\d*) (.*)"))
@vkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sd (\d*) (.*)"))
@kkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sd (\d*) (.*)"))
@lkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sd (\d*) (.*)"))
@mkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sd (\d*) (.*)"))
@sid.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sd (\d*) (.*)"))
@shy.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sd (\d*) (.*)"))
@aan.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sd (\d*) (.*)"))
@ake.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sd (\d*) (.*)"))
@eel.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sd (\d*) (.*)"))
@khu.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sd (\d*) (.*)"))
@shi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sd (\d*) (.*)"))
@yaa.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sd (\d*) (.*)"))
@dav.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sd (\d*) (.*)"))
@raj.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sd (\d*) (.*)"))
@put.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sd (\d*) (.*)"))
@tsi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sd (\d*) (.*)"))
@tsf.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sd (\d*) (.*)"))
@teg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sd (\d*) (.*)"))
@tnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sd (\d*) (.*)"))
@tth.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sd (\d*) (.*)"))
@ton.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sd (\d*) (.*)"))
@ttw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sd (\d*) (.*)"))
@ttr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sd (\d*) (.*)"))
@tfr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sd (\d*) (.*)"))
@tfv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sd (\d*) (.*)"))
@tsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sd (\d*) (.*)"))
@tsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sd (\d*) (.*)"))
@ttg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sd (\d*) (.*)"))
@ttn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sd (\d*) (.*)"))
@fft.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sd (\d*) (.*)"))
@ffo.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sd (\d*) (.*)"))
@ftw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sd (\d*) (.*)"))
@ftr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sd (\d*) (.*)"))
@ffr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sd (\d*) (.*)"))
@ffv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sd (\d*) (.*)"))
@fsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sd (\d*) (.*)"))
@fsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sd (\d*) (.*)"))
@feg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sd (\d*) (.*)"))
@fnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sd (\d*) (.*)"))
@fvt.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sd (\d*) (.*)"))

async def selfdestruct(destroy):
    if destroy.sender_id in SMEX_USERS:
        cat = ("".join(destroy.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(cat) == 2:
            message = cat[1]
            ttl = int(cat[0])
            await destroy.delete()
            smsg = await destroy.client.send_message(destroy.chat_id, message)
            await sleep(ttl)
            await smsg.delete()



# ======================== [REPO!]========================   

@idk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}repo$"))
@ydk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}repo$"))
@wdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}repo$"))
@sdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}repo$"))
@adk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}repo$"))
@bdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}repo$"))
@cdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}repo$"))
@edk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}repo$"))
@hdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}repo$"))
@ddk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}repo$"))
@vkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}repo$"))
@kkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}repo$"))
@lkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}repo$"))
@mkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}repo$"))
@sid.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}repo$"))
@shy.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}repo$"))
@aan.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}repo$"))
@ake.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}repo$"))
@eel.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}repo$"))
@khu.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}repo$"))
@shi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}repo$"))
@yaa.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}repo$"))
@dav.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}repo$"))
@raj.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}repo$"))
@put.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}repo$"))
@tsi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}repo$"))
@tsf.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}repo$"))
@teg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}repo$"))
@tnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}repo$"))
@tth.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}repo$"))
@ton.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}repo$"))
@ttw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}repo$"))
@ttr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}repo$"))
@tfr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}repo$"))
@tfv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}repo$"))
@tsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}repo$"))
@tsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}repo$"))
@ttg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}repo$"))
@ttn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}repo$"))
@fft.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}repo$"))
@ffo.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}repo$"))
@ftw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}repo$"))
@ftr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}repo$"))
@ffr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}repo$"))
@ffv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}repo$"))
@fsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}repo$"))
@fsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}repo$"))
@feg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}repo$"))
@fnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}repo$"))
@fvt.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}repo$"))

async def repo(e):        
    if e.sender_id in SMEX_USERS:
        text = "wait.."
        event = await e.reply(text, parse_mode=None, link_preview=None )
        await event.edit(f"Link repo : [⚡️ ALPHA-XPROJECT ⚡️]({REPO_LINK})")

# ======================== [VSUDO!]========================   


@idk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}vsudo$"))
@ydk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}vsudo$"))
@wdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}vsudo$"))
@sdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}vsudo$"))
@adk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}vsudo$"))
@bdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}vsudo$"))
@cdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}vsudo$"))
@edk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}vsudo$"))
@hdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}vsudo$"))
@ddk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}vsudo$"))
@vkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}vsudo$"))
@kkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}vsudo$"))
@lkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}vsudo$"))
@mkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}vsudo$"))
@sid.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}vsudo$"))
@shy.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}vsudo$"))
@aan.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}vsudo$"))
@ake.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}vsudo$"))
@eel.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}vsudo$"))
@khu.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}vsudo$"))
@shi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}vsudo$"))
@yaa.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}vsudo$"))
@dav.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}vsudo$"))
@raj.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}vsudo$"))
@put.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}vsudo$"))
@tsi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}vsudo$"))
@tsf.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}vsudo$"))
@teg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}vsudo$"))
@tnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}vsudo$"))
@tth.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}vsudo$"))
@ton.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}vsudo$"))
@ttw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}vsudo$"))
@ttr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}vsudo$"))
@tfr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}vsudo$"))
@tfv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}vsudo$"))
@tsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}vsudo$"))
@tsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}vsudo$"))
@ttg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}vsudo$"))
@ttn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}vsudo$"))
@fft.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}vsudo$"))
@ffo.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}vsudo$"))
@ftw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}vsudo$"))
@ftr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}vsudo$"))
@ffr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}vsudo$"))
@ffv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}vsudo$"))
@fsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}vsudo$"))
@fsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}vsudo$"))
@feg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}vsudo$"))
@fnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}vsudo$"))
@fvt.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}vsudo$"))

async def vsudo(e):        
    if e.sender_id in SMEX_USERS:
        text = "wait.."
        event = await e.reply(text, parse_mode=None, link_preview=None )
        await event.edit(f"ID sudo users : `{SUDO}`")


# ========================[SEND TO BY REPLY]========================


@idk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}send (.*)"))
@ydk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}send (.*)"))
@wdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}send (.*)"))
@sdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}send (.*)"))
@adk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}send (.*)"))
@bdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}send (.*)"))
@cdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}send (.*)"))
@edk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}send (.*)"))
@hdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}send (.*)"))
@ddk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}send (.*)"))
@vkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}send (.*)"))
@kkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}send (.*)"))
@lkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}send (.*)"))
@mkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}send (.*)"))
@sid.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}send (.*)"))
@shy.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}send (.*)"))
@aan.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}send (.*)"))
@ake.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}send (.*)"))
@eel.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}send (.*)"))
@khu.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}send (.*)"))
@shi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}send (.*)"))
@yaa.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}send (.*)"))
@dav.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}send (.*)"))
@raj.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}send (.*)"))
@put.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}send (.*)"))
@tsi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}send (.*)"))
@tsf.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}send (.*)"))
@teg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}send (.*)"))
@tnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}send (.*)"))
@tth.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}send (.*)"))
@ton.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}send (.*)"))
@ttw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}send (.*)"))
@ttr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}send (.*)"))
@tfr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}send (.*)"))
@tfv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}send (.*)"))
@tsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}send (.*)"))
@tsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}send (.*)"))
@ttg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}send (.*)"))
@ttn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}send (.*)"))
@fft.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}send (.*)"))
@ffo.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}send (.*)"))
@ftw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}send (.*)"))
@ftr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}send (.*)"))
@ffr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}send (.*)"))
@ffv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}send (.*)"))
@fsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}send (.*)"))
@fsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}send (.*)"))
@feg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}send (.*)"))
@fnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}send (.*)"))
@fvt.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}send (.*)"))


async def send(event):
    if event.sender_id in SMEX_USERS:
        msgawal = await event.reply("`Sedang Memproses...`")

        if not event.is_reply:
            return await event.reply("`Mohon Balas ke pesan!`")

        chat = event.pattern_match.group(1)
        try:
            chat = await event.client.get_entity(chat)
        except (TypeError, ValueError):
            return await event.reply("`Link yang diberikan tidak valid!`")

        message = await event.get_reply_message()

        await event.client.send_message(entity=chat, message=message)
        await msgawal.edit(f"`Berhasil mengirim pesan ini ke` `{chat.title}``!`")



# =======================[!DEL]=======================
# credits: geez & man ubot

@idk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}del$"))
@ydk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}del$"))
@wdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}del$"))
@sdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}del$"))
@adk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}del$"))
@bdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}del$"))
@cdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}del$"))
@edk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}del$"))
@hdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}del$"))
@ddk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}del$"))
@vkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}del$"))
@kkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}del$"))
@lkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}del$"))
@mkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}del$"))
@sid.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}del$"))
@shy.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}del$"))
@aan.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}del$"))
@ake.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}del$"))
@eel.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}del$"))
@khu.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}del$"))
@shi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}del$"))
@yaa.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}del$"))
@dav.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}del$"))
@raj.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}del$"))
@put.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}del$"))
@tsi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}del$"))
@tsf.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}del$"))
@teg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}del$"))
@tnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}del$"))
@tth.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}del$"))
@ton.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}del$"))
@ttw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}del$"))
@ttr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}del$"))
@tfr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}del$"))
@tfv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}del$"))
@tsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}del$"))
@tsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}del$"))
@ttg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}del$"))
@ttn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}del$"))
@fft.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}del$"))
@ffo.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}del$"))
@ftw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}del$"))
@ftr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}del$"))
@ffr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}del$"))
@ffv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}del$"))
@fsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}del$"))
@fsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}del$"))
@feg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}del$"))
@fnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}del$"))
@fvt.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}del$"))

# @bot.on(geezbot_cmd(outgoing=True, pattern=r"del$"))
async def delete_it(delme):
    if delme.sender_id in SMEX_USERS:
        msg_src = await delme.get_reply_message()
        if delme.reply_to_msg_id:
            try:
                await msg_src.delete()
                await delme.delete()
                """
                if BOTLOG:
                    await delme.client.send_message(
                        BOTLOG_CHATID, "Deletion of message was successful")
                """
            except rpcbaseerrors.BadRequestError:
                smsg = await delme.reply("Well, I can't delete a message")
                await sleep(2)
                await smsg.delete()
                """
                if BOTLOG:
                    await delme.client.send_message(
                        BOTLOG_CHATID, "Well, I can't delete a message")
                """


# ======================== [INVITE]========================  

# credit king userbot
from asyncio import sleep
# from userbot import ALIVE_NAME, BOTLOG, BOTLOG_CHATID, CMD_HELP, bot
from datetime import datetime
from telethon import functions
# from emoji import emojize
from math import sqrt
from telethon.tl.functions.channels import GetFullChannelRequest, GetParticipantsRequest
from telethon.tl.functions.messages import GetFullChatRequest, GetHistoryRequest
from telethon.tl.types import MessageActionChannelMigrateFrom, ChannelParticipantsAdmins
from telethon.errors import (
    ChannelInvalidError,
    ChannelPrivateError,
    ChannelPublicGroupNaError)
from telethon.utils import get_input_location
from telethon.tl.types import ChannelParticipantAdmin, ChannelParticipantsBots
# from userbot.events import register
# from userbot.modules.admin import get_user_from_event
from telethon.utils import pack_bot_file_id

@idk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}invite(?: |$)(.*)"))
@ydk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}invite(?: |$)(.*)"))
@wdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}invite(?: |$)(.*)"))
@sdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}invite(?: |$)(.*)"))
@adk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}invite(?: |$)(.*)"))
@bdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}invite(?: |$)(.*)"))
@cdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}invite(?: |$)(.*)"))
@edk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}invite(?: |$)(.*)"))
@hdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}invite(?: |$)(.*)"))
@ddk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}invite(?: |$)(.*)"))
@vkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}invite(?: |$)(.*)"))
@kkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}invite(?: |$)(.*)"))
@lkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}invite(?: |$)(.*)"))
@mkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}invite(?: |$)(.*)"))
@sid.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}invite(?: |$)(.*)"))
@shy.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}invite(?: |$)(.*)"))
@aan.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}invite(?: |$)(.*)"))
@ake.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}invite(?: |$)(.*)"))
@eel.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}invite(?: |$)(.*)"))
@khu.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}invite(?: |$)(.*)"))
@shi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}invite(?: |$)(.*)"))
@yaa.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}invite(?: |$)(.*)"))
@dav.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}invite(?: |$)(.*)"))
@raj.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}invite(?: |$)(.*)"))
@put.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}invite(?: |$)(.*)"))
@tsi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}invite(?: |$)(.*)"))
@tsf.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}invite(?: |$)(.*)"))
@teg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}invite(?: |$)(.*)"))
@tnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}invite(?: |$)(.*)"))
@tth.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}invite(?: |$)(.*)"))
@ton.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}invite(?: |$)(.*)"))
@ttw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}invite(?: |$)(.*)"))
@ttr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}invite(?: |$)(.*)"))
@tfr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}invite(?: |$)(.*)"))
@tfv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}invite(?: |$)(.*)"))
@tsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}invite(?: |$)(.*)"))
@tsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}invite(?: |$)(.*)"))
@ttg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}invite(?: |$)(.*)"))
@ttn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}invite(?: |$)(.*)"))
@fft.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}invite(?: |$)(.*)"))
@ffo.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}invite(?: |$)(.*)"))
@ftw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}invite(?: |$)(.*)"))
@ftr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}invite(?: |$)(.*)"))
@ffr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}invite(?: |$)(.*)"))
@ffv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}invite(?: |$)(.*)"))
@fsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}invite(?: |$)(.*)"))
@fsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}invite(?: |$)(.*)"))
@feg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}invite(?: |$)(.*)"))
@fnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}invite(?: |$)(.*)"))
@fvt.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}invite(?: |$)(.*)"))

# @register(outgoing=True, pattern="^.invite(?: |$)(.*)")
async def _(event):
    if event.sender_id in SMEX_USERS:
        if event.fwd_from:
            return
        to_add_users = event.pattern_match.group(1)
        if event.is_private:
            await event.reply("`.invite` Pengguna Ke Obrolan, Tidak Ke Pesan Pribadi")
        else:
            if not event.is_channel and event.is_group:
                # https://lonamiwebs.github.io/Telethon/methods/messages/add_chat_user.html
                for user_id in to_add_users.split(" "):
                    try:
                        await event.client(functions.messages.AddChatUserRequest(
                            chat_id=event.chat_id,
                            user_id=user_id,
                            fwd_limit=1000000
                        ))
                    except Exception as e:
                        await event.reply(str(e))
                await event.reply("`Sukses Menambahkan Pengguna Ke Obrolan`")
            else:
                # https://lonamiwebs.github.io/Telethon/methods/channels/invite_to_channel.html
                for user_id in to_add_users.split(" "):
                    try:
                        await event.client(functions.channels.InviteToChannelRequest(
                            channel=event.chat_id,
                            users=[user_id]
                        ))
                    except Exception as e:
                        await event.reply(str(e))
                await event.reply("`Sukses Menambahkan Pengguna Ke Obrolan`")


# =======================[!GCAST]=======================
# credits: geez & man ub

@idk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gcast(?: |$)(.*)"))
@ydk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gcast(?: |$)(.*)"))
@wdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gcast(?: |$)(.*)"))
@sdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gcast(?: |$)(.*)"))
@adk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gcast(?: |$)(.*)"))
@bdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gcast(?: |$)(.*)"))
@cdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gcast(?: |$)(.*)"))
@edk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gcast(?: |$)(.*)"))
@hdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gcast(?: |$)(.*)"))
@ddk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gcast(?: |$)(.*)"))
@vkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gcast(?: |$)(.*)"))
@kkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gcast(?: |$)(.*)"))
@lkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gcast(?: |$)(.*)"))
@mkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gcast(?: |$)(.*)"))
@sid.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gcast(?: |$)(.*)"))
@shy.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gcast(?: |$)(.*)"))
@aan.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gcast(?: |$)(.*)"))
@ake.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gcast(?: |$)(.*)"))
@eel.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gcast(?: |$)(.*)"))
@khu.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gcast(?: |$)(.*)"))
@shi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gcast(?: |$)(.*)"))
@yaa.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gcast(?: |$)(.*)"))
@dav.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gcast(?: |$)(.*)"))
@raj.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gcast(?: |$)(.*)"))
@put.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gcast(?: |$)(.*)"))
@tsi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gcast(?: |$)(.*)"))
@tsf.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gcast(?: |$)(.*)"))
@teg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gcast(?: |$)(.*)"))
@tnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gcast(?: |$)(.*)"))
@tth.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gcast(?: |$)(.*)"))
@ton.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gcast(?: |$)(.*)"))
@ttw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gcast(?: |$)(.*)"))
@ttr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gcast(?: |$)(.*)"))
@tfr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gcast(?: |$)(.*)"))
@tfv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gcast(?: |$)(.*)"))
@tsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gcast(?: |$)(.*)"))
@tsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gcast(?: |$)(.*)"))
@ttg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gcast(?: |$)(.*)"))
@ttn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gcast(?: |$)(.*)"))
@fft.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gcast(?: |$)(.*)"))
@ffo.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gcast(?: |$)(.*)"))
@ftw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gcast(?: |$)(.*)"))
@ftr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gcast(?: |$)(.*)"))
@ffr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gcast(?: |$)(.*)"))
@ffv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gcast(?: |$)(.*)"))
@fsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gcast(?: |$)(.*)"))
@fsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gcast(?: |$)(.*)"))
@feg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gcast(?: |$)(.*)"))
@fnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gcast(?: |$)(.*)"))
@fvt.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gcast(?: |$)(.*)"))

# @register(outgoing=True, pattern=r"^\.gcast(?: |$)(.*)")
async def gcast(event):
    if event.sender_id in SMEX_USERS:
        xx = event.pattern_match.group(1)
        if xx:
            msg = xx
        elif event.is_reply:
            msg = await event.get_reply_message()
        else:
            await event.reply("**Berikan Sebuah Pesan atau Reply**")
            return
        kk = await event.reply("`Globally Broadcasting Msg...📢`")
        er = 0
        done = 0
        async for x in event.client.iter_dialogs():
            if x.is_group:
                chat = x.id
                try:
                    done += 1
                    await event.client.send_message(chat, msg)
                except BaseException:
                    er += 1
        await kk.edit(
            f"**Berhasil Mengirim Pesan Ke** `{done}` **Grup, Gagal Mengirim Pesan Ke** `{er}` **Grup**"
        )


# =======================[!GUCAST]=======================
# credits: geez & man ub

@idk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gucast(?: |$)(.*)"))
@ydk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gucast(?: |$)(.*)"))
@wdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gucast(?: |$)(.*)"))
@sdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gucast(?: |$)(.*)"))
@adk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gucast(?: |$)(.*)"))
@bdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gucast(?: |$)(.*)"))
@cdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gucast(?: |$)(.*)"))
@edk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gucast(?: |$)(.*)"))
@hdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gucast(?: |$)(.*)"))
@ddk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gucast(?: |$)(.*)"))
@vkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gucast(?: |$)(.*)"))
@kkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gucast(?: |$)(.*)"))
@lkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gucast(?: |$)(.*)"))
@mkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gucast(?: |$)(.*)"))
@sid.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gucast(?: |$)(.*)"))
@shy.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gucast(?: |$)(.*)"))
@aan.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gucast(?: |$)(.*)"))
@ake.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gucast(?: |$)(.*)"))
@eel.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gucast(?: |$)(.*)"))
@khu.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gucast(?: |$)(.*)"))
@shi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gucast(?: |$)(.*)"))
@yaa.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gucast(?: |$)(.*)"))
@dav.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gucast(?: |$)(.*)"))
@raj.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gucast(?: |$)(.*)"))
@put.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gucast(?: |$)(.*)"))
@tsi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gucast(?: |$)(.*)"))
@tsf.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gucast(?: |$)(.*)"))
@teg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gucast(?: |$)(.*)"))
@tnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gucast(?: |$)(.*)"))
@tth.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gucast(?: |$)(.*)"))
@ton.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gucast(?: |$)(.*)"))
@ttw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gucast(?: |$)(.*)"))
@ttr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gucast(?: |$)(.*)"))
@tfr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gucast(?: |$)(.*)"))
@tfv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gucast(?: |$)(.*)"))
@tsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gucast(?: |$)(.*)"))
@tsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gucast(?: |$)(.*)"))
@ttg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gucast(?: |$)(.*)"))
@ttn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gucast(?: |$)(.*)"))
@fft.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gucast(?: |$)(.*)"))
@ffo.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gucast(?: |$)(.*)"))
@ftw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gucast(?: |$)(.*)"))
@ftr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gucast(?: |$)(.*)"))
@ffr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gucast(?: |$)(.*)"))
@ffv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gucast(?: |$)(.*)"))
@fsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gucast(?: |$)(.*)"))
@fsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gucast(?: |$)(.*)"))
@feg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gucast(?: |$)(.*)"))
@fnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gucast(?: |$)(.*)"))
@fvt.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gucast(?: |$)(.*)"))

# @register(outgoing=True, pattern=r"^\.gucast(?: |$)(.*)")
async def gucast(event):
    if event.sender_id in SMEX_USERS:
        xx = event.pattern_match.group(1)
        if xx:
            msg = xx
        elif event.is_reply:
            msg = await event.get_reply_message()
        else:
            await event.reply("**Berikan Sebuah Pesan atau Reply**")
            return
        kk = await event.reply("`Globally Broadcasting Msg to Users...`")
        er = 0
        done = 0
        async for x in event.client.iter_dialogs():
            if x.is_user and not x.entity.bot:
                chat = x.id
                try:
                    done += 1
                    await event.client.send_message(chat, msg)
                except BaseException:
                    er += 1
        await kk.edit(
            f"**Berhasil Mengirim Pesan Ke** `{done}` **chats, Gagal Mengirim Pesan Ke** `{er}` **chats**"
        )


# ======================== [RESERVED]========================  

@idk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}reserved$"))
@ydk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}reserved$"))
@wdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}reserved$"))
@sdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}reserved$"))
@adk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}reserved$"))
@bdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}reserved$"))
@cdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}reserved$"))
@edk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}reserved$"))
@hdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}reserved$"))
@ddk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}reserved$"))
@vkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}reserved$"))
@kkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}reserved$"))
@lkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}reserved$"))
@mkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}reserved$"))
@sid.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}reserved$"))
@shy.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}reserved$"))
@aan.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}reserved$"))
@ake.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}reserved$"))
@eel.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}reserved$"))
@khu.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}reserved$"))
@shi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}reserved$"))
@yaa.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}reserved$"))
@dav.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}reserved$"))
@raj.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}reserved$"))
@put.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}reserved$"))
@tsi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}reserved$"))
@tsf.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}reserved$"))
@teg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}reserved$"))
@tnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}reserved$"))
@tth.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}reserved$"))
@ton.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}reserved$"))
@ttw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}reserved$"))
@ttr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}reserved$"))
@tfr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}reserved$"))
@tfv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}reserved$"))
@tsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}reserved$"))
@tsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}reserved$"))
@ttg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}reserved$"))
@ttn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}reserved$"))
@fft.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}reserved$"))
@ffo.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}reserved$"))
@ftw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}reserved$"))
@ftr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}reserved$"))
@ffr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}reserved$"))
@ffv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}reserved$"))
@fsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}reserved$"))
@fsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}reserved$"))
@feg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}reserved$"))
@fnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}reserved$"))
@fvt.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}reserved$"))

# @register(outgoing=True, pattern=r"^\.reserved$")
async def mine(event):
    if event.sender_id in SMEX_USERS:
        """For .reserved command, get a list of your reserved usernames."""
        result = await event.client(GetAdminedPublicChannelsRequest())
        output_str = "".join(
            f"{channel_obj.title}\n@{channel_obj.username}\n\n"
            for channel_obj in result.chats
        )

        await event.reply(output_str)


# ========================[SENDBOT]========================
# credit man ub

@idk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sendbot (.*)"))
@ydk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sendbot (.*)"))
@wdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sendbot (.*)"))
@sdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sendbot (.*)"))
@adk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sendbot (.*)"))
@bdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sendbot (.*)"))
@cdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sendbot (.*)"))
@edk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sendbot (.*)"))
@hdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sendbot (.*)"))
@ddk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sendbot (.*)"))
@vkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sendbot (.*)"))
@kkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sendbot (.*)"))
@lkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sendbot (.*)"))
@mkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sendbot (.*)"))
@sid.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sendbot (.*)"))
@shy.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sendbot (.*)"))
@aan.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sendbot (.*)"))
@ake.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sendbot (.*)"))
@eel.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sendbot (.*)"))
@khu.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sendbot (.*)"))
@shi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sendbot (.*)"))
@yaa.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sendbot (.*)"))
@dav.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sendbot (.*)"))
@raj.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sendbot (.*)"))
@put.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sendbot (.*)"))
@tsi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sendbot (.*)"))
@tsf.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sendbot (.*)"))
@teg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sendbot (.*)"))
@tnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sendbot (.*)"))
@tth.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sendbot (.*)"))
@ton.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sendbot (.*)"))
@ttw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sendbot (.*)"))
@ttr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sendbot (.*)"))
@tfr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sendbot (.*)"))
@tfv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sendbot (.*)"))
@tsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sendbot (.*)"))
@tsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sendbot (.*)"))
@ttg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sendbot (.*)"))
@ttn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sendbot (.*)"))
@fft.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sendbot (.*)"))
@ffo.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sendbot (.*)"))
@ftw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sendbot (.*)"))
@ftr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sendbot (.*)"))
@ffr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sendbot (.*)"))
@ffv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sendbot (.*)"))
@fsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sendbot (.*)"))
@fsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sendbot (.*)"))
@feg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sendbot (.*)"))
@fnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sendbot (.*)"))
@fvt.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}sendbot (.*)"))

# @register(outgoing=True, pattern=r"^\.sendbot (.*)")
async def sendbot(event):
    if event.sender_id in SMEX_USERS:
        if event.fwd_from:
            return
        chat = str(event.pattern_match.group(1).split(" ", 1)[0])
        link = str(event.pattern_match.group(1).split(" ", 1)[1])
        if not link:
            return await event.reply("**Maaf BOT Tidak Merespond.**")

        botid = await event.client.get_entity(chat)
        mc1 = await event.reply("`Processing...`")
        async with event.client.conversation(chat) as conv:
            try:
                response = conv.wait_event(
                    events.NewMessage(incoming=True, from_users=botid)
                )
                msg = await event.client.send_message(chat, link)
                response = await response
                await event.client.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit(f"**Unblock Terlebih dahulu {chat} dan coba lagi.**")
                return
            except BaseException:
                await event.edit("**Tidak dapat menemukan bot itu 🥺**")
                await sleep(2)
                return await event.delete()

            await mc1.edit(f"**Pesan Terkirim:** `{link}`\n**Kepada: {chat}**")
            await event.client.send_message(event.chat_id, response.message)
            await event.client.send_read_acknowledge(event.chat_id)
            await event.client.delete_messages(conv.chat_id, [msg.id, response.id])


# =======================[TMSG]=======================
# credits: geez & man ub

import os
from asyncio import sleep

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.messages import ExportChatInviteRequest
from telethon.tl.types import ChannelParticipantsKicked

@idk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}tmsg (.*)"))
@ydk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}tmsg (.*)"))
@wdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}tmsg (.*)"))
@sdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}tmsg (.*)"))
@adk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}tmsg (.*)"))
@bdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}tmsg (.*)"))
@cdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}tmsg (.*)"))
@edk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}tmsg (.*)"))
@hdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}tmsg (.*)"))
@ddk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}tmsg (.*)"))
@vkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}tmsg (.*)"))
@kkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}tmsg (.*)"))
@lkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}tmsg (.*)"))
@mkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}tmsg (.*)"))
@sid.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}tmsg (.*)"))
@shy.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}tmsg (.*)"))
@aan.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}tmsg (.*)"))
@ake.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}tmsg (.*)"))
@eel.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}tmsg (.*)"))
@khu.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}tmsg (.*)"))
@shi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}tmsg (.*)"))
@yaa.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}tmsg (.*)"))
@dav.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}tmsg (.*)"))
@raj.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}tmsg (.*)"))
@put.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}tmsg (.*)"))
@tsi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}tmsg (.*)"))
@tsf.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}tmsg (.*)"))
@teg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}tmsg (.*)"))
@tnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}tmsg (.*)"))
@tth.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}tmsg (.*)"))
@ton.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}tmsg (.*)"))
@ttw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}tmsg (.*)"))
@ttr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}tmsg (.*)"))
@tfr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}tmsg (.*)"))
@tfv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}tmsg (.*)"))
@tsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}tmsg (.*)"))
@tsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}tmsg (.*)"))
@ttg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}tmsg (.*)"))
@ttn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}tmsg (.*)"))
@fft.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}tmsg (.*)"))
@ffo.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}tmsg (.*)"))
@ftw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}tmsg (.*)"))
@ftr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}tmsg (.*)"))
@ffr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}tmsg (.*)"))
@ffv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}tmsg (.*)"))
@fsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}tmsg (.*)"))
@fsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}tmsg (.*)"))
@feg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}tmsg (.*)"))
@fnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}tmsg (.*)"))
@fvt.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}tmsg (.*)"))

# @register(outgoing=True, pattern=r"^\.tmsg (.*)")
async def _(event):
    if event.sender_id in SMEX_USERS:
        k = await event.get_reply_message()
        if k:
            a = await event.client.get_messages(event.chat_id, 0, from_user=k.sender_id)
            return await event.reply(
                f"**Total ada** `{a.total}` **Chat Yang dikirim Oleh** {u} **di Grup Chat ini**"
            )
        u = event.pattern_match.group(1)
        if not u:
            u = "me"
        a = await event.client.get_messages(event.chat_id, 0, from_user=u)
        await event.reply(
            f"**Total ada `{a.total}` Chat Yang dikirim Oleh saya di Grup Chat ini**"
        )


# =======================[FTYPING]=======================

import asyncio

# from userbot import CMD_HELP
# from userbot.events import register

@idk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ftyping(?: |$)(.*)"))
@ydk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ftyping(?: |$)(.*)"))
@wdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ftyping(?: |$)(.*)"))
@sdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ftyping(?: |$)(.*)"))
@adk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ftyping(?: |$)(.*)"))
@bdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ftyping(?: |$)(.*)"))
@cdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ftyping(?: |$)(.*)"))
@edk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ftyping(?: |$)(.*)"))
@hdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ftyping(?: |$)(.*)"))
@ddk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ftyping(?: |$)(.*)"))
@vkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ftyping(?: |$)(.*)"))
@kkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ftyping(?: |$)(.*)"))
@lkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ftyping(?: |$)(.*)"))
@mkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ftyping(?: |$)(.*)"))
@sid.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ftyping(?: |$)(.*)"))
@shy.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ftyping(?: |$)(.*)"))
@aan.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ftyping(?: |$)(.*)"))
@ake.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ftyping(?: |$)(.*)"))
@eel.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ftyping(?: |$)(.*)"))
@khu.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ftyping(?: |$)(.*)"))
@shi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ftyping(?: |$)(.*)"))
@yaa.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ftyping(?: |$)(.*)"))
@dav.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ftyping(?: |$)(.*)"))
@raj.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ftyping(?: |$)(.*)"))
@put.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ftyping(?: |$)(.*)"))
@tsi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ftyping(?: |$)(.*)"))
@tsf.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ftyping(?: |$)(.*)"))
@teg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ftyping(?: |$)(.*)"))
@tnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ftyping(?: |$)(.*)"))
@tth.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ftyping(?: |$)(.*)"))
@ton.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ftyping(?: |$)(.*)"))
@ttw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ftyping(?: |$)(.*)"))
@ttr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ftyping(?: |$)(.*)"))
@tfr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ftyping(?: |$)(.*)"))
@tfv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ftyping(?: |$)(.*)"))
@tsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ftyping(?: |$)(.*)"))
@tsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ftyping(?: |$)(.*)"))
@ttg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ftyping(?: |$)(.*)"))
@ttn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ftyping(?: |$)(.*)"))
@fft.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ftyping(?: |$)(.*)"))
@ffo.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ftyping(?: |$)(.*)"))
@ftw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ftyping(?: |$)(.*)"))
@ftr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ftyping(?: |$)(.*)"))
@ffr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ftyping(?: |$)(.*)"))
@ffv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ftyping(?: |$)(.*)"))
@fsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ftyping(?: |$)(.*)"))
@fsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ftyping(?: |$)(.*)"))
@feg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ftyping(?: |$)(.*)"))
@fnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ftyping(?: |$)(.*)"))
@fvt.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}ftyping(?: |$)(.*)"))

# @register(outgoing=True, pattern=r"^\.ftyping(?: |$)(.*)")
async def _(event):
    if event.sender_id in SMEX_USERS:
        t = event.pattern_match.group(1)
        if not (t or t.isdigit()):
            t = 100
        else:
            try:
                t = int(t)
            except BaseException:
                try:
                    t = await event.ban_time(t)
                except BaseException:
                    return await event.edit("`Masukan jumlah detik yang benar`")
        notif = await event.reply(f"**Memulai Pengetikan Palsu Selama** `{t}` **detik.**")
        await asyncio.sleep(3)
        await notif.delete()
        async with event.client.action(event.chat_id, "typing"):
            await asyncio.sleep(t)


# =======================[GPOTO]=======================
# credit ultro

@idk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gpoto ?(.*)"))
@ydk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gpoto ?(.*)"))
@wdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gpoto ?(.*)"))
@sdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gpoto ?(.*)"))
@adk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gpoto ?(.*)"))
@bdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gpoto ?(.*)"))
@cdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gpoto ?(.*)"))
@edk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gpoto ?(.*)"))
@hdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gpoto ?(.*)"))
@ddk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gpoto ?(.*)"))
@vkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gpoto ?(.*)"))
@kkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gpoto ?(.*)"))
@lkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gpoto ?(.*)"))
@mkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gpoto ?(.*)"))
@sid.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gpoto ?(.*)"))
@shy.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gpoto ?(.*)"))
@aan.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gpoto ?(.*)"))
@ake.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gpoto ?(.*)"))
@eel.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gpoto ?(.*)"))
@khu.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gpoto ?(.*)"))
@shi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gpoto ?(.*)"))
@yaa.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gpoto ?(.*)"))
@dav.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gpoto ?(.*)"))
@raj.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gpoto ?(.*)"))
@put.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gpoto ?(.*)"))
@tsi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gpoto ?(.*)"))
@tsf.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gpoto ?(.*)"))
@teg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gpoto ?(.*)"))
@tnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gpoto ?(.*)"))
@tth.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gpoto ?(.*)"))
@ton.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gpoto ?(.*)"))
@ttw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gpoto ?(.*)"))
@ttr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gpoto ?(.*)"))
@tfr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gpoto ?(.*)"))
@tfv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gpoto ?(.*)"))
@tsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gpoto ?(.*)"))
@tsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gpoto ?(.*)"))
@ttg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gpoto ?(.*)"))
@ttn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gpoto ?(.*)"))
@fft.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gpoto ?(.*)"))
@ffo.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gpoto ?(.*)"))
@ftw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gpoto ?(.*)"))
@ftr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gpoto ?(.*)"))
@ffr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gpoto ?(.*)"))
@ffv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gpoto ?(.*)"))
@fsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gpoto ?(.*)"))
@fsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gpoto ?(.*)"))
@feg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gpoto ?(.*)"))
@fnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gpoto ?(.*)"))
@fvt.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}gpoto ?(.*)"))

# @ultroid_cmd(pattern="poto ?(.*)")
async def gpoto(e):
    if e.sender_id in SMEX_USERS:
        ult = e.pattern_match.group(1)
        a = await e.reply("`Processing...`")
        if not ult and e.is_reply:
            gs = await e.get_reply_message()
            ult = gs.sender_id
        if not (ult or e.is_reply):
            ult = e.chat_id
        try:
            okla = await e.client.download_profile_photo(
                ult,
                "profile.jpg",
                download_big=True,
            )
            await a.delete()
            await e.reply(file=okla)
            os.remove(okla)
        except Exception as er:
            await e.reply(f"ERROR - {str(er)}")


# =======================[ASUPAN|WIBU|CHIKA]=======================
# credit man


import requests

# from userbot import CMD_HELP
# from userbot.events import register


@idk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}asupan$"))
@ydk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}asupan$"))
@wdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}asupan$"))
@sdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}asupan$"))
@adk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}asupan$"))
@bdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}asupan$"))
@cdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}asupan$"))
@edk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}asupan$"))
@hdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}asupan$"))
@ddk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}asupan$"))
@vkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}asupan$"))
@kkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}asupan$"))
@lkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}asupan$"))
@mkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}asupan$"))
@sid.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}asupan$"))
@shy.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}asupan$"))
@aan.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}asupan$"))
@ake.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}asupan$"))
@eel.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}asupan$"))
@khu.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}asupan$"))
@shi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}asupan$"))
@yaa.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}asupan$"))
@dav.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}asupan$"))
@raj.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}asupan$"))
@put.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}asupan$"))
@tsi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}asupan$"))
@tsf.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}asupan$"))
@teg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}asupan$"))
@tnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}asupan$"))
@tth.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}asupan$"))
@ton.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}asupan$"))
@ttw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}asupan$"))
@ttr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}asupan$"))
@tfr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}asupan$"))
@tfv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}asupan$"))
@tsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}asupan$"))
@tsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}asupan$"))
@ttg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}asupan$"))
@ttn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}asupan$"))
@fft.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}asupan$"))
@ffo.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}asupan$"))
@ftw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}asupan$"))
@ftr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}asupan$"))
@ffr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}asupan$"))
@ffv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}asupan$"))
@fsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}asupan$"))
@fsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}asupan$"))
@feg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}asupan$"))
@fnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}asupan$"))
@fvt.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}asupan$"))

# @register(outgoing=True, pattern=r"^\.asupan$")
async def _(event):
    if event.sender_id in SMEX_USERS:
        try:
            response = requests.get("https://api-tede.herokuapp.com/api/asupan/ptl").json()
            await event.client.send_file(event.chat_id, response["url"])
            await event.delete()
        except Exception:
            await event.reply("**Tidak bisa menemukan video asupan.**")


@idk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}wibu$"))
@ydk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}wibu$"))
@wdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}wibu$"))
@sdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}wibu$"))
@adk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}wibu$"))
@bdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}wibu$"))
@cdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}wibu$"))
@edk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}wibu$"))
@hdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}wibu$"))
@ddk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}wibu$"))
@vkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}wibu$"))
@kkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}wibu$"))
@lkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}wibu$"))
@mkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}wibu$"))
@sid.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}wibu$"))
@shy.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}wibu$"))
@aan.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}wibu$"))
@ake.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}wibu$"))
@eel.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}wibu$"))
@khu.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}wibu$"))
@shi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}wibu$"))
@yaa.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}wibu$"))
@dav.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}wibu$"))
@raj.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}wibu$"))
@put.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}wibu$"))
@tsi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}wibu$"))
@tsf.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}wibu$"))
@teg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}wibu$"))
@tnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}wibu$"))
@tth.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}wibu$"))
@ton.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}wibu$"))
@ttw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}wibu$"))
@ttr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}wibu$"))
@tfr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}wibu$"))
@tfv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}wibu$"))
@tsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}wibu$"))
@tsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}wibu$"))
@ttg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}wibu$"))
@ttn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}wibu$"))
@fft.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}wibu$"))
@ffo.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}wibu$"))
@ftw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}wibu$"))
@ftr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}wibu$"))
@ffr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}wibu$"))
@ffv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}wibu$"))
@fsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}wibu$"))
@fsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}wibu$"))
@feg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}wibu$"))
@fnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}wibu$"))
@fvt.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}wibu$"))

# @register(outgoing=True, pattern=r"^\.wibu$")
async def _(event):
    if event.sender_id in SMEX_USERS:
        try:
            response = requests.get("https://api-tede.herokuapp.com/api/asupan/wibu").json()
            await event.client.send_file(event.chat_id, response["url"])
            await event.delete()
        except Exception:
            await event.reply("**Tidak bisa menemukan video wibu.**")


@idk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}chika$"))
@ydk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}chika$"))
@wdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}chika$"))
@sdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}chika$"))
@adk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}chika$"))
@bdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}chika$"))
@cdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}chika$"))
@edk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}chika$"))
@hdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}chika$"))
@ddk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}chika$"))
@vkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}chika$"))
@kkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}chika$"))
@lkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}chika$"))
@mkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}chika$"))
@sid.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}chika$"))
@shy.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}chika$"))
@aan.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}chika$"))
@ake.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}chika$"))
@eel.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}chika$"))
@khu.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}chika$"))
@shi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}chika$"))
@yaa.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}chika$"))
@dav.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}chika$"))
@raj.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}chika$"))
@put.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}chika$"))
@tsi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}chika$"))
@tsf.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}chika$"))
@teg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}chika$"))
@tnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}chika$"))
@tth.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}chika$"))
@ton.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}chika$"))
@ttw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}chika$"))
@ttr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}chika$"))
@tfr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}chika$"))
@tfv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}chika$"))
@tsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}chika$"))
@tsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}chika$"))
@ttg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}chika$"))
@ttn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}chika$"))
@fft.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}chika$"))
@ffo.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}chika$"))
@ftw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}chika$"))
@ftr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}chika$"))
@ffr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}chika$"))
@ffv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}chika$"))
@fsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}chika$"))
@fsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}chika$"))
@feg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}chika$"))
@fnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}chika$"))
@fvt.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}chika$"))

# @register(outgoing=True, pattern=r"^\.chika$")
async def _(event):
    if event.sender_id in SMEX_USERS:
        try:
            response = requests.get("https://api-tede.herokuapp.com/api/chika").json()
            await event.client.send_file(event.chat_id, response["url"])
            await event.delete()
        except Exception:
            await event.reply("**Tidak bisa menemukan video chikakiku.**")



# ========================[EVIL SAME AS EVAL]========================

# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
"""Userbot module for executing code and terminal commands from Telegram."""

import asyncio
import io
import sys
import traceback
from os import remove

# from userbot import CMD_HELP, bot
# from userbot.events import register

MAX_MESSAGE_SIZE_LIMIT = 4095

p = print


@idk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}evil(?:\s|$)([\s\S]*)"))
@ydk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}evil(?:\s|$)([\s\S]*)"))
@wdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}evil(?:\s|$)([\s\S]*)"))
@sdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}evil(?:\s|$)([\s\S]*)"))
@adk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}evil(?:\s|$)([\s\S]*)"))
@bdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}evil(?:\s|$)([\s\S]*)"))
@cdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}evil(?:\s|$)([\s\S]*)"))
@edk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}evil(?:\s|$)([\s\S]*)"))
@hdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}evil(?:\s|$)([\s\S]*)"))
@ddk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}evil(?:\s|$)([\s\S]*)"))
@vkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}evil(?:\s|$)([\s\S]*)"))
@kkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}evil(?:\s|$)([\s\S]*)"))
@lkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}evil(?:\s|$)([\s\S]*)"))
@mkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}evil(?:\s|$)([\s\S]*)"))
@sid.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}evil(?:\s|$)([\s\S]*)"))
@shy.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}evil(?:\s|$)([\s\S]*)"))
@aan.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}evil(?:\s|$)([\s\S]*)"))
@ake.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}evil(?:\s|$)([\s\S]*)"))
@eel.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}evil(?:\s|$)([\s\S]*)"))
@khu.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}evil(?:\s|$)([\s\S]*)"))
@shi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}evil(?:\s|$)([\s\S]*)"))
@yaa.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}evil(?:\s|$)([\s\S]*)"))
@dav.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}evil(?:\s|$)([\s\S]*)"))
@raj.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}evil(?:\s|$)([\s\S]*)"))
@put.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}evil(?:\s|$)([\s\S]*)"))
@tsi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}evil(?:\s|$)([\s\S]*)"))
@tsf.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}evil(?:\s|$)([\s\S]*)"))
@teg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}evil(?:\s|$)([\s\S]*)"))
@tnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}evil(?:\s|$)([\s\S]*)"))
@tth.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}evil(?:\s|$)([\s\S]*)"))
@ton.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}evil(?:\s|$)([\s\S]*)"))
@ttw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}evil(?:\s|$)([\s\S]*)"))
@ttr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}evil(?:\s|$)([\s\S]*)"))
@tfr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}evil(?:\s|$)([\s\S]*)"))
@tfv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}evil(?:\s|$)([\s\S]*)"))
@tsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}evil(?:\s|$)([\s\S]*)"))
@tsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}evil(?:\s|$)([\s\S]*)"))
@ttg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}evil(?:\s|$)([\s\S]*)"))
@ttn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}evil(?:\s|$)([\s\S]*)"))
@fft.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}evil(?:\s|$)([\s\S]*)"))
@ffo.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}evil(?:\s|$)([\s\S]*)"))
@ftw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}evil(?:\s|$)([\s\S]*)"))
@ftr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}evil(?:\s|$)([\s\S]*)"))
@ffr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}evil(?:\s|$)([\s\S]*)"))
@ffv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}evil(?:\s|$)([\s\S]*)"))
@fsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}evil(?:\s|$)([\s\S]*)"))
@fsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}evil(?:\s|$)([\s\S]*)"))
@feg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}evil(?:\s|$)([\s\S]*)"))
@fnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}evil(?:\s|$)([\s\S]*)"))
@fvt.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}evil(?:\s|$)([\s\S]*)"))

# @register(outgoing=True, pattern=r"^\.eval(?:\s|$)([\s\S]*)")

async def _(event):
    if event.sender_id in SMEX_USERS:
        expression = event.pattern_match.group(1)
        if not expression:
            return await event.reply("**Berikan Code untuk di Eksekusi.**")

        if expression in ("userbot.session", "config.env"):
            return await event.reply("**Itu operasi yang berbahaya! Tidak diperbolehkan!**")

        cmd = "".join(event.message.message.split(maxsplit=1)[1:])
        if not cmd:
            return event.reply("**Apa yang harus saya jalankan?**")
        cmd = (
            cmd.replace("sendmessage", "send_message")
            .replace("sendfile", "send_file")
            .replace("editmessage", "edit_message")
        )
        xx = await event.reply("`Processing...`")
        if event.reply_to_msg_id:
            reply_to_id = event.reply_to_msg_id
        old_stderr = sys.stderr
        old_stdout = sys.stdout
        redirected_output = sys.stdout = io.StringIO()
        redirected_error = sys.stderr = io.StringIO()
        stdout, stderr, exc = None, None, None
        reply_to_id = event.message.id

        async def aexec(code, event):
            exec(
                f"async def __aexec(e, client): "
                + "\n message = event = e"
                + "\n reply = await event.get_reply_message()"
                + "\n chat = (await event.get_chat()).id"
                + "".join(f"\n {line}" for line in code.split("\n")),
            )

            return await locals()["__aexec"](event, event.client)

        try:
            await aexec(cmd, event)
        except Exception:
            exc = traceback.format_exc()
        stdout = redirected_output.getvalue()
        stderr = redirected_error.getvalue()
        sys.stdout = old_stdout
        sys.stderr = old_stderr
        evaluation = ""
        if exc:
            evaluation = exc
        elif stderr:
            evaluation = stderr
        elif stdout:
            evaluation = stdout
        else:
            evaluation = "Success"
        final_output = f"**•  Eval : **\n`{cmd}` \n\n**•  Result : **\n`{evaluation}` \n"

        if len(final_output) > 4096:
            man = final_output.replace("`", "").replace("**", "").replace("__", "")
            with io.BytesIO(str.encode(man)) as out_file:
                out_file.name = "eval.txt"
                await event.client.send_file(
                    event.chat_id,
                    out_file,
                    force_document=True,
                    allow_cache=False,
                    caption="**Output terlalu besar, dikirim sebagai file**",
                    reply_to=reply_to_id,
                )
                await xx.delete()
        else:
            await xx.edit(final_output)



# =======================[CLONE & RESTORE]=======================

# credit to t.me/SharingUserbot & t.me/Lunatic0de

from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.photos import DeletePhotosRequest, UploadProfilePhotoRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import InputPhoto

# from userbot import CMD_HELP, LOGS, STORAGE, bot
# from userbot.events import register
from userbot import STORAGE, LOGS

# from .storage import Storage

# STORAGE = (lambda n: Storage(Path("data") / n))
# LOGS = getLogger(__name__)

if not hasattr(STORAGE, "userObj"):
    STORAGE.userObj = False


@idk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}clone ?(.*)"))
@ydk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}clone ?(.*)"))
@wdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}clone ?(.*)"))
@sdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}clone ?(.*)"))
@adk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}clone ?(.*)"))
@bdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}clone ?(.*)"))
@cdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}clone ?(.*)"))
@edk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}clone ?(.*)"))
@hdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}clone ?(.*)"))
@ddk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}clone ?(.*)"))
@vkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}clone ?(.*)"))
@kkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}clone ?(.*)"))
@lkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}clone ?(.*)"))
@mkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}clone ?(.*)"))
@sid.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}clone ?(.*)"))
@shy.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}clone ?(.*)"))
@aan.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}clone ?(.*)"))
@ake.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}clone ?(.*)"))
@eel.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}clone ?(.*)"))
@khu.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}clone ?(.*)"))
@shi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}clone ?(.*)"))
@yaa.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}clone ?(.*)"))
@dav.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}clone ?(.*)"))
@raj.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}clone ?(.*)"))
@put.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}clone ?(.*)"))
@tsi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}clone ?(.*)"))
@tsf.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}clone ?(.*)"))
@teg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}clone ?(.*)"))
@tnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}clone ?(.*)"))
@tth.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}clone ?(.*)"))
@ton.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}clone ?(.*)"))
@ttw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}clone ?(.*)"))
@ttr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}clone ?(.*)"))
@tfr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}clone ?(.*)"))
@tfv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}clone ?(.*)"))
@tsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}clone ?(.*)"))
@tsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}clone ?(.*)"))
@ttg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}clone ?(.*)"))
@ttn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}clone ?(.*)"))
@fft.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}clone ?(.*)"))
@ffo.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}clone ?(.*)"))
@ftw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}clone ?(.*)"))
@ftr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}clone ?(.*)"))
@ffr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}clone ?(.*)"))
@ffv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}clone ?(.*)"))
@fsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}clone ?(.*)"))
@fsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}clone ?(.*)"))
@feg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}clone ?(.*)"))
@fnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}clone ?(.*)"))
@fvt.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}clone ?(.*)"))

# @register(outgoing=True, pattern=r"^\.clone ?(.*)")
async def impostor(event):
    if event.sender_id in SMEX_USERS:
        inputArgs = event.pattern_match.group(1)

        if "restore" in inputArgs:
            await event.reply("**Kembali ke identitas asli...**")
            if not STORAGE.userObj:
                return await event.reply(
                    "**Anda harus mengclone orang dulu sebelum kembali!**"
                )
            await updateProfile(STORAGE.userObj, restore=True)
            return await event.reply("**Berhasil Mengembalikan Akun Anda dari clone**")
        if inputArgs:
            try:
                user = await event.client.get_entity(inputArgs)
            except BaseException:
                return await event.reply("**Username/ID tidak valid.**")
            userObj = await event.client(GetFullUserRequest(user))
        elif event.reply_to_msg_id:
            replyMessage = await event.get_reply_message()
            if replyMessage.sender_id is None:
                return await event.reply("**Tidak dapat menyamar sebagai admin anonim 🥺**")
            userObj = await event.client(GetFullUserRequest(replyMessage.sender_id))
        else:
            return await event.reply("**Ketik** `.help clone` **bila butuh bantuan.**")

        if not STORAGE.userObj:
            STORAGE.userObj = await event.client(GetFullUserRequest(event.sender_id))

        LOGS.info(STORAGE.userObj)

        msg = await event.reply("**Mencuri identitas orang ini...**")
        await updateProfile(userObj)
        await msg.edit("**Aku adalah kamu dan kamu adalah aku. asekk 🥴**")


async def updateProfile(userObj, restore=False):
    firstName = (
        "Deleted Account"
        if userObj.user.first_name is None
        else userObj.user.first_name
    )
    lastName = "" if userObj.user.last_name is None else userObj.user.last_name
    userAbout = userObj.about if userObj.about is not None else ""
    userAbout = "" if len(userAbout) > 70 else userAbout
    if restore:
        userPfps = await client.get_profile_photos("me")
        userPfp = userPfps[0]
        await client(
            DeletePhotosRequest(
                id=[
                    InputPhoto(
                        id=userPfp.id,
                        access_hash=userPfp.access_hash,
                        file_reference=userPfp.file_reference,
                    )
                ]
            )
        )
    else:
        try:
            userPfp = userObj.profile_photo
            pfpImage = await client.download_media(userPfp)
            await client(UploadProfilePhotoRequest(await client.upload_file(pfpImage)))
        except BaseException:
            pass
    await client(
        UpdateProfileRequest(about=userAbout, first_name=firstName, last_name=lastName)
    )

"""
CMD_HELP.update(
    {
        "clone": "**Plugin : **`clone`\
        \n\n  •  **Syntax :** `.clone` <reply/username/ID>\
        \n  •  **Function : **Untuk mengclone identitas dari username/ID Telegram yang diberikan.\
        \n\n  •  **Syntax :** `.clone restore`\
        \n  •  **Function : **Mengembalikan ke identitas asli anda.\
        \n\n  •  **NOTE :** `.clone restore` terlebih dahulu sebelum mau nge `.clone` lagi.\
    "
    }
)
"""


# =======================[RABXEN]=======================

@idk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabxen((01)$|(\s+.*))"))
@ydk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabxen((02)$|(\s+.*))"))
@wdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabxen((03)$|(\s+.*))"))
@sdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabxen((04)$|(\s+.*))"))
@adk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabxen((05)$|(\s+.*))"))
@bdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabxen((06)$|(\s+.*))"))
@cdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabxen((07)$|(\s+.*))"))
@edk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabxen((08)$|(\s+.*))"))
@hdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabxen((09)$|(\s+.*))"))
@ddk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabxen((10)$|(\s+.*))"))
@vkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabxen((11)$|(\s+.*))"))
@kkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabxen((12)$|(\s+.*))"))
@lkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabxen((13)$|(\s+.*))"))
@mkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabxen((14)$|(\s+.*))"))
@sid.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabxen((15)$|(\s+.*))"))
@shy.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabxen((16)$|(\s+.*))"))
@aan.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabxen((17)$|(\s+.*))"))
@ake.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabxen((18)$|(\s+.*))"))
@eel.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabxen((19)$|(\s+.*))"))
@khu.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabxen((20)$|(\s+.*))"))
@shi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabxen((21)$|(\s+.*))"))
@yaa.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabxen((22)$|(\s+.*))"))
@dav.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabxen((23)$|(\s+.*))"))
@raj.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabxen((24)$|(\s+.*))"))
@put.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabxen((25)$|(\s+.*))"))
@tsi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabxen((26)$|(\s+.*))"))
@tsf.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabxen((27)$|(\s+.*))"))
@teg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabxen((28)$|(\s+.*))"))
@tnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabxen((29)$|(\s+.*))"))
@tth.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabxen((30)$|(\s+.*))"))
@ton.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabxen((31)$|(\s+.*))"))
@ttw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabxen((32)$|(\s+.*))"))
@ttr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabxen((33)$|(\s+.*))"))
@tfr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabxen((34)$|(\s+.*))"))
@tfv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabxen((35)$|(\s+.*))"))
@tsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabxen((36)$|(\s+.*))"))
@tsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabxen((37)$|(\s+.*))"))
@ttg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabxen((38)$|(\s+.*))"))
@ttn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabxen((39)$|(\s+.*))"))
@fft.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabxen((40)$|(\s+.*))"))
@ffo.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabxen((41)$|(\s+.*))"))
@ftw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabxen((42)$|(\s+.*))"))
@ftr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabxen((43)$|(\s+.*))"))
@ffr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabxen((44)$|(\s+.*))"))
@ffv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabxen((45)$|(\s+.*))"))
@fsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabxen((46)$|(\s+.*))"))
@fsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabxen((47)$|(\s+.*))"))
@feg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabxen((48)$|(\s+.*))"))
@fnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabxen((49)$|(\s+.*))"))
@fvt.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}rabxen((50)$|(\s+.*))"))


# =====[RABXEN]=====  

async def rabxen(event):
    if event.sender_id in SMEX_USERS:
        reply = random.choice(RABSEN)
        start = datetime.now()
        text = "run..."
        eventx = await event.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        textnew = await eventx.edit(f"**{reply}**\n`{ms}` 𝗺𝘀")
        await sleep(15)
        await textnew.delete()



# =====[RESTART]=====  


@idk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}restart"))
@ydk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}restart"))
@wdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}restart"))
@sdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}restart"))
@adk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}restart"))
@bdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}restart"))
@cdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}restart"))
@edk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}restart"))
@hdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}restart"))
@ddk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}restart"))
@vkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}restart"))
@kkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}restart"))
@lkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}restart"))
@mkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}restart"))
@sid.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}restart"))
@shy.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}restart"))
@aan.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}restart"))
@ake.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}restart"))
@eel.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}restart"))
@khu.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}restart"))
@shi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}restart"))
@yaa.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}restart"))
@dav.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}restart"))
@raj.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}restart"))
@put.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}restart"))
@tsi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}restart"))
@tsf.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}restart"))
@teg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}restart"))
@tnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}restart"))
@tth.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}restart"))
@ton.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}restart"))
@ttw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}restart"))
@ttr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}restart"))
@tfr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}restart"))
@tfv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}restart"))
@tsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}restart"))
@tsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}restart"))
@ttg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}restart"))
@ttn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}restart"))
@fft.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}restart"))
@ffo.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}restart"))
@ftw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}restart"))
@ftr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}restart"))
@ffr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}restart"))
@ffv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}restart"))
@fsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}restart"))
@fsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}restart"))
@feg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}restart"))
@fnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}restart"))
@fvt.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}restart"))


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
            await sdk.disconnect()
        except Exception as e:
            pass
        try:
            await hdk.disconnect() # 5
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
            await edk.disconnect()
        except Exception as e:
            pass
        try:
            await ddk.disconnect() # 10
        except Exception as e:
            pass
        try:
            await vkk.disconnect() 
        except Exception as e:
            pass
        try:
            await kkk.disconnect()
        except Exception as e:
            pass
        try:
            await lkk.disconnect()
        except Exception as e:
            pass
        try:
            await mkk.disconnect()
        except Exception as e:
            pass
        try:
            await sid.disconnect() # 15
        except Exception as e:
            pass
        try:
            await shy.disconnect()
        except Exception as e:
            pass
        try:
            await aan.disconnect()
        except Exception as e:
            pass
        try:
            await ake.disconnect()
        except Exception as e:
            pass
        try:
            await eel.disconnect()
        except Exception as e:
            pass
        try:
            await khu.disconnect() # 20
        except Exception as e:
            pass
        try:
            await shi.disconnect() 
        except Exception as e:
            pass
        try:
            await yaa.disconnect()
        except Exception as e:
            pass
        try:
            await dav.disconnect()
        except Exception as e:
            pass
        try:
            await raj.disconnect()
        except Exception as e:
            pass
        try:
            await put.disconnect() # 25
        except Exception as e:
            pass
        try:
            await tsi.disconnect()
        except Exception as e:
            pass
        try:
            await tsf.disconnect()
        except Exception as e:
            pass
        try:
            await teg.disconnect()
        except Exception as e:
            pass
        try:
            await tnn.disconnect()
        except Exception as e:
            pass
        try:
            await tth.disconnect() # 30
        except Exception as e:
            pass
        try:
            await ton.disconnect()
        except Exception as e:
            pass
        try:
            await ttw.disconnect()
        except Exception as e:
            pass
        try:
            await ttr.disconnect()
        except Exception as e:
            pass
        try:
            await tfr.disconnect()
        except Exception as e:
            pass
        try:
            await tfv.disconnect() # 35
        except Exception as e:
            pass
        try:
            await tsx.disconnect()
        except Exception as e:
            pass
        try:
            await tsv.disconnect()
        except Exception as e:
            pass
        try:
            await ttg.disconnect()
        except Exception as e:
            pass
        try:
            await ttn.disconnect()
        except Exception as e:
            pass
        try:
            await fft.disconnect() # 40
        except Exception as e:
            pass
        try:
            await ffo.disconnect() 
        except Exception as e:
            pass
        try:
            await ftw.disconnect()
        except Exception as e:
            pass
        try:
            await ftr.disconnect()
        except Exception as e:
            pass
        try:
            await ffr.disconnect()
        except Exception as e:
            pass
        try:
            await ffv.disconnect() # 45
        except Exception as e:
            pass
        try:
            await fsx.disconnect()
        except Exception as e:
            pass
        try:
            await fsv.disconnect()
        except Exception as e:
            pass
        try:
            await feg.disconnect()
        except Exception as e:
            pass
        try:
            await fnn.disconnect()
        except Exception as e:
            pass
        try:
            await fvt.disconnect() # 20
        except Exception as e:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()


# ========================[ABOUT]========================

@idk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}about$"))
@ydk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}about$"))
@wdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}about$"))
@sdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}about$"))
@adk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}about$"))
@bdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}about$"))
@cdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}about$"))
@edk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}about$"))
@hdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}about$"))
@ddk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}about$"))
@vkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}about$"))
@kkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}about$"))
@lkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}about$"))
@mkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}about$"))
@sid.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}about$"))
@shy.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}about$"))
@aan.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}about$"))
@ake.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}about$"))
@eel.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}about$"))
@khu.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}about$"))
@shi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}about$"))
@yaa.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}about$"))
@dav.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}about$"))
@raj.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}about$"))
@put.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}about$"))
@tsi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}about$"))
@tsf.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}about$"))
@teg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}about$"))
@tnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}about$"))
@tth.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}about$"))
@ton.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}about$"))
@ttw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}about$"))
@ttr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}about$"))
@tfr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}about$"))
@tfv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}about$"))
@tsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}about$"))
@tsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}about$"))
@ttg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}about$"))
@ttn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}about$"))
@fft.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}about$"))
@ffo.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}about$"))
@ftw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}about$"))
@ftr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}about$"))
@ffr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}about$"))
@ffv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}about$"))
@fsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}about$"))
@fsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}about$"))
@feg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}about$"))
@fnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}about$"))
@fvt.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}about$"))

async def about(event):
    if event.sender_id in SMEX_USERS:
       text = f"""
╭┈─╼━━━━━━━━━━━━━╾─┈ 
│     
│      「 ⚡️𝘿𝙇-𝙓 𝙐𝙎𝙀𝙍𝘽𝙊𝙏⚡️ 」
│     
├┈─╼━━━━━━━━━━━━━╾─┈  
├ [ UB Type ]\t\t       : <b><a href="https://t.me/AlphaXProject/14">DLX-50</a></b>
├ [ Version ]\t\t       : <u>{ubversi}</u>
├ [ Language ]      : #python
├ [ Library ]\t       : #telethon
├ [ Platform ]\t      : #telegram
├ [ Command ]       : <b>{HNDLR}about</b>
├ [ Handler ]\t\t       : <b>" {HNDLR} "</b>
├ [ Host ]\t\t\t          : Heroku
├ [ AppName ]       : <a href="https://dashboard.heroku.com/apps/{HEROKU_APP_NAME}">{HEROKU_APP_NAME}</a>
├ [ Repo ]\t\t\t          : <a href="{REPO_LINK}">Link Here</a>
├ [ Dev Team ]      : @AlphaXProject
├ [ Powered by ]    : @AliansiAlphaX
╰┈─────────────┈
 - [ Sudo Users ]   : <i>{SUDO}</i>
 """
       await event.reply(text, parse_mode='html', link_preview=None )
  
        
# =========[HELP]=========     
        


@idk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}help$"))
@ydk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}help$"))
@wdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}help$"))
@sdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}help$"))
@adk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}help$"))
@bdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}help$"))
@cdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}help$"))
@edk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}help$"))
@hdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}help$"))
@ddk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}help$"))
@vkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}help$"))
@kkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}help$"))
@lkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}help$"))
@mkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}help$"))
@sid.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}help$"))
@shy.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}help$"))
@aan.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}help$"))
@ake.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}help$"))
@eel.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}help$"))
@khu.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}help$"))
@shi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}help$"))
@yaa.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}help$"))
@dav.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}help$"))
@raj.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}help$"))
@put.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}help$"))
@tsi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}help$"))
@tsf.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}help$"))
@teg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}help$"))
@tnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}help$"))
@tth.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}help$"))
@ton.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}help$"))
@ttw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}help$"))
@ttr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}help$"))
@tfr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}help$"))
@tfv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}help$"))
@tsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}help$"))
@tsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}help$"))
@ttg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}help$"))
@ttn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}help$"))
@fft.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}help$"))
@ffo.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}help$"))
@ftw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}help$"))
@ftr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}help$"))
@ffr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}help$"))
@ffv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}help$"))
@fsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}help$"))
@fsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}help$"))
@feg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}help$"))
@fnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}help$"))
@fvt.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}help$"))


async def help(e):
    if e.sender_id in SMEX_USERS:
       text = f"""🔰 𝗔𝘃𝗮𝗶𝗹𝗮𝗯𝗹𝗲 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀

🛠 𝙐𝙩𝙞𝙡𝙨:
<code>.ping</code>
<code>.alive</code>
<code>.restart</code>

🎛 𝙐𝙨𝙚𝙧𝙗𝙤𝙩:
<code>.bio</code>
<code>.join</code>
<code>.pjoin</code>
<code>.leave</code>
<code>.inviteall</code>

☠️ 𝙎𝙥𝙖𝙢:
<code>.spam</code>
<code>.delayspam</code>
<code>.bigspam</code>
<code>.raid</code>
<code>.replyraid</code>
<code>.dreplyraid</code>

⚔️ 𝙓𝙩𝙧𝙖:
<code>.absen</code>
<code>.pinx</code>
<code>.purgeme</code>
<code>.rabsen</code>
<code>.setname</code>
<code>.setpfp</code>
<code>.delpfp</code>
<code>.username</code>
<code>.stats</code>
<code>.dm</code>
<code>.getmemb</code>
<code>.addmemb</code>
<code>.eval</code>
<code>.exec</code>
<code>.term</code>
<code>.ls</code> | <code><i>(bug)</i></code>
<code>.setbio</code>
<code>.pprandom</code> | <code><i>(bug)</i></code>
<code>.sd</code>
<code>.repo</code>
<code>.vsudo</code>
<code>.send</code>
<code>.del</code>
<code>.invite</code>
<code>.gcast</code>
<code>.gucast</code>
<code>.reserved</code>
<code>.sendbot</code>
<code>.about</code>
<code>.tmsg</code>
<code>.ftyping</code>
<code>.gpoto</code>
<code>.asupan</code>
<code>.wibu</code>
<code>.chika</code>
<code>.evil</code>
<code>.clone</code> & <code>.clone restore</code>
<code>.rabxen</code>
<code>.spurgeme</code>

<i>For more help regarding usage \nof plugins type plugins name</i>

🤖 𝘽𝙤𝙩 𝙄𝙣𝙛𝙤 
- <i>Version :</i> <code>{ubversi}</code>
- <i>Type \t\t\t:</i> <code>DLX50 UB</code>
- <i>Project :</i> <code>@AlphaXProject</code>
"""
       await e.reply(text, parse_mode='html', link_preview=None )

        
        
text = f"""

💥 [CONGRATULATIONS] UR 「 ⚡️𝘿𝙇-𝙓𝟓𝟎 𝙐𝘽⚡️ 」 {ubversi} IS READY!
💥 Recode By @AlphaXProject Team"""

print(text)
print("")
print(f"🔥 [INFO] : SMEX! UB STARTED SUCCESFULLY!.")
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
        tsf.disconnect()
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
        tsf.run_until_disconnected()
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
