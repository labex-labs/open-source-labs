# hatches_plot 関数を作成する

hatches_plot 関数は、指定されたハッチパターンで長方形を作成し、それを軸に追加します。また、ハッチパターンを含むテキストも追加します。

```python
def hatches_plot(ax, h):
    ax.add_patch(Rectangle((0, 0), 2, 2, fill=False, hatch=h))
    ax.text(1, -0.5, f"' {h} '", size=15, ha="center")
    ax.axis('equal')
    ax.axis('off')
```
