import os
import glob
import filecmp
import time

tests = []
correct = 0
wrong = 0

settings = {
    "skipTests": [],
    "mixed": False,
    "tps": 100,
    "execDir": "mon.exe",
    "testNames": True,
    "testName": "mon",
}

execDir = settings["execDir"]
mixed = settings["mixed"]

def runOnTest(execDir, testName):
    startTime = time.time()
    outputPath = ""
    inputPath = ""
    if mixed: 
        inputPath = "./tests/mixed/"+testName+".in"
        outputPath = "./tests/mixed/"+testName+".out"
    else:
        inputPath = "./tests/in/"+testName+".in"
        outputPath = "./tests/out/"+testName+".out"

    os.system(execDir + " < " + inputPath +  " > output.out")
    finalTime = (time.time()) - startTime

    a = open("./output.out", 'r').readline()
    b = open(outputPath, 'r').readline()
    if a==b:
        return (True, finalTime)
    else:
        return (False, finalTime)


if not mixed:
    for r, d, f in os.walk("./tests/in"):
        for filename in f:
            if settings["testNames"]:
                if settings["testName"] in filename:
                    tests.append(filename.replace(".in",""))
            else:
                tests.append(filename.replace(".in",""))
else:
    for r, d, f in os.walk("./tests/mixed"):
        for filename in f:
            if ".in" in filename:
                if settings["testNames"]:
                    if settings["testName"] in filename:
                        tests.append(filename.replace(".in",""))
                else:
                    tests.append(filename.replace(".in",""))


for t in tests:
    skip = False
    for pre in settings["skipTests"]:
        if pre in t:
           skip = True 
           break
    if skip: continue
    time.sleep(1/settings["tps"])
    testResult = runOnTest(execDir, t) 
    os.system("cls")
    correct += testResult[0]
    # wrong += not testResult[0]
    if not testResult[0]:
        print(f"❌  wrong in test {t} ❌ \n# output: ")
        outputFile = open("output.out")
        outputLines = outputFile.readlines()
        for line in outputLines:
            print(line.replace("\n",""))    
        print("\n# Expected: ")
        outputFile.close()
        if mixed:
            outputFile = open("./tests/mixed/"+t+".out")
        else:
            outputFile = open("./tests/out/"+t+".out")
        outputLines = outputFile.readlines()
        for line in outputLines:
            print(line.replace("\n",""))    
        break
    print("🕘 Tests result 🕘 \n \n")
    print(f"✅ Correct: { correct }")
    print(f"❌ wrong: { wrong }")
    print(f"Last test took... { round(testResult[1]*10)/10 } s !")



