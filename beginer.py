#program-1
def are_anagrams(str1, str2):
    if len(str1) != len(str2):
        return False

    for ch in str1:
        if str1.count(ch) != str2.count(ch):
            return False

    return True

a = input("Enter first word: ")
b = input("Enter second word: ")
print("The two strings are anagram:" , are_anagrams(a, b))
print(" ")



#program-2
def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False

    return True

num = int(input("Enter an integer: "))
print("Prime?" , is_prime(num))
print(" ")


#program-3
def most_frequent(lst):
    max_count = 0
    common = None
    for item in lst:
        count = lst.count(item)
        if count > max_count:
            max_count = count
            common = item
    return common

a = eval(input("Enter a list: "))
print("Most Frequent:" , most_frequent(a))
