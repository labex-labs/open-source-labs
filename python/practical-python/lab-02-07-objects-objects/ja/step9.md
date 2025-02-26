# 型のチェック

オブジェクトが特定の型であるかどうかを判断する方法。

```python
if isinstance(a, list):
    print('a is a list')
```

複数の可能性のある型のうちの1つをチェックする。

```python
if isinstance(a, (list,tuple)):
    print('a is a list or tuple')
```

\*注意: 型のチェックには度を越してはいけません。それはコードの複雑さを余計に招く可能性があります。通常は、他の人があなたのコードを使用する際に起こりうる一般的なミスを防ぐためにのみ行います。
