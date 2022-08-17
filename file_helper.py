import os
import typing


def get_output_files(output_directory : str, image_extensions : typing.List) -> typing.List:
    
    return [os.path.join(output_directory, filename) for filename in os.listdir(output_directory) if any([filename.endswith(".{}".format(ext)) for ext in image_extensions])]