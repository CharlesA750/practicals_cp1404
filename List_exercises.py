numbers = []
for i in range(5):
    in_nums = input("Number " + str(i) + ": ")
    numbers.append(in_nums)
print("The first number is: " + numbers[0])
print("The last number is: " + numbers[-1])
print("The smallest number is: " + min(numbers))
print("The largest number is: " + max(numbers))
print("The smallest number is: " + min(numbers))




usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

name_check = input("What is your username? \n>>> ")
if name_check in usernames:
    print("Access granted")
else:
    print("Access denied")


