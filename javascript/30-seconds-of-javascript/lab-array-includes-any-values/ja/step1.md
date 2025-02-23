# 配列に特定の値が含まれているかどうかを確認する

コーディングの練習を始めるには、ターミナル/SSH を開いて `node` と入力します。

ある配列に別の配列の少なくとも 1 つの要素が含まれているかどうかを確認するには、`Array.prototype.some()` と `Array.prototype.includes()` を使います。以下は例の関数です。

```js
const includesAny = (arr, values) => values.some((v) => arr.includes(v));
```

この関数を呼び出して、比較したい 2 つの配列を引数として渡すことができます。この関数は、`values` の少なくとも 1 つの要素が `arr` に含まれているかどうかを示すブール値を返します。以下はいくつかの例です。

```js
includesAny([1, 2, 3, 4], [2, 9]); // true
includesAny([1, 2, 3, 4], [8, 9]); // false
```
