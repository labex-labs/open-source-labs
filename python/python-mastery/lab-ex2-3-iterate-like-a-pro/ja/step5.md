# ジェネレータ式

ジェネレータ式は、リスト内包表記とほぼ同じですが、リストを作成しません。代わりに、結果を段階的に生成するオブジェクトを作成します。通常は、反復処理によって消費されます。簡単な例を試してみましょう：

```python
>>> nums = [1,2,3,4,5]
>>> squares = (x*x for x in nums)
>>> squares
<generator object <genexpr> at 0x37caa8>
>>> for n in squares:
        print(n)

1
4
9
16
25
>>>
```

ジェネレータ式は一度だけ使用できることに注意してください。もう一度forループを行うと何が起こるか見てみましょう：

```python
>>> for n in squares:
         print(n)

>>>
```

`next()` 関数を使用すると、結果を1つずつ手動で取得できます。試してみましょう：

```python
>>> squares = (x*x for x in nums)
>>> next(squares)
1
>>> next(squares)
4
>>> next(squares)
9
>>>
```

データがなくなったときに何が起こるかを確認するために、`next()` を続けて入力してください。

実行しているタスクがより複雑な場合でも、ジェネレータ関数を書き、代わりに `yield` 文を使用することでジェネレータの恩恵を受けることができます。たとえば：

```python
>>> def squares(nums):
        for x in nums:
            yield x*x

>>> for n in squares(nums):
        print(n)

1
4
9
16
25
>>>
```

このコースの後半でジェネレータ関数に戻ります。今のところ、このような関数は `for` 文に値を供給するという興味深い特性を持つものと見なしてください。
