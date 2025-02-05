# 使用 \dfrac 绘制数据

我们将使用 \dfrac TeX 宏来绘制数据，并显示生成的图形。

```python
fig, ax = plt.subplots()
ax.plot(x, y, label=r'$\dfrac{sin(x)}{x}$')
ax.legend()
plt.show()
```
