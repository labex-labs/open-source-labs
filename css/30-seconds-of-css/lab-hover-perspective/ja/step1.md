# ホバー時の透視変換

VM 内には既に `index.html` と `style.css` が用意されています。

要素にホバーアニメーション付きの透視変換を作成するには：

1. `transform` プロパティに `perspective()` 関数と `rotateY()` 関数を使って要素に透視を適用します。たとえば、左の透視を作成するには `transform: perspective(1500px) rotateY(15deg);` を使用します。右の透視を作成するには `transform: perspective(1500px) rotateY(-15deg);` を使用します。

2. 要素がホバーされたときに `transform` プロパティをアニメーションさせるために `transition` プロパティを使用します。たとえば `transition: transform 1s ease 0s;` です。

3. 透視効果を左右にミラーリングするには、右の透視では `rotateY()` の値を負に変更します。たとえば `transform: perspective(1500px) rotateY(-15deg);` を使用します。

例の HTML：

```html
<div class="card-container">
  <div class="image-card perspective-left"></div>
  <div class="image-card perspective-right"></div>
</div>
```

例の CSS：

```css
.image-card {
  display: inline-block;
  box-sizing: border-box;
  margin: 1rem;
  width: 240px;
  height: 320px;
  padding: 8px;
  border-radius: 1rem;
  background: url("https://picsum.photos/id/1049/240/320");
  box-shadow: rgba(0, 0, 0, 0.25) 0px 25px 50px -12px;
}

.perspective-left {
  transform: perspective(1500px) rotateY(15deg);
  transition: transform 1s ease 0s;
}

.perspective-left:hover {
  transform: perspective(3000px) rotateY(5deg);
}

.perspective-right {
  transform: perspective(1500px) rotateY(-15deg);
  transition: transform 1s ease 0s;
}

.perspective-right:hover {
  transform: perspective(3000px) rotateY(-5deg);
}
```

画面右下の「Go Live」をクリックして 8080 番ポートでウェブサービスを実行してください。その後、**Web 8080** タブを更新してウェブページをプレビューできます。
