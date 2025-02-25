# グラフを作成する

次に、`matplotlib.pyplot` の `subplots()` 関数を使って 2 つの y 軸付きのグラフを作成します。また、最初の軸の `ylim_changed` イベントを `convert_ax_c_to_celsius()` 関数に接続します。

```python
fig, ax_f = plt.subplots()
ax_c = ax_f.twinx()

ax_f.callbacks.connect("ylim_changed", convert_ax_c_to_celsius)
```
