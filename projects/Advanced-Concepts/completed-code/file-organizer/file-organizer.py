import os
import shutil

DIRECTORIES = {
    "Web": [".html5", ".html", ".htm", ".xhtml", ".css", ".webarchive", ".php",
            ".yaml"],
    "Images": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
               ".heif", ".jfif"],
    "Photoshop": [".psd"],
    "Videos": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
               ".qt", ".mpg", ".mpeg", ".3gp"],
    "Documents": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
                  ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                  ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                  "pptx", ".csv"],
    "Archives": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                 ".dmg", ".rar", ".xar", ".zip"],
    "Audio": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
              ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
    "Plain Text": [".txt", ".in", ".out", ".key", ".md"],
    "PDF": [".pdf"],
    "Code": [".py", ".java", ".RData", ".Rhistory", ".cpp", ".o"],
    "Shortcuts": [".lnk", ".url"],
    "Configuration": [".ini", ".msi", ".apk", ".crdownload"],
    "XML": [".xml"],
    "EXE": [".exe"],
    "SHELL": [".sh"]

}

#The Path of the directory to be sorted
path = '<YOUR_PATH>'
#This populates a list with the filenames in the directory
list_ = os.listdir(path)

#Traverses every file
for file_ in list_:
    name,ext = os.path.splitext(file_)

    #If it is directory, it forces the next iteration
    if ext == '':
        continue
    #If a directory with the name 'ext' exists, it moves the file to that directory
    for key, value in DIRECTORIES.items():
        if ext in value:
            if os.path.exists(path+'/'+key):
                shutil.move(path+'/'+file_,path+'/'+key+'/'+file_)
            #If the directory does not exist, it creates a new directory
            else:
                os.makedirs(path+'/'+key)
                shutil.move(path+'/'+file_,path+'/'+key+'/'+file_)
        else: 
            continue
