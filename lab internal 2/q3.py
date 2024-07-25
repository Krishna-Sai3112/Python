import shutil
from pathlib import Path
file1=
(r"C:\Users\krish\Desktop\engineering\pp\lab internal 2\first.txt")
file2=(r"C:\Users\krish\Desktop\engineering\pp\lab internal 2\second.txt")
new=input("Enter new file name")
print("The merged content will be in: ",new)
with open(new,"w") as wf:
        for f in [file1,file2]:
                with open(f,"r") as fd:
                        shutil.copyfileobj(fd,wf)
print("The content copied successfully")
print("Do you want to open the file?")
check=input()
if(check=='n'):
        exit()
else:
        print()
        c=open(new,"r")
        print(c.read())
        c.close()