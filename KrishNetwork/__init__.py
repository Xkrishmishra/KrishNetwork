from KrishNetwork.core.bot import Hotty
from KrishNetwork.core.dir import dirr
from KrishNetwork.core.git import git
from KrishNetwork.core.userbot import Userbot
from KrishNetwork.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Hotty()
userbot = Userbot()
api = SafoneAPI()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

APP = "Systumm_music_bot"  # connect music api key "Dont change it"
