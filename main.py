def myfunction(arg1, arg2):  # Mauvais espacement et nom de fonction non conforme
    result = arg1 + arg2
    print("The result is: ", result)  # Utilisation de print au lieu de return
    if result > 10:  # Mauvaise indentation
        print("Result is greater than 10")  # Mauvaise indentation
    return result


myList = [1, 2, 3, 4]  # Mauvais espacement
for i in myList:
    print(myfunction(i, i))  # Mauvaise indentation
