# エッチングされたテキスト

VM内には既に`index.html`と`style.css`が用意されています。

背景に表示されるテキストに「エッチング」または彫刻された効果を与えるには、次のCSSプロパティを使用します。

```css
.etched-text {
  text-shadow: 0 2px white;
  font-size: 1.5rem;
  font-weight: bold;
  color: #b8bec5;
}
```

`text-shadow`プロパティは、原点位置から水平方向に`0px`、垂直方向に`2px`オフセットされた白い影を作成します。この効果を得るには、背景が影よりも暗いことを確認してください。また、テキストの色を少し薄くすることで、背景から彫り出されたように見えるようにします。最後に、`etched-text`クラスを、段落などの目的のHTML要素に適用することで、この効果を実現します。

```html
<p class="etched-text">I appear etched into the background.</p>
```

右下隅の「Go Live」をクリックして、ポート8080でWebサービスを実行してください。その後、**Web 8080**タブを更新することで、Webページをプレビューできます。
