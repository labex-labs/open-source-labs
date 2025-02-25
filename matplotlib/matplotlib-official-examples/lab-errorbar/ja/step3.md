# グラフを描画する

これでサンプルデータが用意できたので、`errorbar()` 関数を使ってグラフを描画できます。最初の 2 つのパラメータとして `x` と `y` の配列を渡します。その後、`xerr` と `yerr` パラメータをそれぞれ使って、x 方向の誤差を 0.2、y 方向の誤差を 0.4 と指定します。

```python
fig, ax = plt.subplots()
ax.errorbar(x, y, xerr=0.2, yerr=0.4)
plt.show()
```
