import matplotlib.pyplot as plt
square = [1,4,9,16,25]
plt.plot(square,linewidth = 5)

plt.title('Square numsers', fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of value",fontsize=14)
plt.tick_params(axis="both", labelsize=14)

plt.show()

