# this file will contain the test driver program that creates two objects from TV class

try:
    import pyfiglet
except ImportError:
    print("The required module 'pyfiglet' is not installed.\nPlease install the module to continue.")

border = "_"*180
program_title = ("TV Tester")

print("\n\n" + border + "\n\n" + "\033[95m" + pyfiglet.figlet_format(program_title, justify = "center", font = "isometric1", width = 175) + "\n" + border)

from TV import TV
def main ():
    # object 1: tv1
    tv_1 = TV()
    tv_1.turn_on_TV ()
    tv_1.set_channel(30)
    tv_1.set_volume_level(3)
    test_tv1 = ("TV 1's channel is", tv_1.get_channel(), "and volume level is ", tv_1.get_volume_level())
    print(test_tv1)

    # object 2: tv2
    tv_2 = TV()
    tv_2.turn_on_TV()
    tv_2.set_channel(3)
    tv_2.set_volume_level(2)
    test_tv2 = ("TV 2's channel is", tv_2.get_channel(), "and volume level is ", tv_2.get_volume_level())
    print(test_tv2)

if __name__ == "__main__":
    main()