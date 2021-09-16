from copy_plugin import RunTicket
from os import system

plugin = RunTicket()
plugin.setup()
plugin.fight_x = 614
plugin.fight_y = 833
# plugin.fight_x = 233
# plugin.fight_y = 542
plugin.fight_offset = plugin.screen_high*plugin.fight_y+plugin.fight_x

system(plugin.get_pixel_color_cmd())

