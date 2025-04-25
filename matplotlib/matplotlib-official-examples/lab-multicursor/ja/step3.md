# プロットの作成

次に、`plt.subplots` 関数を使って 3 つのサブプロットを作成します。2 つのプロットは 1 つのグラフに作成し、3 つ目のプロットは別のグラフに作成します。

```python
fig, (ax1, ax2) = plt.subplots(2, sharex=True)
ax1.plot(t, s1)
ax2.plot(t, s2)
fig, ax3 = plt.subplots()
ax3.plot(t, s3)
```
