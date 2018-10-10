n = int(raw_input("find fib : "))
a,b=0,1
ans=[a]
for i in range(n,0,-1):
    ans.append(a+b)
    c = a + b
    a = b
    b = c
print ans

fib = lambda f : f if f <=1 else fib(f-1) + fib(f-2)
f = int(raw_input("find fib f : "))
print fib(f)
