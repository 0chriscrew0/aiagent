import os
import subprocess
from google.genai import types


def run_python_file(working_directory, file_path):
    full_path = os.path.join(working_directory, file_path)
    abs_working_directory = os.path.abspath(working_directory)
    abs_full_path = os.path.abspath(full_path)

    output = ""
    
    if not abs_full_path.startswith(abs_working_directory):
        output += f'\tError: Cannot execute "{file_path}" as it is outside the permitted working directory'
        return output
    
    if not os.path.isfile(full_path):
        output += f'\tError: File "{file_path}" not found.'
        return output
    
    if not file_path.endswith('.py'):
        output += f'\tError: File "{file_path}" is not a Python file.'
        return output
    
    try:
        result = subprocess.run(['python', file_path], capture_output=True, timeout=30, cwd=working_directory)

        output += f'STDOUT: {result.stdout}\n'
        output += f'STDERR: {result.stderr}\n'
        if result.returncode != 0:
            output += f'Process exited with code {result.returncode}\n'
        if not result:
            output += "No output produced."
        return output
    except Exception as e:
        return f'Error: executing Python file: {e}'
    
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python script, capturing and returning its output, errors, and exit status, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The relative path to the Python script file to be executed within the working directory.",
            ),
        },
    ),
)