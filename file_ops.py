'''
syntax:
with open("file_name","mode") as file_handler:
    file_handler.read()
    file_handler.write()
MODES:
r -> read mode , The file will be opened for reading the content if the file exists.
        If the file does not exists then will get the FileNotFoundError
        [read, readline, readlines]
w -> write mode , File will be opened for writing in to it.
    a. IF the file is there already , it will clean the existing content and start
        writing as a fresh file
    b. IF the file is not there, it will create a file and write into it
    [write, writelines]
a -> append mode,
    a. if the file is there it will continue to write (append) along with the existing content
    f. if the file is not there it will create and write as a fresh file
    [write, writelines]

r+ -> File will be opened for both reading and writing. First we need to read the
    existing content and should start writing into it
w+  -> For write and read . First we need to write the file and can read whatever has
    been writing. Since we start writing first the existing file content will be lost
rb - read binary ( to read the binary file (image, video, audio)
wb - write binary

with open('days.txt','r') as fh:
    #print(fh.read())
    #print(fh.readline(3),end='')
    #print(fh.readline())
    print(fh.readlines()[2:6])

with open('myfile.txt','w') as wfh:
    #wfh.write("Hello ERICSSON!!!")
    wfh.writelines(['India\n','Europe\n','Australia\n','America\n','China'])

with open('myfile.txt','a') as afh:
    afh.writelines(['\nPakistan\n','SriLanka\n','Canada\n','Singapore'])

with open('myfile.txt','r+') as fh:
    print(fh.read())
    fh.write('\nEND_OF_LINE')
    # fh.write("PYTHON")
    # print(fh.read())

with open('myfile.txt','w+') as fh:
    fh.writelines(['Chennai\n','Bangalore\n','Hyderabad'])
    fh.seek(0,0)
    print(fh.read())

with open(r'C:\Users\RaghulRamesh\OneDrive\Pictures\puppy.jpg','rb') as fh:
    with open(r'C:\Users\RaghulRamesh\OneDrive\Pictures\puppy_tuesday.jpg', 'wb') as wfh:
        wfh.write(fh.read())
'''
