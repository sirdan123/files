import os
import zipfile
from os.path import basename
import shutil  

path = r'/content/hent-AI/input/'
files = os.listdir(path)

zip_name_base = ""

zip_name_base = files[0][:-10] +"_input.zip"

source = "/content/hent-AI/" +zip_name_base
destination = "/content/drive/My Drive/hent-AI/videos/Output/"

shutil.move(source, destination)