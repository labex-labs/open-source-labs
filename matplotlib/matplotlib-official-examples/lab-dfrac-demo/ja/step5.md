# \dfrac を使ってデータをプロットする

\dfrac の TeX マクロを使ってデータをプロットし、結果のプロットを表示します。

```python
fig, ax = plt.subplots()
ax.plot(x, y, label=r'$\dfrac{sin(x)}{x}$')
ax.legend()
plt.show()
```
