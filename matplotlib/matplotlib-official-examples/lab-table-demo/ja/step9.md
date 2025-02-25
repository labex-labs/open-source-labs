# 軸ラベルとタイトルを追加する

`plt.ylabel`、`plt.yticks`、`plt.xticks`、および`plt.title`関数を使って、グラフに軸ラベルとタイトルを追加します。

```python
values = np.arange(0, 2500, 500)
value_increment = 1000

plt.ylabel(f"Loss in ${value_increment}'s")
plt.yticks(values * value_increment, ['%d' % val for val in values])
plt.xticks([])
plt.title('Loss by Disaster')
```
