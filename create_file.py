"""
A script creating a .py file after getting rid of whitespaces in the given text input.
"""


import re
import pathlib

title: str = input("Please enter a filename: ").strip()
title_sanitized: str = re.sub(r"\s+", "_", title.lower())

file_name: str = f"{title_sanitized}.py"
path: pathlib.Path = pathlib.Path(file_name)
if not path.is_file():
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(f'""" {title} """')
else:
    print(f"{file_name} already exists...")
