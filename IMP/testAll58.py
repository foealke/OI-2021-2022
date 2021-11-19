import subprocess
import os

PATH = "./testy58/out8"


tests = []
with open(PATH, "r") as file:
    for line in file.readlines():
        tst = line.split(" ")
        tests.append([tst[0], tst[1].replace("\n", "")])

def testIndex(idx):
    process = subprocess.Popen([".\imp.exe" ], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    length = len(tests[idx][0])
    process.stdin.write( str.encode(str(length) + "\n") )

    prepInput = ""
    for i in tests[idx][0]:
        prepInput+= i + " "

    process.stdin.write( str.encode( prepInput ) )
    process.stdin.close()
    sb = str(process.communicate()[0].decode().replace("\n",""))
    print(sb)
    return int(tests[idx][1]) == int(sb)

for i in range(0, len(tests)):
    if not testIndex(i):
        print("Failed on: ",i, " - ", tests[i])
        break;
    