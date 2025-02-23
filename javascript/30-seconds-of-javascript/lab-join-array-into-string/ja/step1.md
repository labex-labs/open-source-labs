# 配列を文字列に結合する方法

配列のすべての要素を 1 つの文字列に結合するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングを練習するために `node` と入力します。
2. 次のパラメータを持つ `join()` 関数を使用します。
   - `arr`：結合する配列。
   - `separator`（省略可能）：配列の要素の間に使用する区切り文字。指定しない場合、既定の区切り文字 `,` が使用されます。
   - `end`（省略可能）：配列の最後の 2 つの要素の間に使用する区切り文字。指定しない場合、既定で `separator` と同じ値が使用されます。
3. `join()` 関数は `Array.prototype.reduce()` を使用して配列の要素を 1 つの文字列に結合します。
4. 最終的な文字列が返されます。

ここに `join()` 関数のコードを示します。

```js
const join = (arr, separator = ",", end = separator) =>
  arr.reduce(
    (acc, val, i) =>
      i === arr.length - 2
        ? acc + val + end
        : i === arr.length - 1
          ? acc + val
          : acc + val + separator,
    ""
  );
```

そして、`join()` 関数の使い方のいくつかの例を示します。

```js
join(["pen", "pineapple", "apple", "pen"], ",", "&"); // 'pen,pineapple,apple&pen'
join(["pen", "pineapple", "apple", "pen"], ","); // 'pen,pineapple,apple,pen'
join(["pen", "pineapple", "apple", "pen"]); // 'pen,pineapple,apple,pen'
```
