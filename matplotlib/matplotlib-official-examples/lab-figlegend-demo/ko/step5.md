# 서브플롯에 대한 범례 생성

서브플롯을 생성할 때, `fig.legend()` 함수를 사용하여 모든 서브플롯에 대한 범례를 생성할 수 있습니다. 여기서는 두 개의 서브플롯을 생성하고 각 서브플롯에 두 개의 선을 그립니다.

```python
fig, axs = plt.subplots(1, 2)

x = np.arange(0.0, 2.0, 0.02)
y1 = np.sin(2 * np.pi * x)
y2 = np.exp(-x)
l1, = axs[0].plot(x, y1)
l2, = axs[0].plot(x, y2, marker='o')

y3 = np.sin(4 * np.pi * x)
y4 = np.exp(-2 * x)
l3, = axs[1].plot(x, y3, color='tab:green')
l4, = axs[1].plot(x, y4, color='tab:red', marker='^')

fig.legend((l1, l2), ('Line 1', 'Line 2'), loc='upper left')
fig.legend((l3, l4), ('Line 3', 'Line 4'), loc='upper right')
```
