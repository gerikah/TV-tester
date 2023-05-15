# this will contain the code for the TV class

class TV :
    def __init__(self, channel, volume_level, tv_power):
        # set default values for channel, volume and tv on
        self.channel = 1 #int
        self.volume_level = 1 #int
        self.tv_power = False # boolean

    # TV on and off
    def turn_on_TV(self):
        self.tv_power = True
    def turn_off_TV(self):
        self.tv_power = False
    
    # get and set channel
    def get_channel(self):
        return self.channel
    def set_channel(self, channel):
        if self.tv_power and 1 <= channel <= 120:
            self.channel = channel

    # switch channel up
    def channel_up(self):
        if self.tv_power and  self.channel < 120:
            self.channel += 1
    # switch channel down
    def channel_down(self):
        if self.tv_power and self.channel > 1:
            self.channel -= 1

    # get and set volume level
    def get_volume_level(self):
        return self.volume_level
    def set_volume_level(self, volume_level):
        if self.tv_power and 1 <= volume_level <=7:
            self.volume_level = volume_level

    # switch volume up
    def volume_up(self):
        if self.tv_power and self.volume_level < 7:
            self.volume_level += 1
    # switch volume down
    def volume_down(self):
        if self.tv_power and self.volume_level > 1:
            self.volume_level -= 1

    