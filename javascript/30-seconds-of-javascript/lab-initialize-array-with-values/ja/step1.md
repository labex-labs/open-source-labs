# 指定された値で配列を初期化する関数

コーディングの練習を始めるには、ターミナル/SSH を開いて `node` と入力します。

この関数は、指定された値で配列を初期化します。

- 必要な長さの配列を作成するには、`Array()` コンストラクタを使用します。
- `Array.prototype.fill()` を使用して、必要な値で配列を埋めます。
- 値が指定されていない場合、既定値は `0` になります。

```js
const initializeArrayWithValues = (length, value = 0) =>
  Array(length).fill(value);
```

使用例：

```js
initializeArrayWithValues(5, 2); // [2, 2, 2, 2, 2]
```
