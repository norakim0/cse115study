def sumEvens(lst):
    num = 0
    for i in range (len(lst)):
        if lst[i] % 2 == 0:
            num  = num + lst[i]
    return num

#lst 초기 parameter 설정 안 겹치게 주
#돌려받는 값이 숫자인지 리스트인지 주의 

def createGreeting(str_1,str_2):
    if str_2 == "professor":
        return "Greetings Prof. " + str(str_1)
    if str_2 == "student":
        return "Heya " + str(str_1)
    else:
        return "Greetings " + str(str_1)
    
#important
def createGreetings(lst_n,role):
    str_1 = ""
    for i in range(len(lst_n)):
        str_1 = str_1 + createGreeting(lst_n[i],role) + "! "
    return str_1

#createGreeting 맞는 함수 불렀는지 확
#맞으면 꼭 parameter 확

#important
def increasingLengths(lst_str):
    if len(lst_str) < 2:
        return True
    for i in range(len(lst_str)-1):
        if len(lst_str[i]) >=  len(lst_str[i+1]):
            return False
    return True

#지속 검사는 마지막 return / 찾는 즉시 결과값 도출이 for 안으
#다 확인하고 돌려주는 것은 for 랑 맞춰서 집어넣

def filterByLength(lst_str,num):
         lst=[]
    for i in range(len(lst_str)):
        if len(lst_str[i]) > num:
            lst.append(lst_str[i])
    return lst

#important
def noMoreOs(lst):
    num = 0
    for i in range(len(lst)):
        if "o" in lst[i] or "O" in lst[i]:
            lst[i]=lst[i].replace("O","")
            lst[i]=lst[i].replace("o","")
            num = num + 1
    return num

#덮어쓸때는 반드시 다시 지정해주기 
# or 쓸 때 주의 전체를 쓰고 or 나 and 를 써야한


def StrToNumber(lst_str):
    lst = []
    for i in range(len(lst_str)):
        lst.append(len(lst_str[i])+len(lst_str))
    return lst


def evenList(lst_int):
    lst = [] 
    for i in range(len(lst_int)):
        if lst_int[i] % 2 == 0:
            lst.append(lst_int[i])
    return sorted(lst)

#sorted 은 정렬의 의

def oddList(lst_int):
    sum_num = 0.0
    for i in range(len(lst_int)):
        sum_num = sum_num + lst_int[i]
        sum_even = sum(evenList(lst_int))
        sum_odd = sum_num - sum_even
        result = sum_odd / sum_even
    return round(result,1)
    
def charCheck(lst_str):
    lst= []
    for i in range(len(lst_str)):
        if "A" in lst_str[i] or "a" in lst_str[i]:
            lst.append("Yes")
            lst.append(lst_str[i])
    return lst

def lenCount(lst_str):
    lst = []
    for i in range(len(lst_str)):
        lst.append(len(lst_str[i]))
    return lst

def stringTest(string):
    if string.islower():
        return string.upper()
    else:
        return string.capitalize()

def apCredit(total):
    if total >=24:
        return "Year 2"
    else:
        "Year 1"


def proCredit(total_ap,total_pro):
    if apCredit(total_ap) == "Year 2":
        if total_pro >= 12:
            return "CSE 116"
        else:
            return "CSE 115"
    else:
        return "No credit transfer"

import math

def radCompare(par):
    rad = par/2
    if rad <7:
        return round(math.pi* pow(rad,2),2)
    else:
        return round(3.14 * pow(rad,2),2)

def decideClothing(num):
    if num <= 32:
        return  "Stay heated indoor"

def lstCompare(lst_1,lst_2):
    if len(lst_1) <= len(lst_2):
        lst_1.extend(lst_2)
    else:
        lst_1.insert(len(lst_2),lst_2)
    return lst_1
#왜 리턴을 중간에 넣으면 안되려

def oddUpper(lst_str):
    lst_1=[]
    lst_2=[]
    for i in range(len(lst_str)):
        if i % 2 == 0:
            word_1 = lst_str[i].upper()
            lst_1.append(word_1)
        else:
            word_2 = lst_str[i].capitalize()
            lst_2.append(word_2)
    return lst_1 + lst_2 

#important 
def listRev(lst_str):
    lst=[]
    for i in range(len(lst_str)):
        word_1= list(lst_str[i])
        word_1.reverse()
        word_2= "".join(word_1)
        lst.append(word_2)
    return lst
    
def charPick(lst_str):
    lst = []
    for i in range(len(lst_str)):
        if i %2 ==0:
            letter = lst_str[i].capitalize()
            new_word = lst_str[i] + letter[:1]
            lst.append(new_word)
    return lst 

def itemType(lst_str):
    lst = []
    for i in range(len(lst_str)):
        if len(lst_str) % 2 != 0:
            lst.append(i)
            lst.append(
