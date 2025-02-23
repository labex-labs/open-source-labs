# JavaScript でオブジェクトのキー名を変更する方法

提供された値で複数のオブジェクトのキー名を変更するには、`renameKeys` 関数を使用できます。次の手順に従ってください。

1. ターミナル/SSH を開き、コーディングの練習を始めるために `node` と入力します。
2. `Object.keys()` を `Array.prototype.reduce()` と展開演算子 (`...`) と組み合わせて使用して、オブジェクトのキーを取得し、`keysMap` に従ってそれらのキー名を変更します。
3. `keysMap` とオブジェクト (`obj`) を引数として `renameKeys` 関数に渡します。
4. `renameKeys` 関数は、キー名が変更された新しいオブジェクトを返します。

`renameKeys` 関数の使用方法の例を次に示します。

```js
const renameKeys = (keysMap, obj) =>
  Object.keys(obj).reduce(
    (acc, key) => ({
      ...acc,
      ...{ [keysMap[key] || key]: obj[key] }
    }),
    {}
  );

const obj = { name: "Bobo", job: "Front-End Master", shoeSize: 100 };
renameKeys({ name: "firstName", job: "passion" }, obj);
// { firstName: 'Bobo', passion: 'Front-End Master', shoeSize: 100 }
```
