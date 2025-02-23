# コード演習：配列からランダムな要素を取得する

コーディングを練習するには、ターミナル/SSHを開いて`node`と入力します。次のコードは、Fisher-Yatesアルゴリズムを利用して配列をシャッフルし、配列のサイズまで、一意のキーで`n`個のランダムな一意の要素を取得します。

```js
const sampleSize = ([...arr], n = 1) => {
  let m = arr.length;
  while (m) {
    const i = Math.floor(Math.random() * m--);
    [arr[m], arr[i]] = [arr[i], arr[m]];
  }
  return arr.slice(0, n);
};
```

このコードを使用するには、配列と取得する要素のオプショナルな数`n`を引数に`sampleSize()`を呼び出します。`n`が指定されていない場合、関数は配列からランダムに1つの要素のみを返します。

```js
sampleSize([1, 2, 3], 2); // [3, 1]
sampleSize([1, 2, 3], 4); // [2, 3, 1]
```
