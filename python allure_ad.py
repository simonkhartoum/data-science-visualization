import matplotlib.pyplot as plt
import numpy as np

# Data
months = ["07/2019", "08/2019", "09/2019", "10/2019", "11/2019"]
searches = [50, 53, 59, 56, 62]
direct = [33, 47, 42, 51, 51]
social = [70, 80, 90, 87, 92]

x = np.arange(len(months))
width = 0.25

# Plot
plt.bar(x - width, searches, width, label="Searches", color="skyblue")
plt.bar(x, direct, width, label="Direct", color="lightcoral")
plt.bar(x + width, social, width, label="Social Media", color="gold")

# Labels and style
plt.xlabel("months")
plt.ylabel("visitors in thousands")
plt.title("Visitors by web traffic sources")
plt.xticks(x, months)
plt.legend()

plt.show()
