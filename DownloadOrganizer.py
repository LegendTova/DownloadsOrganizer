import os
from pathlib import Path

# iterates through each file and stores it to folder is destination directory
def main():

	# replace string with path to your downloads folder
    downloadDir = "[PathToDownloads]"
	
	# replace string with path to the folder you want your files sorted
    destinationDir = "SortDestination]"

    dir = ""

    for f in os.listdir(downloadDir):
        dir = findFileType(f, destinationDir)
        Path(downloadDir + f).rename(destinationDir + dir + "\\" + f)
        

# based on file extension returns name of directory to store passed file
def findFileType(file, destinationDir):
    f2 = file.lower()

    if "pdf" in f2:
        
        checkFolderExists(destinationDir + "PDFs")

        return "PDFs"

    elif "fbx" in f2 or "obj" in f2:

        checkFolderExists(destinationDir + "3DFiles")

        return "3DFiles"
    
    elif "wav" in f2 or "mp3" in f2:

        checkFolderExists(destinationDir + "Audio")

        return "Audio"

    elif "docx" in f2:

        checkFolderExists(destinationDir + "Word")

        return "Word"
    
    elif "xls" in f2 or "xlsx" in f2 or "ods" in f2:

        checkFolderExists(destinationDir + "Spreadsheets")

        return "Spreadsheets"
    
    elif "png" in f2 or "jpg" in f2 or "jpeg" in f2:

        checkFolderExists(destinationDir + "images")

        return "images"

    elif "mp3" in f2 or "mp4" in f2 or "mkv" in f2:
        
        checkFolderExists(destinationDir + "Videos")

        return "Videos"

    elif "exe" in f2:

        checkFolderExists(destinationDir + "Applications")

        return "Applications"
    
    elif "." not in f2:

        checkFolderExists(destinationDir + "Folders")

        return "Folders"

    else:
        extension = file[file.rfind(".") + 1:]
            
        checkFolderExists(destinationDir + extension)

        return extension

# determines if directory needed exists and if it doesn't creates it
def checkFolderExists(d):
        
    if not os.path.exists(d):

            os.mkdir(d)

if __name__ == "__main__":
    main()