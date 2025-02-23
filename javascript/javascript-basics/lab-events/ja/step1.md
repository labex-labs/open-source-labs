# イベント

> VM には既に `index.html` が用意されています。

ウェブサイトで本当のインタラクティビティを実現するには、イベントハンドラが必要です。これらは、ブラウザー内のアクティビティを監視し、その応答としてコードを実行するコード構造です。最も明白な例は、[クリックイベント](https://developer.mozilla.org/en-US/docs/Web/API/Element/click_event)を処理することです。これは、マウスで何かをクリックしたときにブラウザーによって発火されます。これを示すために、コンソールに次のコードを入力してから、現在のウェブページをクリックしてください：

```js
document.querySelector("html").addEventListener("click", function () {
  alert("Ouch! Stop poking me!");
});
```

要素にイベントハンドラを追加する方法はいくつかあります。
ここでは、[`<html>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/html) 要素を選択しています。その後、その[`addEventListener()`](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener) 関数を呼び出し、監視するイベントの名前 (`'click'`) とイベントが発生したときに実行する関数を渡します。

ここで `addEventListener()` に渡した関数は、名前がないため _匿名関数_ と呼ばれます。匿名関数を書く別の方法があり、これを _アロー関数_ と呼びます。
アロー関数は `() =>` を使って `function ()` の代わりに書きます：

```js
document.querySelector("html").addEventListener("click", () => {
  alert("Ouch! Stop poking me!");
});
```

> 右下隅の「Go Live」をクリックして、ポート 8080 でウェブサービスを実行してください。その後、**Web 8080** タブを更新してウェブページをプレビューできます。
