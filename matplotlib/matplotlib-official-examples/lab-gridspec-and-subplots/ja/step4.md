# 元の Axes を削除する

次のステップで作成する大きな Axes に覆われる元の Axes を削除します。

```python
for ax in axs[1:, -1]:
    ax.remove()
```
