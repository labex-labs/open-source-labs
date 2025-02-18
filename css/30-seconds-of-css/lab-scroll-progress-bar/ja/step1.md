# スクロール進捗バー

`index.html` と `style.css` はすでに仮想マシン (VM) に用意されています。

ウェブページのスクロール割合を表示する進捗バーを作成するには、以下の手順に従ってください。

1. HTML コードに `id` が "scroll-progress" の `div` 要素を追加します。
2. CSS コードで、要素の `position` を `fixed`、`top` を `0`、`width` を `0%`、`height` を `4px`、`background` 色を `#7983ff` に設定します。
3. `z-index` の値を大きな数値に設定して、進捗バーがページの最上部にあり、他のコンテンツの上に表示されるようにします。
4. JavaScript コードで、`document.getElementById()` メソッドを使用して `scroll-progress` 要素を選択します。
5. `document.documentElement.scrollHeight - document.documentElement.clientHeight` という式を使ってウェブページの高さを計算します。
6. `window` オブジェクトに `scroll` イベントを監視するイベントリスナーを追加します。
7. イベントリスナー関数内で、`(scrollTop / height) * 100` という式を使ってドキュメントのスクロール割合を計算します。
8. `style` プロパティを使用して、`scroll-progress` 要素の `width` をスクロール割合に設定します。

以下がコードです。

```html
<div id="scroll-progress"></div>
```

```css
#scroll-progress {
  position: fixed;
  top: 0;
  width: 0%;
  height: 4px;
  background: #7983ff;
  z-index: 10000;
}
```

```js
const scrollProgress = document.getElementById("scroll-progress");
const height =
  document.documentElement.scrollHeight - document.documentElement.clientHeight;

window.addEventListener("scroll", () => {
  const scrollTop =
    document.body.scrollTop || document.documentElement.scrollTop;
  scrollProgress.style.width = `${(scrollTop / height) * 100}%`;
});
```

右下隅にある 'Go Live' をクリックして、ポート 8080 でウェブサービスを実行してください。その後、**Web 8080** タブを更新すると、ウェブページをプレビューできます。
