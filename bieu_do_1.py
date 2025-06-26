import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y, marker='o', color='green', linestyle='--', linewidth=2, markersize=8, label='Dữ liệu')

plt.title("Biểu đồ đơn giản", fontsize=16, color='blue')
plt.xlabel("Trục X", fontsize=12)
plt.ylabel("Trục Y", fontsize=12)
plt.grid(True, linestyle=':', color='gray', alpha=0.7)
plt.legend()

plt.show()