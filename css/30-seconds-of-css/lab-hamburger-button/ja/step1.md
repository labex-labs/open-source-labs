# ハンバーガーボタン

VM には既に `index.html` と `style.css` が用意されています。

ホバー時にクロスボタンに遷移するハンバーガーメニューを作成するには、次の手順に従ってください。

1. `.hamburger-menu` コンテナの `div` を使用し、これには上部、下部、中央のバーが含まれます。
2. コンテナを `display: flex` で `flex-flow: column wrap` に設定します。
3. `justify-content: space-between` を使用してバー間に距離を追加します。
4. `transform: rotate()` を使用して上部と下部のバーを 45 度回転させ、ホバー時に中央のバーを `opacity: 0` に設定してフェードアウトさせます。
5. `transform-origin: left` を使用して、バーが左側の点を中心に回転するようにします。

対応する HTML コードは次のとおりです。

```html
<div class="hamburger-menu">
  <div class="bar top"></div>
  <div class="bar middle"></div>
  <div class="bar bottom"></div>
</div>
```

そして、CSS コードは次のとおりです。

```css
.hamburger-menu {
  display: flex;
  flex-flow: column wrap;
  justify-content: space-between;
  height: 2.5rem;
  width: 2.5rem;
  cursor: pointer;
}

.hamburger-menu.bar {
  height: 5px;
  background: black;
  border-radius: 5px;
  margin: 3px 0px;
  transform-origin: left;
  transition: all 0.5s;
}

.hamburger-menu:hover.top {
  transform: rotate(45deg);
}

.hamburger-menu:hover.middle {
  opacity: 0;
}

.hamburger-menu:hover.bottom {
  transform: rotate(-45deg);
}
```

右下隅の「Go Live」をクリックして、ポート 8080 で Web サービスを実行してください。その後、**Web 8080** タブを更新して Web ページをプレビューできます。
