# 高さのトランジション

VM 内には既に`index.html`と`style.css`が用意されています。

このコードスニペットは、要素の高さが未知の場合に、以下の手順を行うことで、その高さを`0`から`auto`にトランジションさせます。

- `transition`プロパティを使用して、`max-height`の変更が`0.3秒`の期間でトランジションすることを指定します。
- `overflow`プロパティを`hidden`に設定して、非表示になった要素のコンテンツがそのコンテナをはみ出さないようにします。
- `max-height`プロパティを使用して、初期の高さを`0`に指定します。
- `:hover`疑似クラスを使用して、`max-height`を JavaScript で設定された`--max-height`変数の値に変更します。
- `Element.scrollHeight`プロパティと`CSSStyleDeclaration.setProperty()`メソッドを使用して、`--max-height`の値を要素の現在の高さに設定します。
- **注：** このアプローチは、各アニメーションフレームで再フローを引き起こし、トランジションする要素の下に多数の要素がある場合、遅延を引き起こす可能性があります。

```html
<div class="trigger">
  Hover over me to see a height transition.
  <div class="el">Additional content</div>
</div>
```

```css
.el {
  transition: max-height 0.3s;
  overflow: hidden;
  max-height: 0;
}

.trigger:hover > .el {
  max-height: var(--max-height);
}
```

```js
let el = document.querySelector(".el");
let height = el.scrollHeight;
el.style.setProperty("--max-height", height + "px");
```

右下隅の「Go Live」をクリックして、ポート 8080 でウェブサービスを実行してください。その後、**Web 8080**タブを更新して、ウェブページをプレビューできます。
