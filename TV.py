# this will contain the code for the TV class

class TV :
    def __init__(self):
        # set default values for channel, volume and tv on
        self.channel = 1 #int
        self.volume_level = 1 #int
        self.tv_on = False # boolean

    # TV on and off
    def turn_on_TV(self):
        self.tv_on = True
    def turn_off_TV(self):
        self.tv_on = False
    
    # get and set channel
    def get_channel(self):
        return self.channel
    def set_channel(self, channel):
        if self.on and 1 <= channel <= 120:
            self.channel = channel

    # get and set volume level
    def get_volume_level(self):
        return self.volume_level
    def set_volume_level(self, volume_level):
        if self.on and 1 <= volume_level <=7:
            self.volume_level = volume_level

    




#    UML Diagram


# getvolume(): int
# setVolume(volumeLevel: int): None
# channelUp(): None
# channelDown(): None
# volumeUp(): None
# volumeDown(): None