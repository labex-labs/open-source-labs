# 创建负数数据图和颜色条

我们创建负数数据的图，并使用 `colorbar` 函数为该图添加颜色条。这次，我们指定颜色条的位置，以及锚点和收缩参数。

```python
# 对负数数据重复上述所有操作
# 你可以指定颜色条的位置、锚点并收缩它
neg = plt.imshow(Zneg, cmap='Reds_r', interpolation='none')
plt.colorbar(neg, location='right', anchor=(0, 0.3), shrink=0.7)
```
