# JavaScriptにおける配列の最初の要素を取得する方法

JavaScriptにおいて配列の最初の要素を取得するには、`head`関数を使用できます。その使い方は以下の通りです。

1. ターミナル/SSHを開きます。
2. コーディングを練習するために`node`と入力します。
3. 配列の先頭要素を取得するには、次のコードを使用します。

```js
const head = (arr) => (arr && arr.length ? arr[0] : undefined);
```

4. `head`関数に配列を引数として渡して最初の要素を取得します。配列が空または偽の値の場合、関数は`undefined`を返します。

以下にいくつかの例を示します。

```js
head([1, 2, 3]); // 1
head([]); // undefined
head(null); // undefined
head(undefined); // undefined
```
