# ドーナツの作成

内側と外側のサブパスを連結してドーナツを作成します。各頂点の種類（MOVETO、LINETOなど）を指定するために`codes`を使用します。その後、`mpath.Path`を使って`Path`オブジェクトを作成し、`mpatches.PathPatch`を使って`PathPatch`オブジェクトを作成します。最後に、`ax.add_patch()`を使って`PathPatch`オブジェクトを`Axes`オブジェクトに追加します。

```python
Path = mpath.Path
fig, ax = plt.subplots()

inside_vertices = make_circle(0.5)
outside_vertices = make_circle(1.0)
codes = np.ones(
    len(inside_vertices), dtype=mpath.Path.code_type) * mpath.Path.LINETO
codes[0] = mpath.Path.MOVETO

for i, (inside, outside) in enumerate(((1, 1), (1, -1), (-1, 1), (-1, -1))):
    # 内側と外側のサブパスを連結し、必要に応じてそれらの順序を変更します
    vertices = np.concatenate((outside_vertices[::outside],
                               inside_vertices[::inside]))
    # パスをシフトします
    vertices[:, 0] += i * 2.5
    # コードは、各サブパスの先頭の "MOVETO" 以外はすべて "LINETO" コマンドになります
    all_codes = np.concatenate((codes, codes))
    # Pathオブジェクトを作成します
    path = mpath.Path(vertices, all_codes)
    # プロットして追加します
    patch = mpatches.PathPatch(path, facecolor='#885500', edgecolor='black')
    ax.add_patch(patch)

    ax.annotate(f"外側 {wise(outside)},\n内側 {wise(inside)}",
                (i * 2.5, -1.5), va="top", ha="center")

ax.set_xlim(-2, 10)
ax.set_ylim(-3, 2)
ax.set_title('Mmm, ドーナツ！')
ax.set_aspect(1.0)
plt.show()
```
