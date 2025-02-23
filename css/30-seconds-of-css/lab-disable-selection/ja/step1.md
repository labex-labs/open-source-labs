# 選択を無効にする

VM には既に `index.html` と `style.css` が用意されています。

要素のコンテンツを選択不可能にするには、セレクターに CSS プロパティ `user-select: none` を追加します。ただし、この方法はユーザーがコンテンツをコピーすることを防ぐために完全に安全ではありません。

例：

```html
<p>You can select me.</p>
<p class="unselectable">You can't select me!</p>
```

```css
.unselectable {
  user-select: none;
}
```

右下隅の「Go Live」をクリックして、ポート 8080 で Web サービスを実行してください。その後、**Web 8080** タブを更新して Web ページをプレビューできます。
