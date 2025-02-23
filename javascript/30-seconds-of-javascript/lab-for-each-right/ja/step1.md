# 配列の各要素に対して逆順で関数を実行する方法

配列の最後の要素から始めて、各配列要素に対して関数を実行するには、次の手順に従います。

1. `Array.prototype.slice()` を使って与えられた配列をクローンします。
2. `Array.prototype.reverse()` を使ってクローンした配列を逆順にします。
3. `Array.prototype.forEach()` を使って逆順の配列を反復処理します。

以下はコードの例です。

```js
const forEachRight = (arr, callback) => arr.slice().reverse().forEach(callback);
```

次のコードを実行することで関数をテストできます。

```js
forEachRight([1, 2, 3, 4], (val) => console.log(val)); // '4', '3', '2', '1'
```

コーディングを始めるには、ターミナル/SSH を開いて `node` と入力します。
