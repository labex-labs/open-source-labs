# 論理 AND 演算子の使用

コーディングを練習するには、ターミナル/SSH を開いて `node` と入力します。そして、論理 AND (`&&`) 演算子を使って両方の引数が `true` であるかどうかを確認します。以下はサンプルコードです。

```js
const and = (a, b) => a && b;
and(true, true); // true
and(true, false); // false
and(false, false); // false
```
