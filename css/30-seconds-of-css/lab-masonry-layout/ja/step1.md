# メイソニーレイアウト

VM内には既に`index.html`と`style.css`が用意されています。

メイソニースタイルのレイアウトを作成するには、`.masonry-container`をメインコンテナとして使用し、`.masonry-columns`を内部コンテナとして追加し、その中に`.masonry-brick`要素を配置します。レイアウトは、互いに重なり合う「レンガ」で構成され、完璧なフィットを形成します。垂直レイアウトの場合は`width`を固定し、水平レイアウトの場合は`height`を固定できます。

レイアウトが適切に流れるようにするには、`.masonry-brick`要素に`display: block`を適用します。最初の要素の位置を考慮して、`:first-child`疑似要素セレクタを使用して、最初の要素に異なる`margin`を適用します。

より大きな柔軟性と応答性を得るには、CSS変数とメディアクエリを使用します。`.masonry-container`には、列数とギャップ用のCSS変数があります。列数は、異なる画面サイズに対して異なる列数と幅を指定するメディアクエリによって制御されます。

```html
<div class="masonry-container">
  <div class="masonry-columns">
    <img
      class="masonry-brick"
      src="https://picsum.photos/id/1016/384/256"
      alt="An image"
    />
    <img
      class="masonry-brick"
      src="https://picsum.photos/id/1025/495/330"
      alt="Another image"
    />
    <img
      class="masonry-brick"
      src="https://picsum.photos/id/1024/192/128"
      alt="Another image"
    />
    <img
      class="masonry-brick"
      src="https://picsum.photos/id/1028/518/345"
      alt="One more image"
    />
    <img
      class="masonry-brick"
      src="https://picsum.photos/id/1035/585/390"
      alt="And another one"
    />
    <img
      class="masonry-brick"
      src="https://picsum.photos/id/1074/384/216"
      alt="Last one"
    />
  </div>
</div>
```

```css
.masonry-container {
  --column-count-small: 1;
  --column-count-medium: 2;
  --column-count-large: 3;
  --column-gap: 0.125rem;
  padding: var(--column-gap);
}

.masonry-columns {
  column-gap: var(--column-gap);
  column-count: var(--column-count-small);
  column-width: calc(1 / var(--column-count-small) * 100%);
}

@media only screen and (min-width: 640px) {
  .masonry-columns {
    column-count: var(--column-count-medium);
    column-width: calc(1 / var(--column-count-medium) * 100%);
  }
}

@media only screen and (min-width: 800px) {
  .masonry-columns {
    column-count: var(--column-count-large);
    column-width: calc(1 / var(--column-count-large) * 100%);
  }
}

.masonry-brick {
  width: 100%;
  height: auto;
  margin: var(--column-gap) 0;
  display: block;
}

.masonry-brick:first-child {
  margin: 0 0 var(--column-gap);
}
```

右下隅の「Go Live」をクリックして、ポート8080でウェブサービスを実行してください。その後、**Web 8080**タブを更新して、ウェブページをプレビューできます。
