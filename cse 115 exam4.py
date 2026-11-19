
def whereIs(str1,lst):
    if lst == []:
        return None
    new_lst= []
    for i in range(len(lst)):
        for col in range(len(lst[i])):       
            if lst[i][col] == str1:
                new_lst.append(i)
                new_lst.append(col)
                return new_lst
    return None
       
def sumSurrounding(lst,a,b):
    count = 0
    for i in range(len(lst)):
        if a == i:
            for col in range(len(lst[i])):
                num = lst[i][col]
                count += num
    for i in range(len(lst)):
        for col in range(len(lst[i])):
            if b == col:
                num = lst[i][col]
                count += num
    index = lst[a][b]
    result = count - index
    return result


def copySums(lst):
    image = []
    for i in range(len(lst)):
        row = [ ]
        for col in range(len(lst[i])):
            x = sumSurrounding(lst,i,col)
            row.append(x)
        image.append(row)
    return image









# 그냥 0 in col 처럼 가능

def seatTaken(lst):
    new_lst = [ ]
    for col in lst:
        for 0 in col:
            new_lst.append(col)

    return new_lst


def minInnerList():


def oddNum()

def itemDiscount(lst,num):
    

def spaceDefrag(lst):
    new_lst = []
    all_num = 0 
    for col in lst:
        if sum(col) >= 10:
            new_lst.append(col)

        else:
            all_num = all_num + sum(col)

    new_lst.append([all_num])


    return new_lst
            
            
            v
    



# ===========================================


def colorChange(image):
    for row in range(len(image)):
        for col in range(len(row)):
            if image[row][col] == [255, 0, 0]:
                
                
def disortColor(image):
    new_image = []  
    for row in image:
        new_row = [] 
        for col in row:
            new_col = [] 
            for pixel in col:
                if pixel == 1:
                    new_col.append(1)
                    
                elif pixel < 255:
                    new_col.append(pixel // 2)
                else:
                    new_col.append(pixel)
            new_row.append(new_col)
        new_image.append(new_row)

    return new_image


def makeGreen(image):




def makeGreen(image):
  for row in image:
    for pixel in row:
      new_green = int(pixel[1] * 1.20)
      if new_green <= 255:
        pixel[1] = new_green
  return image

# 그냥 col[0] col[1] 등등 지칭 가능 

def yellowORCyan(image,va) :
    new_image = [ ]
    for row in image:
        

        for col in row:

            for val in col:



def yellowORCyan(image, va):
  new_image = []
  for row in image:
    new_row = []
    for pixel in row:
      avg = (pixel[0] + pixel[1] + pixel[2]) / 3
      if avg >= va:
        new_row.append([255, 255, 0])
      else:
        new_row.append([0, 255, 255])
    new_image.append(new_row)
  return new_image
                





    return new_image 
    
                  
        
    
