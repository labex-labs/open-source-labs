# 配列内の要素をトグルする方法

配列内の要素をトグルするには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングを練習するために `node` と入力します。
2. `Array.prototype.includes()` を使って、与えられた要素が配列内にあるかどうかを確認します。
3. 要素が配列内にある場合、`Array.prototype.filter()` を使って削除します。
4. 要素が配列内にない場合、スプレッド演算子 (`...`) を使って追加します。
5. 配列と値を受け取る `toggleElement` 関数を使って、配列内の要素をトグルします。

```js
const toggleElement = (arr, val) =>
  arr.includes(val) ? arr.filter((el) => el !== val) : [...arr, val];

toggleElement([1, 2, 3], 2); // [1, 3]
toggleElement([1, 2, 3], 4); // [1, 2, 3, 4]
```

これらの手順に従えば、JavaScript を使って配列内の要素を簡単にトグルできます。
