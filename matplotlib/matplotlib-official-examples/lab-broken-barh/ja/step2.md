# 破線の水平棒グラフを作成する

このステップでは、破線の水平棒グラフを作成します。グラフを作成するために、`Axes` クラスの `broken_barh()` メソッドを使用します。`broken_barh()` メソッドは 3 つの引数を取ります。最初の引数はタプルのリストで、各タプルは棒グラフのセグメントを表し、タプルの最初の要素はセグメントの開始点、2 番目の要素はセグメントの長さです。2 番目の引数は棒グラフの y 座標です。3 番目の引数は棒グラフの塗りつぶし色です。

```python
fig, ax = plt.subplots()
ax.broken_barh([(110, 30), (150, 10)], (10, 9), facecolors='tab:blue')
ax.broken_barh([(10, 50), (100, 20), (130, 10)], (20, 9),
               facecolors=('tab:orange', 'tab:green', 'tab:red'))
ax.set_ylim(5, 35)
ax.set_xlim(0, 200)
ax.set_xlabel('seconds since start')
ax.set_yticks([15, 25], labels=['Bill', 'Jim'])
ax.grid(True)
ax.annotate('race interrupted', (61, 25),
            xytext=(0.8, 0.9), textcoords='axes fraction',
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=16,
            horizontalalignment='right', verticalalignment='top')

plt.show()
```
