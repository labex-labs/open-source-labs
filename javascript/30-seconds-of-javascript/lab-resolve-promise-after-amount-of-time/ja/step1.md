# 遅延付きで Promise を作成する

特定の時間の後に解決する新しい Promise を作成するには、次の手順に従います。

1. `Promise` コンストラクタを使って新しい Promise を作成します。
2. Promise のエクスキュータ関数の中で、指定された `delay` の後に、提供された `value` で Promise の `resolve` 関数を呼び出すために `setTimeout()` を使います。

以下は `resolveAfter()` の例の実装です。

```js
const resolveAfter = (value, delay) =>
  new Promise((resolve) => {
    setTimeout(() => resolve(value), delay);
  });
```

これで、指定された遅延の後に提供された値に解決する Promise を取得するために `resolveAfter()` を呼び出せます。

```js
resolveAfter("Hello", 1000);
// 1 秒後に 'Hello' に解決する Promise を返します
```

コーディングの練習を始めるには、ターミナルまたは SSH を開いて `node` と入力します。
