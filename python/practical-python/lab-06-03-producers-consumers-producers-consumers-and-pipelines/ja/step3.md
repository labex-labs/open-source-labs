# 演習 6.8: 単純なパイプラインの設定

パイプラインの考え方を実際に見てみましょう。次の関数を書きましょう。

```python
>>> def filematch(lines, substr):
        for line in lines:
            if substr in line:
                yield line

>>>
```

この関数は、前の演習の最初のジェネレータの例とほぼ同じですが、もはやファイルを開いていません。引数として与えられた行のシーケンスのみを操作します。では、これを試してみましょう。

```python
>>> from follow import follow
>>> lines = follow('stocklog.csv')
>>> goog = filematch(lines, 'GOOG')
>>> for line in goog:
        print(line)

... 出力が表示されるのを待つ...
```

出力が表示されるまでに少し時間がかかる場合がありますが、最終的には GOOG に関するデータを含むいくつかの行が表示されるはずです。

注：これらの演習は、2 つの別々のターミナルで同時に行う必要があります。
