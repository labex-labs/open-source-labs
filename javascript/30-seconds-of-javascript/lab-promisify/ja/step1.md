# promisify 関数

非同期関数を Promise を返す関数に変換するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングを練習するために `node` と入力します。
2. カリングを使って、元の関数を呼び出す `Promise` を返す関数を返します。
3. 残余引数演算子 (`...`) を使ってすべてのパラメータを渡します。
4. Node 8+ を使っている場合、[`util.promisify`](https://nodejs.org/api/util.html#util_util_promisify_original) を使うことができます。
5. 以下はコードの例です。

```js
const promisify =
  (func) =>
  (...args) =>
    new Promise((resolve, reject) =>
      func(...args, (err, result) => (err ? reject(err) : resolve(result)))
    );
```

6. この関数を使うには、非同期関数を定義して、それを `promisify` 関数のパラメータとして渡します。返される関数は現在 Promise を返します。

```js
const delay = promisify((d, cb) => setTimeout(cb, d));
delay(2000).then(() => console.log("Hi!")); // Promise resolves after 2s
```

`delay` 関数は、`promisify` 関数を使って現在 Promise を返す非同期関数の例です。
