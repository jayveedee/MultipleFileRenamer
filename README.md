# Multiple File Renamer

A program that renames/appends every file's name with a specified new filename in any given directory

## Installation

It's a very simple program, so there's not much more to it than just downloading the git repo or the file `multiple_file_renamer.py` and specifying the required arguments

1. Download repo https://github.com/jayveedee/MultipleFileRenamer
2. Run the program `python multiple_file_renamer.py 'PATH' 'NEW_FILENAME' '{OPTIONAL: APPEND}'`
    1. _**PATH** example:_ `~/Downloads/test`
    2. _**NEW_FILENAME** example:_ `test`
    3. _**APPEND** example:_ `s` _or_ `e`
        1. `s` specifies that **NEW_FILENAME** will be appended at the start of the filename
        2. `e` specifies that **NEW_FILENAME** will be appended at the end of the filename
        3. Leaving **APPEND** blank will rename all files to the same **NEW_FILENAME** where at the end of the file name they will be numerically increased
            - _example:_ `test 0000`,`test 0001`,`test 0002`,`test 0003`...`test 0199`...`test 9999`