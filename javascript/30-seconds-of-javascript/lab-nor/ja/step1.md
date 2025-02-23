# JavaScript で論理的 NOR を使用する方法

JavaScript でコーディングを始めるには、ターミナル/SSH にアクセスして `node` と入力します。論理的 NOR は、与えられた引数のどれもが真でないことを確認します。2 つの値の論理和の逆を返すには、論理否定 (`!`) 演算子を使用します。以下は例です：

```js
const nor = (a, b) => !(a || b);
```

以下はいくつかの出力です：

```js
nor(true, true); // false
nor(true, false); // false
nor(false, false); // true
```
