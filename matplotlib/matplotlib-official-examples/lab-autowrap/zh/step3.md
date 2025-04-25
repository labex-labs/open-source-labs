# 自动换行文本

现在，让我们来探索如何在 Matplotlib 中自动换行文本。将你代码中的`plt.text()`行替换为以下内容：

```python
t = ("This is a really long string that I'd rather have wrapped so that it "
     "doesn't go outside of the figure, but if it's long enough it will go "
     "off the top or bottom!")
plt.text(5, 5, t, ha='center', wrap=True)
```

`wrap=True`参数告诉 Matplotlib 自动换行文本。
