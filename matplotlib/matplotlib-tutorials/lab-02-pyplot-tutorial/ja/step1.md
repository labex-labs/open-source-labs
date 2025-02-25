# 単純なグラフの生成

まずは、`pyplot` の `plot` 関数を使って単純なグラフを生成しましょう。この例では、y 値が `[1, 2, 3, 4]` の折れ線グラフを描画します。

```python
import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()
```

解説:

- `matplotlib` から `pyplot` モジュールをインポートし、`plt` というエイリアスで参照できるようにします。
- `plot` 関数は折れ線グラフを生成するために使用されます。y 値の単一のリストを提供することで、x 値は自動的に `[0, 1, 2, 3]` と生成されます。なぜなら、Python の範囲は 0 から始まるためです。
- `ylabel` 関数は y 軸のラベルを設定します。
- 最後に、`show` 関数がグラフを表示します。
