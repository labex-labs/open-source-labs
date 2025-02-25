# 1つ以上の凡例キーを持つ凡例エントリを作成する

このステップでは、1つ以上の凡例キーを持つ凡例エントリを作成します。

```python
# グラフ用のデータを定義
fig, (ax1, ax2) = plt.subplots(2, 1, layout='constrained')
p1 = ax1.scatter([1], [5], c='r', marker='s', s=100)
p2 = ax1.scatter([3], [2], c='b', marker='o', s=100)
p3, = ax1.plot([1, 5], [4, 4],'m-d')

# 1つのエントリに2つのキーを持つ凡例を作成
l = ax1.legend([(p1, p3), p2], ['2つのキー', '1つのキー'], scatterpoints=1,
               numpoints=1, handler_map={tuple: HandlerTuple(ndivide=None)})

# 重ねて2つの棒グラフを作成し、凡例キー間のパディングを変更する
x_left = [1, 2, 3]
y_pos = [1, 3, 2]
y_neg = [2, 1, 4]
rneg = ax2.bar(x_left, y_neg, width=0.5, color='w', hatch='///', label='-1')
rpos = ax2.bar(x_left, y_pos, width=0.5, color='k', label='+1')

# 特定の`HandlerTuple`を使用して各凡例エントリを異なる方法で扱う
l = ax2.legend([(rpos, rneg), (rneg, rpos)], ['pad!=0', 'pad=0'],
               handler_map={(rpos, rneg): HandlerTuple(ndivide=None),
                            (rneg, rpos): HandlerTuple(ndivide=None, pad=0.)})

# グラフを表示
plt.show()
```
