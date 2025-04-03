'''
   N
w -|- E
   S
'''
#右上角頂點
X,Y=map(int,input().split())

D = {'N': 0, 'E': 1, 'S': 2, 'W': 3}
r_D = {0: 'N', 1: 'E', 2: 'S', 3: 'W'}

scent = set()

while(True):
    try:
        x,y,direction=input().split()   #機器人座標跟方向
        x,y=int(x),int(y)

        dnum=D[direction]   #初始方位數字
        lost=False

        order=input()#總指令陣列

        for i in range(len(order)):
            if (order[i]=='R'):
                dnum=(dnum+1)%4
            elif (order[i]=='L'):
                dnum=(dnum-1)%4
            else:
                new_x,new_y=x,y
                if(dnum==0):
                    new_y+=1
                elif(dnum==1):
                    new_x+=1
                elif(dnum==2):
                    new_y-=1
                elif(dnum==3):
                    new_x-=1
                    
                if(new_x>X or new_y>Y or new_x<0 or new_y<0):
                    if(x,y) in scent:
                        continue
                    lost=True
                    scent.add((x,y))
                    break
                else:
                    x,y=new_x,new_y
                
        print(x,y,r_D[dnum],end="")
        
        if lost==True:
            print(" LOST")
        else:
            print()

    except EOFError:
        break