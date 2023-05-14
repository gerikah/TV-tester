# this will contain the code for the TV class

class TV :
    def __init__(self, channel, volume_level, tv_on):
        # set default values for channel, volume and tv on
        self.channel = 1
        self.volume_level = 1
        self.tv_on = False

    # TV on and off
    def turn_on_TV(self):
        self.tv_on = True
    def turn_off_TV(self):
        self.tv_on = False

#    UML Diagram
# channel: int
# volumeLevel: int
# on: bool
# TV()
# turnOn(): None
# turnOff(): None
# getChannel(): int
# setChannel (channel: int): None
# getvolume(): int
# setVolume(volumeLevel: int): None
# channelUp(): None
# channelDown(): None
# volumeUp(): None
# volumeDown(): None