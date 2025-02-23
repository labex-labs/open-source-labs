# 交互テキスト

VM内には既に`index.html`と`style.css`が用意されています。

交互テキストのアニメーションを作成するには、次の手順に従ってください。

1. 交互表示するテキストを保持するために、クラスが"alternating"で`id`が"alternating-text"の`<span>`要素を作成します。

```html
<p>I love coding in <span class="alternating" id="alternating-text"></span>.</p>
```

2. CSSでは、`display: none`を設定することで`<span>`要素を非表示にする`alternating-text`というアニメーションを定義します。

```css
.alternating {
  animation-name: alternating-text;
  animation-duration: 3s;
  animation-iteration-count: infinite;
  animation-timing-function: ease;
}

@keyframes alternating-text {
  90% {
    display: none;
  }
}
```

3. JavaScriptでは、交互表示する異なる単語の配列を定義し、最初の単語を使って`<span>`要素のコンテンツを初期化します。

```js
const texts = ["Java", "Python", "C", "C++", "C#", "Javascript"];
const element = document.getElementById("alternating-text");

let i = 0;
element.innerHTML = texts[0];
```

4. `EventTarget.addEventListener()`を使って、`'animationiteration'`イベントのイベントリスナーを定義します。これにより、アニメーションの反復が完了するたびにイベントハンドラが実行されます。イベントハンドラでは、`Element.innerHTML`を使って`texts`配列の次の要素を`<span>`要素のコンテンツとして表示します。

```js
const listener = (e) => {
  i = i < texts.length - 1 ? i + 1 : 0;
  element.innerHTML = texts[i];
};

element.addEventListener("animationiteration", listener, false);
```

右下隅の「Go Live」をクリックして、ポート8080でWebサービスを実行してください。その後、**Web 8080**タブを更新してWebページをプレビューできます。
