# 軸を移動する

デフォルトでは、軸 (spine) はグラフの端に描画されます。この場合、左と下の軸をグラフの中心に移動させます。

```python
ax.spines[["left", "bottom"]].set_position(("data", 0))
```
