import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
x, y = 0, 0
ax.scatter(x, y)

for i in range(10000):
    p = np.random.randint(1,101)
    if p <= 7:
        nx, ny = -0.15*x + 0.28*y, 0.26*x+0.24*y+0.44
    elif p <=14:
        nx, ny = 0.20*x - 0.26*y, 0.23*x+0.22*y+1.60
    elif p <=99:
        nx, ny = 0.85*x + 0.04*y, -0.04*x+0.85*y+1.60
    else:
        nx, ny = 0,0.16*y
    x, y = nx, ny
    ax.scatter(10*x, 10*y, s=1, c="g")
    print(i)

#plt.show()
fig.savefig('fern3.svg')
ax.axis("scaled")
#plt.show()
fig.savefig('fern3_scaled.svg')