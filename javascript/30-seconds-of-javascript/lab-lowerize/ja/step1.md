# オブジェクトのキーを小文字に変換する

オブジェクトのすべてのキーを小文字に変換するには、以下の手順に従ってください。

1. コーディングの練習を始めるためにターミナル/SSH を開き、`node` と入力します。
2. `Object.keys()` を使ってオブジェクトのキーの配列を取得します。
3. `Array.prototype.reduce()` を使って配列をオブジェクトにマッピングします。
4. `String.prototype.toLowerCase()` を使ってキーを小文字に変換します。

これらの手順を実装したコードの例を以下に示します。

```js
const lowerize = (obj) =>
  Object.keys(obj).reduce((acc, k) => {
    acc[k.toLowerCase()] = obj[k];
    return acc;
  }, {});
```

その後、オブジェクトを引数として `lowerize()` 関数を呼び出すことで、すべてのキーが小文字になった新しいオブジェクトを取得できます。例えば：

```js
lowerize({ Name: "John", Age: 22 }); // { name: 'John', age: 22 }
```
