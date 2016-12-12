import sys
import os

fh = open("output.txt", 'w')

if len(sys.argv)>1:
    filename = sys.argv[1]
    try:
        text = file_in = open(filename, 'rb').read()
        fh.write(str(os.stat(sys.argv[1]).st_size)+"\n")
        sys.exit(0)
    except Exception as e:
        fh.write("Can't open file " + filename+'\n')
        sys.exit(2)
else:
    fh.write('Usage: stat filename\n')
    sys.exit(1)

