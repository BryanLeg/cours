import random

# def invert_values(a, b): 

#     a, b = b, a

#     return a, b

# print(invert_values(4, 5)) 
# print(invert_values("dfs", 5)) 
# print(invert_values("dfs", True)) 

# print("- - - ")

# def is_prime(nb: int) -> bool: 
#     for i in range(2, nb - 1):
#         if nb%i == 0:
#             return f"{nb} is not a prime number"
#     return f"{nb} is a prime number"


# print(is_prime(4))
# print(is_prime(1))
# print(is_prime(5))
# print(is_prime(19))
# print(is_prime(20))

# print("- - - ")

# def sort_list(list_nb: list) -> list:
#     list_len = len(list_nb)
#     for i in range(0, list_len):
#         min = i
#         for j in range(i + 1, list_len):
#             if list_nb[j] < list_nb[min]:
#                 min = j
#         if i != j:
#             list_nb[i], list_nb[min] = list_nb[min], list_nb[i]
#     return list_nb

# print(sort_list([2, 4, 1, 7, 3]))
# print(sort_list([random.randint(0, 20) for x in range(0, 10)]))
# print(sort_list([random.randint(0, 20) for x in range(0, 10)]))
# print(sort_list([random.randint(0, 20) for x in range(0, 10)]))

# print("- - -")

# def is_palindrome():
#     print("We will try if your word is a palindrome.")
#     word = input('Type your word: ').lower()
#     invert_word = []
    
#     for i in range(0, len(word)):
#         invert_word.insert(0, word[i])
    
#     if "".join(invert_word) == word:
#         return f"{word} is a palindrome"
    
#     return f"{word} is not a palindrome"

# print(is_palindrome())


# def to_binary(nb: int) -> int:
#     quotient = nb
#     nb_binary = []
#     while(quotient != 0):
#         nb_binary.insert(0, str(quotient%2))
#         quotient //= 2
#     return "".join(nb_binary)

# print(to_binary(57))
# print(to_binary(15))
# print(to_binary(63))
# print(to_binary(1024))

# def avrg():
#     marks = []
#     sum = 0
#     while (len(marks) < 9):
#         mark = input("type your mark: ")
#         try:
#             mark = float(mark)

#             if mark <= 20 and mark >= 0:
#                 marks.append(mark)
#                 print(f"Your marks: {marks}")
#             else:
#                 ValueError
#                 print("your mark is supposed to be between 0 and 20")

#         except ValueError:
#             print(f"{mark} is not a number")
        
        
#     for i in range(len(marks)):
#         sum += marks[i]
    
#     return f"Your average is: {sum/len(marks):.2f}, congratulations" if sum/len(marks) > 15 else f"Your average is: {sum/len(marks):.2f}" 

# print(avrg())

def to_hexadecimal() -> str:
    nb = input("type a number: ")
    try:
        nb = int(nb)
        quotient = nb
        nb_hexa = []
        hexa_values = [x for x in range(10, 16)]
        alph = list(map(chr, range(97, 103)))
        while(quotient != 0):
            if quotient%16 in hexa_values:
                nb_hexa.insert(0, alph[hexa_values.index(quotient%16)])
            else :
                nb_hexa.insert(0, str(quotient%16))
            quotient //= 16
        
        return f"hexadecimal value: 0x{''.join(nb_hexa)}"

    except ValueError:
        print(f"{nb} is not a number")
    
    

print(to_hexadecimal())