# ヒストグラムのスタイルを変更する

`hist`関数の`histtype`パラメータを指定することで、ヒストグラムのスタイルを変更できます。この例では、色の塗りつぶしがあるステップ曲線のヒストグラムを作成します。

```python
plt.hist(x, bins=20, density=True, histtype='stepfilled', facecolor='g', alpha=0.75)
plt.show()
```
