# 信号をプロットする

これで、Matplotlibを使って2つの信号を時間領域でプロットすることができます。

```python
fig, axs = plt.subplots(2, 1)
axs[0].plot(t, s1, t, s2)
axs[0].set_xlim(0, 2)
axs[0].set_xlabel('Time')
axs[0].set_ylabel('s1 and s2')
axs[0].grid(True)
```
