t=int(input())
while(t):
    nab=list(map(int,input().strip().split()))
    l=list(map(int,input().strip().split()))
    bob=list(filter(lambda x:x%nab[1]==0,l))
    alice=list(filter(lambda x:x%nab[2]==0,l))
    unionAB=list(filter(lambda x:x%nab[1]==0 and x%nab[2]==0,l))
    b=len(bob)-len(unionAB)
    a=len(alice)-len(unionAB)
    if len(unionAB)!=0:
        if b>=a:
            print("BOB")
        else:
            print("ALICE")
    else:
        if b>a:
            print("BOB")
        else:
            print("ALICE")
    t-=1            