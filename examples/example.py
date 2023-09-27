from typing import List

from matplotlib import pyplot as plt

from macaulay import MacaulayBracket, compute, integrate

plt.rcParams.update({"font.size": 20, "figure.autolayout": True})

shear: List[MacaulayBracket] = [
    {"x": 0.25, "power": 0, "coefficient": 10},
    {"x": 0.75, "power": 0, "coefficient": -10},
]

shear_res = compute(shear)
print(shear_res)

plt.plot(shear_res[:, 0], shear_res[:, 1])
plt.xlabel("Length")
plt.ylabel("Shear")
plt.show()

bending = integrate(shear)
bending_res = compute(bending)
print(bending_res)

plt.plot(bending_res[:, 0], bending_res[:, 1])
plt.xlabel("Length")
plt.ylabel("Bending")
plt.show()
