from os import rename, listdir

import sys

try:
    PATH = sys.argv[1]
    R_FILENAME = sys.argv[2]
    APPEND = False
    if len(sys.argv) != 3:
        if sys.argv[3] == "s":
            APPEND = "Start"
        elif sys.argv[3] == "e":
            APPEND = "End"
        elif sys.argv[3] != "s" and sys.argv[3] != "e":
            print("Please enter a valid APPEND argument or leave it blank")
            print("Valid commands are 's' and 'e'")
            print("- 's' appends to the start of the filename")
            print("- 'e' appends to the end of the filename")
            print("- Leaving it blank will change all filenames in the directory to the specified name in a numerical "
                  "increasing order")
            exit()
        if len(sys.argv) > 4:
            print("Please only enter three arguments max and two minimum")
            print("example: python multiple_file_renamer.py /home/user/Downloads/test test e")
            exit()

    files_in_dir = listdir(PATH)

    print(f"Renaming files from this directory: {PATH}\n")

    for file in files_in_dir:
        O_FILENAME = file
        if APPEND == "Start":
            N_FILENAME = R_FILENAME + " " + O_FILENAME
        elif APPEND == "End":
            N_FILENAME = O_FILENAME + " " + R_FILENAME
        else:
            end_of_filename_nr = 0
            files_in_dir = listdir(PATH)
            for n_file in files_in_dir:
                if R_FILENAME in n_file:
                    n_file_array = n_file.split()
                    try:
                        n_end_of_filename_nr = int(n_file_array[len(n_file_array) - 1])
                        if end_of_filename_nr == n_end_of_filename_nr or end_of_filename_nr < n_end_of_filename_nr:
                            end_of_filename_nr = n_end_of_filename_nr + 1
                    except ValueError:
                        pass
            end_of_filename_nr = str(end_of_filename_nr)
            if len(end_of_filename_nr) == 1:
                end_of_filename_nr = "000" + end_of_filename_nr
            elif len(end_of_filename_nr) == 2:
                end_of_filename_nr = "00" + end_of_filename_nr
            elif len(end_of_filename_nr) == 3:
                end_of_filename_nr = "0" + end_of_filename_nr
            N_FILENAME = R_FILENAME + " " + end_of_filename_nr

        print(f"Renaming file: [{O_FILENAME}]\nTo: [{N_FILENAME}]")
        rename(PATH + "/" + O_FILENAME, PATH + "/" + N_FILENAME)

except IndexError:
    print("Please enter valid arguments")
    print("Example: python multiple_file_renamer.py 'PATH' 'NEW_NAME' '{OPTIONAL: APPEND_LOCATION}'")
    print("APPEND_LOCATION has 2 options")
    print("- 'e' appends string to end of file")
    print("- 's' appends string to start of file")
    print("leaving it blank will rename all files in directory in an numerical fashion with the NEW_NAME")
    print("as prefix and end of file with increasing numbers")
