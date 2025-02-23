# JavaScript で与えられたプロパティに基づいて配列をアルファベット順にソートする方法

JavaScript で与えられたプロパティに基づいてオブジェクトの配列をアルファベット順にソートするには、次の手順を実行します。

1. ターミナル/SSH を開き、コーディングを練習するために `node` と入力します。
2. `Array.prototype.sort()` を使って、与えられたプロパティに基づいて配列をソートします。
3. `String.prototype.localeCompare()` を使って、与えられたプロパティの値を比較します。

以下は使用できるコード スニペットの例です。

```js
const alphabetical = (arr, getter, order = "asc") =>
  arr.sort(
    order === "desc"
      ? (a, b) => getter(b).localeCompare(getter(a))
      : (a, b) => getter(a).localeCompare(getter(b))
  );
```

オブジェクトの配列とソート対象のプロパティを返すゲッター関数を使って、`alphabetical` 関数を呼び出すことができます。以下は使用例です。

```js
const people = [{ name: "John" }, { name: "Adam" }, { name: "Mary" }];
alphabetical(people, (g) => g.name);
// [ { name: 'Adam' }, { name: 'John' }, { name: 'Mary' } ]
alphabetical(people, (g) => g.name, "desc");
// [ { name: 'Mary' }, { name: 'John' }, { name: 'Adam' } ]
```
