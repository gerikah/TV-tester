# this file will contain the test driver program that creates two objects from TV class

# object 1: tv1
from TV import TV
def main ():
    tv_1 = TV()
    tv_1.turn_on_TV ()
    tv_1.set_channel(30)
    tv_1.set_volume_level(3)

    tv_2 = TV()
    tv_2.turn_on_TV()
    tv_2.set_channel(3)
    tv_2.set_volume_level(2)

    print("TV 1's channel is", tv_1.get_channel(), "and volume level is ", tv_1.get_volume_level())
    print("TV 2's channel is", tv_2.get_channel(), "and volume level is ", tv_2.get_volume_level())

if __name__ == "__main__":
    main()