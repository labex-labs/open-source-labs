# 配列を HTML リストに変換する

コーディングを始めるには、ターミナル/SSH を起動して `node` を入力します。

この関数は、与えられた配列要素を `<li>` タグに変換し、与えられた id のリストに追加します。

`Array.prototype.map()` と `Document.querySelector()` を使って HTML タグのリストを生成します。

```js
const arrayToHTMLList = (arr, listID) =>
  (document.querySelector(`#${listID}`).innerHTML += arr
    .map((item) => `<li>${item}</li>`)
    .join(""));
```

使用例：

```js
arrayToHTMLList(["item 1", "item 2"], "myListID");
```
