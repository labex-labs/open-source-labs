# サンプルグラフを作成する

y 軸目盛りラベルが右側にある場合のグラフの見た目を確認するために、サンプルグラフを作成しましょう。

```python
x = np.arange(10)

fig, (ax0, ax1) = plt.subplots(2, 1, sharex=True, figsize=(6, 6))

ax0.plot(x)
ax0.yaxis.tick_left()

ax1.plot(x)

plt.show()
```
