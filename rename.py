import os
import re

comic_name = ""
comicPath = f"D:/comic/{comic_name}"
dirs = os.listdir(comicPath)
for dir in dirs:
    num = re.sub(r"\D", "", dir)
    if num[0] == "0":
        num = num[1]
    os.rename(f'{comicPath}/{dir}', f'{comicPath}/{comic_name}{num}')