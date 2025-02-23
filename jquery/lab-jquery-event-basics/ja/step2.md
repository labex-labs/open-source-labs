# 新しいページ要素にイベントを拡張する

`.on()` は、イベントリスナーを設定する際に存在する要素にのみイベントリスナーを作成できることに注意する必要があります。たとえば：

```js
$(document).ready(function () {
  // ここで、alert クラスを持つ新しいボタン要素を作成します。
  $("<button class='alert'>Alert!</button>").appendTo(document.body);
  // 実行時に DOM に存在する alert クラスを持つすべてのボタン要素にクリック動作を設定します
  $("button.alert").on("click", function () {
    console.log("A button with the alert class was clicked!");
  });
});
```

イベントリスナーが設定された後に同様の要素が作成された場合、それらは自動的に以前に設定したイベントの動作を拾い上げません。

> **Web 8080** タブを更新して、ウェブページをプレビューできます。
