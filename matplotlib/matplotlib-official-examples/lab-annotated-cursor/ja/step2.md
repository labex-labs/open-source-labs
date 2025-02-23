# グラフを作成する

NumPy の `linspace` 関数を使って、x の値を -5 から 5 までの間で 1000 個生成し、その後 y を x の二乗として計算することで、放物線の簡単なグラフを作成します。

```python
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_title("Cursor Tracking x Position")

x = np.linspace(-5, 5, 1000)
y = x**2

line, = ax.plot(x, y)
ax.set_xlim(-5, 5)
ax.set_ylim(0, 25)
```
