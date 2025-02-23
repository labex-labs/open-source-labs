# スクロールバーを非表示にする

VM内には既に`index.html`と`style.css`が用意されています。

要素にスクロールバーを非表示にしながらスクロール可能にするには、次の手順に従います。

- 要素にスクロールを有効にするために`overflow: auto`を使用します。
- Firefoxでスクロールバーを非表示にするために`scrollbar-width: none`を使用します。
- WebKitブラウザ（Chrome、Edge、Safariなど）でスクロールバーを非表示にするために`::-webkit-scrollbar`疑似要素に`display: none`を使用します。

以下は実装例です。

```html
<div class="scrollable">
  <p>
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean interdum id
    leo a consectetur. Integer justo magna, ultricies vel enim vitae, egestas
    efficitur leo. Ut nulla orci, rutrum eu augue sed, tempus pellentesque quam.
  </p>
</div>
```

```css
.scrollable {
  width: 200px;
  height: 100px;
  overflow: auto;
  scrollbar-width: none;
}

/* Hide scrollbars on WebKit browsers */
.scrollable::-webkit-scrollbar {
  display: none;
}
```

右下隅の「Go Live」をクリックして、ポート8080でウェブサービスを実行してください。その後、**Web 8080**タブを更新してウェブページをプレビューできます。
