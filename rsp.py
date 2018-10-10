
#print("hello", p1,p2 )
next = 0
while (1):
    p1 = raw_input("P1 call : ")
    p2 = raw_input("P2 call : ")
    if ( (p1=='p' and p2=='r') or (p1=='r' and p2=='s') or (p1=='s' and p2=='p') ):
        #next = 1
        print 'p1 wins'
        break
    elif( (p2=='p' and p1=='r') or (p2=='r' and p1=='s') or (p2=='s' and p1=='p') ):
        #next = 1
        print 'p2 wins'
        break
    else:
        print 'draw \n next game'
