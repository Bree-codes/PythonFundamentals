#opening and reading a file
import os.path

"""file = open("file.txt" , "r")
for line in file:
    print(file.readlines())
file.close()"""

#writing to a file and creating the file if it does not exist
"""file = open("newfile.txt","w")
file.write("Hello breshy!")
file.close()
print("File created successfuly..")"""

#reading each line in the file
"""file = open("newfile.txt" , "r")
print(file.readlines())
file.close()"""

#deleting a file by specifying its path
if os.path.exists("newfile.txt"):
    os.remove("newfile.txt")
    print("File deleted successfully.")
else:
    print("File does not exist!")
