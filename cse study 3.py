
# with open(filename,'r') as file
# for word in words
# number of times = count starting 0
# new_word = word.strip(".,?!").lower() necessary yes 


def wordOcuur(filename,str1):
    count = 0 
    with open(filename,'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                new_word = word.strip(".,?!").lower()
                if new_word == str1.lower()
                count = count +1
        return count

# for i in range(len(lst)):
# file.write(str(a) + ": " + str(b) + "\n")
# open only once in the front

def listToFile(filename,lst):
    with open(filename,'w') as file:
        for i in range(len(lst)):
            if i % 2 != 0 and len(lst[i]) % 2 == 0:
                file.write(str(i) + ": " + str(lst[i]) + "\n")
    return None

# for word in line.split 의 의미가 없다?
# if wanting to make small lst / make one every for loop
# 한 바퀴 돌 떄마다 있고 싶다면 for 안에 

def wCount(filename):
    big_lst = [] 
    line_num = 1 
    with open(filename,'r') as file:
        for line in file:
            lst = []
            word = line.split()
            lst.append(line_num)
            lst.append(len(word))
            big_lst.append(lst)
            line_num = line_num +1
    return big_lst

#file.write

def writeOdd(filename1,filename2):
    line_num = 1
    with open(filename2,'w') as file2:
        with open(filename1,'r') as file1:
            for line in file1:
                word = line.split()
                if len(word) % 2 != 0 :
                    file2.write(str(line_num) + ": " + str(len(word)) + "\n")
                line_num = line_num +1 
    return None


def fileReversed(filename1,filename2):
    with open(filename2,'w') as file2:
        with open(filename1,'r') as file1:
            for line in file1:
                new_line = reverse(line)
                file2.write(str(new_line))
    return None

# --------------------


# new_word = word [-1]
# last_word = new_word.rstrip("\n")

def secretMessage(filename):
    lst = []
    with open(filname,'r') as file:
        for line in file:
            word = line.split(" ")
            new_word = word[-1]
            last_word = new_word.rstrip("\n")
            lst.append(last_word)
    return lst 

    
# make sure you get rid of hidden last line : line.rstrip("\n")
# make sure it is integer : for int(words[i])
# dictA[key] = dictA.get(key, 0) + value 

def aggregateScores(filename):
    dictA = {}
    with open(filename,'r') as file:
        for line in file:
            word = line.split(":")
            key = word[0]
            value = int(word[1])
            if key in dictA:
                dictA[key] = value + dictA[key]
            else:
                dictA[key] = value 

    return dictA

#make a list and go write a new file from that list 

def wordsPerLine(filename):
    lst = []
    with open(filename,'r') as file:
        for line in file:
            word = line.split(" ")
            count = len(word)
            lst.append(count)

    newfile = filename.split(".")
    newfilename = newfile[0] + "-count. " + newfile[1]


    with open(newfilename,'w') as file:
        for i in range(len(lst)):
            file.write(str(lst[i]) + "\n")

# --------------------------------------------

# 리스트를 만들던 사전을 만들든 숫자를 더하든 모두 초기값 0 {} [] 부터 시작하여라 

def calculateShipping(dictA):
    charge = 0 
    if dictA["size"] == "small":
        charge = charge + 2

    if dictA["size"] == "medium":
        charge = charge +6

    if dictA["size"] == "large" :
        charge = charge + 10

    if dictA["weight"] > 20 :
        charge = charge + ( dictA["weight"] - 20 ) * 1.5

    for key in dictA.keys():
        if key == "insurance":
            charge = charge + dictA[key]
             
    return charge
            
        

def filterOutSmall(dictA,num):
    new_dict = {}
    for key in dictA.keys():
        if dictA[key] > num:
            new_dict[key] = dictA[key]

    return new_dict

# for key in dictA.keys():
# if key in dictB.keys() and dictA[key]== dictB[key]:

def findCommon(dictA,dictB):
    lst = []
    for key in dictA.keys():
        if key in dictB.keys() and dictA[key]== dictB[key]:
            lst.append(key)

    return lst 


    

# ----------------------------------------------------

# dict1.keys()
# value = dict1[key]

def aSpecial(dict1,str1):
    lst = []
    for key in dict1.keys():
        if len(str1) < len(key):
            lst.append(key)
    return lst

def valueCheck(dict1):
    new_dict={}
    for key in dict1.keys():
        value = dict1[key]
        if dict1[key] % 2 == 0:
            new_dict[value] = dict1[key] + 2
        else:
            new_dict[value] = dict1[key] * 2
    return new_dict

def keyChange(dict1):
    new_dict = {}
    for key in dict1.keys():
        if len(key) % 2 != 0 :
            new_dict[key] = len(key)
    return new_dict


def oddValue(dictA):
    lst = [ ]
    for key in dictA.keys():
        if dictA[key] % 2 == 0:
            append.lst(dictA[key] + 2)
        else:
            append.lst(dictA[key] * 2)
    return lst
    
def strCheck(dictA, str1):
    new_dict = {}
    for key in dictA.keys():
        if str1.lower() in key:
            new_dict[key] = dictA[key]

        if str1.upper() in key:
            new_dict[key] = dictA[key]

    return new_dict 
