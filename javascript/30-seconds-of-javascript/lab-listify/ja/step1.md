# JavaScript でオブジェクトを配列にマッピングする方法

JavaScript でオブジェクトを配列にマッピングするには、`listify()` 関数を使うことができます。以下にその方法を示します。

1. ターミナル/SSH を開き、コーディングの練習を始めるために `node` と入力します。

2. `Object.entries()` を使って、オブジェクトのキーと値のペアの配列を取得します。

3. `Array.prototype.reduce()` を使って、配列をオブジェクトにマッピングします。

4. `mapFn` を使ってオブジェクトのキーと値をマッピングし、`Array.prototype.push()` を使ってマッピングされた値を配列に追加します。

以下は `listify()` 関数のコードです。

```js
const listify = (obj, mapFn) =>
  Object.entries(obj).reduce((acc, [key, value]) => {
    acc.push(mapFn(key, value));
    return acc;
  }, []);
```

そして、`people` と呼ばれるオブジェクトでそれを使う方法の例を以下に示します。

```js
const people = { John: { age: 42 }, Adam: { age: 39 } };
listify(people, (key, value) => ({ name: key, ...value }));
// [ { name: 'John', age: 42 }, { name: 'Adam', age: 39 } ]
```

この関数を使えば、JavaScript で簡単にオブジェクトを配列にマッピングすることができます。
