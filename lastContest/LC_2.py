import os
import sys

n = int(sys.argv[1])
for i in range(2, 2+ n):
    try:
        print(sys.argv[i] + '=' + os.environ[sys.argv[i].upper()])
    except:
        print('')

# for item in os.environ.items():
#     print(item)

# ('PROMPT', '$P$G')
# ('PATHEXT', '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC')
# ('JAVA_HOME', 'C:\\Program Files\\Java\\jdk1.8.0_101')
# ('HOMEPATH', '\\Users\\Val')
# ('SYSTEMDRIVE', 'C:')
