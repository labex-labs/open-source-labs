# 使用美元符号格式化y轴标签

现在，让我们将y轴标签格式化为显示美元符号。我们将使用 `matplotlib.ticker` 模块中的 `StrMethodFormatter` 类来格式化标签。

```python
import matplotlib.ticker as ticker

# 使用美元符号格式化y轴标签
fmt = '${x:,.2f}'
tick = ticker.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick)
```

在上述代码中，我们使用格式字符串 `'$ {x:,.2f}'` 创建了一个 `StrMethodFormatter` 对象。这个格式字符串指定我们想要一个美元符号，后面跟着一个空格，再后面跟着一个带两位小数的逗号分隔数字。

接下来，我们使用刚刚创建的 `StrMethodFormatter` 对象创建一个 `Tick` 对象。最后，我们将y轴主格式化器设置为 `Tick` 对象。
