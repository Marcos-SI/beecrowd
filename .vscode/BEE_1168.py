n = int(input())
v = [6,2,5,5,4,5,6,3,7,6]
#soma =0
led = []
while n:
    soma = 0
    num = input()
    for i in num:
        led.append(int(i))
    for i in range(len(led)):
        soma += v[led[i]]
   # print(soma)
    led = []
    print(f'{soma} leds')
    ##for i in range(len(led)):
     ##   led.pop()
    
    n -=1