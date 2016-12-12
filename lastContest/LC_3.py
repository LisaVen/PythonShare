import sys

fh = open("output.txt", 'w')

if len(sys.argv)>1:
    filename = sys.argv[1]
    # print(filename)
    try:
        size = sys.getsizeof(filename)
        if size>0:
            fh.write(str(size)+'\n')
            sys.exit(0)
        else:
            raise Exception
    except Exception as e:
        print(e)
        fh.write("Can't open file " + filename)
        sys.exit(2)
    finally:
        fh.close()
else:
    fh.write('Usage: stat filename\n')
    fh.close()
    sys.exit(1)

