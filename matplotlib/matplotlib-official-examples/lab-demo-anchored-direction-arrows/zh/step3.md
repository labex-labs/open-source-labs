# 创建一个简单箭头

现在，我们将使用`AnchoredDirectionArrows`类创建一个简单的带锚定方向箭头。这个箭头将在绘图中指示 X 和 Y 方向。

```python
# 简单示例
simple_arrow = AnchoredDirectionArrows(ax.transAxes, 'X', 'Y')
ax.add_artist(simple_arrow)
```
