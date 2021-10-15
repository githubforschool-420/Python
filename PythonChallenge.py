S = int(input(("Enter # of small-sized treats:")))
M = int(input(("Enter # of medium-sized treats:")))
L = int(input(("Enter # of large-sized treats:")))

score = S*1 + M*2 + L*3

if score >= 10:
    print ("happy")
else:
    print ("sad")

