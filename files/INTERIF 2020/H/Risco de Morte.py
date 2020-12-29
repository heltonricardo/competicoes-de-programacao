e = input().split()

s = e[0]
i = int(e[1])
c = e[2]
r = int(e[3])


if s == 'H':
    ps = 0.58
else:
    ps = 0.42

if i >= 70:
    pi = 0.25
elif i >= 60 and i < 70 :
    pi = 0.24
elif i >= 50 and i < 60 :
    pi = 0.20
elif i >= 40 and i < 50 :
    pi = 0.15
elif i >= 30 and i < 40 :
    pi = 0.10
elif i >= 15 and i < 30 :
    pi = 0.05
else:
    pi = 0.01

if c == 'P':
    pc = 0.5
elif c == 'B':
    pc = 0.36
else:
    pc = 0.14
    
if r <= 3000:
    pr = 0.66
elif r > 3000 and r < 6500:
    pr = 0.21
else:
    pr = 0.13

pt = ps * pi * pc * pr

t = 200000 * pt

print("{:.2f}".format(t))
