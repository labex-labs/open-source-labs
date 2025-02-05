# 枢轴点和箭头频率

`quiver()` 函数还可用于自定义箭头的枢轴点以及箭头的显示频率。`pivot` 参数可设置为 `'mid'` 或 `'tip'`，并且传递给 `quiver()` 的数组可以切片，以便仅每隔第 n 个箭头显示一次。

```python
fig2, ax2 = plt.subplots()
ax2.set_title("pivot='mid'; every third arrow; units='inches'")
Q = ax2.quiver(X[::3, ::3], Y[::3, ::3], U[::3, ::3], V[::3, ::3],
               pivot='mid', units='inches')
qk = ax2.quiverkey(Q, 0.9, 0.9, 1, r'$1 \frac{m}{s}$', labelpos='E',
                   coordinates='figure')
ax2.scatter(X[::3, ::3], Y[::3, ::3], color='r', s=5)
plt.show()
```
