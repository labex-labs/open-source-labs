# 演習 2.25: 辞書の作成

キー名と値のシーケンスがある場合、`dict()` 関数が簡単に辞書を作成できることを覚えていますか？列ヘッダーから辞書を作成してみましょう。

```python
>>> headers
['name','shares', 'price']
>>> converted
['AA', 100, 32.2]
>>> dict(zip(headers, converted))
{'price': 32.2, 'name': 'AA','shares': 100}
>>>
```

もちろん、あなたがリスト内包表記に精通しているなら、辞書内包表記を使って 1 ステップで全体の変換を行うことができます。

```python
>>> { name: func(val) for name, func, val in zip(headers, types, row) }
{'price': 32.2, 'name': 'AA','shares': 100}
>>>
```
