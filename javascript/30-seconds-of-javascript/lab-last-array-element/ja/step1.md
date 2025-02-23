# JavaScript で配列の最後の要素を取得する方法

コーディングを始めるには、ターミナル/SSH を開いて `node` と入力します。次の関数は配列の最後の要素を返します。

```js
const last = (arr) => (arr && arr.length ? arr[arr.length - 1] : undefined);
```

これを使用するには、引数として配列を提供する必要があります。この関数は、配列が真であり、`length` プロパティを持っているかどうかを確認します。両方の条件が true の場合、配列の最後の要素のインデックスを計算して返します。それ以外の場合は、`undefined` を返します。

以下はいくつかの例です。

```js
last([1, 2, 3]); // 3
last([]); // undefined
last(null); // undefined
last(undefined); // undefined
```
