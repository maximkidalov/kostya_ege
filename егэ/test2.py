for x in '0123456789ABCDEF' :
    x1=int('2'+ x +'84',16)
    x2=int('2B3' + x,19)
    num=x1+x2
    if num%88==0:
        print(num//88)
        break