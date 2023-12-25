# Необхідно розробити функцію, яка приймає рядок як вхідний параметр, 
# додає всі його символи до двосторонньої черги (deque з модуля collections в Python), 
# а потім порівнює символи з обох кінців черги, щоб визначити, чи є рядок паліндромом. 
# Програма повинна правильно враховувати як рядки з парною, так і з непарною кількістю символів, 
# а також бути нечутливою до регістру та пробілів.

from collections import deque

def palindrome_string(input_str):
    d = deque()

    for char in input_str.lower():
        if char.isalnum():  # Додавання лише букв і цифр
            d.append(char)

    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True

# Приклади паліндрому
print(palindrome_string("А роза упала на лапу Азора"))  
print(palindrome_string("Анна"))  
print(palindrome_string("Це не паліндром"))



