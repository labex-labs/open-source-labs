# 垂直スクロール付き画像ギャラリー

`index.html` と `style.css` はすでに仮想マシン (VM) 内に用意されています。

このコードは、水平方向にスクロール可能な画像ギャラリーを作成します。以下の手順が行われます。

1. コンテナのレイアウトは `display: flex` と `justify-content: center` を使用して設定されます。
2. スライドのレイアウトは `display: flex` と `flex-direction: column` を使用して設定されます。
3. `scroll-snap-type: y mandatory` と `overscroll-behavior-y: contain` を使用して、垂直スクロール時にスナップ効果を作成します。`scroll-snap-align: start` を使用して要素をコンテナの先頭にスナップさせます。
4. `scrollbar-width: none` を使用し、疑似要素 `::-webkit-scrollbar` を `display: none` とスタイル設定することで、スクロールバーを非表示にします。
5. `Element.scrollTo()` を使用して `scrollToElement` 関数を定義し、ギャラリーを指定されたアイテムまでスクロールさせます。
6. `.thumbnails` 要素は `Array.prototype.map()` と `Array.prototype.join()` を使用して作成されます。各サムネイルには画像のインデックスを持つ `data-id` 属性が付与されます。
7. `Document.querySelectorAll()`、`Array.prototype.forEach()`、`EventTarget.addEventListener()` および `scrollToElement` 関数を使用して、各サムネイルに `'click'` イベントのハンドラーを登録します。
8. `Document.querySelector()` と `EventTarget.addEventListener()` を使用して `'scroll'` イベントのハンドラーを登録します。`scrollThumb` 関数を使用して、`.thumbnails` と `.scrollbar` 要素を現在のスクロール位置に合わせて更新します。

HTML:

```html
<div class="gallery-container">
  <div class="thumbnails"></div>
  <div class="scrollbar">
    <div class="thumb"></div>
  </div>
  <div class="slides">
    <div><img src="https://picsum.photos/id/1067/540/720" /></div>
    <div><img src="https://picsum.photos/id/122/540/720" /></div>
    <div><img src="https://picsum.photos/id/188/540/720" /></div>
    <div><img src="https://picsum.photos/id/249/540/720" /></div>
    <div><img src="https://picsum.photos/id/257/540/720" /></div>
    <div><img src="https://picsum.photos/id/259/540/720" /></div>
    <div><img src="https://picsum.photos/id/283/540/720" /></div>
    <div><img src="https://picsum.photos/id/288/540/720" /></div>
    <div><img src="https://picsum.photos/id/299/540/720" /></div>
  </div>
</div>
```

CSS:

```css
.gallery-container {
  display: flex;
  justify-content: center;
}

.thumbnails {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.thumbnails img {
  width: 40px;
  height: 40px;
  cursor: pointer;
}

.scrollbar {
  width: 1px;
  height: 720px;
  background: #ccc;
  display: block;
  margin: 0 0 0 8px;
}

.thumb {
  width: 1px;
  position: absolute;
  height: 0;
  background: #000;
}

.slides {
  margin: 0 16px;
  display: grid;
  grid-auto-flow: row;
  gap: 1rem;
  width: calc(540px + 1rem);
  padding: 0 0.25rem;
  height: 720px;
  overflow-y: auto;
  overscroll-behavior-y: contain;
  scroll-snap-type: y mandatory;
  scrollbar-width: none;
}

.slides > div {
  scroll-snap-align: start;
}

.slides img {
  width: 540px;
  object-fit: contain;
}

.slides::-webkit-scrollbar {
  display: none;
}
```

JavaScript:

```js
const slideGallery = document.querySelector(".slides");
const slides = slideGallery.querySelectorAll("div");
const scrollbarThumb = document.querySelector(".thumb");
const slideCount = slides.length;
const slideHeight = 720;
const marginTop = 16;

const scrollThumb = () => {
  const index = Math.floor(slideGallery.scrollTop / slideHeight);
  scrollbarThumb.style.height = `${((index + 1) / slideCount) * slideHeight}px`;
};

const scrollToElement = (el) => {
  const index = parseInt(el.dataset.id, 10);
  slideGallery.scrollTo(0, index * slideHeight + marginTop);
};

document.querySelector(".thumbnails").innerHTML += [...slides]
  .map(
    (slide, i) => `<img src="${slide.querySelector("img").src}" data-id="${i}">`
  )
  .join("");

document.querySelectorAll(".thumbnails img").forEach((el) => {
  el.addEventListener("click", () => scrollToElement(el));
});

slideGallery.addEventListener("scroll", (e) => scrollThumb());

scrollThumb();
```

右下隅にある「Go Live」をクリックして、ポート 8080 でウェブサービスを起動してください。その後、**Web 8080** タブを更新すると、ウェブページをプレビューできます。
