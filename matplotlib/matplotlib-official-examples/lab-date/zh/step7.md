# 手动设置刻度标签格式

我们将使用 `DateFormatter` 手动设置第三个子图上的刻度标签格式，以便使用 `datetime.date.strftime` 中记录的格式字符串来格式化日期。

```python
ax = axs[2]
ax.set_title('Manual DateFormatter', loc='left', y=0.85, x=0.02, fontsize='medium')
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%b'))
for label in ax.get_xticklabels(which='major'):
    label.set(rotation=30, horizontalalignment='right')
```
