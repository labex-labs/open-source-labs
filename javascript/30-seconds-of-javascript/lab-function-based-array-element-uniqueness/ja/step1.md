# 関数を使って配列内のすべての要素が一意であるかどうかをチェックする

与えられたマッピング関数に基づいて配列内のすべての要素が一意であるかどうかをチェックするには、次の手順に従います。

1. ターミナル/SSHを開き、コーディングを練習するために `node` と入力します。
2. `Array.prototype.map()` メソッドを使用して、与えられた関数 `fn` を `arr` 配列のすべての要素に適用します。
3. マッピングされた値から新しい `Set` を作成して、一意の出現のみを保持します。
4. `Array.prototype.length` と `Set.prototype.size` メソッドを使用して、一意のマッピングされた値の長さと元の配列の長さを比較します。

以下がコードです。

```js
const allUniqueBy = (arr, fn) => arr.length === new Set(arr.map(fn)).size;
```

配列内のすべての要素が一意であるかどうかをチェックするために、`allUniqueBy()` 関数を使用できます。たとえば：

```js
allUniqueBy([1.2, 2.4, 2.9], Math.round); // true
allUniqueBy([1.2, 2.3, 2.4], Math.round); // false
```
