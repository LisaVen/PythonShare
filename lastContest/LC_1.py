import sys
s = 0
for i in range(1, len(sys.argv)):
    try:
        s+=int(sys.argv[i])
    except:
        pass
sys.exit(s)