# プロットを作成する

次に、`matplotlib.pyplot`を使ってプロットを作成します。正弦波をプロットし、y = 0に水平線を追加します。

```python
fig, ax = plt.subplots()

ax.plot(t, s, color='black')
ax.axhline(0, color='black')
```
