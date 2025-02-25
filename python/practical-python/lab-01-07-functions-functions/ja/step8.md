# 演習1.31：エラー処理

欠落したフィールドがあるファイルに対して関数を試した場合、何が起こりますか？

```python
>>> portfolio_cost('missing.csv')
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "pcost.py", line 11, in portfolio_cost
    nshares    = int(fields[1])
ValueError: invalid literal for int() with base 10: ''
>>>
```

この時点で、あなたは選択を迫られます。プログラムを動作させるには、不良な行を削除することで元の入力ファイルをクリーンアップするか、またはコードを修正して不良な行を何らかの方法で処理することができます。

`pcost.py` プログラムを修正して、例外をキャッチし、警告メッセージを表示し、その後ファイルの残りの部分を処理し続けるようにしましょう。
