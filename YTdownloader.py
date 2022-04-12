from check_input import Check_input
from visual_menu import Visual_menu
import sys

check_input = Check_input()

if __name__ == "__main__":
    try:
        try:
            if sys.argv[2] == "-a":
                check_input.check_params(sys.argv[1], True)
            else:
                check_input.check_params(sys.argv[1], False)
        except IndexError:
            check_input.check_params(sys.argv[1], False)
    except IndexError:
        Visual_menu()
