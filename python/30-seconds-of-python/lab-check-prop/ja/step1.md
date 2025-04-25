# プロパティをチェックする

`check_prop` という名前の関数を作成します。この関数は 2 つのパラメータを受け取ります。`fn` と `prop` です。`fn` パラメータは述語関数で、辞書の指定されたプロパティに適用されます。`prop` パラメータは文字列で、述語関数が適用されるプロパティの名前を表します。

`check_prop` 関数は、辞書を受け取り、述語関数 `fn` を指定されたプロパティに適用するラムダ関数を返す必要があります。

```python
def check_prop(fn, prop):
  return lambda obj: fn(obj[prop])
```

```python
check_age = check_prop(lambda x: x >= 18, 'age')
user = {'name': 'Mark', 'age': 18}
check_age(user) # True
```
