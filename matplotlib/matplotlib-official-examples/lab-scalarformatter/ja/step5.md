# 目盛りラベルの書式設定を構成する

サブプロットの目盛りラベルの書式設定を構成します。最初のサブプロットはデフォルト設定を使用し、2 番目のサブプロットは数学的な式の見栄えの良い書式設定を使用し、3 番目のサブプロットはオフセット表記を使用しません。

```python
# Subplot 1 (default settings)
axs[0, 0].set_title("default settings")

# Subplot 2 (useMathText=True)
for ax in axs[:, 1]:
    ax.ticklabel_format(useMathText=True)
axs[0, 1].set_title("useMathText=True")

# Subplot 3 (useOffset=False)
for ax in axs[:, 2]:
    ax.ticklabel_format(useOffset=False)
axs[0, 2].set_title("useOffset=False")
```
