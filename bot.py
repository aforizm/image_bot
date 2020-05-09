# -*- coding: utf-8 -*-
#!venv/bin/python3.8
import os
import logging
from aiogram import Bot, Dispatcher, executor, types

#apihelper.proxy = {'https': 'socks5://330810376:g5nihUaG@orbtl.s5.opennetwork.cc:999'}
PROXY_URL = 'socks5://330810376:g5nihUaG@orbtl.s5.opennetwork.cc:999'

# Configure logging
logging.basicConfig(level=logging.INFO)


# Initialize bot and dispatcher
bot = Bot(token=os.environ.get('BOT_TOKEN'), proxy=PROXY_URL)
dp = Dispatcher(bot)