def recPerimeter(length,width):
    rectangle = 2*(length + width)
    return round(rectangle,2)

def mileKilo(kilo):
    miles= kilo*1.60934
    return round(miles,2)

def totalDays(months,weeks,days):
    total_days = months*30 + weeks*7 + days
    return total_days

def strangeAdd(first,two,last):
    addition = first+two
    concatenate = str(addition) + str(last)
    return concatenate

def repUpper(word):
    new_word= word.replace("+"," ")
    final= new_word.upper()
    return final

# word.replace() 랑 new_word.upper() 외우기

def absRange(first,second):
    almost= abs(first-second)
    final= round(almost,2)
    return final

import math 

def cylinVolume(radius,height):
    volume= math.pi * pow(radius,2) * height
    final= round(volume,2)
    return final

def semiPerimeter(a,b,c):
    s = (a+b+c)/2
    return round(s,2)


def heronFormula(a,b,c):
    s=semiPerimeter(a,b,c)
    area = abs(s*(s-a)*(s-b)*(s-c))
    final_area= math.sqrt(area)
    return round(final_area,2)

def triangleDiff(base_1,height_1,base_2,height_2):
    area= 1/2 * base_1 * height_1
    area_2 = 1/2 * base_2 * height_2
    diff= area - area_2
    return round(diff,2)


def totalPrice(price,tax_rate):
    total= price * (1+tax_rate)
    return round(total,2)

def digitize(word):
    new_word = word.lower( )
    a= new_word.replace("a","4")
    b= a.replace("e","3")
    c= b.replace("oo","00")
    return c

def priceDifference(purchase,tax_1,tax_2):
    p_1= totalPrice(purchase,tax_1)
    p_2 = totalPrice(purchase,tax_2)
    diff= abs(p_1 - p_2)
    return round(diff,2)


def partA():
    return "Spider-Man"


def partB(x):
    return x-32

def partC(a,b):
    return (a-b)*8


    
    
    

