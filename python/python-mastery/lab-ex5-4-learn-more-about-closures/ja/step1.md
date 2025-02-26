# データ構造としてのクロージャ

クロージャの1つの潜在的な用途は、データのカプセル化のためのツールとしてのものです。この例を試してみてください。

```python
def counter(value):
    def incr():
        nonlocal value
        value += 1
        return value

    def decr():
        nonlocal value
        value -= 1
        return value

    return incr, decr
```

このコードは、値を操作する2つの内部関数を定義しています。試してみましょう。

```python
>>> up, down = counter(0)
>>> up()
1
>>> up()
2
>>> up()
3
>>> down()
2
>>> down()
1
>>>
```

ここではクラス定義がまったく関係していないことに注意してください。また、グローバル変数もありません。それでも、`up()` 関数と `down()` 関数は「舞台裏」の値を操作しています。かなり不思議です。
