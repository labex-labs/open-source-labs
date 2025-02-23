# フルスクリーン

VM内には既に`index.html`と`style.css`が用意されています。

フルスクリーンモードで要素にスタイルを適用するには、`:fullscreen` CSS疑似要素セレクタを使用できます。また、`<button>`と`Element.requestFullscreen()`を使って、プレビュー用に要素をフルスクリーンにするボタンを作成することもできます。以下はコード例です。

```html
<div class="container">
  <p>
    <em>下のボタンをクリックすると、要素がフルスクリーンモードになります。</em>
  </p>
  <div class="element" id="element">
    <p>フルスクリーンモードで色が変わります！</p>
  </div>
  <br />
  <button
    onclick="var el = document.getElementById('element'); el.requestFullscreen();"
  >
    フルスクリーンにする！
  </button>
</div>
```

```css
.container {
  margin: 40px auto;
  max-width: 700px;
}

.element {
  padding: 20px;
  height: 300px;
  width: 100%;
  background-color: skyblue;
  box-sizing: border-box;
}

.element p {
  text-align: center;
  color: white;
  font-size: 3em;
}

/* Internet Explorer用 */
.element:-ms-fullscreen p {
  visibility: visible;
}

/* 最新ブラウザ用 */
.element:fullscreen {
  background-color: #e4708a;
  width: 100vw;
  height: 100vh;
}
```

右下隅の「Go Live」をクリックして、ポート8080でウェブサービスを実行してください。その後、**Web 8080**タブを更新してウェブページをプレビューできます。
