import numpy as np

cnt_win = 0

def show():
    print("  0   1   2   3   4   5   6   7   8   9  ")
    for i in range(10):
        print(i,end=" ")
        for j in range(10):
            if showing[i*10 + j]:
                print(int(grid[i*10 + j]),end=" | ")
            elif Flag[i*10 +j]:
                print("F",end = " | ")
            else:
                print(" ", end=" | ")
        print()

def initial_dig(i,c):
    global cnt_win
    if i in mines or showing[i] or c==3:
        return 0
    showing[i] = True
    cnt_win+=1
    for j in temp:
        if 0 <= i + j < 100 and abs(i//10 - (i+j)//10) <= 1 and abs(i%10 - (i+j)%10) <= 1:
            initial_dig(i+j,c+1)

numberOfMines = {
    "easy" : 15,
    "medium" : 20,
    "hard" : 25
}
try:
    difficulty = input("Enter your difficulty(Easy , Medium , Hard): ").lower()
    mines = np.random.choice(100,size = numberOfMines[difficulty],replace=False)
except:
    print("please input proper difficulty")
Flag = [False] * 100
showing = [False] * 100
grid = np.zeros(100)
temp = np.array([1,-1,10,-10,-11,-9,9,11])
for i in range(100):
    if i in mines:
        grid[i] = -1
        continue
    cnt = 0
    for j in temp:
        if 0 <= i + j < 100 and abs(i//10 - (i+j)//10) <= 1 and abs(i%10 - (i+j)%10) <= 1:
            if i+j in mines:
                cnt+=1
    grid[i] = cnt
flag = True
show()
x,y,z = map(int , input("Enter your choice (row column 1 for flag / row column 0 for dig): ").split())

if x*10 + y in mines:
    print("You lost!")
else:
    initial_dig(x*10 + y,0)
    show()
    while flag:
        x,y,z = map(int , input("Enter your choice (row column 1 for flag / row column 0 for dig): ").split())
        if z == 0:
            pos = x*10 + y
            if pos in mines:
                print("You lost")
                flag = False
                continue
            if not showing[pos]:
                if grid[pos] == 0:
                    initial_dig(pos, 0)
                else:
                    showing[pos] = True
                    cnt_win += 1
            show()
            if 100 - cnt_win == numberOfMines[difficulty]:
                print("You won")
                flag = False
        elif z == 1:
            if(not showing[x*10+y]):
                Flag[x*10+y] = not Flag[x*10+y]
            show()
        