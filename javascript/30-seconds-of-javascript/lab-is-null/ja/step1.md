# 値が null かどうかをチェックする

JavaScript で値が `null` かどうかをチェックするには、厳密な等価演算子 (`===`) を使用します。ここに、`isNull` と呼ばれる関数を定義するコード スニペットを示します。この関数は、与えられた値が `null` の場合に `true` を返し、それ以外の場合は `false` を返します。

```js
const isNull = (val) => val === null;
```

この関数をテストするには、チェックしたい値を引数として関数を呼び出します。たとえば、`isNull(null)` は `true` を返します。
