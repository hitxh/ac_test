
def list_multiply(one_list):
    '''''
    列表内元素乘积
    '''
    res=1
    for i in range(len(one_list)):
        res*=one_list[i]
    return res

def putback_arrangement(list_input):
    n = [len(v) for v in list_input]
    n_sum = sum(n)
    mul_sum = list_multiply(n)
    combination_all = []
    for i in range(len(list_input)-1):
        combination_all.append([])
        for j in range(mul_sum):
            combination_all[i].append(list_input[i][j//list_multiply(n[i+1:])%len(list_input[i])])
            # print(combination_all)
    # 最后一项特殊处理
    combination_all.append([])
    for j in range(mul_sum):
        combination_all[-1].append(list_input[-1][j%n[-1]])
    # print(combination_all)
    # 对列表进行转置
    # combination_all_copy = combination_all[:]
    # combination_all = []
    # for j in range(len(combination_all_copy[0])):
    #     combination_all.append([combination_all_copy[i][j] for i in range(len(combination_all_copy))])

    combination_all = [[row[i] for row in combination_all] for i in range(len(combination_all[0]))]
    return combination_all
