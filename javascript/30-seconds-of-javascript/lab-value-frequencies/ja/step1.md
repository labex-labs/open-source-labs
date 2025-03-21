# 値の頻度をカウントするための手順

配列内の値の頻度をカウントするには、次の手順に従ってください。

1. ターミナル/SSH を開き、コーディングの練習を始めるために `node` と入力します。
2. `Array.prototype.reduce()` メソッドを使用して、一意の値をオブジェクトのキーにマッピングし、同じ値が見つかるたびに既存のキーに追加します。これにより、配列の一意の値をキーとし、その頻度を値とするオブジェクトが作成されます。
3. この操作のコードは次のとおりです。

```js
const frequencies = (arr) =>
  arr.reduce((a, v) => {
    a[v] = a[v] ? a[v] + 1 : 1;
    return a;
  }, {});
```

4. この関数を使用するには、配列を引数として `frequencies` を呼び出します。たとえば：

```js
frequencies(["a", "b", "a", "c", "a", "a", "b"]); // { a: 4, b: 2, c: 1 }
frequencies([..."ball"]); // { b: 1, a: 1, l: 2 }
```

これらの手順に従えば、任意の配列内の値の頻度を簡単にカウントすることができます。
