# JavaScript でオブジェクトのプロパティを比較する方法

2 つのオブジェクトを比較し、同じプロパティ値を持っているかどうかを確認するには、`matches` 関数を使います。使い方は以下の通りです。

1. ターミナル/SSH を開き、コーディングを始めるために `node` と入力します。
2. `matches` 関数のコードをコピーして、JavaScript ファイルに貼り付けます。
3. 関数を呼び出し、2 つのオブジェクトを引数として渡します。最初のオブジェクトは比較したいオブジェクトで、2 番目のオブジェクトはそれと比較したいオブジェクトです。

```js
matches({ age: 25, hair: "long", beard: true }, { hair: "long", beard: true });
// true
matches({ hair: "long", beard: true }, { age: 25, hair: "long", beard: true });
// false
```

`matches` 関数は、`Object.keys()` を使って 2 番目のオブジェクトのすべてのキーを取得し、その後、`Array.prototype.every()`、`Object.prototype.hasOwnProperty()` および厳密な比較を使って、最初のオブジェクトにすべてのキーが存在し、同じ値を持っているかどうかを確認します。
