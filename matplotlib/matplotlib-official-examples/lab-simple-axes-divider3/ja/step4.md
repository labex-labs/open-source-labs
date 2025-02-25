# 軸の範囲と外観をカスタマイズする

`set_xlim`、`set_ylim`、および `tick_params` メソッドを使って、各軸の範囲と外観をカスタマイズします。

```python
ax[0].set_xlim(0, 2)
ax[1].set_xlim(0, 1)
ax[0].set_ylim(0, 1)
ax[2].set_ylim(0, 2)
for ax1 in ax:
    ax1.tick_params(labelbottom=False, labelleft=False)
```
