#EX1
#RETURN SE
 

# def sum_of_list(numbers):
#     return sum(numbers)

# result = sum_of_list([10, 20, 30, 40, 50])
# print(result)


# EX2

# def largest_number(numbers):
#     return max(numbers)

# result = largest_number([10, 25, 8, 45, 30])
# print(result)

# EX3

# - Using return: Write a function that takes a list of integers and returns the smallest number in the list.

# def smallest_number(numbers):
#     return min(numbers)

# result = smallest_number([10, 25, 8, 45, 30])
# print(result)

# EX4

# - Using return: Write a function that takes a list and an element as input and returns True if the element exists in the list, otherwise returns False.

# def check_element(my_list, element):
#     return element in my_list

# result = check_element([10, 20, 30, 40, 50], 30)
# print(result)

# EX 5

# - Using return: Write a function that takes a list of integers and returns the count of even numbers present in the list.


# def count_even(numbers):
#     count = 0

#     for num in numbers:
#         if num % 2 == 0:
#             count += 1

#     return count

# result = count_even([10, 15, 20, 25, 30, 35])
# print(result)

# EX 6




# - Using return: Write a function that takes a list of integers and returns the count of odd numbers present in the list.


# def count_odd(numbers):
#     count = 0

#     for num in numbers:
#         if num % 2 != 0:
#             count += 1

#     return count

# result = count_odd([10, 15, 20, 25, 30, 35])
# print(result)

# EX 7

# Using return: Write a function that takes a list of integers and returns the average of all the numbers.

# def calculate_average(numbers):
#     return sum(numbers) / len(numbers)

# result = calculate_average([10, 20, 30, 40, 50])
# print(result)


# EX8

# - Using return: Write a function that takes a list of integers and returns the counts of positive numbers and negative numbers.

# def count_positive_negative(numbers):
#     positive = 0
#     negative = 0

#     for num in numbers:
#         if num > 0:
#             positive += 1
#         elif num < 0:
#             negative += 1

#     return positive, negative

# result = count_positive_negative([10, -5, 20, -8, 0, 15, -3])
# print(result)

# EX9

# - Using return: Write a function that takes a string and returns the number of vowels present in it.

# def count_vowels(text):
#     count = 0

#     for char in text:
#         if char.lower() in "aeiou":
#             count += 1

#     return count

# result = count_vowels("Hello World")
# print(result)

# EX10

# - Using return: Write a function that takes a string and returns whether it is a palindrome or not (True or False).

# def is_palindrome(text):
#     return text == text[::-1]

# result = is_palindrome("madam")
# print(result)

# EX 11

# - Using return: Write a function that takes a list of integers and returns a list containing all the numbers divisible by 5.

# def divisible_by_5(numbers):
#     result = []

#     for num in numbers:
#         if num % 5 == 0:
#             result.append(num)

#     return result

# output = divisible_by_5([10, 12, 15, 22, 25, 31, 40])
# print(output)

# EX 12

# Using return: Write a function that takes two lists and returns a list of common elements between them.

# def common_elements(list1, list2):
#     result = []

#     for num in list1:
#         if num in list2 and num not in result:
#             result.append(num)

#     return result

# output = common_elements([10, 20, 30, 40], [20, 40, 50, 60])
# print(output)

# EX 13

# * Using return: Write a function that takes a list of integers and returns a list containing the factorial of each element.

# def factorial_list(numbers):
#     result = []

#     for num in numbers:
#         factorial = 1

#         for i in range(1, num + 1):
#             factorial *= i

#         result.append(factorial)

#     return result

# output = factorial_list([3, 4, 5])
# print(output)

# EX 14

# - Using return: Write a function that takes a list of integers and returns a list containing only the prime numbers from the list.

def is_prime(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


def prime_numbers(numbers):
    result = []

    for num in numbers:
        if is_prime(num):
            result.append(num)

    return result


output = prime_numbers([2, 4, 5, 8, 11, 15, 17, 20])
print(output)