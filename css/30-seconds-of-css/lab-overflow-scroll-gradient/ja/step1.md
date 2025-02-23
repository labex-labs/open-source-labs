# はみ出しスクロールグラデーション

VM内には既に`index.html`と`style.css`が用意されています。

はみ出た要素にフェードインググラデーションを追加し、スクロールする追加のコンテンツがあることを示すには、次の手順に従います。

1. `::after`疑似要素を使って、`transparent`から`white`に（上から下に）フェードする`linear-gradient()`を作成します。
2. 疑似要素を親要素内で`position: absolute`、`width`、および`height`を使って配置とサイズを設定します。
3. `pointer-events: none`を使って疑似要素をマウスイベントから除外し、その後ろのテキストを選択可能/インタラクティブに保ちます。

以下は、HTMLとCSSのコードスニペットの例です。

```html
<div class="overflow-scroll-gradient">
  <div class="overflow-scroll-gradient-scroller">
    Lorem ipsum dolor sit amet consectetur adipisicing elit. <br />
    Iure id exercitationem nulla qui repellat laborum vitae, <br />
    molestias tempora velit natus. Quas, assumenda nisi. <br />
    Quisquam enim qui iure, consequatur velit sit? <br />
    Lorem ipsum dolor sit amet consectetur adipisicing elit.<br />
    Iure id exercitationem nulla qui repellat laborum vitae, <br />
    molestias tempora velit natus. Quas, assumenda nisi. <br />
    Quisquam enim qui iure, consequatur velit sit?
  </div>
</div>
```

```css
.overflow-scroll-gradient {
  position: relative;
}

.overflow-scroll-gradient::after {
  content: "";
  position: absolute;
  bottom: 0;
  width: 250px;
  height: 25px;
  background: linear-gradient(transparent, white);
  pointer-events: none;
}

.overflow-scroll-gradient-scroller {
  overflow-y: scroll;
  background: white;
  width: 240px;
  height: 200px;
  padding: 15px;
  line-height: 1.2;
}
```

右下隅の「Go Live」をクリックして、ポート8080でウェブサービスを実行してください。その後、**Web 8080**タブを更新してウェブページをプレビューできます。
