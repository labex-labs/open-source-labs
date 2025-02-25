# 異なる要素の表示を切り替える

`bxp()` 関数の様々なパラメータを使用して、ボックスプロットの異なる要素の表示を切り替えることができます。この例では、平均値、ボックス、キャップ、ノッチ、および外れ値の表示を表示するか非表示にする方法を示します。

```python
# Toggle the display of different elements
plt.bxp(stats, showmeans=True, showbox=False, showcaps=False, shownotches=True, showfliers=False)
plt.show()
```
