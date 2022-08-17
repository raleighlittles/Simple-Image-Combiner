
import typing
import subprocess
import os
import random
import string

def generate_concat_command(files : typing.List, output_directory, horizontal : bool) -> str:

    convert_cmd = "convert "

    convert_cmd += " ".join(files)

    if horizontal:
        convert_cmd += " +"

    else:
        convert_cmd += " -"

    convert_cmd += "append "

    # The resulting file takes the extension of the last filename in the list
    # since all files are supposed to have the same extension before being merged.

    file_ext = os.path.splitext(files[-1])[1][1:]

    # Output file name consists of a random 10-letter string (it will be deleted later once the final image is created)
    output_filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10)) + "." + file_ext

    convert_cmd += os.path.join(output_directory, output_filename)

    print("Running command ", convert_cmd)

    return convert_cmd

def concatenate_images_in_row_or_column(files: typing.List, output_directory : str,  is_row: bool):
    
    concat_cmd = generate_concat_command(files, output_directory, is_row)

    p = subprocess.Popen(concat_cmd, shell=True)
    p.communicate()