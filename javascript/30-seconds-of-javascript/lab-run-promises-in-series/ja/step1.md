# 直列でプロミスを実行する

直列で一連のプロミスを実行するには、`Array.prototype.reduce()` を使ってプロミスチェーンを作成します。各プロミスは解決した後、次のプロミスを返します。

まず、ターミナル/SSH を開き、コーディングを練習するために `node` と入力します。

以下はコードの例です。

```js
const runPromisesInSeries = (ps) =>
  ps.reduce((p, next) => p.then(next), Promise.resolve());
```

次に、`runPromisesInSeries` 関数を使ってプロミスを順次実行できます。以下の例を参照してください。

```js
const delay = (d) => new Promise((r) => setTimeout(r, d));
runPromisesInSeries([() => delay(1000), () => delay(2000)]);
// このコードは各プロミスを順次実行し、合計 3 秒かけて完了します。
```
