# JavaScript でランダムな英数字文字列を生成する方法

JavaScript でランダムな英数字文字列を生成するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングの練習を始めるために`node`と入力します。
2. `Array.from()`を使って指定された長さの新しい配列を作成します。
3. `Math.random()`を使ってランダムな浮動小数点数を生成します。
4. `radix`値を`36`に設定して`Number.prototype.toString()`を使って数値を英数字文字列に変換します。
5. `String.prototype.slice()`を使って各生成された数値から整数部分と小数点を削除します。
6. 各回変数の長さの文字列を生成するため、`Array.prototype.some()`を使って必要な回数だけこのプロセスを繰り返します。
7. 生成された文字列が与えられた`length`より長い場合、`String.prototype.slice()`を使ってその文字列を短縮します。
8. 生成された文字列を返します。

以下がコードです。

```js
const randomAlphaNumeric = (length) => {
  let s = "";
  Array.from({ length }).some(() => {
    s += Math.random().toString(36).slice(2);
    return s.length >= length;
  });
  return s.slice(0, length);
};
```

引数として望ましい長さを指定して`randomAlphaNumeric()`関数を呼び出すことができます。たとえば：

```js
randomAlphaNumeric(5); // '0afad'
```
