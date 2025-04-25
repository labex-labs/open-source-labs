# 配列内の重複を確認する方法

配列に重複する値があるかどうかを確認するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングの練習を始めるために `node` と入力します。
2. `Set` を使って配列内の一意の値を取得します。
3. `Set.prototype.size` と `Array.prototype.length` を使って、一意の値の数が元の配列の要素数と同じかどうかを確認します。

配列内の重複を確認するコードの例は次のとおりです。

```js
const hasDuplicates = (arr) => new Set(arr).size !== arr.length;
```

この関数を次のコードでテストできます。

```js
hasDuplicates([0, 1, 1, 2]); // true
hasDuplicates([0, 1, 2, 3]); // false
```

`hasDuplicates` 関数は、配列に重複する値がある場合は `true` を返し、そうでない場合は `false` を返します。
