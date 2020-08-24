import os

def clean_work_dirs():
    print("Cleaning work dirs...")
    folders = ["/content/hent-AI/input/","/content/hent-AI/input_orig/"]
    for folder in folders:
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('ERROR in clean_work_dirs: Failed to delete %s. Reason: %s' % (file_path, e))

clean_work_dirs()
