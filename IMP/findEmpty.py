class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



def calc(n):
    data = []

    with open("in/imp"+str(n)+".in", "r") as file:
        file.readline()
        d = file.readline()[:-1]
        data = d.split(" ")
        data = list(map(int,data))

    sol = [[]] * len(data)
    sol[1] = data[0]
    sol[len(data)-2] = data[len(data)-1]
    sol[0] = [data[1]]
    sol[len(data)-1] = [data[len(data)-2]]
    taken = [False] * (len(data)+1)
    taken[data[len(data)-1]] = True
    taken[data[0]] = True


    for i in range(2, len(sol)-2):
        sol[i] = [ data[i-1], data[i+1] ]

    for i in range(2, len(sol)-2):
        if sol[i][0] == sol[i][1]:
            taken[sol[i][0]] = True
            sol[i] = sol[i][0]

    for i in range(2, len(sol)-2):
        if type(sol[i-2]) == int:
            if sol[i-2] != data[i-1]:
                sol[i] = data[i-1]
        if type(sol[i+2]) == int:
            if sol[i+2] != data[i+1]:
                sol[i] = data[i+1]

    # ctr = [0] * len(sol)

    for i in range(0, len(sol)):
        if type(sol[i]) == int:
            taken[sol[i]] = True

    for i in range(0, len(sol)):
        if type(sol[i]) == list:
            sol[i] = list(filter(lambda x: not taken[x], sol[i]))

    counter = [0] * (len(sol)+1)
    for i in range(0, len(sol)):
        if type(sol[i]) == int:
            counter[ sol[i] ] += 1 
        else:
            for x in sol[i]:
                counter[x] += 1
    
    updated = True
    ctr=0
    while updated:
        ctr+=1
        updated = False
        for i in range(0, len(sol)):
            if type(sol[i] ) == list:
                for x in range(0, len(sol[i])):
                    if counter[ sol[i][x] ] == 1:
                        if len(sol[i]) > 1:
                            counter[ sol[i][not x] ] -= 1
                        sol[i] = sol[i][x] 
                        updated = True
                        break


    # print(data)
    


    s = ""
    for i in sol:
        if type(i) == int:
            s += "D"
        if type(i) == list:
            if len(i) == 2:
                s+= "C"
            if len(i) == 1:
                s+= "B"
            if len(i) == 0:
                s+= "A"

    sForPrint = ""
    for i in sol:
        if type(i) == int:
            sForPrint += bcolors.FAIL + "D" + bcolors.ENDC
        if type(i) == list:
            if len(i) == 2:
                sForPrint+= bcolors.OKGREEN + "C" + bcolors.ENDC
            if len(i) == 1:
                sForPrint+= bcolors.OKCYAN + "B" + bcolors.ENDC
            if len(i) == 0:
                sForPrint+= bcolors.OKBLUE + "A" + bcolors.ENDC

    bdb_ctr = 0
    bbcbb_ctr = 0

    for i in range(0, len(s)-2):
        if "BDB" in s[i]+s[i+1]+s[i+2]:
            bdb_ctr+=1

    for i in range(0, len(s)-4):
        if "BBCBB" in s[i]+s[i+1]+s[i+2]+s[i+3]+s[i+4]:
            bbcbb_ctr+=1
    
    found_bb=False
    found2_bb = False
    c_counter_arr=[]
    c_counter = 0
    for i in range(1, len(s)):
        if not found_bb and s[i-1]+s[i] == "BB":
            found_bb = True
        elif found_bb and not found2_bb:
            if s[i] == "C":
                c_counter+=1
            elif s[i-1]+s[i]=="BB":
                found2_bb = True
            else:
                found_bb=False
                found2_bb=False
                if c_counter > 1:
                    c_counter_arr.append(c_counter)
                c_counter=0

    null_places = 0
    dual_places = 0
    single_places = 0
    for i in range(0, len(s)):
        if type(sol[i]) == int:
            continue
        if len(sol[i]) == 0:
            null_places += 1
        elif len(sol[i]) == 2:
            dual_places += 1
        elif len(sol[i]) == 1:
            single_places += 1

    solution = 0
    with open("out/imp"+str(n)+".out", "r") as file:
        solution = int(file.read())
        sForPrint+=" - " + str(solution)
    if True:
        print(n)
        print(sol)
        print(list(filter(lambda x: x not in data ,range(1, len(data)+1))))
        print(sForPrint + " - " + str(bdb_ctr), " - ", bbcbb_ctr, " - ", c_counter_arr)
        print(null_places, " | ", dual_places, " | ", single_places )
        print("counter: ", ctr)
        print("")

for i in range(1, 57):
    calc(i)