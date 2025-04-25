# タイプライターエフェクト

VM 内には既に`index.html`と`style.css`が用意されています。

タイプライターエフェクトのアニメーションを作成するには、次の手順に従ってください。

1. `typing`と`blink`の 2 つのアニメーションを定義します。`typing`は文字をアニメーション化し、`blink`はカレットをアニメーション化します。
2. `::after`疑似要素を使用して、ケアレットをコンテナ要素に追加します。
3. JavaScript を使用して、内部要素のテキストを設定し、文字数を含む`--characters`変数を設定します。この変数は、テキストをアニメーション化するために使用されます。
4. 必要に応じて、`white-space: nowrap`と`overflow: hidden`を使用してコンテンツを非表示にします。

以下が HTML コードです。

```html
<div class="typewriter-effect">
  <div class="text" id="typewriter-text"></div>
</div>
```

以下が CSS コードです。

```css
.typewriter-effect {
  display: flex;
  justify-content: center;
  font-family: monospace;
}

.typewriter-effect > .text {
  max-width: 0;
  animation: typing 3s steps(var(--characters)) infinite;
  white-space: nowrap;
  overflow: hidden;
}

.typewriter-effect::after {
  content: " |";
  animation: blink 1s infinite;
  animation-timing-function: step-end;
}

@keyframes typing {
  75%,
  100% {
    max-width: calc(var(--characters) * 1ch);
  }
}

@keyframes blink {
  0%,
  75%,
  100% {
    opacity: 1;
  }
  25% {
    opacity: 0;
  }
}
```

最後に、以下が JavaScript コードです。

```js
const typeWriter = document.getElementById("typewriter-text");
const text = "Lorem ipsum dolor sit amet.";

typeWriter.innerHTML = text;
typeWriter.style.setProperty("--characters", text.length);
```

右下隅の「Go Live」をクリックして、ポート 8080 でウェブサービスを実行してください。その後、**Web 8080**タブを更新して、ウェブページをプレビューできます。
