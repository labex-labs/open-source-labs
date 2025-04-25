# オブジェクトの配列から値を抜き出す方法

オブジェクトの配列から値を抜き出すには、次の手順を実行できます。

1. ターミナル/SSH を開き、コーディングの練習を始めるために `node` と入力します。
2. `Array.prototype.map()` を使用して、各オブジェクトの指定された `key` の値にオブジェクトの配列をマッピングします。
3. 次の関数を実装します。

```js
const pluck = (arr, key) => arr.map((i) => i[key]);
```

4. オブジェクトのサンプル配列を使用して関数をテストします。

```js
const simpsons = [
  { name: "lisa", age: 8 },
  { name: "homer", age: 36 },
  { name: "marge", age: 34 },
  { name: "bart", age: 10 }
];
pluck(simpsons, "age"); // [8, 36, 34, 10]
```

これにより、オブジェクトの配列から指定された `key` に対応する値の配列が返されます。
