
def my_min_mid_max(a, b, c):
    maxx = max(a, max(b,c))
    minn = min(a, min(b,c))
    mid = a+b+c-maxx-minn
    return minn, mid, maxx

num1 = int(input())
num2 = int(input())
num3 = int(input())

minn, mid, maxx = my_min_mid_max(num1, num2, num3)
print(f'min = {minn}\nmid = {mid}\nmax = {maxx}')
