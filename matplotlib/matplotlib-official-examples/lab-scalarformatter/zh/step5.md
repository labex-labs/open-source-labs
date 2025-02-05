# 配置刻度标签格式

我们将为子图配置刻度标签格式。第一个子图将使用默认设置，第二个子图将使用数学表达式的精美格式，第三个子图将不使用偏移表示法。

```python
# 子图1（默认设置）
axs[0, 0].set_title("default settings")

# 子图2（useMathText=True）
for ax in axs[:, 1]:
    ax.ticklabel_format(useMathText=True)
axs[0, 1].set_title("useMathText=True")

# 子图3（useOffset=False）
for ax in axs[:, 2]:
    ax.ticklabel_format(useOffset=False)
axs[0, 2].set_title("useOffset=False")
```
