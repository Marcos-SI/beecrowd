cont = 0
gi = 0
gg = 0
emp = 0
while True:
    #print('Novo grenal (1-sim 2-nao)')
    #n = int(input())
    #if n == 1:
    i,g = list(map(int,input().split()))
    cont += 1
    if i > g:
        gi += 1
    elif g > i:
        gg += 1
    else:
        emp += 1
    print('Novo grenal (1-sim 2-nao)')
    n = int(input())
    if n == 2 :
        break
    #cont += 1
    #if i > g:
       # gi += 1
    #elif g > i:
      #  gg +=1
    #else:
     #   emp +=1
print(f'{cont} grenais')
print(f'Inter:{gi}')
print(f'Gremio:{gg}')
print(f'Empates:{emp}')
if gi > gg:
    print('Inter venceu mais')
else:
    print('Gremio venceu mais')

        #cont += 1
        #if i > g:
         #   gi +=1
        #else:
         #   gg +=1
    #if n == 2:
     #   break




