import os
import feedparser
from sql import db
from time import sleep, time
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from apscheduler.schedulers.background import BackgroundScheduler
from requests.utils import requote_uri


api_id = ""   # Get it from my.telegram.org
api_hash = ""   # Get it from my.telegram.org
feed_url = ""   # RSS Feed URL of the site.
feed_url1 = ""   # RSS Feed URL of the site.
feed_url2 = ""   # RSS Feed URL of the site.
feed_url3 = ""   # RSS Feed URL of the site.
feed_url4 = ""   # RSS Feed URL of the site.
feed_url5 = ""   # RSS Feed URL of the site.
feed_url6 = ""   # RSS Feed URL of the site.
feed_url7 = ""   # RSS Feed URL of the site.
feed_url8 = ""   # RSS Feed URL of the site.
bot_token = ""   # Get it by creating a bot on https://t.me/botfather
log_channel = ""   # Telegram Channel ID where the bot is added and have write permission. You can use group ID too.
check_interval = 5   # Check Interval in seconds.  
max_instances = 5   # Max parallel instance to be used.
if os.environ.get("ENV"):   # Add a ENV in Environment Variables if you wanna configure the bot via env vars.
  api_id = os.environ.get("APP_ID")
  api_hash = os.environ.get("API_HASH")
  feed_url = os.environ.get("FEED_URL")
  feed_url1 = os.environ.get("FEED_URL1")
  feed_url2 = os.environ.get("FEED_URL2")
  feed_url3 = os.environ.get("FEED_URL3")
  feed_url5 = os.environ.get("FEED_URL5")
  feed_url6 = os.environ.get("FEED_URL6")
  feed_url7 = os.environ.get("FEED_URL7")
  feed_url8 = os.environ.get("FEED_URL8")
  bot_token = os.environ.get("BOT_TOKEN")
  log_channel = int(os.environ.get("LOG_CHANNEL", None))
  check_interval = int(os.environ.get("INTERVAL", 5))
  max_instances = int(os.environ.get("MAX_INSTANCES", 5))

if db.get_link(feed_url) == None:
   db.update_link(feed_url, "*")

app = Client(":memory:", api_id=api_id, api_hash=api_hash, bot_token=bot_token)      
      
def check_feed():
    FEED = feedparser.parse(feed_url)
    entry = FEED.entries[0]
    if entry.id != db.get_link(feed_url).link:
      criterion_1_list = ["1080p", "megusta"]
      if all(criterion_1 in entry.title.lower() for criterion_1 in criterion_1_list):
        message = f"/dank {entry['torrent_magneturi']}"
      else:
        message = f"unwanted"
      try:
        app.send_message(log_channel, message)
        db.update_link(feed_url, entry.id)
      except FloodWait as e:
        print(f"FloodWait: {e.x} seconds")
        sleep(e.x)
      except Exception as e:
        print(e)
    else:
      print(f"Checked RSS FEED - EZTV")
      

if db.get_link(feed_url1) == None:
   db.update_link(feed_url1, "*")

app = Client(":memory:", api_id=api_id, api_hash=api_hash, bot_token=bot_token)      
      
def check_feed1():
    FEED = feedparser.parse(feed_url1)
    entry = FEED.entries[0]
    if entry.link != db.get_link(feed_url1).link:
        criterion_1_list = ["720p", "hdtv", "leagueweb", "lmovhd", "480p", "576p", "cmct", "ltvhd", "beitai", "leaguetv", "pterweb", "bae", "hdsweb", "720", "hdctv"]
        criterion_2_list = ["2160p", "1080p"]
        criterion_3_list = ["cinefeel", "ntb", "tepes", "appletor", "telly", "tommy", "monkee", "kings", "sbr", "don", "btn", "ijp", "t7st", "rcvr", "visum", "ntg", "apj69", "trollhd", "trolluhd", "flux", "sigma", "epsilon", "bordure", "leaguenf", "cinefile"]
        if "tv" in entry.category.lower() and any(criterion_2 in entry.title.lower() for criterion_2 in criterion_2_list) and any(criterion_3 in entry.title.lower() for criterion_3 in criterion_3_list):
            message = f"/wink {entry.enclosures[0]['href']}"
        elif "remux" in entry.title.lower():
            message = f"/kink {entry.enclosures[0]['href']}"
        elif any(criterion_1 in entry.title.lower() for criterion_1 in criterion_1_list):
            message = f"unwanted"
        else:
            message = f"/get {entry.enclosures[0]['href']}"
        try:
          app.send_message(log_channel, message)
          db.update_link(feed_url1, entry.link)
        except FloodWait as e:
          print(f"FloodWait: {e.x} seconds")
          sleep(e.x)
        except Exception as e:
          print(e)
    else:
      print(f"Checked RSS FEED1 - LHD Encodes")

if db.get_link(feed_url2) == None:
   db.update_link(feed_url2, "*")

app = Client(":memory:", api_id=api_id, api_hash=api_hash, bot_token=bot_token)      

def check_feed2():
    FEED = feedparser.parse(feed_url2)
    entry = FEED.entries[0]
    if entry.id != db.get_link(feed_url2).link:
      criterion_1_list = ["1080p", "2160p"]
      criterion_2_list = ["gerald", "dovi", "bhd", "zgxyi", "bbqddq", "club", "exkinoray", "selezen"]
      criterion_3 = "remux"
      if any(criterion_1 in entry.title.lower() for criterion_1 in criterion_1_list) and any(criterion_2 in entry.title.lower() for criterion_2 in criterion_2_list):
          message = f"/chink {requote_uri(entry.enclosures[0]['href'])}"
      elif criterion_3 in entry.title.lower():
          message = f"/kink {requote_uri(entry.enclosures[0]['href'])}"           
      else:
          message = f"unwanted"
      try:
        app.send_message(log_channel, message)
        db.update_link(feed_url2, entry.id)
      except FloodWait as e:
        print(f"FloodWait: {e.x} seconds")
        sleep(e.x)
      except Exception as e:
        print(e)
    else:
      print(f"Checked RSS FEED2 - Torlock Movies")  
            
        
if db.get_link(feed_url3) == None:
   db.update_link(feed_url3, "*")

app = Client(":memory:", api_id=api_id, api_hash=api_hash, bot_token=bot_token)      
      
def check_feed3():
    FEED = feedparser.parse(feed_url3)
    entry = FEED.entries[0]
    if entry.link != db.get_link(feed_url3).link:
        criterion_1_list = ["1080p", "freeleech"]
        criterion_2_list = ["cinefeel", "ntb", "tepes", "telly", "tommy", "monkee", "kings", "sbr", "don", "btn", "ijp", "t7st", "rcvr", "visum", "ntg", "apj69", "trollhd", "trolluhd", "appletor", "flux", "sigma"]
        if all(criterion_1 in entry.title.lower() for criterion_1 in criterion_1_list) and any(criterion_2 in entry.title.lower() for criterion_2 in criterion_2_list):
            message = f"/wink {entry.link}"
        else:
            message = f"unwanted"
        try:
          app.send_message(log_channel, message)
          db.update_link(feed_url3, entry.link)
        except FloodWait as e:
          print(f"FloodWait: {e.x} seconds")
          sleep(e.x)
        except Exception as e:
          print(e)
    else:
      print(f"Checked RSS FEED3 - Filelist")             

      
if db.get_link(feed_url5) == None:
   db.update_link(feed_url5, "*")

app = Client(":memory:", api_id=api_id, api_hash=api_hash, bot_token=bot_token)      
      
def check_feed5():
    FEED = feedparser.parse(feed_url5)
    entry = FEED.entries[0]
    if entry.id != db.get_link(feed_url5).link:
       criterion_1 = "1080p"
       criterion_2_list = ["wiki", "beast", "chd", "ank", "lhd"]
       if criterion_1 in entry.title.lower() and any(criterion_2 in entry.title.lower() for criterion_2 in criterion_2_list):         
         message = f"/get {entry.enclosures[0]['href']}"
       elif 'remux' in entry.title.lower():
         message = f"/kink {entry.enclosures[0]['href']}"
       else:
         message = f"unwanted"
       try:
        app.send_message(log_channel, message)
        db.update_link(feed_url5, entry.id)
       except FloodWait as e:
        print(f"FloodWait: {e.x} seconds")
        sleep(e.x)
       except Exception as e:
        print(e)
    else:
      print(f"Checked RSS FEED5 - HDTime Encodes")           

      
if db.get_link(feed_url6) == None:
   db.update_link(feed_url6, "*")

app = Client(":memory:", api_id=api_id, api_hash=api_hash, bot_token=bot_token)      
      
def check_feed6():
    FEED = feedparser.parse(feed_url6)
    entry = FEED.entries[0]
    if entry.link != db.get_link(feed_url6).link:
      criterion_1 = "remux"
      if criterion_1 in entry.title.lower():
        message = f"/kink {entry.enclosures[0]['href']}"
      else:
        message = f"/get {entry.enclosures[0]['href']}"
      try:
        app.send_message(log_channel, message)
        db.update_link(feed_url6, entry.link)
      except FloodWait as e:
        print(f"FloodWait: {e.x} seconds")
        sleep(e.x)
      except Exception as e:
        print(e)
    else:
      print(f"Checked RSS FEED6 - LHD REMUX")       
      

if db.get_link(feed_url7) == None:
   db.update_link(feed_url7, "*")

app = Client(":memory:", api_id=api_id, api_hash=api_hash, bot_token=bot_token)      
      
def check_feed7():
    FEED = feedparser.parse(feed_url7)
    entry = FEED.entries[0]
    if entry.link != db.get_link(feed_url7).link:
      criterion_1 = "1080p"
      criterion_2_list = ["playhd", "ift", "ctrlhd", "lord", "don", "zq", "viethd", "tayto", "sa89", "gyroscope", "ebp"]
      if criterion_1 in entry.title and any(criterion_2 in entry.title.lower() for criterion_2 in criterion_2_list):
        message = f"/mirror2 {entry.link}"
      else:
        message = f"unwanted"
      try:
        app.send_message(log_channel, message)
        db.update_link(feed_url7, entry.link)
      except FloodWait as e:
        print(f"FloodWait: {e.x} seconds")
        sleep(e.x)
      except Exception as e:
        print(e)
    else:
      print(f"Checked RSS FEED7 - Filelist 1080p")      

      
if db.get_link(feed_url8) == None:
   db.update_link(feed_url8, "*")

app = Client(":memory:", api_id=api_id, api_hash=api_hash, bot_token=bot_token)      
      
def check_feed8():
    FEED = feedparser.parse(feed_url8)
    entry = FEED.entries[0]
    if entry.id != db.get_link(feed_url8).link:
      criterion_1 = "1080p"
      criterion_2_list = ["-ks-", "iahd", "kaidubs", "judas", "anime time", "golumpa", "subsplease"]
      if criterion_1 in entry.title and any(criterion_2 in entry.title.lower() for criterion_2 in criterion_2_list):
        message = f"/anime {entry.link}"
      else:
        message = f"infinity is gei"
      try:
        app.send_message(log_channel, message)
        db.update_link(feed_url8, entry.id)
      except FloodWait as e:
        print(f"FloodWait: {e.x} seconds")
        sleep(e.x)
      except Exception as e:
        print(e)
    else:
      print(f"Checked RSS FEED8 - Nyaa")            
      
        
scheduler = BackgroundScheduler()
scheduler.add_job(check_feed, "interval", seconds=check_interval, max_instances=max_instances, misfire_grace_time=None)
scheduler.add_job(check_feed1, "interval", seconds=check_interval, max_instances=max_instances, misfire_grace_time=None)
scheduler.add_job(check_feed2, "interval", seconds=check_interval, max_instances=max_instances, misfire_grace_time=None)
scheduler.add_job(check_feed3, "interval", seconds=check_interval, max_instances=max_instances, misfire_grace_time=None)
scheduler.add_job(check_feed5, "interval", seconds=check_interval, max_instances=max_instances, misfire_grace_time=None)
scheduler.add_job(check_feed6, "interval", seconds=check_interval, max_instances=max_instances, misfire_grace_time=None)
scheduler.add_job(check_feed7, "interval", seconds=check_interval, max_instances=max_instances, misfire_grace_time=None)
scheduler.add_job(check_feed8, "interval", seconds=check_interval, max_instances=max_instances, misfire_grace_time=None)
scheduler.start()
app.run()
