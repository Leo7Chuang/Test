import matplotlib.pyplot as plt

Rx = 3
Nx = 10
NN = Nx * 10
x = []
y = []

def fnin(R, r):
    return r/(R*R*R)

def fnout(r):
    return 1/(r*r)


for dx in range(NN):
    r = dx/10
    x.append(r)
    if r<=Rx:
        y.append(fnin(Rx, r))
    else:
        y.append(fnout(r))

#plt.plot(x, y, 'ro')
plt.plot(x, y)

ax = [0, Nx, 0, 0.15]
plt.axis(ax)

plt.show()


