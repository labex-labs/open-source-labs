# 関数を可変長関数に変換する

配列を受け取る関数を可変長関数に変換するには、次の手順に従うことができます。

1. ターミナル/SSH を開き、コーディングを練習するために `node` と入力します。

2. すべての入力を配列を受け取る関数に収集するクロージャを返します。

```js
const collectInto =
  (fn) =>
  (...args) =>
    fn(args);
```

3. `collectInto` 関数を使って関数を可変長関数に変換します。

```js
const Pall = collectInto(Promise.all.bind(Promise));
let p1 = Promise.resolve(1);
let p2 = Promise.resolve(2);
let p3 = new Promise((resolve) => setTimeout(resolve, 2000, 3));
Pall(p1, p2, p3).then(console.log); // [1, 2, 3] (約 2 秒後)
```

これにより、関数で任意の数の引数を受け取り、それらを配列に収集してさらに処理することができます。
