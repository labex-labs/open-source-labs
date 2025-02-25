# タイトルの設定

このステップでは、各プロットのタイトルを設定する必要があります。

```python
axs[0, 0].set_title('Linear normalization')

for ax, gamma in zip(axs.flat[1:], gammas):
    ax.set_title(r'Power law $(\gamma=%1.1f)$' % gamma)
```
