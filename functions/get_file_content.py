import os

from .config import MAX_CHARS


def get_file_content(working_directory, file_path):
    full_path = os.path.join(working_directory, file_path)
    abs_working_directory = os.path.abspath(working_directory)
    abs_full_path = os.path.abspath(full_path)

    output = ""
    
    if not abs_full_path.startswith(abs_working_directory):
        output += f'\tError: Cannot list "{file_path}" as it is outside the permitted working directory'
        return output

    if not os.path.isfile(full_path):
        output += f'\tError: File not found or is not a regular file: "{file_path}"'
        return output
    
    try:
        with open(full_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)

        output += file_content_string

        if os.path.getsize(full_path) > MAX_CHARS:
            output += f'[...File "{file_path}" truncated at 10000 characters]'

        return output
    except Exception as e:
        return f'Error: {e}'

    
