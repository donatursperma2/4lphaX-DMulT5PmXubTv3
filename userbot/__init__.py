# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
# inline credit @keselekpermen69
# Recode by @mrismanaziz
# t.me/SharingUserbot
#
""" Userbot initialization. """

import os
import re
import sys
import time

from sys import version_info
from logging import basicConfig, getLogger, INFO, DEBUG
from distutils.util import strtobool as sb
from math import ceil

from pathlib import Path
# from pylast import LastFMNetwork, md5
# from pySmartDL import SmartDL
# from pymongo import MongoClient
# from redis import StrictRedis
from dotenv import load_dotenv
from requests import get
from telethon.sync import TelegramClient, custom, events
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
from telethon.sessions import StringSession

from .storage import Storage

STORAGE = (lambda n: Storage(Path("data") / n))

load_dotenv("config.env")

LOGS = getLogger(__name__)

if version_info[0] < 3 or version_info[1] < 9:
    LOGS.info("Anda HARUS memiliki python setidaknya versi 3.9."
              "Beberapa fitur tergantung versi python ini. Bot berhenti.")
    sys.exit(1)
