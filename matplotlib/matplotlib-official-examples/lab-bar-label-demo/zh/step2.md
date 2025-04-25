# 垂直柱状图标注

我们将首先创建一个垂直柱状图，并使用`bar_label`函数为其添加标注。我们使用的数据是按性别统计的企鹅数量，数据来自 https://allisonhorst.github.io/palmerpenguins/ 。

```python
species = ('阿德利企鹅', '帽带企鹅', '巴布亚企鹅')
性别数量 = {
    '雄性': np.array([73, 34, 61]),
    '雌性': np.array([73, 34, 58]),
}
宽度 = 0.6  # 柱状图的宽度：也可以是 x 的长度序列

fig, ax = plt.subplots()
底部 = np.zeros(3)

for 性别, 性别数量 in 性别数量.items():
    p = ax.bar(物种, 性别数量, 宽度, label=性别, bottom=底部)
    底部 += 性别数量

    ax.bar_label(p, label_type='center')

ax.set_title('按性别统计的企鹅数量')
ax.legend()

plt.show()
```

注：原文中 species 翻译为“物种”更合适，这里为了和代码中的变量名对应，翻译为“物种”，实际在文档语境中理解为“企鹅种类”更准确。你可根据实际需求调整。
