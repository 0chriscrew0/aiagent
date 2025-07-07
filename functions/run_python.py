import os
import subprocess


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