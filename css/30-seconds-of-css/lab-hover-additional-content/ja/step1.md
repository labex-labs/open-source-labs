# ホバー時に追加コンテンツを表示する

VM 内には既に`index.html`と`style.css`が用意されています。

ホバー時に追加コンテンツを表示するカードを作成するには、次の手順に従います。

1. カードに`overflow: hidden`を使用して、垂直方向にはみ出る要素を非表示にします。
2. `:hover`と`:focus-within`疑似クラスセレクタを使用して、要素がホバーされ、フォーカスされ、またはその子孫要素のいずれかがフォーカスされたときにカードのスタイリングを変更します。
3. `transition: 0.3s ease all`を設定して、ホバー/フォーカス時にスムーズなトランジション効果を作成します。

以下は、カードの例となる HTML コードです。

```html
<div class="card">
  <img src="https://picsum.photos/id/404/367/267" />
  <h3>Lorem ipsum</h3>
  <div class="focus-content">
    <p>
      Lorem ipsum dolor sit amet, consectetur adipiscing elit.<br />
      <a href="#">Link to source</a>
    </p>
  </div>
</div>
```

そして、カードをスタイリングする CSS コードは次の通りです。

```css
.card {
  width: 300px;
  height: 280px;
  padding: 0;
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.1);
  border-radius: 8px;
  box-sizing: border-box;
  overflow: hidden;
}

.card * {
  transition: 0.3s ease all;
}

.card img {
  margin: 0;
  width: 300px;
  height: 224px;
  object-fit: cover;
  display: block;
}

.card h3 {
  margin: 0;
  padding: 12px 12px 48px;
  line-height: 32px;
  font-weight: 500;
  font-size: 20px;
}

.card.focus-content {
  display: block;
  padding: 8px 12px;
}

.card p {
  margin: 0;
  line-height: 1.5;
}

.card:hover img,
.card:focus-within img {
  margin-top: -80px;
}

.card:hover h3,
.card:focus-within h3 {
  padding: 8px 12px 0;
}
```

右下隅の「Go Live」をクリックして、ポート 8080 でウェブサービスを実行してください。その後、**Web 8080**タブを更新してウェブページをプレビューできます。
