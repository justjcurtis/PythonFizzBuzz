#main loop

def main():
    print()

    a = getNum("starting", "")
    b = getNum("ending", "")

    x = generateNums(a, b)

    r = getRules()

    x = doRules(x, r)

    print("printing...")
    for num in x:
        doPrint(num)

    print("done.")

#methods

def getRules():
    print()
    print("enter 1 rule at a time")
    print("ie. type 3 and then press enter to add rule 3")
    print()
    print("type a rule and press enter to remove a rule")
    print()
    print("type done and press enter when you are done.")
    
    availableRules = [3, 5, 7, 11, 13]
    r = list()
    getting = True
    while(getting):
        r.sort()
        availableRules.sort()
        if(len(availableRules) > 0):

            if(len(r) > 0):
                print("current active rules are :")
                print(r)
            else:
                print("no rules currently active")

            print("available rules are:")
            print(availableRules)
        else:
            print("all rules currently active")

        rn = getNum("", "done")
        if(rn == "done"):
            break
        if rn in r:
            availableRules.append(rn)
            r.remove(rn)
        else:
            if rn in availableRules:
                availableRules.remove(rn)
                r.append(rn)
            else:
                print(str(rn) + " is not an available rule")
    print()
    return r

def getNum(s, ex):
    print()
    getting = True

    while(getting):
        getting = False
        if(s != ""):
            print("input " + s + " number")
        try:
            num = input("=> ")
            if(ex != "" and num.lower() == ex):
                return num
            else:
                num = int(num)
        except ValueError:
            getting = True
            print("only numbers may be entered")
    return num

def generateNums(a, b):
    print()
    print("generating nums...")
    x = list(range(a, b+1))
    print("done generating.")
    print()
    return x

def doPrint(num):
    if(num != "skip"):
        print(num)

def doRules(x, r):
    print()
    i = 0
    y = x
    print("doing rules...")
    for num in y:
        if 7 in r:
            x[i] = Rule7(num, x[i])
        if 3 in r:
            x[i] = Rule3(num, x[i])
        if 5 in r:
            x[i] = Rule5(num, x[i])
        if 11 in r:
            x[i] = Rule11(num, x[i])
        if 13 in r:
            x[i] = Rule13(num, x[i])

        i += 1

    print("done rules.")
    return x

#Rules

def Rule3(num, numSoFar):
    if(num % 3 == 0):
        if(numSoFar == num):
            num = "Fizz"
        else:
            return numSoFar + "Fizz"
    else:
        return numSoFar
    return num


def Rule5(num, numSoFar):
    if(num % 5 == 0):
        if(numSoFar == num):
            num = "Buzz"
        else:
            return numSoFar + "Buzz"
    else:
        return numSoFar
    return num


def Rule7(num, numSoFar):
    if(num % 7 == 0):
        if(numSoFar == num):
            num = "bing"
        else:
            return numSoFar + "bing"
    else:
        return numSoFar
    return num


def Rule11(num, numSoFar):
    if(num % 11 == 0):
        num = "BONG!"
    else:
        return numSoFar
    return num

def Rule13(num, numSoFar):
    if(num % 13 == 0):
        num = "skip"
    else:
        return numSoFar
    return num

#run
def Run():
    while(True):
        main()
        print()

        print("press enter to run again")
        c = input("=> ")

        if (c.lower() == "x"):
            quit()
Run()
