#  w mode - open the file of writing 
# create new file if file not exist 
fh = open("file3.txt",'wt')
fh.write("this file overwritten using 'w' mode in python ")

fh.close()