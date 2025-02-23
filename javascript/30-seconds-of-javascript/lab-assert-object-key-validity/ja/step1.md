# オブジェクトのキーを検証する

オブジェクト内のすべてのキーが指定された `keys` と一致することを確認するには、次の手順に従います。

- ターミナル/SSH を開き、コーディングを練習するために `node` と入力します。
- `Object.keys()` を使用して、オブジェクト `obj` のキーを取得します。
- `Array.prototype.every()` と `Array.prototype.includes()` を使用して、オブジェクト内の各キーが `keys` 配列に含まれていることを検証します。

以下は、実装例です。

```js
const validateObjectKeys = (obj, keys) =>
  Object.keys(obj).every((key) => keys.includes(key));
```

この関数を次のように使用できます。

```js
validateObjectKeys({ id: 10, name: "apple" }, ["id", "name"]); // true
validateObjectKeys({ id: 10, name: "apple" }, ["id", "type"]); // false
```
