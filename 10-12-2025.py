import sys


def movezero(n,arr):
    i=0
    j=0
    while j<=n-1:
        if arr[j]==0:
            j+=1
        else:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j+=1
    return arr

if __name__=="__main__":
    a=sys.stdin.readline()
    b=sys.stdin.readline()
    try:
        n=int(a.strip())
        arr=list(map(int,b.strip("[]").split(",")))
    except ValueError:
        pass
    res=movezero(n,arr)
    print(*res)