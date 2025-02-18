# 水平スクロール付き画像ギャラリー

`index.html` と `style.css` はすでに仮想マシン (VM) に用意されています。

水平スクロール可能な画像ギャラリーを作成するための手順は以下の通りです。

1. `.thumbnails` をコンテナの下部に配置するには、`.thumbnails` クラスに `position: absolute; bottom: 8px;` を設定します。
2. 水平スクロールにスナップ効果を作成するには、`scroll-snap-type: x mandatory` と `overscroll-behavior-x: contain` を使用します。`scroll-snap-align: start` を使用して要素をコンテナの先頭にスナップさせます。
3. `scrollbar-width: none` を設定してスクロールバーを非表示にします。疑似要素 `::-webkit-scrollbar` をスタイルするには、`display: none;` を追加します。
4. `Element.scrollTo()` を使用して `scrollToElement` 関数を定義し、ギャラリーを指定されたアイテムまでスクロールさせます。
5. `Array.prototype.map()` と `Array.prototype.join()` を使用して `.thumbnails` 要素を埋めます。各サムネイルに画像のインデックスを持つ `data-id` 属性を付与します。
6. `Document.querySelectorAll()` と `Array.prototype.forEach()` を使用して、各サムネイルの `'click'` イベントにハンドラーを登録します。`EventTarget.addEventListener()` と `scrollToElement` 関数を使用します。
7. `Document.querySelector()` と `EventTarget.addEventListener()` を使用して `'scroll'` イベントにハンドラーを登録します。`highlightThumbnail` 関数を使用して `.thumbnails` 要素を現在のスクロール位置に合わせて更新します。

ギャラリーの HTML コードは次のとおりです。

```html
<div class="gallery-container">
  <div class="thumbnails"></div>
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

ギャラリーの CSS コードは次のとおりです。

```css
.gallery-container {
  position: relative;
  display: flex;
  justify-content: center;
}

.thumbnails {
  position: absolute;
  bottom: 8px;
  display: flex;
  flex-direction: row;
  gap: 6px;
}

.thumbnails div {
  width: 8px;
  height: 8px;
  cursor: pointer;
  background: #aaa;
  border-radius: 100%;
}

.thumbnails div.highlighted {
  background-color: #777;
}

.slides {
  margin: 0 16px;
  display: grid;
  grid-auto-flow: column;
  gap: 1rem;
  width: 540px;
  padding: 0 0.25rem;
  height: 720px;
  overflow-y: auto;
  overscroll-behavior-x: contain;
  scroll-snap-type: x mandatory;
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

ギャラリーの JavaScript コードは次のとおりです。

```js
const slideGallery = document.querySelector(".slides");
const slides = slideGallery.querySelectorAll("div");
const thumbnailContainer = document.querySelector(".thumbnails");
const slideCount = slides.length;
const slideWidth = 540;

const highlightThumbnail = () => {
  thumbnailContainer
    .querySelectorAll("div.highlighted")
    .forEach((el) => el.classList.remove("highlighted"));
  const index = Math.floor(slideGallery.scrollLeft / slideWidth);
  thumbnailContainer
    .querySelector(`div[data-id="${index}"]`)
    .classList.add("highlighted");
};

const scrollToElement = (el) => {
  const index = parseInt(el.dataset.id, 10);
  slideGallery.scrollTo(index * slideWidth, 0);
};

thumbnailContainer.innerHTML += [...slides]
  .map((slide, i) => `<div data-id="${i}"></div>`)
  .join("");

thumbnailContainer.querySelectorAll("div").forEach((el) => {
  el.addEventListener("click", () => scrollToElement(el));
});

slideGallery.addEventListener("scroll", (e) => highlightThumbnail());

highlightThumbnail();
```

右下隅にある「Go Live」をクリックして、ポート 8080 で Web サービスを実行してください。その後、**Web 8080** タブを更新すると、Web ページをプレビューできます。
