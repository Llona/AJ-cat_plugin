from copy_plugin import RunTicket
from os import system
import settings

plugin = RunTicket()
plugin.setup()
plugin.screen_high = 2220
plugin.screen_wight = 1080
plugin.fight_x = 554
plugin.fight_y = 833
# plugin.fight_x = 233
# plugin.fight_y = 542
plugin.fight_offset = plugin.screen_high*plugin.fight_y+plugin.fight_x

settings.DEVICE_ID = '2785a241e41c7ece'
settings.FIGHTING_COLOR = "3c5e85"

system(plugin.get_pixel_color_cmd())

