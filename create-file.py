# a script creating a .py file after getting rid of whitespaces in the given text input

import re
import pathlib

title: str = input("").strip()
title_sanitized: str = re.sub("\s+", "-", title.lower())

file_name: str = f"{title_sanitized}.py"
path: pathlib.PosixPath = pathlib.Path(file_name)
if not path.is_file():
    with open(file_name, "w") as f:
        f.write(f"# {title}")
else:
    print(f"{file_name} already exists...")