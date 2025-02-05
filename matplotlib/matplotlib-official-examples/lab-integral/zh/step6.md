# 添加积分标签

使用 `text` 向绘图添加积分标签。该标签应位于 a 和 b 之间中点处，并使用数学文本进行格式化。

```python
ax.text(0.5 * (a + b), 30, r"$\int_a^b f(x)\mathrm{d}x$",
        horizontalalignment='center', fontsize=20)
```
