import os
import zipfile
from os.path import basename
import shutil  

path = r'/content/hent-AI/input/'
files = os.listdir(path)

zip_name_base = ""

zip_name_base = files[0][:-10] +"_input.zip"
print(zip_name_base)

print("test")
def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            path = os.path.join(root, file)
            ziph.write(path, basename(path))
        
        
        
zipf = zipfile.ZipFile(zip_name_base , 'w', zipfile.ZIP_DEFLATED)
zipdir(path, zipf)
zipf.close()

shutil.move(source, destination)