# ボックスプロットの統計量をカスタマイズする

手順 2 で計算されたボックスプロットの統計量のいずれかを変更することができます。この例では、各セットの中央値をすべてのデータの中央値に設定し、平均を 2 倍にします。

```python
for n in range(len(stats)):
    stats[n]['med'] = np.median(data)
    stats[n]['mean'] *= 2
```
