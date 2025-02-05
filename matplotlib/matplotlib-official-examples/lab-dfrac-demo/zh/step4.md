# 使用 \frac 绘制数据

我们将使用 \frac TeX 宏来绘制数据，并显示生成的图形。

```python
ax.plot(x, y, label=r'$\frac{sin(x)}{x}$')
ax.legend()
plt.show()
```
