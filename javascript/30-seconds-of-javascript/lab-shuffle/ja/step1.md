# 配列のシャッフルアルゴリズム

JavaScriptで配列をシャッフルするには、フィッシャー・ヤーツのアルゴリズムを使います。このアルゴリズムは配列の要素をランダムに並び替え、新しい配列を返します。

コーディングの練習を始めるには、ターミナル/SSHを開き、`node`と入力します。

以下はフィッシャー・ヤーツのアルゴリズムのコードです。

```js
const shuffle = ([...arr]) => {
  let m = arr.length;
  while (m) {
    const i = Math.floor(Math.random() * m--);
    [arr[m], arr[i]] = [arr[i], arr[m]];
  }
  return arr;
};
```

配列をシャッフルするには、配列を`shuffle`関数に渡すと、シャッフルされた配列が返されます。たとえば：

```js
const foo = [1, 2, 3];
shuffle(foo); // returns [2, 3, 1], and foo is still [1, 2, 3]
```
