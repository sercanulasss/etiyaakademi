def fibo():
    fib =[1,1]
    for i in range(18):
     toplam = fib[i] + fib[i+1]
     fib.append(toplam)
    
    print(fib) 

fibo()




