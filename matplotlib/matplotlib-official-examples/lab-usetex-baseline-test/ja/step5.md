# グラフの範囲とラベルを設定する

望ましい出力に合わせて、グラフの範囲とラベルを設定します。

```python
for ax in axs:
    ax.set(xlim=(-0.1, 1.1), ylim=(-.8, 3.9), xticks=[], yticks=[])
    ax.set_title(f"usetex={ax.usetex}\n")
```
