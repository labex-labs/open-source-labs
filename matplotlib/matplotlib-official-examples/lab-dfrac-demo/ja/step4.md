# \fracを使ってデータをプロットする

\fracのTeXマクロを使ってデータをプロットし、結果のプロットを表示します。

```python
ax.plot(x, y, label=r'$\frac{sin(x)}{x}$')
ax.legend()
plt.show()
```
