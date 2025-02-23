# JavaScript で値が null または undefined であるかどうかを確認する方法

JavaScript で値が `null` または `undefined` であるかどうかを判断するには、厳密な等価演算子 (`===`) を使用できます。指定された値が `null` または `undefined` であるかどうかをチェックするコード スニペットの例を次に示します。

```js
const isNil = (val) => val === undefined || val === null;
```

この関数を使用して、値が `null` または `undefined` であるかどうかをチェックすることができます。例えば：

```js
isNil(null); // true
isNil(undefined); // true
isNil(""); // false
```

JavaScript でコーディングを練習するには、ターミナル/SSH を開いて `node` と入力します。
