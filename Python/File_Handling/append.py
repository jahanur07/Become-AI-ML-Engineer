# a mode =>  append mode
# when file dose not exist then a mode also work as w mode create new file
fh = open("file4.txt",'at')
fh.write("\nThis content write by using 'a'mode \n")
fh.write("'a' mode add new content end of the file\n")
fh.write("good bye !!")
fh.close()
