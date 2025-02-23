# オブジェクトが深く凍結されているかどうかを確認する方法

JavaScript でオブジェクトが深く凍結されているかどうかを確認するには、次の手順を使用します。

1. ターミナル/SSH を開き、コーディングを練習するために `node` と入力します。
2. 再帰を使用して、オブジェクトのすべてのプロパティが深く凍結されているかどうかを確認します。
3. 与えられたオブジェクトに `Object.isFrozen()` を使用して、それが浅く凍結されているかどうかを確認します。
4. `Object.keys()` を使用してオブジェクトのすべてのプロパティを取得し、`Array.prototype.every()` を使用してすべてのキーが深く凍結されたオブジェクトまたは非オブジェクト値であることを確認します。

オブジェクトが深く凍結されているかどうかを確認するためのコード スニペットの例を次に示します。

```js
const isDeepFrozen = (obj) =>
  Object.isFrozen(obj) &&
  Object.keys(obj).every(
    (prop) => typeof obj[prop] !== "object" || isDeepFrozen(obj[prop])
  );
```

次のように、`isDeepFrozen` 関数を使用してオブジェクトが深く凍結されているかどうかを確認できます。

```js
const x = Object.freeze({ a: 1 });
const y = Object.freeze({ b: { c: 2 } });
isDeepFrozen(x); // true
isDeepFrozen(y); // false
```
