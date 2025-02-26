# 強制

関数アノテーションを介して付加された値のチェックを強制するように `ValidatedFunction` クラスを変更します。たとえば：

```python
>>> def add(x: Integer, y:Integer):
        return x + y
>>> add = ValidatedFunction(add)
>>> add(2,3)
5
>>> add('two','three')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "validate.py", line 67, in __call__
    self.func.__annotations__[name].check(val)
  File "validate.py", line 21, in check
    raise TypeError(f'Expected {cls.expected_type}')
TypeError: expected <class 'int'>
>>>>
```

ヒント：これを行うには、シグネチャバインディングを試してみましょう。`Signature` オブジェクトの `bind()` メソッドを使用して、関数の引数を引数名にバインドします。その後、この情報を `__annotations__` 属性と照合して、異なるバリデータクラスを取得します。

忘れないでください。見た目は関数のようなオブジェクトを作成していますが、実際はそうではありません。裏では魔法が起こっています。
