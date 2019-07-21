def subsequences(random_type, length):
    list_char = list(random_type)           # 입력 인수를 리스트형으로 바꾸어준다.
    for i in range(len(list_char)):
        list_char[i] = str(list_char[i])            # 리스트 내의 숫자들을 문자열로 바꾸기 위함

    from itertools import combinations

    list_comb = list(combinations(list_char, length))           # combinations 함수로 조합 튜플을 리스트로 생성
    n = len(list_comb)
    result = list(range(n))         # 조합 개수 길이의 리스트를 생성
    for i in range(n):
        result[i] = ''.join(list_comb[i])           # 리스트의 각 요소를 조합 튜플 내의 문자를 합친 문자열이 되도록 만든다.

    return result


sub1 = subsequences('ABCD', 2)
print(sub1)

sub2 = subsequences(range(4), 3)
print(sub2)
