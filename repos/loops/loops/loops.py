
result = []

def permutations(n):
    if not n:
        return [[]]
    ret_list = []
    for i in range(len(n)):
        el = n[i]
        rem_list = n[:i] + n[i+1:]
        sub_list = permutations(rem_list)
        for sub in sub_list:
            tmp_list = sub.copy()
            tmp_list.insert(0, el)       
            ret_list.append(tmp_list)
    ret_list.append([])
    return ret_list

for i in range(100,1000):
    ret_list = []
    num_list = []
    digitlist = [int(c) for c in str(i)]
    returned = permutations(digitlist)
    for item in returned:
        if len(item) == 3:
            ret_list.append(item)
    for item in ret_list:
        num = ""
        for elem in item:
            num += str(elem)
            num = int(num)
            num_list.append(num)
    sum_ = 0
    for item in num_list:
        sum_ += item
    avrg = sum_ // 6
    if avrg == i:
        result.append(i)

print(result)