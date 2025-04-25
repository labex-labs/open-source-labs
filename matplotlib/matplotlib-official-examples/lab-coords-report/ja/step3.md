# プロットの作成

データが用意できたので、Matplotlib を使ってプロットを作成します。この例では、plot() 関数を使って散布図を作成します。

```python
fig, ax = plt.subplots()
plt.plot(x, y, 'o')
```
