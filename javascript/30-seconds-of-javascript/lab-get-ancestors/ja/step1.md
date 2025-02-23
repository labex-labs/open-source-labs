# 要素の祖先を取得する

ドキュメントルートから指定された要素までの要素の祖先を取得するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングを練習するために `node` と入力します。
2. `Node.parentNode` と `while` ループを使って、要素の祖先ツリーを辿ります。
3. `Array.prototype.unshift()` を使って、各新しい祖先を配列の先頭に追加します。

以下は、上記の手順を実装したサンプルコードです。

```js
const getAncestors = (el) => {
  let ancestors = [];
  while (el) {
    ancestors.unshift(el);
    el = el.parentNode;
  }
  return ancestors;
};
```

特定の要素の祖先を取得するには、`querySelector()` メソッドを使って要素を選択し、それを `getAncestors()` 関数に引数として渡します。たとえば：

```js
getAncestors(document.querySelector("nav"));
// [document, html, body, header, nav]
```

これにより、指定された要素のすべての祖先が、ドキュメントルートから要素自体までの順序で配列として返されます。
