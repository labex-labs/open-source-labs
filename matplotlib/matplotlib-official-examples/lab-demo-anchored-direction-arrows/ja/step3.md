# 簡単な矢印を作成する

次に、`AnchoredDirectionArrows` クラスを使って簡単な固定方向矢印を作成します。この矢印は、プロット内の X 方向と Y 方向を示します。

```python
# Simple example
simple_arrow = AnchoredDirectionArrows(ax.transAxes, 'X', 'Y')
ax.add_artist(simple_arrow)
```
