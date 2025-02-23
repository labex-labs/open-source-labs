# 条件が満たされるまで配列を初期化する方法

コーディングの練習を始めるには、ターミナル/SSHを開いて `node` と入力します。

関数で生成された値で配列を初期化して埋める手順は以下の通りです。

1. 空の配列 `arr`、インデックス変数 `i`、要素 `el` を作成します。
2. `conditionFn` 関数が与えられたインデックス `i` と要素 `el` に対して `true` を返すまで、`mapFn` 関数を使って配列に要素を追加するために `do...while` ループを使用します。
3. `conditionFn` 関数には3つの引数があります。現在のインデックス、前の要素、配列自体。
4. `mapFn` 関数には3つの引数があります。現在のインデックス、現在の要素、配列自体。

コードは以下の通りです。

```js
const initializeArrayUntil = (conditionFn, mapFn) => {
  const arr = [];
  let i = 0;
  let el = undefined;
  do {
    el = mapFn(i, el, arr);
    arr.push(el);
    i++;
  } while (!conditionFn(i, el, arr));
  return arr;
};
```

`initializeArrayUntil` 関数を使用するには、2つの関数を引数として渡します。

```js
initializeArrayUntil(
  (i, val) => val > 10, //conditionFn
  (i, val, arr) => (i <= 1 ? 1 : val + arr[i - 2]) //mapFn
); // [1, 1, 2, 3, 5, 8, 13]
```

このコードは、10を超える最初の数までのフィボナッチ数列で配列を初期化します。`conditionFn` 関数は現在の値が10を超えるかどうかをチェックし、`mapFn` 関数は数列の次の数を生成します。
