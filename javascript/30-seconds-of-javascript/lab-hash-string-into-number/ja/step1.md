# JavaScript を使って文字列を数値にハッシュ化する方法

JavaScript を使って入力文字列を整数にハッシュ化するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングの練習を始めるために `node` と入力します。
2. `String.prototype.split()` と `Array.prototype.reduce()` メソッドを使って、ビットシフトを利用して入力文字列のハッシュを作成します。
3. ハッシュ化アルゴリズムを実装する `sdbm` 関数のコードは次のとおりです。

```js
const sdbm = (str) => {
  let arr = str.split("");
  return arr.reduce(
    (hashCode, currentVal) =>
      (hashCode =
        currentVal.charCodeAt(0) +
        (hashCode << 6) +
        (hashCode << 16) -
        hashCode),
    0
  );
};
```

4. 関数をテストするには、文字列引数で関数を呼び出します。

```js
sdbm("name"); // -3521204949
```

これにより、入力文字列 "name" のハッシュ値が返されます。
