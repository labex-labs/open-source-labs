# \frac を使ってデータをプロットする

\frac の TeX マクロを使ってデータをプロットし、結果のプロットを表示します。

```python
ax.plot(x, y, label=r'$\frac{sin(x)}{x}$')
ax.legend()
plt.show()
```
