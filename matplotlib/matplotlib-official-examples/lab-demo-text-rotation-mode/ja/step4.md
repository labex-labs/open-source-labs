# サブプロットを作成する

ここでは、`subplots` 関数を使ってサブプロットを作成します。同じアスペクト比のサブプロットのグリッドを作成し、x 軸と y 軸の目盛りを削除します。また、各サブプロットの中央に垂直と水平の線を追加して配置を視覚化しやすくします。

```python
axs = fig.subplots(len(va_list), len(ha_list), sharex=True, sharey=True,
                   subplot_kw=dict(aspect=1),
                   gridspec_kw=dict(hspace=0, wspace=0))

for i, va in enumerate(va_list):
    for j, ha in enumerate(ha_list):
        ax = axs[i, j]
        ax.set(xticks=[], yticks=[])
        ax.axvline(0.5, color="skyblue", zorder=0)
        ax.axhline(0.5, color="skyblue", zorder=0)
        ax.plot(0.5, 0.5, color="C0", marker="o", zorder=1)
```
