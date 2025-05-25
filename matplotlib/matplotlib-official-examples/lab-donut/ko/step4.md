# 도넛 생성

내부 및 외부 하위 경로를 연결하여 도넛을 생성합니다. 각 정점의 유형 (MOVETO, LINETO 등) 을 지정하기 위해 `codes`를 사용합니다. 그런 다음 `mpath.Path`를 사용하여 `Path` 객체를 생성하고 `mpatches.PathPatch`를 사용하여 `PathPatch` 객체를 생성합니다. 마지막으로 `ax.add_patch()`를 사용하여 `PathPatch` 객체를 `Axes` 객체에 추가합니다.

```python
Path = mpath.Path
fig, ax = plt.subplots()

inside_vertices = make_circle(0.5)
outside_vertices = make_circle(1.0)
codes = np.ones(
    len(inside_vertices), dtype=mpath.Path.code_type) * mpath.Path.LINETO
codes[0] = mpath.Path.MOVETO

for i, (inside, outside) in enumerate(((1, 1), (1, -1), (-1, 1), (-1, -1))):
    # Concatenate the inside and outside subpaths together, changing their
    # order as needed
    vertices = np.concatenate((outside_vertices[::outside],
                               inside_vertices[::inside]))
    # Shift the path
    vertices[:, 0] += i * 2.5
    # The codes will be all "LINETO" commands, except for "MOVETO"s at the
    # beginning of each subpath
    all_codes = np.concatenate((codes, codes))
    # Create the Path object
    path = mpath.Path(vertices, all_codes)
    # Add plot it
    patch = mpatches.PathPatch(path, facecolor='#885500', edgecolor='black')
    ax.add_patch(patch)

    ax.annotate(f"Outside {wise(outside)},\nInside {wise(inside)}",
                (i * 2.5, -1.5), va="top", ha="center")

ax.set_xlim(-2, 10)
ax.set_ylim(-3, 2)
ax.set_title('Mmm, donuts!')
ax.set_aspect(1.0)
plt.show()
```
