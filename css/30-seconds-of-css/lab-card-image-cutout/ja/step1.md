# 画像切り抜き付きのカード

VM には既に `index.html` と `style.css` が用意されています。

画像切り抜き付きのカードを作成するには、次の手順に従います。

1. `.container` 要素に `background` プロパティを使って色付きの背景を追加します。
2. `.card` 要素を作成し、その中に `figure` 要素を追加し、必要な画像とその他のコンテンツを配置します。
3. `::before` 疑似要素を使って `figure` 要素の周りに `border` を追加します。枠の色を `.container` 要素の `background` 色と一致させて、`.card` に切り抜きの錯覚を作り出します。

ここにカードの例となる HTML コードを示します。

```html
<div class="container">
  <div class="card">
    <figure>
      <img alt="" src="https://picsum.photos/id/447/400/400" />
    </figure>
    <p class="content">
      Lorem ipsum dolor sit amet consectetur adipisicing elit.
    </p>
  </div>
</div>
```

そして、対応する CSS コードを示します。

```css
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 96px 24px 48px;
  background: #f3f1fe;
}

.card {
  width: 350px;
  margin: 8px;
  display: flex;
  flex-direction: column;
  align-items: center;
  background: #fff;
  border-radius: 10px;
  box-shadow: 0 0 5px -2px rgba(0, 0, 0, 0.1);
}

.card figure {
  width: 120px;
  height: 120px;
  margin-top: -60px;
  border-radius: 50%;
  position: relative;
}

.card figure::before {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  width: 100%;
  height: 100%;
  transform: translate(-50%, -50%);
  border-radius: inherit;
  border: 1rem solid #f3f1fe;
  box-shadow: 0 1px rgba(0, 0, 0, 0.1);
}

.card figure img {
  width: 100%;
  height: 100%;
  border-radius: inherit;
  object-fit: cover;
}

.card.content {
  margin: 2rem;
  text-align: center;
  line-height: 1.5;
  color: #101010;
}
```

右下隅の「Go Live」をクリックして、ポート 8080 でウェブサービスを実行してください。その後、**Web 8080** タブを更新してウェブページをプレビューできます。
