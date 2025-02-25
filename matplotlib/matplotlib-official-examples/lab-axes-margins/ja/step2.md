# 固定エッジ

Matplotlibの一部のプロット作成関数は、軸の制限を「固定」させるか、`margins()`メソッドに対して免疫にすることができます。たとえば、`imshow()`と`pcolor()`は、ユーザーがプロットに表示されるピクセルの周りの制限を厳密にすることを望んでいると想定しています。この動作が望ましくない場合は、`use_sticky_edges`を`False`に設定する必要があります。このステップでは、Matplotlibの固定エッジを回避する方法を学びます。

```python
# グリッドを作成
y, x = np.mgrid[:5, 1:6]

# ポリゴンの座標を定義
poly_coords = [
    (0.25, 2.75), (3.25, 2.75),
    (2.25, 0.75), (0.25, 0.75)
]

# サブプロットを作成
fig, (ax1, ax2) = plt.subplots(ncols=2)

# ax1で固定エッジを使用し、ax2で固定エッジをオフにする
ax2.use_sticky_edges = False

# 両方のサブプロットにプロットする
for ax, status in zip((ax1, ax2), ('Is', 'Is Not')):
    cells = ax.pcolor(x, y, x+y, cmap='inferno', shading='auto') # 固定
    ax.add_patch(
        Polygon(poly_coords, color='forestgreen', alpha=0.5)
    ) # 固定ではない
    ax.margins(x=0.1, y=0.05)
    ax.set_aspect('equal')
    ax.set_title(f'{status} Sticky')

plt.show()
```
