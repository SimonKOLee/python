import datetime
import glob2

def getFileContent(path):
    with open(path,"r") as file:
        content = file.read()
    return content
'''path1 = "./Sample-Files/file1.txt"
path2 = "./Sample-Files/file2.txt"
path3 = "./Sample-Files/file3.txt"

con1 = getFileContent(path1)
con2 = getFileContent(path2)
con3 = getFileContent(path3)'''

files = glob2.glob("Sample-Files/*.txt")
filename = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f.txt")
with open(filename,"w") as newfile:
    for file in files:
        con = getFileContent(file)
        newfile.write(con+"\n")
