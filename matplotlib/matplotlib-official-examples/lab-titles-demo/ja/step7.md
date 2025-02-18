# RCParam を使用した Y 軸位置の設定

`rcParams` の `titley` と `titlepad` パラメータを設定して、タイトルの垂直位置を調整します。

```python
fig, ax = plt.subplots()
ax.plot(range(10))
ax.xaxis.set_label_position('top')
ax.set_xlabel('X-label')
plt.rcParams['axes.titley'] = 1.0
plt.rcParams['axes.titlepad'] = -14
ax.set_title('RCParam Y Positioning')
```
