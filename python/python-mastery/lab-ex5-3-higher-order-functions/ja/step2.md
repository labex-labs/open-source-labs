# マッピング

関数型プログラミングにおける最も一般的な操作の1つは、関数をシーケンスの値にマッピングする `map()` 操作です。Pythonにはこれを行う組み込みの `map()` 関数があります。たとえば：

```python
>>> nums = [1,2,3,4]
>>> squares = map(lambda x: x*x, nums)
>>> for n in squares:
        print(n)

1
4
9
16
>>>
```

`map()` はイテレータを生成するため、リストが必要な場合は明示的に作成する必要があります：

```python
>>> squares = list(map(lambda x: x*x, nums))
>>> squares
[1, 4, 9, 16]
>>>
```

`convert_csv()` 関数で `map()` を使ってみてください。
