def playlist(duration,N,tripLength):
    Matrix=[[0 for x in range(tripLength+1)] for x in range(N+1)]
    for i in range(1,N+1):
        for v in range(1,tripLength+1):
            case1=Matrix[i-1][v]
            case2=0
            if duration[i-1]<=v:
                case2=duration[i-1]+Matrix[i-1][v-duration[i-1]]
            Matrix[i][v]=max(case1,case2)
    solution=[]
    ID=[]
    i=len(duration)
    V=tripLength

    for row in Matrix:
        print(row)
    while i > 0:
        if Matrix[i][V] !=Matrix[i-1][V]:
            solution.append(duration[i-1])
            ID.append(i)
            V-=duration[i-1]
        i-=1
    ID.reverse()
    solution.reverse()

    sum=0
    for time in solution:
        sum+=time
    if sum !=tripLength:
        print("Bad Luck Alice!")
    else:
        print("Playlist:")
        for i in range(len(ID)):
            print("ID:",ID[i],"Duration:",solution[i])

with open("songs.txt") as f:
    content = f.readlines()
    alist=[]
    blist=[]
    duration=[]
    for x in content:
        line=x.strip()
        alist.append(line)
    blist.append(alist[1])
    for y in blist:
        num=str(y).split()
    for str in num:
        duration.append(int(str))
    N=int(alist[0])

tripLength=int(input("Enter trip length:"))
assert tripLength>0,"trip length must be positive"
playlist(duration,N,tripLength)