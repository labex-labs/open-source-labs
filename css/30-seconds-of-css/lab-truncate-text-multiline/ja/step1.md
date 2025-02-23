# 複数行のテキストを切り詰める

VM には既に `index.html` と `style.css` が用意されています。

1 行より長いテキストを切り詰めるには、次の手順に従います。

1. `overflow: hidden` を使用して、テキストがその寸法を超えないようにします。
2. 要素が少なくとも 1 つの一定の寸法を持つように、固定幅 `400px` を設定します。
3. `font-size` から計算される `height: 109.2px` を設定します。計算式は `font-size * line-height * numberOfLines` です（この場合 `26 * 1.4 * 3 = 109.2`）。
4. HTML の `p` 要素に `truncate-text-multiline` クラスを追加します。
5. CSS の `.truncate-text-multiline` クラスに対して、`font-size: 26px` と `line-height: 1.4` を設定します。
6. テキストのスタイルを設定するために、`color: #333` と `background: #f5f6f9` を設定します。
7. `transparent` から `background-color` に向かうグラデーションを作成するには、`.truncate-text-multiline::after` 疑似要素に次の CSS ルールを追加します。

```css
.truncate-text-multiline::after {
  content: "";
  position: absolute;
  bottom: 0;
  right: 0;
  width: 150px;
  height: 36.4px;
  background: linear-gradient(to right, rgba(0, 0, 0, 0), #f5f6f9 50%);
}
```

これにより、グラデーション コンテナが作成されます。このコンテナの高さは `36.4px` で、計算式は `font-size * line-height` です（この場合 `26 * 1.4 = 36.4`）。`::after` 疑似要素は `.truncate-text-multiline` 要素の右下隅に配置されます。

右下隅の「Go Live」をクリックして、ポート 8080 でウェブ サービスを実行してください。その後、**Web 8080** タブを更新して、ウェブ ページをプレビューできます。
