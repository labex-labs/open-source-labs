# データをプロットする

`plot` 関数を使って、すべての 3 つのサブプロットにデータをプロットします。

```python
for ax in axs:
    ax.plot('date', 'adj_close', data=data)
    ax.grid(True)
    ax.set_ylabel(r'Price [\$]')
```
