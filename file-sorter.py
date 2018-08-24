import os
import shutil

destination = '/home/christian/Desktop/School/'
number_of_transfers = 0

# loop through all files in current dir and destination dir.
files_in_current_dir = os.listdir( os.getcwd() )
files_in_destination = os.listdir( destination )

# get first word of all filenames separated by underscore
# and remove extensions
for f in files_in_current_dir:
    initial = f.split('_')
    no_ext = os.path.splitext( initial[0] )[0]

    # if file matches a directory name, place the file in the directory.
    for fi in files_in_destination:
        if no_ext == fi.split('_')[0] and len(fi.split('.')) < 2:
            shutil.move(os.getcwd() + '/' + f, destination + fi)
            number_of_transfers += 1
            print("Moved file '{}' to directory '{}'".format(f, fi))

print( "Transfers: {}".format(number_of_transfers) )
