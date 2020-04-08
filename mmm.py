def fctor(a):
    k = []
    j = 0
    for i in range(2, 20):
        while a % i == 0:
            x = a / i
            a = x
            k.append(i)
            j += 1

    return k


x = int(input("Enter how many number you want to enter="))
y = []
s1 = []
o = []
f = []
j = 0
while j < x:
    z = int(input("Plz enter ur values=="))

    y.append(z)
    j += 1
for a in y:
    s1 = fctor(a)
    print(f"your factor for {a} are ")
    print(s1)
