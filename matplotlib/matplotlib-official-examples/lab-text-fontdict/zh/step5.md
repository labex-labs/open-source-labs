# 向绘图添加文本

我们可以使用text()函数向绘图添加文本。在这个例子中，我们将使用字体字典来定制样式，向绘图添加一个LaTeX表达式。

```python
plt.text(2, 0.65, r'$\cos(2 \pi t) \exp(-t)$', fontdict=font)
```
