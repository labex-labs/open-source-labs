# 範囲で配列を初期化する関数

数値の範囲で配列を初期化するには、次の関数を使用します。

```js
const initializeArrayWithRange = (end, start = 0, step = 1) => {
  const length = Math.ceil((end - start + 1) / step);
  return Array.from({ length }, (_, i) => i * step + start);
};
```

この関数には 3 つの引数があります。`end`（必須）、`start`（省略可能、デフォルト値は`0`）、および`step`（省略可能、デフォルト値は`1`）です。これは、指定された範囲の数値を含む配列を返します。ここで、`start`と`end`はそれぞれ共通の差分`step`を持って含まれます。

この関数を使用するには、必要な範囲パラメータでそれを単に呼び出します。

```js
initializeArrayWithRange(5); // [0, 1, 2, 3, 4, 5]
initializeArrayWithRange(7, 3); // [3, 4, 5, 6, 7]
initializeArrayWithRange(9, 0, 2); // [0, 2, 4, 6, 8]
```

この関数は、必要な長さの配列を作成するために`Array.from()`を使用し、その後、マップ関数を使用して、与えられた範囲の必要な値で配列を埋めます。2 番目の引数`start`を省略すると、デフォルト値`0`が使用されます。最後の引数`step`を省略すると、デフォルト値`1`が使用されます。
