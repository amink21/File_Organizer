import os, shutil

path = r"C:/Users/Amin/Downloads/"

fileName = os.listdir(path)


folderNames = ['JPG FILES', 'PNG FILES', 'PDF FILES', 'PSD FILES', 'ZIP FILES', 'M_DOC FILES', 'POWERPOINT FILES']

folderLength = len(folderNames)

for index in range(0, folderLength):
    if not os.path.exists(path + folderNames[index]):
        print("Created: " + folderNames[index])
        os.makedirs(path + folderNames[index])


for file in fileName:
    if ".jpg" in file and not os.path.exists(path + "JPG FILES/" + file):
        shutil.move(path + file, path + "JPG FILES/" + file)
    elif ".jpeg" in file and not os.path.exists(path + "JPG FILES/" + file):
        shutil.move(path + file, path + "JPG FILES/" + file)
    elif ".png" in file and not os.path.exists(path + "PNG FILES/" + file):
        shutil.move(path + file, path + "PNG FILES/" + file)
    elif ".pdf" in file and not os.path.exists(path + "PDF FILES/" + file):
        shutil.move(path + file, path + "PDF FILES/" + file)
    elif ".psd" in file and not os.path.exists(path + "PSD FILES/" + file):
        shutil.move(path + file, path + "PSD FILES/" + file)
    elif ".zip" in file and not os.path.exists(path + "ZIP FILES/" + file):
        shutil.move(path + file, path + "ZIP FILES/" + file)
    elif ".doc" in file and not os.path.exists(path + "M_DOC FILES/" + file):
        shutil.move(path + file, path + "M_DOC FILES/" + file)
    elif ".pptx" in file and not os.path.exists(path + "POWERPOINT FILES/" + file):
        shutil.move(path + file, path + "POWERPOINT FILES/" + file)