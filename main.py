
import re
from ac_packet import *
# n = int(input("输入n: "))
# num_str = input("输入乱序的数列:")
n=25
num_str ='11025211312413514615781691718192021222324'

num_str_copy = num_str[:]
num_str_result = []

if n<10:
    print(' '.join(list(num_str)))
else:         # 当n>=10的时候  这里只关心2位数
    num_loca = []
    for i in range(10, n+1):
        num_loca.append([m.start() for m in re.finditer(str(i), num_str)])
    combination_all = putback_arrangement(num_loca)
    for i in range(len(combination_all)):
        A = combination_all[i][:]
        A.sort()
        if 1 not in [A[i] - A[i - 1] for i in range(1, len(A))]:
            num_loca = combination_all[i]
            break
    for i in range(len(num_str)):
        if i in num_loca:
            num_str_result.append(num_str[i:i + 2])
        elif i-1 in num_loca:
            pass
        else:
            num_str_result.append(num_str[i])
print(num_str_result)
'''
if n<10:
    print(' '.join(list(num_str)))
else:   # 当n>10的时候
    single_num = n if n<10 else 9
    one_num = 0 if n<10 else n<20 and n-9 or 10  # ps and or三目运算不人性化
    two_num = 0 if n<20 else n-19
    for i in range(two_num):
        num2_loca.append([m.start() for m in re.finditer('2'+ str(i), num_str_copy)])
    for i in range(one_num):
        num1_loca.append([m.start() for m in re.finditer('1'+ str(i), num_str_copy)])

    num_loca = num1_loca + num2_loca

    combination_all = not_putback_arrangement(num_loca)
    for i in range(len(combination_all)):
        A = combination_all[i][:]
        A.sort()
        if 1 not in [A[i] - A[i - 1] for i in range(1, len(A))]:
            num1_loca = combination_all[i][0:len(num1_loca)]
            num2_loca = combination_all[i][len(num1_loca):len(num_loca)]
            break
    # print(num1_loca)
    # print(num2_loca)
    for i in range(len(num_str)):
        if i in num2_loca:
            num_str_result.append(num_str[i:i + 2])
        elif i-1 in num2_loca:
            pass
        elif i in num1_loca:
            num_str_result.append(num_str[i:i+2])
        elif i-1 in num1_loca:
            pass
        else:
            num_str_result.append(num_str[i])
print(num_str_result)
'''
'''
if n<10:
    print(' '.join(list(num_str)))
elif n>=10 and n < 20:
    single_num = 9
    one_num = n - 9
    for i in range(n-9):
        num1_loca.append(num_str_copy.index('1'+ str(i)))
    for i in range(len(num_str)):
        if i in num1_loca:
            num_str_result.append(num_str[i:i+2])
        elif i-1 in num1_loca:
            pass
        else:
            num_str_result.append(num_str[i])
    print(num_str)
    print(' '.join(num_str_result))
elif n >=20 and n <= 25:
    single_num = 9
    one_num = 10
    two_num = n-19
    for i in range(two_num):
        num2_loca.append([m.start() for m in re.finditer('2'+ str(i), num_str_copy)])
    for i in range(one_num):
        num1_loca.append([m.start() for m in re.finditer('1'+ str(i), num_str_copy)])

    num_loca = num1_loca + num2_loca

    combination_all = not_putback_arrangement(num_loca)
    for i in range(len(combination_all)):
        A = combination_all[i][:]
        A.sort()
        if 1 not in [A[i] - A[i - 1] for i in range(1, len(A))]:
            num1_loca = combination_all[i][0:len(num1_loca)]
            num2_loca = combination_all[i][len(num1_loca):len(num_loca)]
            break
    print(num1_loca)
    print(num2_loca)
    for i in range(len(num_str)):
        if i in num2_loca:
            num_str_result.append(num_str[i:i + 2])
        elif i-1 in num2_loca:
            pass
        elif i in num1_loca:
            num_str_result.append(num_str[i:i+2])
        elif i-1 in num1_loca:
            pass
        else:
            num_str_result.append(num_str[i])
print(num_str_result)
'''
'''
import time

start = time.clock()

list_input =[[0, 1, 2], [0, 1, 2],[0, 1]]
combination_all = not_putback_arrangement(list_input)
print(combination_all)

end = time.clock()
print('Running time: %s Seconds'%(end-start))#其中end-start就是程序运行的时间，单位是秒。

'''