# データのプロット

これで、`plot` 関数を使ってデータをプロットできます。手順 3 で作成したデータを使って、2 つの線を作成します。

```python
ax.plot(theta, r, color="tab:orange", lw=3, label="a line")
ax.plot(0.5 * theta, r, color="tab:blue", ls="--", lw=3, label="another line")
```
