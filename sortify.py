import os
import shutil
from tqdm import tqdm

def makeFolders(path,folderNames):  

    for folder in folderNames:
        folderPath = os.path.join(path,folder)
        if os.path.exists(folderPath):
            shutil.rmtree(folderPath)
            os.mkdir(folderPath)
        else:
            os.mkdir(folderPath)


def moveFilesIntoRespectiveFolders(currPath,folderNames,folderMap):

    all_files_path = os.path.join(currPath,"temp")
    files  = os.listdir(all_files_path)

    print("")
    for idx in tqdm(range(0,len(files))):
        extension = os.path.splitext(files[idx])[1]

        source = os.path.join(currPath,"temp",files[idx]) 
        destination = os.path.join(currPath,folderMap[extension] if extension in folderMap else "anonymous",files[idx])

        shutil.move(source,destination)

    shutil.rmtree(all_files_path)

def askUser(text):

    print(text)
    answer = input("--- Answer : ")
    return answer


def deleteFolders(currPath,folderNames):

    for folder in folderNames:
        path = os.path.join(currPath,folder)
        if os.path.exists(path): shutil.rmtree(path)


def sortTheFiles(currPath,folderNames,folderMap,file_to_be_sorted):

    #1
    makeFolders(currPath,folderNames)

    #2
    answer = askUser("\n==> To sort the files, do you want to copy or move the files from the target folder ? \n--- PRESS 1 : for copying\n--- PRESS 2 : for moving files\n--- PRESS any other key : to abort process ")

    if answer == "1":
        os.system(f"find {file_to_be_sorted} -type f -print0 | xargs -0 cp -t ./temp")
    elif answer == "2":
        os.system(f"find {file_to_be_sorted} -type f -print0 | xargs -0 mv -t ./temp")
        shutil.rmtree(file_to_be_sorted)
    else:
        answer = askUser("\n==> Delete the formed folders ?\n--- PRESS 'y'/'n'")
        if answer == "y":
            deleteFolders(currPath,folderNames)

        return 

    #3
    moveFilesIntoRespectiveFolders(currPath,folderNames,folderMap)




if __name__ == "__main__":
        
    hashMaps = {"videos" : {".mp4", ".m4a", ".m4v", ".f4v", ".f4a", ".m4b", ".m4r", ".f4b", ".mov","webm"},
                "images" : {".jpeg",".jpg",".png",".gif",".tiff","PNG"},
                "mp3" : {".mpeg",".mp3"},
                "documents": {".pdf",".doc",".docx",".ppt",".pptx",".odx",".rtf",".html",".htm",".txt"}
                }

    folderMap = { extension : k for k,v in hashMaps.items() for extension in v }
    folderNames = ["videos","images","mp3","documents","anonymous","temp"]


    currPath = os.path.abspath(os.getcwd())
    file_to_be_sorted = os.path.join(currPath,"targetFolder")

    sortTheFiles(currPath,folderNames,folderMap,file_to_be_sorted)


    print("\n******Your files are now sorted******")
    print("*****Thank you for using SORTIFY*****")
