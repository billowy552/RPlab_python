def check(str1, str2):
    list1 = list(str1)
    list2 = list(str2)
    list1.sort()
    list2.sort()
    if list1 == list2:
        return "True"
    else:
        return "False"


input1, input2 = "abcd", "dacb"
print(check(input1, input2))