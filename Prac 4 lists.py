numlist = [3, 1, 4, 1, 5, 9, 2]
#numbers[0] -> 3
#numbers[-1] -> 2
#numbers[3] -> 1
#numbers[:-1] -> 2 x, correct: [3, 1, 4, 1, 5, 9]
#numbers[3:4] -> 1
#5 in numbers -> True
#7 in numbers -> True
#"3" in numbers -> False
#numbers + [6, 5, 3] -> [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
print(numlist[0])
print(numlist[-1])
print(numlist[3])
print(numlist[:-1])
print(numlist[3:4])
print(5 in numlist)
print(7 in numlist)
print("3" in numlist)
print(numlist + [6, 5, 3])

#1.
numlist[0] = "ten"
print(numlist)
#2.
numlist[6] = 1
#3.
print(numlist[:1])
#4.
print(9 in numlist)

