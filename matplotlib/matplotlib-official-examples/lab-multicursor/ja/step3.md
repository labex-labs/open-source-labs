# プロットの作成

次に、`plt.subplots` 関数を使って3つのサブプロットを作成します。2つのプロットは1つのグラフに作成し、3つ目のプロットは別のグラフに作成します。

```python
fig, (ax1, ax2) = plt.subplots(2, sharex=True)
ax1.plot(t, s1)
ax2.plot(t, s2)
fig, ax3 = plt.subplots()
ax3.plot(t, s3)
```
