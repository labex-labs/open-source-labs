# 右側にデフォルトのy軸目盛りラベルを設定する

次のコードを使用して、グラフの右側にデフォルトのy軸目盛りラベルを設定できます。

```python
plt.rcParams['ytick.right'] = plt.rcParams['ytick.labelright'] = True
plt.rcParams['ytick.left'] = plt.rcParams['ytick.labelleft'] = False
```
