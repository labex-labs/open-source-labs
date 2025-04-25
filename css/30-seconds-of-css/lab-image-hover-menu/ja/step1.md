# 画像ホバー時のメニュー

VM 内には既に`index.html`と`style.css`が用意されています。

ユーザーが画像の上にマウスを乗せたときにメニューオーバーレイを表示するには、`<img>`要素を囲む`<figure>`と、メニューリンクを含む`<div>`要素を使用します。次の CSS プロパティを適用して、ホバー時に画像をアニメーションさせ、スライドエフェクトを作成します。

- `opacity`
- `right`
  `<div>`の`left`属性を要素の`width`のマイナス値に設定します。親要素の上にマウスを乗せたときにメニューをスライドインさせるために、それを`0`にリセットします。最後に、`<div>`に`display: flex`、`flex-direction: column`、`justify-content: center`を使用して、メニュー項目を垂直方向に中央揃えにします。

```html
<figure class="hover-menu">
  <img src="https://picsum.photos/id/1060/800/480.jpg" />
  <div>
    <a href="#">Home</a>
    <a href="#">Pricing</a>
    <a href="#">About</a>
  </div>
</figure>
```

```css
.hover-menu {
  position: relative;
  overflow: hidden;
  margin: 8px;
  min-width: 340px;
  max-width: 480px;
  max-height: 290px;
  width: 100%;
  background: #000;
  text-align: center;
  box-sizing: border-box;
}

.hover-menu * {
  box-sizing: border-box;
}

.hover-menu img {
  position: relative;
  max-width: 100%;
  top: 0;
  right: 0;
  opacity: 1;
  transition:
    opacity 0.3s ease-in-out,
    right 0.3s ease-in-out;
}

.hover-menu div {
  position: absolute;
  top: 0;
  left: -120px;
  width: 120px;
  height: 100%;
  padding: 8px 4px;
  background: #000;
  transition:
    left 0.3s ease-in-out,
    opacity 0.3s ease-in-out;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.hover-menu div a {
  display: block;
  line-height: 2;
  color: #fff;
  text-decoration: none;
  opacity: 0.8;
  padding: 5px 15px;
  position: relative;
  transition: opacity 0.3s ease-in-out;
}

.hover-menu div a:hover {
  text-decoration: underline;
}

.hover-menu:hover img {
  opacity: 0.5;
  right: -120px;
}

.hover-menu:hover div {
  left: 0;
  opacity: 1;
}
```

右下隅の「Go Live」をクリックして、ポート 8080 でウェブサービスを実行してください。その後、**Web 8080**タブを更新して、ウェブページをプレビューできます。
