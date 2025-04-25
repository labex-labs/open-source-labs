# データをプロットする

二次軸の使用方法を示すために、単純なサイン波を作成します。x 軸に度数を使用してサイン波をプロットします。

```python
fig, ax = plt.subplots(layout='constrained')
x = np.arange(0, 360, 1)
y = np.sin(2 * x * np.pi / 180)
ax.plot(x, y)
ax.set_xlabel('angle [degrees]')
ax.set_ylabel('signal')
ax.set_title('Sine wave')
```
