# Feel free to edit this file.
# For any queries please refer to readme.md file or go to
# Settings > HELP

def policeAndThief(arr,n,k):
    i=0
    l=0
    r=0
    res = 0
    thief = []
    police = []
    while(i<n):
        if(arr[i]=='P'):
            police.append(i)
        elif(arr[i]=='T'):
            thief.append(i)
        i+=1
    while(l<len(thief) and r<len(police)):
        if(abs(thief[l]- police[r])<=k):
            res+=1
            l+=1
            r+=1
        elif(thief[l]<police[r]):
            l+=1
        else:
            r+=1
    return res


if __name__ == '__main__':
    n,k = map(int,input().split())
    #arr = ['P','T','T','P','T']
    #arr = list(map(list,input().split()))
    arr = input().split()
    print(policeAndThief(arr,n,k))