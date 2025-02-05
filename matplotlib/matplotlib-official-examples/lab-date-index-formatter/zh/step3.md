# 创建自定义索引格式化器

为了根据从0、1、...、数据长度的索引来绘制数据，我们将创建一个自定义索引格式化器。这个格式化器会将刻度标记格式化为时间，而不是整数。

```python
# 创建自定义索引格式化器
fig, ax2 = plt.subplots(figsize=(6, 3))
ax2.plot(r.adj_close, 'o-')

# 将x轴格式化为时间
def format_date(x, _):
    try:
        # 将datetime64转换为datetime，并使用datetime的strftime：
        return r.date[round(x)].item().strftime('%a')
    except IndexError:
        pass

ax2.set_title("Creating Custom Index Formatter")
ax2.xaxis.set_major_formatter(format_date)  # 内部创建FuncFormatter
```
