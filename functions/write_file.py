import os


def write_file(working_directory, file_path, content):
    full_path = os.path.join(working_directory, file_path)
    abs_working_directory = os.path.abspath(working_directory)
    abs_full_path = os.path.abspath(full_path)

    output = ""
    
    if not abs_full_path.startswith(abs_working_directory):
        output += f'\tError: Cannot list "{file_path}" as it is outside the permitted working directory'
        return output

    try:
        directory = os.path.dirname(full_path)

        if not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)

        with open(full_path, "w") as f:
            f.write(content)

        output += f'Successfully wrote to "{full_path}" ({len(content)} characters written)'
        
        return output
    except Exception as e:
        return f'Error: {e}'
    