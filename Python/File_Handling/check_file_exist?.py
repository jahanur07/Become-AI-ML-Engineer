#os.path.exists()

# import os

# file_name = "/Users/jahanurraman/Desktop/Study/Become AI:ML Engineer/Python/File_Handling/file5.txt"

# if os.path.exists(file_name):
#   print("File exists")
# else:
#   print("File Not exists")
  
#pathlib.path.exists()

from pathlib import Path

file_name = Path("/Users/jahanurraman/Desktop/Study/Become AI:ML Engineer/Python/File_Handling/file6.txt")

if file_name.exists():
  print("File exists , cannot create file")
else:
  print("File Not exists , create new file")
  fh=open(file_name,'xt')
  fh.write("This is creating new file")
  fh.close()