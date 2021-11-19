RG = 57

for i in range(1, 57):
    p = False
    res = ""
    with open("in/imp"+str(i)+".in", "r") as file:
        res += file.readline()[:-1]
        p = int(res) % 2 == 1
        res += " - " + file.readline()[:-1]
    with open("out/imp"+str(i)+".out", "r") as file:
        d = file.read()
        if int(d) <= 1:
            p = False
        res += " - " + d
    print(i, ": ", res)
