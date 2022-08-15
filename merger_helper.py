from lib2to3.pytree import convert
import typing
import subprocess
import os

def generate_concat_command(files : typing.List, horizontal : bool) -> str:

    convert_cmd = "convert "

    convert_cmd += " ".join(files)

    if horizontal:
        convert_cmd += " +"

    else:
        convert_cmd += " -"

    convert_cmd += "append"

    # The resulting file takes the extension of the last filename in the list
    # since all files are supposed to have the same extension before being merged.

    file_ext = os.path.splitext(files[-1])[1][1:]

    # Output file name consists of a random 10-letter string (it will be deleted later once the final image is created)

    convert_cmd += " output/output." + file_ext

    return convert_cmd

def concatenate_images_in_row_or_column(files: typing.List, is_row: bool):
    
    concat_cmd = generate_concat_command(files, is_row)

    p = subprocess.Popen(concat_cmd, shell=True)
    p.communicate()

