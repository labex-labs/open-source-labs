# 1つの特徴量に対する部分依存の描画

このステップでは、同じ軸上に単一の特徴量「年齢」に対する部分依存曲線を描画します。この場合、`tree_disp.axes_`が2番目の描画関数に渡されます。

```python
tree_disp = PartialDependenceDisplay.from_estimator(tree, X, ["age"])
mlp_disp = PartialDependenceDisplay.from_estimator(
    mlp, X, ["age"], ax=tree_disp.axes_, line_kw={"color": "red"}
)
```
