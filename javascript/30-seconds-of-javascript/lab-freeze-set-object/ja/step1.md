# JavaScript における凍結された Set オブジェクトの作成

JavaScript において凍結された `Set` オブジェクトを作成するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングを練習するために `node` と入力します。
2. `Set` コンストラクタを使用して、`iterable` から新しい `Set` オブジェクトを作成します。
3. 新しく作成されたオブジェクトの `add`、`delete`、および `clear` メソッドを `undefined` に設定して、オブジェクトを効果的に凍結します。

以下はコードの例です。

```js
const frozenSet = (iterable) => {
  const s = new Set(iterable);
  s.add = undefined;
  s.delete = undefined;
  s.clear = undefined;
  return s;
};

console.log(frozenSet([1, 2, 3, 1, 2]));
// 出力: Set { 1, 2, 3, add: undefined, delete: undefined, clear: undefined }
```

このコードは、数値の反復可能オブジェクトから凍結された `Set` オブジェクトを作成し、その `add`、`delete`、および `clear` メソッドが `undefined` に設定されたオブジェクトを返します。
