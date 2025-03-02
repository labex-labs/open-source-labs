# JavaScript で関数の実行を遅らせる方法

JavaScript で関数の実行を遅らせるには、`setTimeout()` メソッドを使用できます。方法は以下の通りです。

1. ターミナル/SSH を開き、コーディングの練習を始めるために `node` と入力します。
2. 関数 `fn` の実行を `ms` ミリ秒遅らせるには、次の構文を使用します。

```js
const delay = (fn, ms, ...args) => setTimeout(fn, ms, ...args);
```

3. 関数に引数を渡すには、次のようにスプレッド (`...`) 演算子を使用します。

```js
delay(
  function (text) {
    console.log(text);
  },
  1000,
  "later"
); // 1 秒後に 'later' をログに出力します。
```

このコードでは、指定されたミリ秒数 (`ms`) 後に提供された関数 `fn` が呼び出されます。`...args` パラメータを使用することで、任意の数の引数を関数に渡すことができます。
