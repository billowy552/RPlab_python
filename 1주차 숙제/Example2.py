def check_parentheses(input_expression):
    list1 = list(input_expression[0])           # 리스트 input_expression에 있는 문자열을 리스트로 바꿔줌
    list2 = []
    pair = {"(": 1, ")": -1, "{": 2, "}": -2, "[": 3, "]": -3}          # 열어주는 괄호는 +, 닫는 괄호는 -로 설정, 같은쌍이면 합이 0

    for i in list1:
        if i in ['(', ')', '{', '}', '[', ']']:
            list2.append(i)         # 문자열에서 괄호 문자만 따로 리스트로 만듦

    if len(list2) % 2 == 1:
        return "Unbalanced"         # 괄호 개수가 홀수이면 "Unbalanced"을 출력

    list2_index = 0         # list2의 인덱스
    while len(list2) != 0:
        i = list2[list2_index]          # list2의 첫 괄호부터 i에 대입
        if pair[i] > 0:
            left = i
            list2_index += 1            # list2에 있는 괄호가 열어주는 괄호이면 left에 저장하고 다음 인덱스로 넘어감
        elif pair[i] < 0:
            if pair[left] + pair[i] == 0:
                del list2[list2_index - 1]
                del list2[list2_index - 1]          # 처음으로 닫힌 괄호가 나왔을 때 최근에 저장된 열어주는 괄호와 쌍이맞으면 그 쌍을 삭제
                list2_index = 0         # 쌍이 맞는 괄호를 삭제한 후 처음부터 다시 시작
            else:
                return "Unbalanced"         # 합이 0이 아니면 괄호가 불완전하게 닫혀있으므로 "Unbalanced" 출력

    return "Balanced"           # 괄호쌍이 정확하면 리스트에서 모두 삭제되므로 list2에 요소가 없어지면 while문 탈출, "Balanced"를 출력


inp = ["abc{def[ghi]{(jkl))}}"]
a = check_parentheses(inp)
print(a)