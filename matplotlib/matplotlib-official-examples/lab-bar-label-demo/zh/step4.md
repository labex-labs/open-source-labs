# 高级柱状图标注

在这一步中，我们将展示一些使用柱状图标签可以实现的更高级的操作。我们将使用与上一步相同的水平柱状图。

```python
fig, ax = plt.subplots()

hbars = ax.barh(y_pos, performance, xerr=error, align='center')
ax.set_yticks(y_pos, labels=people)
ax.invert_yaxis()  # 标签从上到下读取
ax.set_xlabel('性能')
ax.set_title('你今天想多快到达？')

# 使用给定的标题、自定义填充和注释选项进行标注
ax.bar_label(hbars, labels=[f'±{e:.2f}' for e in error],
             padding=8, color='b', fontsize=14)
ax.set_xlim(right=16)

plt.show()
```
