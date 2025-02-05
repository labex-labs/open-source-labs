# 自定义图例

我们可以通过更改图例的位置、字体大小和其他参数来自定义它。要更改图例的位置，我们使用 `loc` 参数。我们还可以使用 `fontsize` 参数来更改字体大小。

```python
plt.legend(labels=['sin(2pix)', 'sin(4pix)'], loc='lower right', fontsize='large')
```
