# 将颜色映射到值

我们还可以使用`ScalarMappable.set_array`函数将一组值数组映射到颜色。我们将创建一组新的数据，并创建一个新的`LineCollection`对象，将`array`参数设置为`x`值。然后，我们可以使用`Figure`对象的`colorbar`方法为绘图添加一个颜色条。

```python
N = 50
x = np.arange(N)
ys = [x + i for i in x]
segs = [np.column_stack([x, y]) for y in ys]

fig, ax = plt.subplots()
ax.set_xlim(np.min(x), np.max(x))
ax.set_ylim(np.min(ys), np.max(ys))

line_segments = LineCollection(segs, array=x,
                               linewidths=(0.5, 1, 1.5, 2),
                               linestyles='solid')
ax.add_collection(line_segments)
axcb = fig.colorbar(line_segments)
axcb.set_label('Line Number')
ax.set_title('Line Collection with mapped colors')
plt.sci(line_segments)
plt.show()
```
