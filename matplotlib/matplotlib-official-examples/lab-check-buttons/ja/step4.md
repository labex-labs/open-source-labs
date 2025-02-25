# チェックボタンの追加

次に、`CheckButtons`関数を使ってチェックボタンをプロットに追加します。プロットされた線をラベルとして渡し、各線の初期の可視性を設定します。また、チェックボタンのプロパティを調整して、プロットされた線の色に合わせます。

```python
lines_by_label = {l.get_label(): l for l in [l0, l1, l2]}
line_colors = [l.get_color() for l in lines_by_label.values()]

rax = fig.add_axes([0.05, 0.4, 0.1, 0.15])
check = CheckButtons(
    ax=rax,
    labels=lines_by_label.keys(),
    actives=[l.get_visible() for l in lines_by_label.values()],
    label_props={'color': line_colors},
    frame_props={'edgecolor': line_colors},
    check_props={'facecolor': line_colors},
)
```
