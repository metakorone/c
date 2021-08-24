import zipfile
import os
import shutil

comic_name = ""
comicPath = f"D:/comic/{comic_name}"
dirs = os.listdir(path=comicPath)
for dir in dirs:
    comics = os.listdir(path=comicPath+f'/{dir}')
    with zipfile.ZipFile(comicPath+f"/{dir}.zip", 'w', compression=zipfile.ZIP_DEFLATED) as new_zip:
        for comic in comics:
            new_zip.write(comicPath+f"/{dir}/{comic}", arcname=f'{comic}')
        shutil.rmtree(comicPath+f'/{dir}')
