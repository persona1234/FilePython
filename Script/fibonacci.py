
N=int(input('Per quanti numeri devo eseguire la successione di Fibonacci?: ' ))
    
a,b=1,1
for i in range (N):
    print(a)
    r = a+b
    a,b=b,r
    # Qui ho unito due espressioni distinti; ovvero ho detto che a è uguale a b e b è uguale ad r.
    
