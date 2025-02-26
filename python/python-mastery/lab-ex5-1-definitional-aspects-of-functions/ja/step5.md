# APIチャレンジ：型ヒント

関数には、引数と戻り値に付加されるオプションの型ヒントを持つことができます。たとえば：

```python
def add(x:int, y:int) -> int:
    return x + y
```

`typing`モジュールには、コンテナを含むより複雑な種類の型を表現するための追加のクラスがあります。たとえば：

```python
from typing import List

def sum_squares(nums: List[int]) -> int:
    total = 0
    for n in nums:
        total += n*n
    return total
```

あなたのチャレンジ：`reader.py`内のコードを変更して、すべての関数に型ヒントを付けます。型ヒントをできるだけ正確にするようにしてください。これを行うには、[typingモジュール](https://docs.python.org/3/library/typing.html)のドキュメントを参照する必要があるかもしれません。
