
# Dictionary mapping website names (in lowercase) to their URLs
websites = {
    "youtube": "https://www.youtube.com",
    "gmail": "https://mail.google.com",
    "disney": "https://www.hotstar.com",
    "facebook": "https://www.facebook.com",
    "instagram": "https://www.instagram.com",
    "twitter": "https://www.twitter.com",
    "linkedin": "https://www.linkedin.com",
    "reddit": "https://www.reddit.com",
    "amazon": "https://www.amazon.com",
    "google": "https://www.google.com",
    "netflix": "https://www.netflix.com",
    "wikipedia": "https://www.wikipedia.org",
    "yahoo": "https://www.yahoo.com",
    "ebay": "https://www.ebay.com",
    "pinterest": "https://www.pinterest.com",
    "whatsapp": "https://web.whatsapp.com",
    "tiktok": "https://www.tiktok.com",
    "bing": "https://www.bing.com",
    "apple": "https://www.apple.com",
    "spotify": "https://www.spotify.com",
    "dropbox": "https://www.dropbox.com",
    "paypal": "https://www.paypal.com",
    "microsoft": "https://www.microsoft.com",
    "quora": "https://www.quora.com",
    "hulu": "https://www.hulu.com",
    "twitch": "https://www.twitch.tv",
    "airbnb": "https://www.airbnb.com",
    "zoom": "https://zoom.us",
    "adobe": "https://www.adobe.com",
    "cnn": "https://www.cnn.com",
    "bbc": "https://www.bbc.com",
    "nytimes": "https://www.nytimes.com",
    "the guardian": "https://www.theguardian.com",
    "slack": "https://slack.com",
    "github": "https://github.com",
    "vimeo": "https://vimeo.com",
    "coursera": "https://www.coursera.org",
    "udemy": "https://www.udemy.com",
    "khan academy": "https://www.khanacademy.org",
    "medium": "https://medium.com",
    "stackoverflow": "https://stackoverflow.com",
    "wordpress": "https://wordpress.com",
    "shopify": "https://www.shopify.com",
    "walmart": "https://www.walmart.com",
    "target": "https://www.target.com",
    "costco": "https://www.costco.com",
    "best buy": "https://www.bestbuy.com",
    "aliexpress": "https://www.aliexpress.com",
    "etsy": "https://www.etsy.com",
    "discord": "https://discord.com",
    "fiverr": "https://www.fiverr.com",
    "upwork": "https://www.upwork.com",
    "canva": "https://www.canva.com",
    "wetransfer": "https://wetransfer.com",
    "soundcloud": "https://soundcloud.com",
    "deezer": "https://www.deezer.com",
    "flipkart": "https://www.flipkart.com",
    "alibaba": "https://www.alibaba.com",
    "telegram": "https://web.telegram.org",
    "wechat": "https://www.wechat.com",
    "yandex": "https://yandex.com",
    "baidu": "https://www.baidu.com",
    "duckduckgo": "https://duckduckgo.com",
    "mozilla": "https://www.mozilla.org",
    "trello": "https://trello.com",
    "notion": "https://www.notion.so",
    "asana": "https://asana.com",
    "xfinity": "https://www.xfinity.com",
    "verizon": "https://www.verizon.com",
    "att": "https://www.att.com",
    "t-mobile": "https://www.t-mobile.com",
    "salesforce": "https://www.salesforce.com",
    "oracle": "https://www.oracle.com",
    "sap": "https://www.sap.com",
    "ibm": "https://www.ibm.com",
    "intel": "https://www.intel.com",
    "amd": "https://www.amd.com",
    "nvidia": "https://www.nvidia.com",
    "tesla": "https://www.tesla.com",
    "ford": "https://www.ford.com",
    "gm": "https://www.gm.com",
    "uber": "https://www.uber.com",
    "lyft": "https://www.lyft.com",
    "booking.com": "https://www.booking.com",
    "expedia": "https://www.expedia.com",
    "tripadvisor": "https://www.tripadvisor.com",
    "zillow": "https://www.zillow.com",
    "realtor": "https://www.realtor.com",
    "indeed": "https://www.indeed.com",
    "glassdoor": "https://www.glassdoor.com",
    "monster": "https://www.monster.com",
    "craigslist": "https://www.craigslist.org",
    "angi": "https://www.angi.com",
    "homedepot": "https://www.homedepot.com",
    "lowes": "https://www.lowes.com",
    "wayfair": "https://www.wayfair.com",
    "ikea": "https://www.ikea.com",
    "overstock": "https://www.overstock.com",
    "sephora": "https://www.sephora.com",
    "ulta": "https://www.ulta.com",
    "nordstrom": "https://www.nordstrom.com",
    "macys": "https://www.macys.com",
    "nike": "https://www.nike.com",
    "adidas": "https://www.adidas.com",
    "under armour": "https://www.underarmour.com",
    "puma": "https://www.puma.com",
    "weather": "https://weather.com",
    "accuweather": "https://www.accuweather.com",
    "espn": "https://www.espn.com",
    "bleacher report": "https://bleacherreport.com",
    "mlb": "https://www.mlb.com",
    "nfl": "https://www.nfl.com",
    "nba": "https://www.nba.com",
    "nhl": "https://www.nhl.com",
    "cbs": "https://www.cbs.com",
    "nbc": "https://www.nbc.com",
    "abc": "https://abc.com",
    "fox news": "https://www.foxnews.com",
    "bloomberg": "https://www.bloomberg.com",
    "reuters": "https://www.reuters.com",
    "financial times": "https://www.ft.com",
    "forbes": "https://www.forbes.com",
    "business insider": "https://www.businessinsider.com",
    "investopedia": "https://www.investopedia.com",
    "coinbase": "https://www.coinbase.com",
    "binance": "https://www.binance.com",
    "kraken": "https://www.kraken.com",
    "opensea": "https://opensea.io",
    "tether": "https://tether.to",
    "ethereum": "https://ethereum.org",
    "bitcoin": "https://bitcoin.org",
    "nasa": "https://www.nasa.gov",
    "spacex": "https://www.spacex.com",
    "national geographic": "https://www.nationalgeographic.com",
    "smithsonian": "https://www.si.edu",
    "who": "https://www.who.int",
    "unicef": "https://www.unicef.org",
    "un": "https://www.un.org",
    "imf": "https://www.imf.org",
    "world bank": "https://www.worldbank.org",
    "wto": "https://www.wto.org",
    "oecd": "https://www.oecd.org",
    "venus": "https://www.venusgemtestinglab.com",
    "dekho": "https://www.cardekho.com",
    "cardekho": "https://www.cardekho.com",
    "memes": "https://www.memes.com",

}

import webbrowser
import os
from os import getcwd
from TTS_B import speak

   
def openweb(webname):
  try:
      # Normalize input to lowercase and split into words
      website_name = webname.lower().strip().split()  # Ensure input is trimmed and split
      counts = {}
      # Count occurrences of each website name
      for name in website_name:
          name = name.strip()  # Extra check to ensure no extra spaces
          counts[name] = counts.get(name, 0) + 1
      
      urls_to_open = []
      # Check if each name corresponds to a website
      for name, count in counts.items():
          if name in websites:
              urls_to_open.extend([websites[name]] * count)
              website_name = name
              speak(f"Opening {website_name} ")
              
          else:
              print(f"Website '{name}' not found in the list.")  # Debug info if not found
              
      # Open the URLs
      for url in urls_to_open:
          
          print(f"Opening {url}...")  # Debug statement to confirm what URLs are being opened
          webbrowser.open(url)
          speak(f"Successfully Opened {website_name} website Sir")
          
      if urls_to_open:
          print("Opening websites...")
          
      else:
          print("No valid websites found in your input.")
          
  except Exception as e:
      print(f"Error opening website: {e}")
