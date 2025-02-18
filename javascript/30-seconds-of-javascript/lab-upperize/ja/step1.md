# JavaScript でオブジェクトのキーを大文字にする方法

JavaScript でオブジェクトのすべてのキーを大文字に変換するには、次の手順に従ってください。

1. `Object.keys()` を使って、オブジェクトのキーの配列を取得します。
2. `Array.prototype.reduce()` を使って、配列をオブジェクトにマッピングします。
3. `String.prototype.toUpperCase()` を使って、キーを大文字に変換します。

コードは次のとおりです。

```js
const upperize = (obj) =>
  Object.keys(obj).reduce((acc, k) => {
    acc[k.toUpperCase()] = obj[k];
    return acc;
  }, {});
```

この関数をテストするには、次のように呼び出すことができます。

```js
upperize({ Name: "John", Age: 22 }); // { NAME: 'John', AGE: 22 }
```
