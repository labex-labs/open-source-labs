# 文字列の順列アルゴリズム

重複を含む文字列のすべての順列を生成するには、次のアルゴリズムを使用します。

1. ターミナル/SSH を開き、コーディングを練習するために `node` と入力します。
2. 再帰を使用して、与えられた文字列のすべての可能な順列を作成します。
3. 与えられた文字列の各文字に対して、その残りの文字のすべての部分順列を作成します。
4. `Array.prototype.map()` を使用して、その文字と各部分順列を結合します。
5. `Array.prototype.reduce()` を使用して、すべての順列を 1 つの配列に結合します。
6. 基本ケースは、`String.prototype.length` が `2` または `1` に等しい場合です。
7. ⚠️ **警告**: 実行時間は各文字に対して指数関数的に増加します。8 文字以上 10 文字以下の文字列の場合、環境はすべての異なる組み合わせを解こうとするときにハングアップする場合があります。

ここにアルゴリズムの JavaScript コードを示します。

```js
const stringPermutations = (str) => {
  if (str.length <= 2) return str.length === 2 ? [str, str[1] + str[0]] : [str];
  return str
    .split("")
    .reduce(
      (acc, letter, i) =>
        acc.concat(
          stringPermutations(str.slice(0, i) + str.slice(i + 1)).map(
            (val) => letter + val
          )
        ),
      []
    );
};
```

次のコードで `stringPermutations` 関数をテストできます。

```js
stringPermutations("abc"); // ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
```
