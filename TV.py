# this will contain the code for the TV class

class TV :
    def __init__(self, channel, volume_level, tv_on):
        # set default values for channel, volume and tv on
        self.channel = 1
        self.volume_level = 1
        self.tv_on = False

    def turn_on_TV(self):
        self.tv_on