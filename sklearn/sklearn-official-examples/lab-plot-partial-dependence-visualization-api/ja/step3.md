# 2 つのモデルの部分依存をまとめて描画する

このステップでは、同じプロット上に 2 つのモデルの部分依存曲線を描画します。

```python
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))
tree_disp.plot(ax=ax1)
ax1.set_title("Decision Tree")
mlp_disp.plot(ax=ax2, line_kw={"color": "red"})
ax2.set_title("Multi-layer Perceptron")
```

曲線を比較する別の方法は、互いの上に描画することです。ここでは、1 行 2 列の図を作成します。軸は`PartialDependenceDisplay.plot`関数にリストとして渡され、各モデルの部分依存曲線を同じ軸上に描画します。軸のリストの長さは、描画するプロットの数と等しくなければなりません。

```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 6))
tree_disp.plot(ax=[ax1, ax2], line_kw={"label": "Decision Tree"})
mlp_disp.plot(
    ax=[ax1, ax2], line_kw={"label": "Multi-layer Perceptron", "color": "red"}
)
ax1.legend()
ax2.legend()
```

`tree_disp.axes_`は、部分依存プロットを描画するために使用される軸を格納する numpy 配列です。これを`mlp_disp`に渡すことで、互いの上にプロットを描画する同じ効果を得ることができます。さらに、`mlp_disp.figure_`は図を格納しており、`plot`を呼び出した後に図のサイズを変更することができます。この場合、`tree_disp.axes_`は 2 次元であるため、`plot`は最も左のプロットにのみ y ラベルと y 目盛りを表示します。

```python
tree_disp.plot(line_kw={"label": "Decision Tree"})
mlp_disp.plot(
    line_kw={"label": "Multi-layer Perceptron", "color": "red"}, ax=tree_disp.axes_
)
tree_disp.figure_.set_size_inches(10, 6)
tree_disp.axes_[0, 0].legend()
tree_disp.axes_[0, 1].legend()
plt.show()
```
