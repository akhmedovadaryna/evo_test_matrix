import numpy as np

a = np.random.randint(0, 10, (10, 10,10))
print(a)

def for_x():
    s = 0
    sum1 = 0
    sum_list = []
    for i in a:
        for j in i:
            sum = 0
            while s<10:
                sum = j[s]+sum
                s = s + 1
            if sum>sum1:
                sum1 = sum
            s = 0
            sum_list.append(sum)
    find_ind = sum_list.index(max(sum_list))
    if find_ind<10:
        string = 'X: ' + 'matrix number: ' + str(0) + ' , ' + 'string number: '+str(find_ind)
        print(string)
    else:
        string = 'X: ' + 'matrix number: '+str(int(find_ind/10))+ ' , '  + 'string number: '+str(find_ind%10)
        print(string)


def for_z():
    sum1 = 0
    ind_list_first = []
    ind_list_last = []
    sum_list = []
    for i in range(10):
        s = 0
        for j in range(10):
            s += a[j][i]
        pop = 0
        while pop<len(s):
            if s[pop]>sum1:
                sum1 = s[pop]
                ind = pop
            pop = pop+1
        sum_list.append(sum1)
        sum1=0
        ind_list_last.append(ind)
        ind_list_first.append(i)
    find_ind = sum_list.index(max(sum_list))
    f = 0
    for i, c in enumerate(ind_list_last):
        if i == find_ind:
            f = c
    string = 'Z: ' + 'string number: '+str(find_ind) + ' , ' 'column number:  ' + str(f)
    print(string)

def for_y():
    sum1 = 0
    ind_list_first = []
    ind_list_last = []
    sum_list = []
    for i in a:
        s = 0
        sum = []
        for j in range(10):
            for k in range(10):
                s += i[k][j]
            sum.append(s)
            s = 0
        pop = 0
        while pop<len(sum):
            if sum[pop]>sum1:
                sum1 = sum[pop]
                ind = pop
            pop = pop+1
        sum_list.append(sum1)
        sum1=0
        ind_list_last.append(ind)
    for first in range(10):
        ind_list_first.append(first)
    find_ind = sum_list.index(max(sum_list))
    f = 0
    for i, c in enumerate(ind_list_last):
        if i == find_ind:
            f = c
    string = 'Y: ' + 'matrix number: '+str(find_ind) + ' , ' 'column number:  ' + str(f)
    print(string)

for_x()
for_y()
for_z()
