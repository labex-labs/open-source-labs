# 创建甜甜圈

我们将通过把内部和外部子路径连接在一起来创建甜甜圈。我们将使用 `codes` 来指定每个顶点的类型（如 MOVETO、LINETO 等）。然后，我们将使用 `mpath.Path` 创建一个 `Path` 对象，并使用 `mpatches.PathPatch` 创建一个 `PathPatch` 对象。最后，我们将使用 `ax.add_patch()` 把 `PathPatch` 对象添加到 `Axes` 对象中。

```python
Path = mpath.Path
fig, ax = plt.subplots()

inside_vertices = make_circle(0.5)
outside_vertices = make_circle(1.0)
codes = np.ones(
    len(inside_vertices), dtype=mpath.Path.code_type) * mpath.Path.LINETO
codes[0] = mpath.Path.MOVETO

for i, (inside, outside) in enumerate(((1, 1), (1, -1), (-1, 1), (-1, -1))):
    # 把内部和外部子路径连接在一起，根据需要改变它们的顺序
    vertices = np.concatenate((outside_vertices[::outside],
                               inside_vertices[::inside]))
    # 移动路径
    vertices[:, 0] += i * 2.5
    # 除了每个子路径开头的 "MOVETO" 命令外，所有代码都将是 "LINETO" 命令
    all_codes = np.concatenate((codes, codes))
    # 创建 Path 对象
    path = mpath.Path(vertices, all_codes)
    # 添加并绘制它
    patch = mpatches.PathPatch(path, facecolor='#885500', edgecolor='black')
    ax.add_patch(patch)

    ax.annotate(f"外部 {wise(outside)},\n内部 {wise(inside)}",
                (i * 2.5, -1.5), va="top", ha="center")

ax.set_xlim(-2, 10)
ax.set_ylim(-3, 2)
ax.set_title('Mmm, 甜甜圈!')
ax.set_aspect(1.0)
plt.show()
```
