# 関数を合成する

## 問題

`compose(*fns)` という名前の関数を書きます。この関数は 1 つ以上の関数を引数として受け取り、入力関数を右から左に合成した結果である新しい関数を返します。最後の（最も右の）関数は 1 つ以上の引数を受け取ることができます。残りの関数は単項関数でなければなりません。

## 例

```python
add5 = lambda x: x + 5
multiply = lambda x, y: x * y
multiply_and_add_5 = compose(add5, multiply)
multiply_and_add_5(5, 2) # 15
```

上記の例では、`add5` と `multiply` の 2 つの関数を定義しています。その後、`compose()` 関数を使って、最初に 2 つの引数を乗算し、その結果に 5 を加える新しい関数 `multiply_and_add_5` を作成しています。`multiply_and_add_5(5, 2)` を呼び出すと、結果 `15` が得られます。
