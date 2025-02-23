# フォームをオブジェクトに変換する

コーディングを練習するには、ターミナル/SSHを開いて`node`と入力します。以下の手順を使って、一連のフォーム要素をオブジェクトとしてエンコードできます。

1. `FormData`コンストラクタを使って、HTMLの`form`を`FormData`に変換します。
2. `Array.from()`を使って`FormData`を配列に変換します。
3. `Array.prototype.reduce()`を使って配列からオブジェクトを収集します。

以下はコードの例です。

```js
const formToObject = (form) =>
  Array.from(new FormData(form)).reduce(
    (acc, [key, value]) => ({
      ...acc,
      [key]: value
    }),
    {}
  );
```

特定のフォームを変換するには、`formToObject`関数を呼び出して、フォーム要素を引数として渡します。

```js
formToObject(document.querySelector("#form"));
// { email: 'test@email.com', name: 'Test Name' }
```
