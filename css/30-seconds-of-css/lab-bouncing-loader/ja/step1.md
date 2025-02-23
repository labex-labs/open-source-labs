# バウンシングローダー

VM内には既に`index.html`と`style.css`が用意されています。

バウンシングローダーアニメーションを作成するには：

1. `opacity`と`transform`プロパティを使った`@keyframes`アニメーションを定義し、より良いパフォーマンスのために`transform: translate3d()`で単一軸の平行移動を行います。
2. `.bouncing-loader`クラスを持つ親コンテナを作成し、`display: flex`と`justify-content: center`を使ってバウンシングする円を中央に配置します。
3. バウンシングする円用の3つの`<div>`要素に同じ`width`、`height`、`border-radius: 50%`を与えて円形にします。
4. 3つのバウンシングする円それぞれに`bouncing-loader`アニメーションを適用します。
5. 各円に異なる`animation-delay`を使い、`animation-direction: alternate`を使って適切な効果を作成します。

以下がHTMLコードです：

```html
<div class="bouncing-loader">
  <div></div>
  <div></div>
  <div></div>
</div>
```

以下がCSSコードです：

```css
@keyframes bouncing-loader {
  to {
    opacity: 0.1;
    transform: translate3d(0, -16px, 0);
  }
}

.bouncing-loader {
  display: flex;
  justify-content: center;
}

.bouncing-loader > div {
  width: 16px;
  height: 16px;
  margin: 3rem 0.2rem;
  background: #8385aa;
  border-radius: 50%;
  animation: bouncing-loader 0.6s infinite alternate;
}

.bouncing-loader > div:nth-child(2) {
  animation-delay: 0.2s;
}

.bouncing-loader > div:nth-child(3) {
  animation-delay: 0.4s;
}
```

右下隅の「Go Live」をクリックして8080番ポートでウェブサービスを実行してください。その後、**Web 8080**タブを更新してウェブページをプレビューできます。
