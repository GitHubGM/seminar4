n1=int(input())
n2=int(input())
n3=int(input())
def exe1(a,b,c):
    if a+b>b+c:
        if a+b>a+c:
            print("наибольшая сумма у a+b",a+b)
        elif a+b<a+c:
            print("наибольшее число у a+c",a+c)
    elif a+b<b+c:
        if a+c<b+c:
            print("наибольшая сумма у b+c",b+c)
    else:
        print("суммы равны")
exe1(n1,n2,n3)

