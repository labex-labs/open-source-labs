# プロットを作成する

次に、Matplotlib の`subplots()`関数を使ってプロットを作成し、Google の株価の調整後終値を時間の経過とともにプロットします。

```python
fig, ax = plt.subplots()
ax.plot(r.date, r.adj_close)
```
