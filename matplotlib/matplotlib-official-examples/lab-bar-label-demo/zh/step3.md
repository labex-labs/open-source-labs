# 水平柱状图标注

接下来，我们将创建一个水平柱状图，并使用`bar_label`函数为其添加标注。我们将使用上一步中的数据，但这次我们将为每个人生成一些随机的性能数据。

```python
人员 = ('汤姆', '迪克', '哈里', '斯利姆', '吉姆')
y_pos = np.arange(len(人员))
性能 = 3 + 10 * np.random.rand(len(人员))
误差 = np.random.rand(len(人员))

fig, ax = plt.subplots()

水平柱状图 = ax.barh(y_pos, 性能, xerr=误差, align='center')
ax.set_yticks(y_pos, labels=人员)
ax.invert_yaxis()  # 标签从上到下读取
ax.set_xlabel('性能')
ax.set_title('你今天想多快到达？')

# 用特殊格式的浮点数标注
ax.bar_label(水平柱状图, fmt='%.2f')
ax.set_xlim(right=15)  # 调整xlim以适应标签

plt.show()
```
