# コーディングと共通キーの見つけ方に関するヒント

コーディングを練習するには、ターミナル/SSH を開いて `node` と入力します。

2 つのオブジェクト間の共通キーを見つけるには、次の手順に従います。

1. `Object.keys()` を使用して最初のオブジェクトのキーを取得します。
2. `Object.prototype.hasOwnProperty()` を使用して、2 番目のオブジェクトに最初のオブジェクトに含まれるキーがあるかどうかを確認します。
3. `Array.prototype.filter()` を使用して、両方のオブジェクトに含まれていないキーをフィルタリングします。

以下はコードの例です。

```js
const commonKeys = (obj1, obj2) =>
  Object.keys(obj1).filter((key) => obj2.hasOwnProperty(key));
```

この例でコードをテストできます。

```js
commonKeys({ a: 1, b: 2 }, { a: 2, c: 1 }); // ['a']
```
