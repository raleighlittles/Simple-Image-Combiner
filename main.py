import argparse
import os
import sys
import math

# local
import merger_helper
import file_helper

argparse_parser = argparse.ArgumentParser()

argparse_parser.add_argument("-i", "--input-directory", type=str, help="Directory where input images are stored.")
argparse_parser.add_argument("-o", "--output-directory", type=str, help="Directory where output images will be stored")
# Use argparse boolean type
argparse_parser.add_argument("-s", "--force-square", type=int, help="If number of images is an evenly divisible number, then concatenate the images in such a way that a square is produced. 0 for false, 1 for true")
argparse_parser.add_argument("-r", "--num-rows", type=int, help="Number of rows in concatenated image")
argparse_parser.add_argument("-c", "--num-cols", type=int, help="Number of columns in concatenated image")

argparse_args = argparse_parser.parse_args()

all_files = []

image_extensions = ['jpg', 'jpeg', 'png', 'tiff', 'tif', 'webp']

for filename in os.listdir(argparse_args.input_directory):
    rel_filename = os.path.join(argparse_args.input_directory, filename)
    file_extension = os.path.splitext(rel_filename)[1][1:]

    if file_extension.lower() in image_extensions:
        #print("Adding image {} to list".format(filename))
        all_files.append(rel_filename)

num_files = len(all_files)

print(num_files, " images ready to be concatenated")

# Sanity check: if the user asked us to construct a square image, did they provide a square-number of images?
if (argparse_args.force_square) and (math.isqrt(num_files) ** 2 != num_files):

    print("ERROR: Can't create a square out of {} images".format(len(all_files)))
    sys.exit(2)


# Sanity check: did user pass in a valid value for the number of rows and columns (if they didn't already say to create a square)
if (not argparse_args.force_square) and ((argparse_args.num_rows * argparse_args.num_cols) != num_files):

    print("ERROR: {} images total, so {} and {} are not valid row column numbers".format(num_files, argparse_parser.num_rows, argparse_parser.num_cols))
    sys.exit(2)


num_rows = argparse_args.num_rows if (argparse_args.num_rows is not None) else (math.isqrt(num_files))
num_cols = argparse_args.num_cols if (argparse_args.num_cols is not None) else (math.isqrt(num_files))

# The first two cases are simple -- the user wants all images concatenated in a single row or column
if num_rows == 1:
    merger_helper.concatenate_images_in_row_or_column(all_files, argparse_args.output_directory, True)

elif num_cols == 1:
    merger_helper.concatenate_images_in_row_or_column(all_files, argparse_args.output_directory, False)

else:
    for file_num in range(0, num_files, num_cols):
        
        files_in_row = all_files[file_num : file_num + num_cols]
        convert_cmd = merger_helper.concatenate_images_in_row_or_column(files_in_row, argparse_args.output_directory, True)

    # Now that the rows have been generated, concatenate those rows vertically
    intermediate_files = file_helper.get_output_files(argparse_args.output_directory, image_extensions)
    merger_helper.concatenate_images_in_row_or_column(intermediate_files, argparse_args.output_directory, False)

    # Cleanup
    print("Cleaning up {} intermediate files".format(len(intermediate_files)))
    [os.remove(file) for file in intermediate_files]