# 回転するカード

VM 内には既に`index.html`と`style.css`が用意されています。

マウスオーバー時に回転する両面カードを作成するには、次の手順に従ってください。

1. カードの`backface-visibility`を`none`に設定して、デフォルトで裏面が表示されないようにします。
2. 最初は、カードの裏面に`rotateY(-180deg)`を設定し、表に`rotateY(0deg)`を設定します。
3. マウスオーバー時に、表に`rotateY(180deg)`を設定し、裏に`rotateY(0deg)`を設定します。
4. 回転効果を作成するために適切な`perspective`値を設定します。

以下は、HTML と CSS のコードの例です。

```html
<div class="card">
  <div class="card-side front">
    <div>表</div>
  </div>
  <div class="card-side back">
    <div>裏</div>
  </div>
</div>
```

```css
.card {
  perspective: 150rem;
  position: relative;
  height: 40rem;
  max-width: 400px;
  margin: 2rem;
  box-shadow: none;
  background: none;
}

.card-side {
  height: 35rem;
  border-radius: 15px;
  transition: all 0.8s ease;
  backface-visibility: hidden;
  position: absolute;
  top: 0;
  left: 0;
  width: 80%;
  padding: 2rem;
  color: white;
}

.card-side.back {
  transform: rotateY(-180deg);
  background: linear-gradient(43deg, #4158d0 0%, #c850c0 46%, #ffcc70 100%);
}

.card-side.front {
  background: linear-gradient(160deg, #0093e9 0%, #80d0c7 100%);
}

.card:hover.card-side.front {
  transform: rotateY(180deg);
}

.card:hover.card-side.back {
  transform: rotateY(0deg);
}
```

右下隅の「Go Live」をクリックして、ポート 8080 でウェブサービスを実行してください。その後、**Web 8080**タブを更新してウェブページをプレビューできます。
