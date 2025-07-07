import os
from google.genai import types


def get_files_info(working_directory, directory=None):
    full_path = os.path.join(working_directory, directory)
    abs_working_directory = os.path.abspath(working_directory)
    abs_full_path = os.path.abspath(full_path)

    output = ""
    if directory == ".":
        output += "Result for current directory:\n"
    else:
        output += f'Result for \'{directory}\':\n'
    
    if not abs_full_path.startswith(abs_working_directory):
        output += f'\tError: Cannot list "{directory}" as it is outside the permitted working directory'
        return output

    if not os.path.isdir(full_path):
        output += f'\tError: "{directory}" is not a directory'
        return output
    
    try:
        for file in os.listdir(full_path):
            file_path = os.path.join(full_path, file)
            output += " - "
            output += file + ": "
            output += "file_size=" + str(os.path.getsize(file_path)) + " bytes, "
            output += "is_dir=" + str(os.path.isdir(file_path)) + "\n"

        return output
    except Exception as e:
        return f'Error: {e}'
    
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
    ]
)