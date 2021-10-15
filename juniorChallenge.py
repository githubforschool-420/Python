one = int(input())
two = int(input())
three = int(input())
four = int(input())

answer = True

if one == 8 or 9:
    if two == three:
        if four == 8 or 9:
            answer = False

if answer == True:
    print("answer")
else:
    print("ignore")