# 各リスト要素に対して関数を実行する

## 問題

`for_each(itr, fn)` という関数を書きなさい。この関数は、リスト `itr` と関数 `fn` を引数として受け取ります。この関数は、`itr` の各要素に対して `fn` を 1 回実行する必要があります。

## 例

```python
def print_square(num):
    print(num*num)

for_each([1, 2, 3], print_square) # 1 4 9 と表示される
```

上記の例では、`for_each` 関数はリスト `[1, 2, 3]` と関数 `print_square` を引数に呼び出されます。`print_square` 関数は、リストの各要素に対して 1 回実行され、各数字の二乗が表示されます。
