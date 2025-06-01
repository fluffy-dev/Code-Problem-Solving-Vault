
n = 1000

data_list = list(range(1, n))

we_want_to_find = 61

l, r = 0, n

while l <= r:
    mid = (l + r) // 2
    if data_list[mid] < we_want_to_find:
        l = mid + 1
    elif data_list[mid] > we_want_to_find:
        r = mid - 1
    else:
        print(mid)
        break