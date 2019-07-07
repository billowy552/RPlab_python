def pair_count(input_list):
    num = len(input_list)   # input_list에 있는 문자열의 개수
    count = 0               # 같은 문자가 두개 있는지 카운트
    for i in range(0, num-1):            # 첫번째 문자열부터 반복 시작
        for j in range(i+1, num):        # 중복 비교를 제외하기 위해 i+1번째 문자열부터 비교한다
            set1 = set(input_list[i])
            set2 = set(input_list[j])
            if len(set1 & set2) == 2:
                count = count + 1           # 문자열을 각각 집합으로 만들고 같은 알파벳이 2개면 교집합이 2개일 때 카운트한다

    return count


example1 = ["bcd", "bce", "cce"]
result1 = pair_count(example1)

InputList = ["abe", "rea", "pcd", "dpt", "iae"]
result2 = pair_count(InputList)
print(result1)
print(result2)
