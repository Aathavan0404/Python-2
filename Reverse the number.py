Num = int(input('Enter the number: '))
Ans = int
Mod = int

while Ans != 0:
    Mod = Num % 10
    Ans = Num // 10
    print(Mod,end="")
    Num = Ans


