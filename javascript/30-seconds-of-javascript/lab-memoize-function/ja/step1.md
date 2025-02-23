# メモ化関数

コーディングを始めるには、ターミナル/SSH を開き、`node` と入力します。この関数は、メモ化された（キャッシュされた）関数を返します。この関数を使用する手順は以下の通りです。

1. 空のキャッシュを作成するために新しい `Map` オブジェクトをインスタンス化します。
2. メモ化関数に渡される単一の引数を持つ関数を返します。関数を実行する前に、その特定の入力値に対する出力が既にキャッシュされているかどうかを確認します。もしキャッシュされていれば、キャッシュされた出力を返します。そうでなければ、それを格納して返します。
3. 必要に応じて `this` コンテキストを変更できるようにするために `function` キーワードを使用します。
4. 返された関数のプロパティとして `cache` を設定して、それにアクセスできるようにします。

ここにメモ化関数を実装するコードがあります。

```js
const memoize = (fn) => {
  const cache = new Map();
  const cached = function (val) {
    return cache.has(val)
      ? cache.get(val)
      : cache.set(val, fn.call(this, val)) && cache.get(val);
  };
  cached.cache = cache;
  return cached;
};
```

この関数がどのように機能するかを見るには、`anagrams` 関数と一緒に使用できます。以下は例です。

```js
const anagramsCached = memoize(anagrams);
anagramsCached("javascript"); // 時間がかかります
anagramsCached("javascript"); // キャッシュされているため、ほぼ即座に返されます
console.log(anagramsCached.cache); // キャッシュされたアナグラムのマップ
```
