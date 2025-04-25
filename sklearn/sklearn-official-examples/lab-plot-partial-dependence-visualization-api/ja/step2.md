# 2 つの特徴量に対する部分依存の描画

このステップでは、決定木に対する「年齢」と「BMI」（身体質量指数）の特徴量に対する部分依存曲線を描画します。2 つの特徴量の場合、`PartialDependenceDisplay.from_estimator`は 2 つの曲線を描画することを期待しています。ここでは、描画関数が`ax`によって定義された空間を使って 2 つのプロットのグリッドを配置します。

```python
fig, ax = plt.subplots(figsize=(12, 6))
ax.set_title("Decision Tree")
tree_disp = PartialDependenceDisplay.from_estimator(tree, X, ["age", "bmi"], ax=ax)
```

多層パーセプトロンに対しても部分依存曲線を描画することができます。この場合、曲線の色を変更するために`line_kw`が`PartialDependenceDisplay.from_estimator`に渡されます。

```python
fig, ax = plt.subplots(figsize=(12, 6))
ax.set_title("Multi-layer Perceptron")
mlp_disp = PartialDependenceDisplay.from_estimator(
    mlp, X, ["age", "bmi"], ax=ax, line_kw={"color": "red"}
)
```
