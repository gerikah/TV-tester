# Alday, Gerikah L.
# BSCPE 1-5
# Object Oriented Programming : Assignment 6

# this file will contain the test driver program that creates two objects from TV class

# import module with exception handling
try:
    import pyfiglet
except ImportError:
    print("The required module 'pyfiglet' is not installed.\nPlease install the module to continue.")

# for design
border = "_"*180
program_title = ("TV Tester")

# import from TV class
from TV import TV
def main ():
    # object 1: tv1
    tv_1 = TV()
    tv_1.turn_on_TV ()
    tv_1.set_channel(30)
    tv_1.set_volume_level(3)
    test_tv1 = ("TV 1's channel is", tv_1.get_channel(), "and volume level is ", tv_1.get_volume_level())
    centered_tv1 = ' '.join(str(item) for item in test_tv1).center(180)

    # object 2: tv2
    tv_2 = TV()
    tv_2.turn_on_TV()
    tv_2.set_channel(3)
    tv_2.set_volume_level(2)
    test_tv2 = ("TV 2's channel is", tv_2.get_channel(), "and volume level is ", tv_2.get_volume_level())
    centered_tv2 = ' '.join(str(item) for item in test_tv1).center(180)

    # print all the results
    print("\n\n" + border + "\n\n" + "\033[95m" + pyfiglet.figlet_format(program_title, justify = "center", font = "isometric1", width = 175) + "\n" + border)
    print("\n\n" + centered_tv1)
    print("\n\n" + centered_tv2)
    print("\n" + border)

if __name__ == "__main__":
    main()