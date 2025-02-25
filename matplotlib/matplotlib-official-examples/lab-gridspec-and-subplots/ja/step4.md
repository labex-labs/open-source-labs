# 元のAxesを削除する

次のステップで作成する大きなAxesに覆われる元のAxesを削除します。

```python
for ax in axs[1:, -1]:
    ax.remove()
```
