# プロットを作成する

このステップでは、前のステップで作成したマスク配列を使ってプロットを作成します。それぞれのマスク配列を個別にプロットし、それぞれに異なる色を使います。

```python
fig, ax = plt.subplots()
ax.plot(t, smiddle, t, slower, t, supper)
plt.show()
```
