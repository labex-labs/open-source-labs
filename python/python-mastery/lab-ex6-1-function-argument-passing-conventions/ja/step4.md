# 属性名の制限

現在、私たちの `Structure` クラスは、そのインスタンスに任意の属性を設定できるようになっています。初心者にとっては、これは最初は便利に見えるかもしれませんが、実際には多くの問題を引き起こす可能性があります。クラスを使用する際には、特定の属性が存在し、特定の方法で使用されることを期待します。ユーザーが属性名を誤って入力したり、元の設計に含まれていない属性を設定しようとしたりすると、見つけにくいエラーが発生する可能性があります。

## 属性制限の必要性

属性名を制限する必要がある理由を理解するために、簡単なシナリオを見てみましょう。以下のコードを考えてみます。

```python
s = Stock('GOOG', 100, 490.1)
s.shares = 50      # Correct attribute name
s.share = 60       # Typo in attribute name - creates a new attribute instead of updating
```

2 行目では、タイプミスがあります。`shares` の代わりに `share` と書いています。Python では、エラーを発生させる代わりに、`share` という新しい属性を作成します。これは、`shares` 属性を更新していると思っているのに、実際には新しい属性を作成しているため、微妙なバグを引き起こす可能性があります。これにより、コードが予期せぬ動作をし、デバッグが非常に困難になる可能性があります。

## 属性制限の実装

この問題を解決するために、`__setattr__` メソッドをオーバーライドすることができます。このメソッドは、オブジェクトに属性を設定しようとするたびに呼び出されます。これをオーバーライドすることで、どの属性を設定できるか、できないかを制御することができます。

`structure.py` の `Structure` クラスを以下のコードで更新します。

```python
def __setattr__(self, name, value):
    """
    Restrict attribute setting to only those defined in _fields
    or attributes starting with underscore (private attributes).
    """
    if name.startswith('_'):
        # Allow setting private attributes (starting with '_')
        super().__setattr__(name, value)
    elif name in self._fields:
        # Allow setting attributes defined in _fields
        super().__setattr__(name, value)
    else:
        # Raise an error for other attributes
        raise AttributeError(f'No attribute {name}')
```

このメソッドは以下のように動作します。

1. 属性名がアンダースコア (`_`) で始まる場合、それはプライベート属性と見なされます。プライベート属性は、クラスの内部目的でよく使用されます。これらの属性はクラスの内部実装の一部であるため、設定を許可します。
2. 属性名が `_fields` リストに含まれている場合、それはクラス設計で定義された属性の 1 つであることを意味します。これらの属性はクラスの期待される動作の一部であるため、設定を許可します。
3. 属性名がこれらの条件のいずれにも該当しない場合、`AttributeError` を発生させます。これにより、ユーザーに対して、クラスに存在しない属性を設定しようとしていることを伝えます。

## 属性制限のテスト

属性制限を実装したので、期待通りに動作することを確認するためにテストしましょう。以下のコードを含む `test_attributes.py` という名前のファイルを作成します。

```python
# test_attributes.py
from structure import Stock

s = Stock('GOOG', 100, 490.1)

# This should work - valid attribute
print("Setting shares to 50")
s.shares = 50
print(f"Shares is now: {s.shares}")

# This should work - private attribute
print("\nSetting _internal_data")
s._internal_data = "Some data"
print(f"_internal_data is: {s._internal_data}")

# This should fail - invalid attribute
print("\nTrying to set an invalid attribute:")
try:
    s.share = 60  # Typo in attribute name
    print("This should not print")
except AttributeError as e:
    print(f"Error correctly caught: {e}")
```

テストを実行するには、ターミナルを開き、以下のコマンドを入力します。

```bash
python3 test_attributes.py
```

以下の出力が表示されるはずです。

```
Setting shares to 50
Shares is now: 50

Setting _internal_data
_internal_data is: Some data

Trying to set an invalid attribute:
Error correctly caught: No attribute share
```

この出力は、私たちのクラスが誤った属性設定エラーを防止していることを示しています。有効な属性とプライベート属性の設定を許可しますが、無効な属性を設定しようとするとエラーを発生させます。

## 属性制限の価値

属性名を制限することは、堅牢で保守可能なコードを書くために非常に重要です。理由は以下の通りです。

1. 属性名のタイプミスを検出するのに役立ちます。属性名を入力する際にミスを犯した場合、コードは新しい属性を作成する代わりにエラーを発生させます。これにより、開発プロセスの早い段階でエラーを見つけて修正することが容易になります。
2. クラス設計に存在しない属性を設定しようとする試みを防止します。これにより、クラスが意図された通りに使用され、コードが予測可能に動作することが保証されます。
3. 新しい属性の誤った作成を回避します。新しい属性を作成すると、予期せぬ動作が発生し、コードの理解と保守が困難になる可能性があります。

属性名を制限することで、コードをより信頼性が高く、使いやすくすることができます。
