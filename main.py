import argparse


argparse_parser = argparse.ArgumentParser()

argparse_parser.add_argument("-i", "--input-directory", type=str, help="Directory where input images are stored")
argparse_parser.add_argument("-o", "--output-directory", type=str, help="Directory where output image(s) will be stored")
argparse_parser.add_argument("-s", "--force-square", type=???, help="If number of images is an evenly divisible number, then concatenate the images in such a way that a square is produced")
argparse_parser.add_argument("-m", "--max-rows", type=int, help="Max number of rows for resulting image")
argparse_parser.add_argument("-n", "--max-cols", type=int, help="Max number of columsn for resulting image")