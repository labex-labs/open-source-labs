# グラフの作成

これでグラフを作成する準備が整いました。Matplotlib の`plot`関数を使って、同じグラフに 3 つの線を描画し、それぞれ事前定義されたラベルを付けます。各線にラベルを割り当てるために`label`パラメータを使用します。

```python
# Create plots with pre-defined labels.
fig, ax = plt.subplots()
ax.plot(a, c, 'k--', label='Model length')
ax.plot(a, d, 'k:', label='Data length')
ax.plot(a, c + d, 'k', label='Total message length')
```
