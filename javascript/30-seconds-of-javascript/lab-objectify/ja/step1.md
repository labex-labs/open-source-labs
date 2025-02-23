# JavaScript で配列をオブジェクトにマッピングする方法

JavaScript でオブジェクト配列をオブジェクトにマッピングするには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングを練習するために `node` と入力します。
2. `Array.prototype.reduce()` を使用して配列をオブジェクトにマッピングします。
3. `mapKey` パラメータを使用してオブジェクトのキーをマッピングし、`mapValue` パラメータを使用して値をマッピングします。

以下は、`objectify` 関数を使用してオブジェクト配列をオブジェクトにマッピングする方法を示すコード スニペットです。

```js
const objectify = (arr, mapKey, mapValue = (i) => i) =>
  arr.reduce((acc, item) => {
    acc[mapKey(item)] = mapValue(item);
    return acc;
  }, {});
```

次に、`objectify` 関数を使用してオブジェクト配列をオブジェクトにマッピングする方法を以下に示します。

```js
const people = [
  { name: "John", age: 42 },
  { name: "Adam", age: 39 }
];

// 名前プロパティをキーとしてオブジェクト配列をオブジェクトにマッピングする
objectify(people, (p) => p.name.toLowerCase());
// 出力: { john: { name: 'John', age: 42 }, adam: { name: 'Adam', age: 39 } }

// 名前プロパティをキーとし、年齢プロパティを値としてオブジェクト配列をオブジェクトにマッピングする
objectify(
  people,
  (p) => p.name.toLowerCase(),
  (p) => p.age
);
// 出力: { john: 42, adam: 39 }
```
