# 创建帽形图

在这一步中，我们将使用上一步准备的数据和 `hat_graph` 函数来创建帽形图。

```python
fig, ax = plt.subplots()
hat_graph(ax, xlabels, [playerA, playerB], ['Player A', 'Player B'])

# 添加一些文本用于标签、标题和自定义 x 轴刻度标签等
ax.set_xlabel('Games')
ax.set_ylabel('Score')
ax.set_ylim(0, 60)
ax.set_title('Scores by number of game and players')
ax.legend()

fig.tight_layout()
plt.show()
```
