# 特定のキーに基づいて配列をオブジェクトに変換する

特定のキーに基づいて配列をオブジェクトに変換し、そのキーを各値から除外するには、次の手順に従います。

- ターミナル/SSH を開き、コーディングの練習を始めるために `node` と入力します。
- `Array.prototype.reduce()` を使用して、提供された配列からオブジェクトを作成します。
- オブジェクトの分解構文を使用して、指定された `key` の値と関連付けられた `data` を抽出し、その後、キーと値のペアをオブジェクトに追加します。

以下は、例となる実装です。

```js
const indexOn = (arr, key) =>
  arr.reduce((obj, v) => {
    const { [key]: id, ...data } = v;
    obj[id] = data;
    return obj;
  }, {});
```

次に、この関数を次のように使用できます。

```js
indexOn(
  [
    { id: 10, name: "apple" },
    { id: 20, name: "orange" }
  ],
  "id"
);
// { '10': { name: 'apple' }, '20': { name: 'orange' } }
```
