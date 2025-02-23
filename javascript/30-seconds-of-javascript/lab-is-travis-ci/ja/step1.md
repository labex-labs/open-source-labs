# Travis CI 環境かどうかを確認する

あなたが Travis CI 上で実行されているかどうかを確認するには、`isTravisCI()` 関数を使用します。この関数は、`TRAVIS` と `CI` の環境変数が存在するかどうかを確認します。

```js
const isTravisCI = () => "TRAVIS" in process.env && "CI" in process.env;
```

Travis CI でコーディングを開始するには、ターミナル/SSH を開き、`node` と入力します。
