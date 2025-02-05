# 设置等高线颜色

我们可以强制所有等高线为相同颜色，或者将负等高线设置为实线而非虚线。

```python
fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z, 6, colors='k')  # 负等高线默认是虚线。
ax.clabel(CS, fontsize=9, inline=True)
ax.set_title('Single color - negative contours dashed')
```

```python
plt.rcParams['contour.negative_linestyle'] = 'solid'
fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z, 6, colors='k')  # 负等高线默认是虚线。
ax.clabel(CS, fontsize=9, inline=True)
ax.set_title('Single color - negative contours solid')
```
