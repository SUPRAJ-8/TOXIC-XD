import time

def crackfile():
    while True:
        print('\033[0;97m-----------------------------------------------')
        print(' [\u001b[36m•\033[1;37m] Input File Name Without /sdcard ')
        filename = input(' [\u001b[36m•\033[1;37m] Enter The Name Of File : ')
        o = '/sdcard/' + filename  # Form the complete file path
        try:
            with open(o) as file:
                lines = file.read().splitlines()
        except FileNotFoundError:
            print('\033[0;97m-----------------------------------------------')
            print(' [×] FILE NOT FOUND')
            input(" Please Press Enter to retry...")

        # Assuming `id` is defined elsewhere in your code
        for line in lines:
            id.append(line)

# Call the crackfile function
crackfile()
