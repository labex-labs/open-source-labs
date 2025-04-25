# 配列にすべての値が含まれているかどうかをチェックする関数

配列 `values` のすべての要素が別の配列 `arr` に含まれているかどうかをチェックしたい場合は、JavaScript の `includesAll` 関数を使用できます。

この関数を使用し始めるには、ターミナル/SSH を開いて `node` と入力します。

`includesAll` 関数の動作方法は次のとおりです。

- `Array.prototype.every()` と `Array.prototype.includes()` メソッドを使用して、`values` のすべての要素が `arr` に含まれているかどうかをチェックします。
- `values` のすべての要素が `arr` に含まれている場合、関数は `true` を返します。それ以外の場合は `false` を返します。

```js
const includesAll = (arr, values) => values.every((v) => arr.includes(v));
```

`includesAll` 関数の使用例は次のとおりです。

```js
includesAll([1, 2, 3, 4], [1, 4]); // true
includesAll([1, 2, 3, 4], [1, 5]); // false
```
