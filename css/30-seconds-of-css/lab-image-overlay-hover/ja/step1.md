# マウスオーバー時の画像オーバーレイ

VM 内には既に`index.html`と`style.css`が用意されています。

画像にマウスオーバー時のオーバーレイ効果を表示するには、次の手順に従います。

1. オーバーレイの上部と下部のバーにそれぞれ`::before`と`::after`疑似要素を使用します。それらの`opacity`、`transform`、`transition`を設定して、望ましい効果を生成します。
2. オーバーレイのテキストには`<figcaption>`を使用します。`display: flex`、`flex-direction: column`、`justify-content: center`を設定して、画像の中央にテキストを配置します。
3. `:hover`疑似セレクタを使用して、すべての要素の`opacity`と`transform`を更新し、オーバーレイを表示します。

使用する HTML コードは次のとおりです。

```html
<figure class="hover-img">
  <img src="https://picsum.photos/id/200/440/320.jpg" />
  <figcaption>
    <h3>Lorem <br />Ipsum</h3>
  </figcaption>
</figure>
```

使用する CSS コードは次のとおりです。

```css
.hover-img {
  display: inline-block;
  margin: 8px;
  width: 100%;
  max-width: 320px;
  min-width: 240px;
  overflow: hidden;
  position: relative;
  text-align: center;
  background-color: #000;
  color: #fff;
}

.hover-img * {
  box-sizing: border-box;
  transition: all 0.45s ease;
}

.hover-img::before,
.hover-img::after {
  content: "";
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  background-color: rgba(0, 0, 0, 0.5);
  border-top: 32px solid rgba(0, 0, 0, 0.5);
  border-bottom: 32px solid rgba(0, 0, 0, 0.5);
  z-index: 1;
  opacity: 0;
  transform: scaleY(2);
  transition: all 0.3s ease;
}

.hover-img::before {
  content: "";
  top: 0;
  bottom: auto;
}

.hover-img img {
  vertical-align: top;
  max-width: 100%;
  backface-visibility: hidden;
}

.hover-img figcaption {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  align-items: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
  line-height: 1.1em;
  opacity: 0;
  z-index: 2;
  transition-delay: 0.1s;
  font-size: 24px;
  font-family: sans-serif;
  font-weight: 400;
  letter-spacing: 1px;
  text-transform: uppercase;
}

.hover-img:hover::before,
.hover-img:hover::after {
  transform: scale(1);
  opacity: 1;
}

.hover-img:hover img {
  opacity: 0.7;
}

.hover-img:hover figcaption {
  opacity: 1;
}
```

右下隅の「Go Live」をクリックして、ポート 8080 でウェブサービスを実行してください。その後、**Web 8080**タブを更新して、ウェブページをプレビューできます。
