# JavaScript でオブジェクトのキーをシンボル化する方法

JavaScript でオブジェクトのキーをシンボル化するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングの練習を始めるために `node` と入力します。
2. シンボル化したいオブジェクトのキーを取得するには、`Object.keys()` メソッドを使用します。
3. `Array.prototype.reduce()` メソッドと `Symbol` を使用して、各キーが `Symbol` に変換された新しいオブジェクトを作成します。
4. 以下はコードの例です。

```js
const symbolizeKeys = (obj) =>
  Object.keys(obj).reduce(
    (acc, key) => ({ ...acc, [Symbol(key)]: obj[key] }),
    {}
  );
```

5. 関数をテストするには、オブジェクトを引数として `symbolizeKeys()` を呼び出します。

```js
symbolizeKeys({ id: 10, name: "apple" });
// { [Symbol(id)]: 10, [Symbol(name)]: 'apple' }
```

これらの手順に従えば、JavaScript の任意のオブジェクトのキーを簡単にシンボル化できます。
