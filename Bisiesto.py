def is_leap(year):
    leap = False
    
    n = year % 4
    l = year % 400
    m = year % 100
    print(n)
    print(l)
    print(m)
    if n == 0:
        if l == 0:
            leap = True
        elif m == 0:
            leap = False
        else:
            leap = True
    return leap

year = int(input())
print(is_leap(year))