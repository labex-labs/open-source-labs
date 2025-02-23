# オブジェクトをディープクローンする手順

オブジェクトをディープクローンするには、次の手順に従います。

1. 新しいターミナル/SSH インスタンスを作成し、コーディングの練習を始めるために `node` と入力します。
2. 再帰を使って、クラス インスタンスを除くプリミティブ型、配列、およびオブジェクトをクローンします。
3. 渡されたオブジェクトが `null` であるかどうかを確認し、その場合は `null` を返します。
4. `Object.assign()` と空のオブジェクト (`{}`) を使って、元のオブジェクトのシャロークローンを作成します。
5. `Object.keys()` と `Array.prototype.forEach()` を使って、どのキーと値のペアがディープクローンする必要があるかを判断します。
6. オブジェクトが `Array` の場合、`clone` の `length` を元のものに設定し、`Array.from()` を使ってクローンを作成します。
7. 次のコードを使ってディープクローニングを実装します。

```js
const deepClone = (obj) => {
  if (obj === null) return null;
  let clone = Object.assign({}, obj);
  Object.keys(clone).forEach(
    (key) =>
      (clone[key] =
        typeof obj[key] === "object" ? deepClone(obj[key]) : obj[key])
  );
  if (Array.isArray(obj)) {
    clone.length = obj.length;
    return Array.from(clone);
  }
  return clone;
};
```

次のコードを使って、ディープクローニング関数をテストします。

```js
const a = { foo: "bar", obj: { a: 1, b: 2 } };
const b = deepClone(a); // a!== b, a.obj!== b.obj
```
