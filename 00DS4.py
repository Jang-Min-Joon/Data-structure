num = [2, 4, 1, 8, 9, 3]

def max(num, n):
    if n==1:
        return num[0]
    return num [0] if num[0] > max(num[1:], n-1) else max(num[1:],n-1)

print(max(num, len(num)-1))