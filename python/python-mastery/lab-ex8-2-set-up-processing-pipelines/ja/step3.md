# さらに頑張ろう

ああ、もっと上手にできるはずだ。これをあなたのテーブル生成コードに組み込もう。プログラムを次のように変更します。

```python
# ticker.py
...

if __name__ == '__main__':
    from follow import follow
    import csv
    from tableformat import create_formatter, print_table

    formatter = create_formatter('text')

    lines = follow('stocklog.csv')
    rows = csv.reader(lines)
    records = (Ticker.from_row(row) for row in rows)
    negative = (rec for rec in records if rec.change < 0)
    print_table(negative, ['name','price','change'], formatter)
```

これにより、次のような出力が生成されるはずです。

          name      price     change
    ---------- ---------- ----------
             C      53.12      -0.21
           UTX      70.04      -0.19
           AXP      62.86      -0.18
           MMM      85.72      -0.22
           MCD      51.38      -0.03
           WMT      49.85      -0.23
            KO       51.6      -0.07
           AIG      71.39      -0.14
            PG      63.05      -0.02
            HD      37.76      -0.19

さあ、これはすごい！そしてとても素敵だ。

**考察**

学んだこと：様々なジェネレータ関数を作成し、それらをチェーンでつなげることで、データフローパイプラインを含む処理を行うことができる。

ジェネレータ関数に対する良いイメージとしては、レゴブロックがあります。小さな反復子パターンのコレクションを作り、様々な方法で積み重ね始めることができます。これは非常に強力なプログラミング方法になり得ます。
