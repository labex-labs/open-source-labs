# グラフを作成する

`subplots`関数を使って2x2のサブプロットのグリッドを作成します。その後、`plot`関数を使って各サブプロットにデータをプロットします。

```python
fig, axs = plt.subplots(2, 2, layout='constrained')

axs[0, 0].plot(cms, cms)

axs[0, 1].plot(cms, cms, xunits=cm, yunits=inch)

axs[1, 0].plot(cms, cms, xunits=inch, yunits=cm)
axs[1, 0].set_xlim(-1, 4)  # スカラーは現在の単位で解釈されます

axs[1, 1].plot(cms, cms, xunits=inch, yunits=inch)
axs[1, 1].set_xlim(3*cm, 6*cm)  # cmはインチに変換されます
```
