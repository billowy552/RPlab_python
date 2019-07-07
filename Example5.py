def sort_tuple(input_dict):
    list_temp = list(input_dict.values())           # input 딕셔너리의 value를 리스트로 저장한다.
    list_temp2 = list(input_dict.items())           # input 딕셔너리의 key,value 튜플을 리스트로 저장한다.

    list_temp.sort()            # input의 value를 오름차순으로 정렬한다.
    result = list(range(len(list_temp2)))           # 결과로 반환할 리스트를 임의로 만든다.
    for i in list_temp2:
        for j in range(len(list_temp2)):
            if i[1] == list_temp[j]:
                result[j] = i[0]            # (key, value) 튜플의 value가 오름차순 정렬한 값과 같으면 같은 위치에 key를 저장한다.

    return tuple(result)            # 튜플형으로 변환하여 반환한다.


a = {'2': 'c', '10': 'a', '1': 'f', '4': 'z'}
print(sort_tuple(a))
