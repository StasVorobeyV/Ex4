#task 2
#Напишите функцию, которая проверяет: является ли слово палиндромом

def check_palindrome(string):
# прохождение строки от последнего к первому
    reversed_string = string[::-1]
    if string == reversed_string:
        print(string, "полиндром")
    else:
        print(string, "не является полиндромом")

#test
check_palindrome("RADAR")
check_palindrome("PythonPool")