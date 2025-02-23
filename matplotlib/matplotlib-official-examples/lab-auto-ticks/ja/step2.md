# round_numbers オートリミットモード付きの散布図

このステップでは、`axes.autolimit_mode` を 'round_numbers' に切り替え、目盛りを丸い数に維持し且つ端にも目盛りを表示するように散布図を作成します。

```python
plt.rcParams['axes.autolimit_mode'] = 'round_numbers'

fig, ax = plt.subplots()
ax.scatter(x, y, c=x+y)
plt.show()
```
