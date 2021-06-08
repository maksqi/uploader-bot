import pyshorteners
from data.config import BITLY_KEY, CUTTLY_KEY


async def short_link(url):
    try:
        s = pyshorteners.Shortener()
        dagb = s.dagd.short(url)
    except:
        dagb = '404'

    try:
        s = pyshorteners.Shortener(api_key=BITLY_KEY)
        bitly = s.bitly.short(url)
    except:
        bitly = '404'

    try:
        s = pyshorteners.Shortener(api_key=CUTTLY_KEY)
        cuttly = s.cuttly.short(url)
    except:
        cuttly = '404'

    return bitly, cuttly, dagb
