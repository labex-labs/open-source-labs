# 画面外

VM には既に `index.html` と `style.css` が用意されています。

この手法は、DOM 内の要素を完全に非表示にしながらもアクセス可能に保ちます。これを達成するには、次の手順に従うことができます。

- すべてのボーダーとパディングを削除し、要素のオーバーフローを非表示にします。
- `clip` を使用して、要素の一部が表示されないようにします。
- 要素の `height` と `width` を `1px` に設定し、`margin: -1px` を使用してそれらを反転させます。
- `position: absolute` を使用して、要素が DOM 内のスペースを占有しないようにします。
- この手法は、アクセシビリティとレイアウトの親和性の点で、`display: none`（スクリーンリーダーで読み取れない）や `visibility: hidden`（DOM 内の物理的なスペースを占有する）よりも優れた代替策であることに注意してください。

以下は、HTML と CSS でこの手法を使用する方法の例です。

```html
<a class="button" href="https://google.com">
  Learn More <span class="offscreen">about pants</span>
</a>
```

```css
.offscreen {
  border: 0;
  clip: rect(0 0 0 0);
  height: 1px;
  margin: -1px;
  overflow: hidden;
  padding: 0;
  position: absolute;
  width: 1px;
}
```

右下隅の「Go Live」をクリックして、ポート 8080 で Web サービスを実行してください。その後、**Web 8080** タブを更新して Web ページをプレビューできます。
