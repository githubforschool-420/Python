List = [1,2,3,4,5,6,7,8,9,10]

def isEven (x):
    return x % 2 == 0

i = 0
while i < len (List):
    if isEven (List[i]):
        print("Even!")
    else:
        print("Odd!")
    i += 1

for checker in range (len (List)):
    if isEven (List[checker]):
        print ('even')
    else:
        print ('odd')