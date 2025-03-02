# app/utils/file_utils.py
import os

def validate_file_paths(file_paths: list[str]) -> tuple[list[str], list[str]]:
    """
    Validate file paths and return valid and invalid paths.
    """
    valid_paths = []
    invalid_paths = []

    for path in file_paths:
        if os.path.isfile(path):
            valid_paths.append(path)
        else:
            invalid_paths.append(path)

    return valid_paths, invalid_paths