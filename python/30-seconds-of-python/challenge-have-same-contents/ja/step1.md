# 2 つのリストが同じ内容を持っているかどうかを確認する

## 問題

2 つのリストを引数として受け取り、それらが同じ内容を持っている場合は`True`を返し、そうでない場合は`False`を返す関数`have_same_contents(a, b)`を書きます。この関数は、2 つのリストが同じ要素を含んでいるかどうかを順序に関係なく確認する必要があります。

この問題を解くには、次の手順に従うことができます。

1. 両方のリストの組み合わせに対して`set()`を使用して、一意の値を見つけます。
2. `for`ループを使ってそれらを反復処理し、各リストの各一意の値の`count()`を比較します。
3. どの要素についてもカウントが一致しない場合は`False`を返し、そうでない場合は`True`を返します。

## 例

```python
have_same_contents([1, 2, 4], [2, 4, 1]) # True
have_same_contents([1, 2, 4], [2, 4, 5]) # False
```
