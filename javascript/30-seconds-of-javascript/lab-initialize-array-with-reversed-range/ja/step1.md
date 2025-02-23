# JavaScript で逆順の範囲で配列を初期化する方法

JavaScript で逆順の範囲で配列を初期化するには、次の関数を使用します。

```js
const initializeArrayWithRangeRight = (end, start = 0, step = 1) =>
  Array.from({ length: Math.ceil((end + 1 - start) / step) }).map(
    (v, i, arr) => (arr.length - i - 1) * step + start
  );
```

この関数は、指定された範囲の数値を逆順で含む配列を作成します。`start` と `end` パラメータは両端を含み、`step` パラメータは範囲内の数値間の公差を指定します。

この関数を使用するには、必要な `end`、`start`、および `step` の値を引数として関数を呼び出します。例えば：

```js
initializeArrayWithRangeRight(5); // [5, 4, 3, 2, 1, 0]
initializeArrayWithRangeRight(7, 3); // [7, 6, 5, 4, 3]
initializeArrayWithRangeRight(9, 0, 2); // [8, 6, 4, 2, 0]
```

`start` 引数を省略すると、デフォルト値は `0` になります。`step` 引数を省略すると、デフォルト値は `1` になります。
