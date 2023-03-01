import os
import shutil

FromDir="C:\\Users\\aarya\\Downloads\\Test"
ToDir = "C:\\Users\\aarya\\Downloads\\Test"
ListOfFiles = os.listdir(FromDir)
print(ListOfFiles)
for FileName in ListOfFiles:
    Name,Ext=os.path.splitext(FileName)
    if Ext == "":
        continue
    if Ext in [".doc",".docx",".pdf",".txt"]:
        path1=FromDir+"\\"+FileName
        path2=FromDir+"\\"+Ext
        path3=ToDir+"\\"+Ext+"\\"+FileName
        if os.path.exists(path2):
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)
