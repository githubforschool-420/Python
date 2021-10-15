# le input for les numbers
FirstHalf = input()
SecondHalf = input()
# Creates a list to input the input
seqList = [int(FirstHalf[0]), int(SecondHalf[0]), int(SecondHalf[1])]
# if the hour is 2 digits then it appends the second digit into the second position
if len(FirstHalf) == 2:
    seqList.insert(1, int(FirstHalf[1]))
# finds the difference then finds out if the whole sequence follows the pattern
def check_arithmeticness(thething):
    checker = 0
    difference = int(seqList[2]) - int(seqList[1])
    arithmeticness = True
    for _ in range(len(seqList) - 1):
        if seqList[checker] + difference != seqList[checker + 1]:
            arithmeticness = False
        checker += 1
    if arithmeticness:
        print("Arithmetic")
    else:
        print("Not Arithmetic")
# runs this function
check_arithmeticness(seqList)