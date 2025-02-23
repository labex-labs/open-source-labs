# サイクルジェネレータの使い方

コーディングの練習を始めるには、ターミナル/SSH を開いて `node` と入力します。その後、与えられた配列を無限にループするジェネレータを作成します。以下が手順です。

1. 非終了の `while` ループを使用し、`Generator.prototype.next()` が呼び出されるたびに値を `yield` します。
2. `Array.prototype.length` とモジュロ演算子 (`%`) を使用して、次の値のインデックスを取得し、各 `yield` ステートメントの後でカウンタをインクリメントします。

以下は `cycleGenerator` 関数の例です。

```js
const cycleGenerator = function* (arr) {
  let i = 0;
  while (true) {
    yield arr[i % arr.length];
    i++;
  }
};
```

次に、この関数を以下のように使用できます。

```js
const binaryCycle = cycleGenerator([0, 1]);
binaryCycle.next(); // { value: 0, done: false }
binaryCycle.next(); // { value: 1, done: false }
binaryCycle.next(); // { value: 0, done: false }
binaryCycle.next(); // { value: 1, done: false }
```

これらの指示に従えば、任意の配列を無限にループするサイクルジェネレータを作成できます。
